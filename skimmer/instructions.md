# Skimmer Build and Run Instructions

## Prerequisites

The login node (UAF) runs EL8. The skimmer supports two target architectures:

| Architecture | SCRAM_ARCH | CMSSW | Singularity needed on UAF? |
|---|---|---|---|
| **EL8** (default) | `el8_amd64_gcc12` | `CMSSW_14_1_0_pre4` | No |
| **EL9** | `el9_amd64_gcc13` | `CMSSW_16_0_0_pre4` | Yes |

## Set Up the Environment

### EL8 (default, no singularity needed)

Since UAF is already EL8, just source the setup script directly:

```bash
source mysetup.sh          # defaults to el8
# or explicitly:
source mysetup.sh el8
```

### EL9 (requires singularity)

First enter the EL9 Singularity container, then source the setup:

```bash
/cvmfs/cms.cern.ch/common/cmssw-el9 -B/ceph
source mysetup.sh el9
```

## Compile

```bash
cd skimmer/
make clean
make -j4
```

This produces the `skim` executable in `skimmer/`. The Makefile auto-detects the correctionlib path based on `$SCRAM_ARCH`.

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

**Important:** `submit.py` must be run **outside** any singularity container, since `condor_submit` is not available inside it.

### Build the tarball and submit

```bash
# Set up the environment (inside singularity for el9, directly for el8)
source mysetup.sh          # el8 (default)
# source mysetup.sh el9   # or el9 (inside cmssw-el9 singularity)

# Build the tarball
cd skimmer/condor/
./maketar.sh

# Exit singularity if you are in one, then submit
cd skimmer/condor/
python3 submit.py              # defaults to --arch el8
# python3 submit.py --arch el9  # for el9 (uses singularity on condor workers)
```

### submit.py options

| Option | Description |
|--------|-------------|
| `--arch el8` | EL8 target (default). No singularity on condor workers. |
| `--arch el9` | EL9 target. Condor jobs run inside an EL9 singularity container. |

`maketar.sh` compiles, records the git state, and packages `skim`, `data/`, and `gitversion.txt` into `package.tar.xz`.
