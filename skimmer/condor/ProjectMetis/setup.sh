#!/bin/bash

# Usage: source setup.sh [el8|el9]
# Default: el8

ARCH=${1:-el8}

[ ! -z "$CMSSW_BASE" ] || {
    [ -e /cvmfs/ ] && {
        source /cvmfs/cms.cern.ch/cmsset_default.sh

        if [ "$ARCH" == "el8" ]; then
            export SCRAM_ARCH=el8_amd64_gcc12
            export CMSSW_VERSION=CMSSW_14_1_0_pre4
        elif [ "$ARCH" == "el9" ]; then
            export SCRAM_ARCH=el9_amd64_gcc13
            export CMSSW_VERSION=CMSSW_16_0_0_pre4
        else
            echo "Unknown architecture: $ARCH (use el8 or el9)"
            return 1
        fi

        cd /cvmfs/cms.cern.ch/$SCRAM_ARCH/cms/cmssw/$CMSSW_VERSION/src && eval `scramv1 runtime -sh` && cd -
    }
}

export METIS_BASE="$( cd "$(dirname "$BASH_SOURCE")" ; pwd -P )"

# CRAB screws up our PYTHONPATH. Go figure.
export PYTHONPATH=${METIS_BASE}:$PYTHONPATH

# Add some scripts to the path
export PATH=${METIS_BASE}/scripts:$PATH

export USEDASGOCLIENT=x # or USEDASGOCLIENT= to fall back to dis

# export GRIDUSER=$(voms-proxy-info -identity -dont-verify-ac | cut -d '/' -f6 | cut -d '=' -f2)
export GRIDUSER=$(voms-proxy-info -identity | cut -d '/' -f6 | cut -d '=' -f2)
