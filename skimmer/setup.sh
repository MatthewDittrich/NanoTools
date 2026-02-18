#!/bin/bash

# Usage: source setup.sh [el8|el9]
# Default: el8

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

ARCH=${1:-el8}

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

cd /cvmfs/cms.cern.ch/$SCRAM_ARCH/cms/cmssw/$CMSSW_VERSION/src
eval `scramv1 runtime -sh`
cd - > /dev/null

echo "Setup $ARCH environment:"
echo "  SCRAM_ARCH = $SCRAM_ARCH"
echo "  CMSSW_VERSION = $CMSSW_VERSION"
which root

#eof
