#!/bin/bash

# Usage: source mysetup.sh [el8|el9]
# Default: el8

ARCH=${1:-el8}

source /cvmfs/cms.cern.ch/cmsset_default.sh

if [ "$ARCH" == "el8" ]; then
    cd /cvmfs/cms.cern.ch/el8_amd64_gcc12/cms/cmssw/CMSSW_14_1_0_pre4/ ; cmsenv ; cd -
elif [ "$ARCH" == "el9" ]; then
    cd /cvmfs/cms.cern.ch/el9_amd64_gcc13/cms/cmssw/CMSSW_16_0_0_pre4/ ; cmsenv ; cd -
else
    echo "Unknown architecture: $ARCH (use el8 or el9)"
    return 1
fi

echo "Setup $ARCH environment with CMSSW:"
echo "  SCRAM_ARCH = $SCRAM_ARCH"
echo "  CMSSW_VERSION = $CMSSW_VERSION"
