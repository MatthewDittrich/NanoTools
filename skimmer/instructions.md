# Skimmer Build and Run Instructions

## Prerequisites

The login node (UAF) runs EL8, but the skimmer targets EL9.
All compilation and local running must be done inside the `cmssw-el9` Singularity container.

## Enter the EL9 Environment

```bash
/cvmfs/cms.cern.ch/common/cmssw-el9
```

This drops you into an EL9 shell. From there, set up CMSSW:

```bash
source /cvmfs/cms.cern.ch/cmsset_default.sh
cd /cvmfs/cms.cern.ch/el9_amd64_gcc13/cms/cmssw/CMSSW_16_0_0_pre4/
cmsenv
cd -
```

Or equivalently:

```bash
source mysetup.sh
```

## Compile

```bash
cd skimmer/
make clean
make -j4
```

This produces the `skim` executable in `skimmer/`.

## Run Interactively

```bash
./skim <input_file(s)> -t Events -T Events -a <analysis_tag> -d ./ -n output
```

### Required Options

| Option | Description |
|--------|-------------|
| `-t Events` | Input TTree name |
| `-T Events` | Output TTree name |
| `-a <tag>` | Analysis to run (see below) |
| `-d <dir>` | Output directory |
| `-n <name>` | Output file name (without `.root`) |

### Available Analysis Tags

`4Lep`, `3Lep`, `2Lep2FJ`, `2Lep1FJ`, `1Lep1FJ`, `0Lep3FJ`, `0Lep2FJ`, `0Lep1FJ`, `0Lep0FJ`

### Optional Flags

| Flag | Description |
|------|-------------|
| `--is_data` | Run on data |
| `--is_signal` | Run on signal MC |
| `--dump_truth` | Dump truth info (signal only) |
| `--debug` | Enable debug output |
| `-V <variation>` | Systematic variation (`up`, `down`, `nominal`) |
| `-s <factor>` | Global event weight scale factor |

### Example

```bash
./skim root://cmsxrootd.fnal.gov//store/mc/.../file.root \
    -t Events -T Events -a 2Lep1FJ -d ./ -n test_output
```

## Condor Submission

Build the tarball and submit:

```bash
cd skimmer/condor/
./maketar.sh
python submit.py
```

`maketar.sh` compiles, records the git state, and packages `skim`, `data/`, and `gitversion.txt` into `package.tar.xz`. The condor jobs run inside an EL9 Singularity container (`+SingularityImage` is set in `submit.py`).
