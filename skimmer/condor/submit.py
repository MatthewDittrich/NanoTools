import os
import sys
import argparse
import math
import subprocess
from time import sleep

from metis.Sample import DBSSample, DirectorySample
from metis.CondorTask import CondorTask
from metis.StatsParser import StatsParser
import samples
from das_nevents import das_info

condorpath = os.path.dirname(os.path.realpath(__file__))

# ------------------------------------------------------------------
# Helper functions
# ------------------------------------------------------------------
MIN_EVENTS_PER_JOB = 3_000_000

def query_das_single(dsname):
    """Query dasgoclient for nevents and nfiles for a single dataset."""
    try:
        result_nevents = subprocess.run(
            ["dasgoclient", "-query", f"dataset={dsname} | grep dataset.nevents"],
            capture_output=True, text=True, timeout=120
        )
        nevents = int(result_nevents.stdout.strip()) if result_nevents.stdout.strip() else 0

        result_nfiles = subprocess.run(
            ["dasgoclient", "-query", f"dataset={dsname} | grep dataset.nfiles"],
            capture_output=True, text=True, timeout=120
        )
        nfiles = int(result_nfiles.stdout.strip()) if result_nfiles.stdout.strip() else 0

        evts_per_file = nevents // nfiles if nfiles > 0 else 0
        return {"nevents": nevents, "nfiles": nfiles, "evts_per_file": evts_per_file}
    except Exception as e:
        print(f"ERROR querying DAS for {dsname}: {e}")
        return None

def split_func(dsname):
    if dsname not in das_info:
        print(f"WARNING: {dsname} not found in das_info, querying DAS...")
        result = query_das_single(dsname)
        if result and result["evts_per_file"] > 0:
            das_info[dsname] = result
            # Append to das_nevents.py so future runs don't need to re-query
            das_nevents_path = os.path.join(condorpath, "das_nevents.py")
            with open(das_nevents_path, "r") as f:
                content = f.read()
            entry = f'    "{dsname}": {{"nevents": {result["nevents"]}, "nfiles": {result["nfiles"]}, "evts_per_file": {result["evts_per_file"]}}},\n'
            content = content.replace("\n}\n", "\n" + entry + "}\n")
            with open(das_nevents_path, "w") as f:
                f.write(content)
            print(f"  -> Found {result['nevents']} events in {result['nfiles']} files ({result['evts_per_file']} evts/file), saved to das_nevents.py")
        else:
            print(f"  -> DAS query failed or returned 0, defaulting to 1 file per job")
            return 20
    evts_per_file = das_info[dsname]["evts_per_file"]
    if evts_per_file > 0:
        return max(1, math.ceil(MIN_EVENTS_PER_JOB / evts_per_file))
    return 1

def njobs_to_process(dsname):
    return -1  # -1 = unlimited

# ------------------------------------------------------------------
# Main
# ------------------------------------------------------------------
if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("--arch", choices=["el8", "el9"], default="el8",
                        help="Target architecture: el8 (no singularity) or el9 (uses singularity)")
    args = parser.parse_args()

    unique_key = "Run2_Sig_v15_26Feb2026_v1"

    # Architecture-dependent CMSSW settings (must match setup.sh)
    if args.arch == "el9":
        singularity_image = "/cvmfs/singularity.opensciencegrid.org/cmssw/cms:rhel9"
        cmssw_version = "CMSSW_16_0_0_pre4"
        scram_arch = "el9_amd64_gcc13"
    else:
        singularity_image = "/cvmfs/singularity.opensciencegrid.org/cmssw/cms:rhel8"
        cmssw_version = "CMSSW_14_1_0_pre4"
        scram_arch = "el8_amd64_gcc12"

    # Samples
    datasets = samples.samples_to_submit

    # Analysis tags
    analysis_tags = [
        "Sig",
#        "4Lep",
#        "3Lep",
#        "2Lep2FJ",
#        "2Lep1FJ",
#        "1Lep1FJ",
#        "0Lep3FJ",
#        "0Lep2FJ",
#        "0Lep1FJ",
#        "0Lep0FJ"
    ]

    # Optional extra flags for signal datasets
    signal_flags = ""

    # Task summary (all datasets × tags)
    task_summary = {}

    # Skip tail events?
    skip_tail = False

    # ------------------------------------------------------------------
    # Infinite loop until all tasks complete
    # ------------------------------------------------------------------
    while True:
        all_tasks_complete = True

        # ------------------------------------------------------------------
        # Process datasets
        # ------------------------------------------------------------------
        for ds in datasets:
            files = ds.get_files()
            print(f"Found {len(files)} files")
            for analysis_tag in analysis_tags:
                tag = f"{unique_key}_{analysis_tag}"

                task = CondorTask(
                    verbose=True,
                    sample=ds,
                    files_per_output=split_func(ds.get_datasetname()),
                    output_name="output.root",
                    tag=tag,
                    condor_submit_params=dict({
                        "use_xrootd": True,
                        "sites": "T2_US_UCSD",
                        "classads": [["metis_extraargs", f"{signal_flags} -d ./ -a {analysis_tag} -t Events -T Events"]]
                    }, **({"container": singularity_image} if singularity_image else {})),
                    max_jobs=njobs_to_process(ds.get_datasetname()),
                    cmssw_version=cmssw_version,
                    scram_arch=scram_arch,
                    input_executable=f"{condorpath}/condor_executable_metis.sh",
                    tarfile=f"{condorpath}/package.tar.xz",
                    #special_dir=f"skim/{tag}",
                    special_dir=f"VVH_Skims/{tag}",
                    min_completion_fraction=0.50 if skip_tail else 1.0
                )

                if not task.complete():
                    print(f"Submitting task for {ds.get_datasetname()} with tag {tag}")
                    task.process()
                else:
                    print(f"Task already complete for {ds.get_datasetname()} with tag {tag}")


                #if not task.complete():
                #    task.process()

                # Aggregate completion
                all_tasks_complete = all_tasks_complete and task.complete()

                # Update master task summary
                key = f"{task.get_sample().get_datasetname()}_{analysis_tag}"
                task_summary[key] = task.get_task_summary()

        # ------------------------------------------------------------------
        # Generate JSON summaries and dashboards per tag
        # ------------------------------------------------------------------
        for analysis_tag in analysis_tags:

            # Filter summary for this tag
            tag_summary = {k: v for k, v in task_summary.items() if k.endswith(f"_{analysis_tag}")}

            webdir = os.path.expanduser(f"~/public_html/{unique_key}/{analysis_tag}")
            os.makedirs(webdir, exist_ok=True)
            os.system(f"rm -f {webdir}/web_summary.json")

            StatsParser(data=tag_summary, webdir=webdir, summary_fname=f"{webdir}/summary.json", wsummary_name=f"{webdir}/web_summary.json").do()

            os.system("chmod -R 755 {}".format(webdir))
            os.system(f"msummary -r -i {webdir}/web_summary.json")


        # If all done exit the loop
        if all_tasks_complete:
            print("")
            print("All job finished")
            print("")
            break

        # Neat trick to not exit the script for force updating
        print('Press Ctrl-C to force update, otherwise will sleep for 600 seconds')
        try:
            for i in reversed(range(0, 600)):
                sleep(1) # could use a backward counter to be preeety :)
                sys.stdout.write("\r{} mins {} seconds till updating ...".format(i//60, i%60))
                sys.stdout.flush()
        except KeyboardInterrupt:
            input("Press Enter to force update, or Ctrl-C to quit.")
            print("Force updating...")
