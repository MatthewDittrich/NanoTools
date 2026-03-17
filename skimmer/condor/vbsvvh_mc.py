#!/bin/env python
from metis.Sample import DBSSample, DirectorySample

nanoaodv9_test = [
    DBSSample(dataset="/QCD_HT100to200_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM"),
    DBSSample(dataset="/QCD_HT100to200_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"),
    DBSSample(dataset="/QCD_HT100to200_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM"),
    DBSSample(dataset="/QCD_HT100to200_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM"),
]

nanoaodv9_bkg = [
    # TTToHadronic: /TTToHadronic_TuneCP5_13TeV*/*NanoAOD*v9-106X*/NANOAODSIM
    DBSSample(dataset="/TTToHadronic_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM"),
    DBSSample(dataset="/TTToHadronic_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"),
    DBSSample(dataset="/TTToHadronic_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM"),
    DBSSample(dataset="/TTToHadronic_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM"),
    # TTToSemiLeptonic: /TTToSemiLeptonic_TuneCP5_13TeV*/*NanoAOD*v9-106X*/NANOAODSIM
    DBSSample(dataset="/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM"),
    DBSSample(dataset="/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"),
    DBSSample(dataset="/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM"),
    DBSSample(dataset="/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM"),
    # QCD (50 <= HT < 100): /QCD_HT50to100*_TuneCP5_PSWeights_13TeV-madgraph-pythia8/*NanoAOD*v9-106X*/NANOAODSIM
    DBSSample(dataset="/QCD_HT50to100_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM"), # low stats
    DBSSample(dataset="/QCD_HT50to100_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"), # low stats
    DBSSample(dataset="/QCD_HT50to100_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM"), # low stats
    DBSSample(dataset="/QCD_HT50to100_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM"), # low stats
    # QCD (100 <= HT < 200): /QCD_HT100to200*_TuneCP5_PSWeights_13TeV-madgraph-pythia8/*NanoAOD*v9-106X*/NANOAODSIM
    DBSSample(dataset="/QCD_HT100to200_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM"),
    DBSSample(dataset="/QCD_HT100to200_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"),
    DBSSample(dataset="/QCD_HT100to200_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM"),
    DBSSample(dataset="/QCD_HT100to200_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM"),
    # QCD (200 <= HT < 300): /QCD_HT200to300*_TuneCP5_PSWeights_13TeV-madgraph-pythia8/*NanoAOD*v9-106X*/NANOAODSIM
    DBSSample(dataset="/QCD_HT200to300_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM"),
    DBSSample(dataset="/QCD_HT200to300_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"),
    DBSSample(dataset="/QCD_HT200to300_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM"),
    DBSSample(dataset="/QCD_HT200to300_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM"),
    # QCD (300 <= HT < 500): /QCD_HT300to500*_TuneCP5_PSWeights_13TeV-madgraph-pythia8/*NanoAOD*v9-106X*/NANOAODSIM
    DBSSample(dataset="/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM"),
    DBSSample(dataset="/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"),
    DBSSample(dataset="/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM"),
    DBSSample(dataset="/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM"),
    # QCD (500 <= HT < 700): /QCD_HT500to700*_TuneCP5_PSWeights_13TeV-madgraph-pythia8/*NanoAOD*v9-106X*/NANOAODSIM
    DBSSample(dataset="/QCD_HT500to700_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM"),
    DBSSample(dataset="/QCD_HT500to700_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"),
    DBSSample(dataset="/QCD_HT500to700_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM"),
    DBSSample(dataset="/QCD_HT500to700_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM"),
    # QCD (700 <= HT < 1000): /QCD_HT700to1000*_TuneCP5_PSWeights_13TeV-madgraph-pythia8/*NanoAOD*v9-106X*/NANOAODSIM
    DBSSample(dataset="/QCD_HT700to1000_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM"),
    DBSSample(dataset="/QCD_HT700to1000_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"),
    DBSSample(dataset="/QCD_HT700to1000_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM"),
    DBSSample(dataset="/QCD_HT700to1000_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM"),
    # QCD (1000 <= HT < 1500): /QCD_HT1000to1500*_TuneCP5_PSWeights_13TeV-madgraph-pythia8/*NanoAOD*v9-106X*/NANOAODSIM
    DBSSample(dataset="/QCD_HT1000to1500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM"),
    DBSSample(dataset="/QCD_HT1000to1500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"),
    DBSSample(dataset="/QCD_HT1000to1500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM"),
    DBSSample(dataset="/QCD_HT1000to1500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM"),
    # QCD (1500 <= HT < 2000): /QCD_HT1500to2000*_TuneCP5_PSWeights_13TeV-madgraph-pythia8/*NanoAOD*v9-106X*/NANOAODSIM
    DBSSample(dataset="/QCD_HT1500to2000_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM"),
    DBSSample(dataset="/QCD_HT1500to2000_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"),
    DBSSample(dataset="/QCD_HT1500to2000_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM"),
    DBSSample(dataset="/QCD_HT1500to2000_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM"),
    # QCD (2000 <= HT < Inf): /QCD_HT200toInf*_TuneCP5_PSWeights_13TeV-madgraph-pythia8/*NanoAOD*v9-106X*/NANOAODSIM
    DBSSample(dataset="/QCD_HT2000toInf_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM"),
    DBSSample(dataset="/QCD_HT2000toInf_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"),
    DBSSample(dataset="/QCD_HT2000toInf_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM"),
    DBSSample(dataset="/QCD_HT2000toInf_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM"),
    # TTH (H to bb)
    DBSSample(dataset="/ttHTobb_M125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM"),
    DBSSample(dataset="/ttHTobb_M125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM"),
    DBSSample(dataset="/ttHTobb_M125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM"),
    DBSSample(dataset="/ttHTobb_M125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM"),
    # TTH (H to non-bb)
    DBSSample(dataset="/ttHToNonbb_M125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM"),
    DBSSample(dataset="/ttHToNonbb_M125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM"),
    DBSSample(dataset="/ttHToNonbb_M125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM"),
    DBSSample(dataset="/ttHToNonbb_M125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM"),
    # TTW
    DBSSample(dataset="/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM"),
    DBSSample(dataset="/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"),
    DBSSample(dataset="/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM"),
    DBSSample(dataset="/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM"),
    # TTWW
    DBSSample(dataset="/TTWW_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM"),
    DBSSample(dataset="/TTWW_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"),
    DBSSample(dataset="/TTWW_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM"),
    DBSSample(dataset="/TTWW_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM"),
    # TTWZ
    DBSSample(dataset="/TTWZ_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM"),
    DBSSample(dataset="/TTWZ_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"),
    DBSSample(dataset="/TTWZ_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM"),
    DBSSample(dataset="/TTWZ_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM"),
    # TTbb
    DBSSample(dataset="/TTbb_4f_TTToHadronic_TuneCP5-Powheg-Openloops-Pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"),
    DBSSample(dataset="/TTbb_4f_TTToHadronic_TuneCP5-Powheg-Openloops-Pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM"),
    DBSSample(dataset="/TTbb_4f_TTToHadronic_TuneCP5-Powheg-Openloops-Pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM"),
    DBSSample(dataset="/TTbb_4f_TTToHadronic_TuneCP5-Powheg-Openloops-Pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM"),
    # ST (t-channel, top): /ST_t-channel_top_4f_InclusiveDecays_TuneCP5_13TeV*/*NanoAOD*v9-106X*/NANOAODSIM
    DBSSample(dataset="/ST_t-channel_top_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM"),
    DBSSample(dataset="/ST_t-channel_top_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"),
    DBSSample(dataset="/ST_t-channel_top_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM"),
    DBSSample(dataset="/ST_t-channel_top_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM"),
    # ST (t-channel, antitop): /ST_t-channel_antitop_4f_InclusiveDecays_TuneCP5_13TeV*/*NanoAOD*v9-106X*/NANOAODSIM
    DBSSample(dataset="/ST_t-channel_antitop_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM"),
    DBSSample(dataset="/ST_t-channel_antitop_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"),
    DBSSample(dataset="/ST_t-channel_antitop_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM"),
    DBSSample(dataset="/ST_t-channel_antitop_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM"),
    # ST (tW, top): /ST_tW_top_5f_inclusive*/*NanoAOD*v9-106X*/NANOAODSIM
    DBSSample(dataset="/ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM"),
    DBSSample(dataset="/ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM"),
    DBSSample(dataset="/ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM"),
    DBSSample(dataset="/ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM"),
    # ST (tW, antitop): /ST_tW_antitop_5f_inclusive*/*NanoAOD*v9-106X*/NANOAODSIM
    DBSSample(dataset="/ST_tW_antitop_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM"),
    DBSSample(dataset="/ST_tW_antitop_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM"),
    DBSSample(dataset="/ST_tW_antitop_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM"),
    DBSSample(dataset="/ST_tW_antitop_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM"),
    # WJetsToQQ (200 <= HT < 400): /WJetsToQQ_HT-200to400*/*NanoAOD*v9-106X*/NANOAODSIM
    DBSSample(dataset="/WJetsToQQ_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM"),
    DBSSample(dataset="/WJetsToQQ_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM"),
    DBSSample(dataset="/WJetsToQQ_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM"),
    DBSSample(dataset="/WJetsToQQ_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM"),
    # WJetsToQQ (400 <= HT < 600): /WJetsToQQ_HT-400to600*/*NanoAOD*v9-106X*/NANOAODSIM
    DBSSample(dataset="/WJetsToQQ_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM"),
    DBSSample(dataset="/WJetsToQQ_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM"),
    DBSSample(dataset="/WJetsToQQ_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM"),
    DBSSample(dataset="/WJetsToQQ_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM"),
    # WJetsToQQ (600 <= HT < 800): /WJetsToQQ_HT-600to800*/*NanoAOD*v9-106X*/NANOAODSIM
    DBSSample(dataset="/WJetsToQQ_HT-600to800_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM"),
    DBSSample(dataset="/WJetsToQQ_HT-600to800_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM"),
    DBSSample(dataset="/WJetsToQQ_HT-600to800_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM"),
    DBSSample(dataset="/WJetsToQQ_HT-600to800_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM"),
    # WJetsToQQ (800 <= HT < Inf): /WJetsToQQ_HT-800toInf*/*NanoAOD*v9-106X*/NANOAODSIM
    DBSSample(dataset="/WJetsToQQ_HT-800toInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM"),
    DBSSample(dataset="/WJetsToQQ_HT-800toInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM"),
    DBSSample(dataset="/WJetsToQQ_HT-800toInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM"),
    DBSSample(dataset="/WJetsToQQ_HT-800toInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM"),
    # ZJetsToQQ (200 <= HT < 400): /ZJetsToQQ_HT-200to400*/*NanoAOD*v9-106X*/NANOAODSIM
    DBSSample(dataset="/ZJetsToQQ_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM"),
    DBSSample(dataset="/ZJetsToQQ_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM"),
    DBSSample(dataset="/ZJetsToQQ_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM"),
    DBSSample(dataset="/ZJetsToQQ_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM"),
    # ZJetsToQQ (400 <= HT < 600): /ZJetsToQQ_HT-400to600*/*NanoAOD*v9-106X*/NANOAODSIM
    DBSSample(dataset="/ZJetsToQQ_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM"),
    DBSSample(dataset="/ZJetsToQQ_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM"),
    DBSSample(dataset="/ZJetsToQQ_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM"),
    DBSSample(dataset="/ZJetsToQQ_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM"),
    # ZJetsToQQ (600 <= HT < 800): /ZJetsToQQ_HT-600to800*/*NanoAOD*v9-106X*/NANOAODSIM
    DBSSample(dataset="/ZJetsToQQ_HT-600to800_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM"),
    DBSSample(dataset="/ZJetsToQQ_HT-600to800_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM"),
    DBSSample(dataset="/ZJetsToQQ_HT-600to800_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM"),
    DBSSample(dataset="/ZJetsToQQ_HT-600to800_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM"),
    # ZJetsToQQ (800 <= HT < Inf): /ZJetsToQQ_HT-800toInf*/*NanoAOD*v9-106X*/NANOAODSIM
    DBSSample(dataset="/ZJetsToQQ_HT-800toInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM"),
    DBSSample(dataset="/ZJetsToQQ_HT-800toInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM"),
    DBSSample(dataset="/ZJetsToQQ_HT-800toInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM"),
    DBSSample(dataset="/ZJetsToQQ_HT-800toInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM"),
    # WW (WW to qqqq): /WWTo4Q*/*NanoAOD*v9-106X*/NANOAODSIM
    DBSSample(dataset="/WWTo4Q_4f_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v3/NANOAODSIM"),
    DBSSample(dataset="/WWTo4Q_4f_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"),
    DBSSample(dataset="/WWTo4Q_4f_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM"),
    DBSSample(dataset="/WWTo4Q_4f_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM"),
    # WW (WW to lnuqq): /WWTo1L1Nu2Q*/*NanoAOD*v9-106X*/NANOAODSIM
    DBSSample(dataset="/WWTo1L1Nu2Q_4f_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"),
    DBSSample(dataset="/WWTo1L1Nu2Q_4f_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM"),
    DBSSample(dataset="/WWTo1L1Nu2Q_4f_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM"),
    DBSSample(dataset="/WWTo1L1Nu2Q_4f_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM"),
    # WZ (W to qq, Z to ll): /WZTo2Q2L*/*NanoAOD*v9-106X*/NANOAODSIM
    DBSSample(dataset="/WZTo2Q2L_mllmin4p0_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM"),
    DBSSample(dataset="/WZTo2Q2L_mllmin4p0_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM"),
    DBSSample(dataset="/WZTo2Q2L_mllmin4p0_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM"),
    DBSSample(dataset="/WZTo2Q2L_mllmin4p0_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM"),
    # WZ (W to lnu, Z to qq): /WZTo1L1Nu2Q*/*NanoAOD*v9-106X*/NANOAODSIM
    DBSSample(dataset="/WZTo1L1Nu2Q_4f_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"),
    DBSSample(dataset="/WZTo1L1Nu2Q_4f_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM"),
    DBSSample(dataset="/WZTo1L1Nu2Q_4f_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM"),
    DBSSample(dataset="/WZTo1L1Nu2Q_4f_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM"),
    # ZZ (ZZ to nunuqq): /ZZTo2Nu2Qu*/*NanoAOD*v9*-106X*/NANOAODSIM
    DBSSample(dataset="/ZZTo2Nu2Q_5f_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM"),
    DBSSample(dataset="/ZZTo2Nu2Q_5f_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"),
    DBSSample(dataset="/ZZTo2Nu2Q_5f_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM"),
    DBSSample(dataset="/ZZTo2Nu2Q_5f_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM"),
    # ZZ (ZZ to qqqq): /ZZTo4Q*/*NanoAOD*v9*-106X*/NANOAODSIM
    DBSSample(dataset="/ZZTo4Q_5f_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM"),
    DBSSample(dataset="/ZZTo4Q_5f_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"),
    DBSSample(dataset="/ZZTo4Q_5f_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM"),
    DBSSample(dataset="/ZZTo4Q_5f_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM"),
    # ZZ (ZZ to qqll): /ZZTo2Q2L*/*NanoAOD*v9*-106X*/NANOAODSIM
    DBSSample(dataset="/ZZTo2Q2L_mllmin4p0_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM"),
    DBSSample(dataset="/ZZTo2Q2L_mllmin4p0_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"),
    DBSSample(dataset="/ZZTo2Q2L_mllmin4p0_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM"),
    DBSSample(dataset="/ZZTo2Q2L_mllmin4p0_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM"),
    # WWW
    DBSSample(dataset="/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11_ext1-v1/NANOAODSIM"),
    DBSSample(dataset="/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17_ext1-v1/NANOAODSIM"),
    DBSSample(dataset="/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9_ext1-v2/NANOAODSIM"),
    DBSSample(dataset="/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1_ext1-v2/NANOAODSIM"),
    # WWZ
    DBSSample(dataset="/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11_ext1-v1/NANOAODSIM"),
    DBSSample(dataset="/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17_ext1-v1/NANOAODSIM"),
    DBSSample(dataset="/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM"),
    DBSSample(dataset="/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1_ext1-v2/NANOAODSIM"),
    # WZZ
    DBSSample(dataset="/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11_ext1-v1/NANOAODSIM"),
    DBSSample(dataset="/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17_ext1-v1/NANOAODSIM"),
    DBSSample(dataset="/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9_ext1-v2/NANOAODSIM"),
    DBSSample(dataset="/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1_ext1-v2/NANOAODSIM"),
    # ZZZ
    DBSSample(dataset="/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11_ext1-v1/NANOAODSIM"),
    DBSSample(dataset="/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17_ext1-v1/NANOAODSIM"),
    DBSSample(dataset="/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9_ext1-v2/NANOAODSIM"),
    DBSSample(dataset="/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1_ext1-v2/NANOAODSIM"),
    # VH (H to non-bb)
    DBSSample(dataset="/VHToNonbb_M125_TuneCP5_13TeV-amcatnloFXFX_madspin_pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM"),
    DBSSample(dataset="/VHToNonbb_M125_TuneCP5_13TeV-amcatnloFXFX_madspin_pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM"),
    DBSSample(dataset="/VHToNonbb_M125_TuneCP5_13TeV-amcatnloFXFX_madspin_pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM"),
    DBSSample(dataset="/VHToNonbb_M125_TuneCP5_13TeV-amcatnloFXFX_madspin_pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM"),
    # W-H (W- to lnu): /WminusH_HToBB_WToLNu_M-125_TuneCP5_13TeV*/*NanoAOD*v9-106X*/NANOAODSIM
    DBSSample(dataset="/WminusH_HToBB_WToLNu_M-125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM"),
    DBSSample(dataset="/WminusH_HToBB_WToLNu_M-125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"),
    DBSSample(dataset="/WminusH_HToBB_WToLNu_M-125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM"),
    DBSSample(dataset="/WminusH_HToBB_WToLNu_M-125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM"),
    # W+H (W+ to lnu): /WminusH_HToBB_WToLNu_M-125_TuneCP5_13TeV*/*NanoAOD*v9-106X*/NANOAODSIM
    DBSSample(dataset="/WplusH_HToBB_WToLNu_M-125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM"),
    DBSSample(dataset="/WplusH_HToBB_WToLNu_M-125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"),
    DBSSample(dataset="/WplusH_HToBB_WToLNu_M-125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM"),
    DBSSample(dataset="/WplusH_HToBB_WToLNu_M-125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM"),
    # ZH (Z to qq): /ZH_HToBB_ZToQQ_M-125*/*NanoAOD*v9-106X*/NANOAODSIM
    DBSSample(dataset="/ZH_HToBB_ZToQQ_M-125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM"),
    DBSSample(dataset="/ZH_HToBB_ZToQQ_M-125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM"),
    DBSSample(dataset="/ZH_HToBB_ZToQQ_M-125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM"),
    DBSSample(dataset="/ZH_HToBB_ZToQQ_M-125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"),
    # EWK W+ (W+ to qq)
    DBSSample(dataset="/EWKWplus2Jets_WToQQ_dipoleRecoilOn_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM"),
    DBSSample(dataset="/EWKWplus2Jets_WToQQ_dipoleRecoilOn_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"),
    DBSSample(dataset="/EWKWplus2Jets_WToQQ_dipoleRecoilOn_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM"),
    DBSSample(dataset="/EWKWplus2Jets_WToQQ_dipoleRecoilOn_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM"),
    # EWK W- (W- to qq)
    DBSSample(dataset="/EWKWminus2Jets_WToQQ_dipoleRecoilOn_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM"),
    DBSSample(dataset="/EWKWminus2Jets_WToQQ_dipoleRecoilOn_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"),
    DBSSample(dataset="/EWKWminus2Jets_WToQQ_dipoleRecoilOn_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM"),
    DBSSample(dataset="/EWKWminus2Jets_WToQQ_dipoleRecoilOn_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM"),
    # EWK Z (Z to ll)
    DBSSample(dataset="/EWKZ2Jets_ZToLL_M-50_TuneCP5_withDipoleRecoil_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM"),
    DBSSample(dataset="/EWKZ2Jets_ZToLL_M-50_TuneCP5_withDipoleRecoil_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"),
    DBSSample(dataset="/EWKZ2Jets_ZToLL_M-50_TuneCP5_withDipoleRecoil_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM"),
    DBSSample(dataset="/EWKZ2Jets_ZToLL_M-50_TuneCP5_withDipoleRecoil_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM"),
    # EWK Z (Z to nunu)
    DBSSample(dataset="/EWKZ2Jets_ZToNuNu_M-50_TuneCP5_withDipoleRecoil_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM"),
    DBSSample(dataset="/EWKZ2Jets_ZToNuNu_M-50_TuneCP5_withDipoleRecoil_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM"),
    DBSSample(dataset="/EWKZ2Jets_ZToNuNu_M-50_TuneCP5_withDipoleRecoil_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM"),
    DBSSample(dataset="/EWKZ2Jets_ZToNuNu_M-50_TuneCP5_withDipoleRecoil_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM"),
    # EWK Z (Z to qq)
    DBSSample(dataset="/EWKZ2Jets_ZToQQ_dipoleRecoilOn_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM"),
    DBSSample(dataset="/EWKZ2Jets_ZToQQ_dipoleRecoilOn_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"),
    DBSSample(dataset="/EWKZ2Jets_ZToQQ_dipoleRecoilOn_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM"),
    DBSSample(dataset="/EWKZ2Jets_ZToQQ_dipoleRecoilOn_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM"),
    # EWK WZ
    DBSSample(dataset="/WZJJ_EWK_InclusivePolarization_TuneCP5_13TeV_madgraph-madspin-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM"),
    DBSSample(dataset="/WZJJ_EWK_InclusivePolarization_TuneCP5_13TeV_madgraph-madspin-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"),
    DBSSample(dataset="/WZJJ_EWK_InclusivePolarization_TuneCP5_13TeV_madgraph-madspin-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM"),
    DBSSample(dataset="/WZJJ_EWK_InclusivePolarization_TuneCP5_13TeV_madgraph-madspin-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM"),
    #TTTo2L2Nu
    DBSSample(dataset="/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM"),
    DBSSample(dataset="/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"),
    DBSSample(dataset="/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM"),
    DBSSample(dataset="/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM"),
    #ST_s-channel_4f_leptonDecays
    DBSSample(dataset="/ST_s-channel_4f_leptonDecays_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM"),
    DBSSample(dataset="/ST_s-channel_4f_leptonDecays_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"),
    DBSSample(dataset="/ST_s-channel_4f_leptonDecays_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM"),
    DBSSample(dataset="/ST_s-channel_4f_leptonDecays_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM"),
    #WJetsToLNu_HT-70To100
    DBSSample(dataset="/WJetsToLNu_HT-70To100_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM"),
    DBSSample(dataset="/WJetsToLNu_HT-70To100_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"),
    DBSSample(dataset="/WJetsToLNu_HT-70To100_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM"),
    DBSSample(dataset="/WJetsToLNu_HT-70To100_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM"),
    #WJetsToLNu_HT-100To200
    DBSSample(dataset="/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM"),
    DBSSample(dataset="/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"),
    DBSSample(dataset="/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM"),
    DBSSample(dataset="/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM"),
    #WJetsToLNu_HT-200To400
    DBSSample(dataset="/WJetsToLNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM"),
    DBSSample(dataset="/WJetsToLNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"),
    DBSSample(dataset="/WJetsToLNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM"),
    DBSSample(dataset="/WJetsToLNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM"),
    #WJetsToLNu_HT-400To600
    DBSSample(dataset="/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM"),
    DBSSample(dataset="/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"),
    DBSSample(dataset="/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM"),
    DBSSample(dataset="/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM"),
    #WJetsToLNu_HT-600To800
    DBSSample(dataset="/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM"),
    DBSSample(dataset="/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"),
    DBSSample(dataset="/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM"),
    DBSSample(dataset="/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM"),
    #WJetsToLNu_HT-800To1200
    DBSSample(dataset="/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM"),
    DBSSample(dataset="/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"),
    DBSSample(dataset="/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v3/NANOAODSIM"),
    DBSSample(dataset="/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM"),
    #WJetsToLNu_HT-1200To2500
    DBSSample(dataset="/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM"),
    DBSSample(dataset="/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"),
    DBSSample(dataset="/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM"),
    DBSSample(dataset="/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM"),
    #WJetsToLNu_HT-2500ToInf
    DBSSample(dataset="/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM"),
    DBSSample(dataset="/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM"),
    DBSSample(dataset="/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM"),
    DBSSample(dataset="/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM"),
    #WJetsToLNu
    DBSSample(dataset="/WJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM"),
    DBSSample(dataset="/WJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM"),
    DBSSample(dataset="/WJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM"),
    DBSSample(dataset="/WJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM"),
    #DYJetsToLL_M-10to50
    DBSSample(dataset="/DYJetsToLL_M-10to50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM"),
    DBSSample(dataset="/DYJetsToLL_M-10to50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"),
    DBSSample(dataset="/DYJetsToLL_M-10to50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM"),
    DBSSample(dataset="/DYJetsToLL_M-10to50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM"),
    #DYJetsToLL_M-50
    DBSSample(dataset="/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM"),
    DBSSample(dataset="/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"),
    DBSSample(dataset="/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM"),
    DBSSample(dataset="/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM"),
    #EWKWMinus2Jets_WToLNu_M-50
    DBSSample(dataset="/EWKWMinus2Jets_WToLNu_M-50_TuneCP5_withDipoleRecoil_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM"),
    DBSSample(dataset="/EWKWMinus2Jets_WToLNu_M-50_TuneCP5_withDipoleRecoil_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"),
    DBSSample(dataset="/EWKWMinus2Jets_WToLNu_M-50_TuneCP5_withDipoleRecoil_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM"),
    DBSSample(dataset="/EWKWMinus2Jets_WToLNu_M-50_TuneCP5_withDipoleRecoil_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM"),
    #EWKWPlus2Jets_WToLNu_M-50
    DBSSample(dataset="/EWKWPlus2Jets_WToLNu_M-50_TuneCP5_withDipoleRecoil_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM"),
    DBSSample(dataset="/EWKWPlus2Jets_WToLNu_M-50_TuneCP5_withDipoleRecoil_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"),
    DBSSample(dataset="/EWKWPlus2Jets_WToLNu_M-50_TuneCP5_withDipoleRecoil_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM"),
    DBSSample(dataset="/EWKWPlus2Jets_WToLNu_M-50_TuneCP5_withDipoleRecoil_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM"),
    #TTWJetsToLNu
    DBSSample(dataset="/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM"),
    DBSSample(dataset="/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"),
    DBSSample(dataset="/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM"),
    DBSSample(dataset="/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM"),
    #TTZToLLNuNu_M-10
    DBSSample(dataset="/TTZToLLNuNu_M-10_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM"),
    DBSSample(dataset="/TTZToLLNuNu_M-10_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"),
    DBSSample(dataset="/TTZToLLNuNu_M-10_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM"),
    DBSSample(dataset="/TTZToLLNuNu_M-10_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM"),
    #TTbb_4f_TTTo2L2Nu
    DBSSample(dataset="/TTbb_4f_TTTo2L2Nu_TuneCP5-Powheg-Openloops-Pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM"),
    DBSSample(dataset="/TTbb_4f_TTTo2L2Nu_TuneCP5-Powheg-Openloops-Pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"),
    DBSSample(dataset="/TTbb_4f_TTTo2L2Nu_TuneCP5-Powheg-Openloops-Pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM"),
    DBSSample(dataset="/TTbb_4f_TTTo2L2Nu_TuneCP5-Powheg-Openloops-Pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM"),
    #TTbb_4f_TTToSemiLeptonic
    DBSSample(dataset="/TTbb_4f_TTToSemiLeptonic_TuneCP5-Powheg-Openloops-Pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM"),
    DBSSample(dataset="/TTbb_4f_TTToSemiLeptonic_TuneCP5-Powheg-Openloops-Pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"),
    DBSSample(dataset="/TTbb_4f_TTToSemiLeptonic_TuneCP5-Powheg-Openloops-Pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM"),
    DBSSample(dataset="/TTbb_4f_TTToSemiLeptonic_TuneCP5-Powheg-Openloops-Pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM"),
    #ttWJets
    DBSSample(dataset="/ttWJets_TuneCP5_13TeV_madgraphMLM_pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM"),
    DBSSample(dataset="/ttWJets_TuneCP5_13TeV_madgraphMLM_pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"),
    DBSSample(dataset="/ttWJets_TuneCP5_13TeV_madgraphMLM_pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM"),
    DBSSample(dataset="/ttWJets_TuneCP5_13TeV_madgraphMLM_pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM"),
    #ttZJets
    DBSSample(dataset="/ttZJets_TuneCP5_13TeV_madgraphMLM_pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM"),
    DBSSample(dataset="/ttZJets_TuneCP5_13TeV_madgraphMLM_pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"),
    DBSSample(dataset="/ttZJets_TuneCP5_13TeV_madgraphMLM_pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM"),
    DBSSample(dataset="/ttZJets_TuneCP5_13TeV_madgraphMLM_pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM"),
    #VBFWH_HToBB_WToLNu_M-125_dipoleRecoilOn
    DBSSample(dataset="/VBFWH_HToBB_WToLNu_M-125_dipoleRecoilOn_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM"),
    DBSSample(dataset="/VBFWH_HToBB_WToLNu_M-125_dipoleRecoilOn_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"),
    DBSSample(dataset="/VBFWH_HToBB_WToLNu_M-125_dipoleRecoilOn_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM"),
    DBSSample(dataset="/VBFWH_HToBB_WToLNu_M-125_dipoleRecoilOn_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM"),
    #WWJJToLNuLNu_EWK_noTop
    DBSSample(dataset="/WWJJToLNuLNu_EWK_noTop_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM"),
    DBSSample(dataset="/WWJJToLNuLNu_EWK_noTop_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"),
    DBSSample(dataset="/WWJJToLNuLNu_EWK_noTop_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM"),
    DBSSample(dataset="/WWJJToLNuLNu_EWK_noTop_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM"),
    #WWTo2L2Nu
    DBSSample(dataset="/WWTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM"),
    DBSSample(dataset="/WWTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"),
    DBSSample(dataset="/WWTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM"),
    DBSSample(dataset="/WWTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM"),
    #WZTo1L3Nu_4f
    DBSSample(dataset="/WZTo1L3Nu_4f_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM"),
    DBSSample(dataset="/WZTo1L3Nu_4f_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"),
    DBSSample(dataset="/WZTo1L3Nu_4f_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM"),
    DBSSample(dataset="/WZTo1L3Nu_4f_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM"),
    #WZTo3LNu
    DBSSample(dataset="/WZTo3LNu_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM"),
    DBSSample(dataset="/WZTo3LNu_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"),
    DBSSample(dataset="/WZTo3LNu_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM"),
    DBSSample(dataset="/WZTo3LNu_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM"),
    #WminusH_HToBB_WToQQ_M-125
#    DBSSample(dataset="/WminusH_HToBB_WToQQ_M-125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODAPVv9-20UL16APVJMENano_106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM"),
    DBSSample(dataset="/WminusH_HToBB_WToQQ_M-125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"),
    DBSSample(dataset="/WminusH_HToBB_WToQQ_M-125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM"),
    DBSSample(dataset="/WminusH_HToBB_WToQQ_M-125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM"),
    #WplusH_HToBB_WToQQ_M-125
#    DBSSample(dataset="/WplusH_HToBB_WToQQ_M-125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODAPVv9-20UL16APVJMENano_106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM"),
    DBSSample(dataset="/WplusH_HToBB_WToQQ_M-125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"),
    DBSSample(dataset="/WplusH_HToBB_WToQQ_M-125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM"),
    DBSSample(dataset="/WplusH_HToBB_WToQQ_M-125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM"),
    #ZH_HToBB_ZToLL_M-125
    DBSSample(dataset="/ZH_HToBB_ZToLL_M-125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM"),
    DBSSample(dataset="/ZH_HToBB_ZToLL_M-125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"),
    DBSSample(dataset="/ZH_HToBB_ZToLL_M-125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM"),
    DBSSample(dataset="/ZH_HToBB_ZToLL_M-125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM"),
    #ZH_HToBB_ZToBB_M-125
    DBSSample(dataset="/ZH_HToBB_ZToBB_M-125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM"),
    DBSSample(dataset="/ZH_HToBB_ZToBB_M-125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM"),
    DBSSample(dataset="/ZH_HToBB_ZToBB_M-125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM"),
    DBSSample(dataset="/ZH_HToBB_ZToBB_M-125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM"),
    #ZH_HToBB_ZToNuNu_M-125
    DBSSample(dataset="/ZH_HToBB_ZToNuNu_M-125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM"),
    DBSSample(dataset="/ZH_HToBB_ZToNuNu_M-125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"),
    DBSSample(dataset="/ZH_HToBB_ZToNuNu_M-125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM"),
    DBSSample(dataset="/ZH_HToBB_ZToNuNu_M-125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM"),
    #ZZJJTo4L
    DBSSample(dataset="/ZZJJTo4L_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM"),
    DBSSample(dataset="/ZZJJTo4L_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM"),
    DBSSample(dataset="/ZZJJTo4L_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM"),
    DBSSample(dataset="/ZZJJTo4L_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM"),
    #ZZTo2L2Nu
    DBSSample(dataset="/ZZTo2L2Nu_TuneCP5_13TeV_powheg_pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM"),
    DBSSample(dataset="/ZZTo2L2Nu_TuneCP5_13TeV_powheg_pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"),
    DBSSample(dataset="/ZZTo2L2Nu_TuneCP5_13TeV_powheg_pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM"),
    DBSSample(dataset="/ZZTo2L2Nu_TuneCP5_13TeV_powheg_pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM"),
    #ZZTo4L_M-1toInf
    DBSSample(dataset="/ZZTo4L_M-1toInf_TuneCP5_13TeV_powheg_pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM"),
    DBSSample(dataset="/ZZTo4L_M-1toInf_TuneCP5_13TeV_powheg_pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"),
    DBSSample(dataset="/ZZTo4L_M-1toInf_TuneCP5_13TeV_powheg_pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM"),
    DBSSample(dataset="/ZZTo4L_M-1toInf_TuneCP5_13TeV_powheg_pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM"),
    #ggZH_HToBB_ZToLL_M-125
    DBSSample(dataset="/ggZH_HToBB_ZToLL_M-125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM"),
    DBSSample(dataset="/ggZH_HToBB_ZToLL_M-125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"),
    DBSSample(dataset="/ggZH_HToBB_ZToLL_M-125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM"),
    DBSSample(dataset="/ggZH_HToBB_ZToLL_M-125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM"),
    #ggZH_HToBB_ZToBB_M-125
    DBSSample(dataset="/ggZH_HToBB_ZToBB_M-125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM"),
    DBSSample(dataset="/ggZH_HToBB_ZToBB_M-125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM"),
    DBSSample(dataset="/ggZH_HToBB_ZToBB_M-125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM"),
    DBSSample(dataset="/ggZH_HToBB_ZToBB_M-125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM"),
    #ggZH_HToBB_ZToNuNu_M-125
    DBSSample(dataset="/ggZH_HToBB_ZToNuNu_M-125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM"),
    DBSSample(dataset="/ggZH_HToBB_ZToNuNu_M-125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"),
    DBSSample(dataset="/ggZH_HToBB_ZToNuNu_M-125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM"),
    DBSSample(dataset="/ggZH_HToBB_ZToNuNu_M-125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM"),
    #ggZH_HToBB_ZToQQ_M-125
    DBSSample(dataset="/ggZH_HToBB_ZToQQ_M-125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM"),
    DBSSample(dataset="/ggZH_HToBB_ZToQQ_M-125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"),
    DBSSample(dataset="/ggZH_HToBB_ZToQQ_M-125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM"),
    DBSSample(dataset="/ggZH_HToBB_ZToQQ_M-125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM"),
    #WZ
    DBSSample(dataset="/WZ_TuneCP5_13TeV-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM"),
    DBSSample(dataset="/WZ_TuneCP5_13TeV-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"),
    DBSSample(dataset="/WZ_TuneCP5_13TeV-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM"),
    DBSSample(dataset="/WZ_TuneCP5_13TeV-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM"),
    #WW
    DBSSample(dataset="/WW_TuneCP5_13TeV-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM"),
    DBSSample(dataset="/WW_TuneCP5_13TeV-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"),
    DBSSample(dataset="/WW_TuneCP5_13TeV-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM"),
    DBSSample(dataset="/WW_TuneCP5_13TeV-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM"),
    #ZZ
    DBSSample(dataset="/ZZ_TuneCP5_13TeV-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM"),
    DBSSample(dataset="/ZZ_TuneCP5_13TeV-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"),
    DBSSample(dataset="/ZZ_TuneCP5_13TeV-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM"),
    DBSSample(dataset="/ZZ_TuneCP5_13TeV-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM"),
    #GluGluHToZZTo4L_M125
    DBSSample(dataset="/GluGluHToZZTo4L_M125_TuneCP5_13TeV_powheg2_JHUGenV7011_pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM"),
    DBSSample(dataset="/GluGluHToZZTo4L_M125_TuneCP5_13TeV_powheg2_JHUGenV7011_pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM"),
    DBSSample(dataset="/GluGluHToZZTo4L_M125_TuneCP5_13TeV_powheg2_JHUGenV7011_pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM"),
    DBSSample(dataset="/GluGluHToZZTo4L_M125_TuneCP5_13TeV_powheg2_JHUGenV7011_pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM"),
    #SSWW
    DBSSample(dataset="/SSWW_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM"),
    DBSSample(dataset="/SSWW_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"),
    DBSSample(dataset="/SSWW_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM"),
    DBSSample(dataset="/SSWW_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM"),
    #TWZToLL_tlept_Wlept_5f_DR
    DBSSample(dataset="/TWZToLL_tlept_Wlept_5f_DR_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM"),
    DBSSample(dataset="/TWZToLL_tlept_Wlept_5f_DR_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"),
    DBSSample(dataset="/TWZToLL_tlept_Wlept_5f_DR_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM"),
    DBSSample(dataset="/TWZToLL_tlept_Wlept_5f_DR_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM"),
    #tZq_ll_4f_ckm_NLO
    DBSSample(dataset="/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM"),
    DBSSample(dataset="/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"),
    DBSSample(dataset="/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v1/NANOAODSIM"),
    DBSSample(dataset="/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v1/NANOAODSIM"),
    #GluGluToContinToZZTo2e2mu
    DBSSample(dataset="/GluGluToContinToZZTo2e2mu_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM"),
    DBSSample(dataset="/GluGluToContinToZZTo2e2mu_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"),
    DBSSample(dataset="/GluGluToContinToZZTo2e2mu_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM"),
    DBSSample(dataset="/GluGluToContinToZZTo2e2mu_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM"),
    #GluGluToContinToZZTo2e2tau
    DBSSample(dataset="/GluGluToContinToZZTo2e2tau_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM"),
    DBSSample(dataset="/GluGluToContinToZZTo2e2tau_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"),
    DBSSample(dataset="/GluGluToContinToZZTo2e2tau_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM"),
    DBSSample(dataset="/GluGluToContinToZZTo2e2tau_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM"),
    #GluGluToContinToZZTo2mu2tau
    DBSSample(dataset="/GluGluToContinToZZTo2mu2tau_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM"),
    DBSSample(dataset="/GluGluToContinToZZTo2mu2tau_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"),
    DBSSample(dataset="/GluGluToContinToZZTo2mu2tau_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM"),
    DBSSample(dataset="/GluGluToContinToZZTo2mu2tau_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM"),
    #GluGluToContinToZZTo4e
    DBSSample(dataset="/GluGluToContinToZZTo4e_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM"),
    DBSSample(dataset="/GluGluToContinToZZTo4e_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM"),
    DBSSample(dataset="/GluGluToContinToZZTo4e_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM"),
    DBSSample(dataset="/GluGluToContinToZZTo4e_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM"),
    #GluGluToContinToZZTo4mu
    DBSSample(dataset="/GluGluToContinToZZTo4mu_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM"),
    DBSSample(dataset="/GluGluToContinToZZTo4mu_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM"),
    DBSSample(dataset="/GluGluToContinToZZTo4mu_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM"),
    DBSSample(dataset="/GluGluToContinToZZTo4mu_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM"),
    #GluGluToContinToZZTo4tau
    DBSSample(dataset="/GluGluToContinToZZTo4tau_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM"),
    DBSSample(dataset="/GluGluToContinToZZTo4tau_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v1/NANOAODSIM"),
    DBSSample(dataset="/GluGluToContinToZZTo4tau_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM"),
    DBSSample(dataset="/GluGluToContinToZZTo4tau_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM"),
    #HZJ_HToWWTo2L2Nu_ZTo2L_M-125
    DBSSample(dataset="/HZJ_HToWWTo2L2Nu_ZTo2L_M-125_TuneCP5_13TeV-powheg-jhugen727-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v2/NANOAODSIM"),
    DBSSample(dataset="/HZJ_HToWWTo2L2Nu_ZTo2L_M-125_TuneCP5_13TeV-powheg-jhugen727-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM"),
    DBSSample(dataset="/HZJ_HToWWTo2L2Nu_ZTo2L_M-125_TuneCP5_13TeV-powheg-jhugen727-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM"),
    DBSSample(dataset="/HZJ_HToWWTo2L2Nu_ZTo2L_M-125_TuneCP5_13TeV-powheg-jhugen727-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM"),
    #GluGluZH_HToWWTo2L2Nu_M-125
    DBSSample(dataset="/GluGluZH_HToWWTo2L2Nu_M-125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODAPVv9-106X_mcRun2_asymptotic_preVFP_v11-v1/NANOAODSIM"),
    DBSSample(dataset="/GluGluZH_HToWWTo2L2Nu_M-125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv9-106X_mcRun2_asymptotic_v17-v2/NANOAODSIM"),
    DBSSample(dataset="/GluGluZH_HToWWTo2L2Nu_M-125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv9-106X_mc2017_realistic_v9-v2/NANOAODSIM"),
    DBSSample(dataset="/GluGluZH_HToWWTo2L2Nu_M-125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv9-106X_upgrade2018_realistic_v16_L1v1-v2/NANOAODSIM"),
]


nanoaodv9_sig = [
    DirectorySample(
        location="/ceph/cms/store/user/jguiang/VBSVVHSignalGeneration/v1/VBSOSWWH_Inclusive_4f_TuneCP5_RunIISummer20UL16-106X_privateMC_NANOGEN_v1",
        dataset="VBSOSWWH_Inclusive_4f_TuneCP5_RunIISummer20UL16-106X_privateMC_NANOGEN_v1",
        globber="merged*.root",
        use_xrootd=True
    ),
    DirectorySample(
        location="/ceph/cms/store/user/jguiang/VBSVVHSignalGeneration/v1/VBSOSWWH_Inclusive_4f_TuneCP5_RunIISummer20UL16APV-106X_privateMC_NANOGEN_v1",
        dataset="VBSOSWWH_Inclusive_4f_TuneCP5_RunIISummer20UL16APV-106X_privateMC_NANOGEN_v1",
        globber="merged*.root",
        use_xrootd=True
    ),
    DirectorySample(
        location="/ceph/cms/store/user/jguiang/VBSVVHSignalGeneration/v1/VBSOSWWH_Inclusive_4f_TuneCP5_RunIISummer20UL17-106X_privateMC_NANOGEN_v1",
        dataset="VBSOSWWH_Inclusive_4f_TuneCP5_RunIISummer20UL17-106X_privateMC_NANOGEN_v1",
        globber="merged*.root",
        use_xrootd=True
    ),
    DirectorySample(
        location="/ceph/cms/store/user/jguiang/VBSVVHSignalGeneration/v1/VBSOSWWH_Inclusive_4f_TuneCP5_RunIISummer20UL18-106X_privateMC_NANOGEN_v1",
        dataset="VBSOSWWH_Inclusive_4f_TuneCP5_RunIISummer20UL18-106X_privateMC_NANOGEN_v1",
        globber="merged*.root",
        use_xrootd=True
    ),
    DirectorySample(
        location="/ceph/cms/store/user/jguiang/VBSVVHSignalGeneration/v1/VBSWWH_Inclusive_4f_TuneCP5_RunIISummer20UL16-106X_privateMC_NANOGEN_v1",
        dataset="VBSWWH_Inclusive_4f_TuneCP5_RunIISummer20UL16-106X_privateMC_NANOGEN_v1",
        globber="merged*.root",
        use_xrootd=True
    ),
    DirectorySample(
        location="/ceph/cms/store/user/jguiang/VBSVVHSignalGeneration/v1/VBSWWH_Inclusive_4f_TuneCP5_RunIISummer20UL16APV-106X_privateMC_NANOGEN_v1",
        dataset="VBSWWH_Inclusive_4f_TuneCP5_RunIISummer20UL16APV-106X_privateMC_NANOGEN_v1",
        globber="merged*.root",
        use_xrootd=True
    ),
    DirectorySample(
        location="/ceph/cms/store/user/jguiang/VBSVVHSignalGeneration/v1/VBSWWH_Inclusive_4f_TuneCP5_RunIISummer20UL17-106X_privateMC_NANOGEN_v1",
        dataset="VBSWWH_Inclusive_4f_TuneCP5_RunIISummer20UL17-106X_privateMC_NANOGEN_v1",
        globber="merged*.root",
        use_xrootd=True
    ),
    DirectorySample(
        location="/ceph/cms/store/user/jguiang/VBSVVHSignalGeneration/v1/VBSWWH_Inclusive_4f_TuneCP5_RunIISummer20UL18-106X_privateMC_NANOGEN_v1",
        dataset="VBSWWH_Inclusive_4f_TuneCP5_RunIISummer20UL18-106X_privateMC_NANOGEN_v1",
        globber="merged*.root",
        use_xrootd=True
    ),
    DirectorySample(
        location="/ceph/cms/store/user/jguiang/VBSVVHSignalGeneration/v1/VBSWZH_Inclusive_4f_TuneCP5_RunIISummer20UL16-106X_privateMC_NANOGEN_v1",
        dataset="VBSWZH_Inclusive_4f_TuneCP5_RunIISummer20UL16-106X_privateMC_NANOGEN_v1",
        globber="merged*.root",
        use_xrootd=True
    ),
    DirectorySample(
        location="/ceph/cms/store/user/jguiang/VBSVVHSignalGeneration/v1/VBSWZH_Inclusive_4f_TuneCP5_RunIISummer20UL16APV-106X_privateMC_NANOGEN_v1",
        dataset="VBSWZH_Inclusive_4f_TuneCP5_RunIISummer20UL16APV-106X_privateMC_NANOGEN_v1",
        globber="merged*.root",
        use_xrootd=True
    ),
    DirectorySample(
        location="/ceph/cms/store/user/jguiang/VBSVVHSignalGeneration/v1/VBSWZH_Inclusive_4f_TuneCP5_RunIISummer20UL17-106X_privateMC_NANOGEN_v1",
        dataset="VBSWZH_Inclusive_4f_TuneCP5_RunIISummer20UL17-106X_privateMC_NANOGEN_v1",
        globber="merged*.root",
        use_xrootd=True
    ),
    DirectorySample(
        location="/ceph/cms/store/user/jguiang/VBSVVHSignalGeneration/v1/VBSWZH_Inclusive_4f_TuneCP5_RunIISummer20UL18-106X_privateMC_NANOGEN_v1",
        dataset="VBSWZH_Inclusive_4f_TuneCP5_RunIISummer20UL18-106X_privateMC_NANOGEN_v1",
        globber="merged*.root",
        use_xrootd=True
    ),
    DirectorySample(
        location="/ceph/cms/store/user/jguiang/VBSVVHSignalGeneration/v1/VBSZZH_Inclusive_4f_TuneCP5_RunIISummer20UL16-106X_privateMC_NANOGEN_v1",
        dataset="VBSZZH_Inclusive_4f_TuneCP5_RunIISummer20UL16-106X_privateMC_NANOGEN_v1",
        globber="merged*.root",
        use_xrootd=True
    ),
    DirectorySample(
        location="/ceph/cms/store/user/jguiang/VBSVVHSignalGeneration/v1/VBSZZH_Inclusive_4f_TuneCP5_RunIISummer20UL16APV-106X_privateMC_NANOGEN_v1",
        dataset="VBSZZH_Inclusive_4f_TuneCP5_RunIISummer20UL16APV-106X_privateMC_NANOGEN_v1",
        globber="merged*.root",
        use_xrootd=True
    ),
    DirectorySample(
        location="/ceph/cms/store/user/jguiang/VBSVVHSignalGeneration/v1/VBSZZH_Inclusive_4f_TuneCP5_RunIISummer20UL17-106X_privateMC_NANOGEN_v1",
        dataset="VBSZZH_Inclusive_4f_TuneCP5_RunIISummer20UL17-106X_privateMC_NANOGEN_v1",
        globber="merged*.root",
        use_xrootd=True
    ),
    DirectorySample(
        location="/ceph/cms/store/user/jguiang/VBSVVHSignalGeneration/v1/VBSZZH_Inclusive_4f_TuneCP5_RunIISummer20UL18-106X_privateMC_NANOGEN_v1",
        dataset="VBSZZH_Inclusive_4f_TuneCP5_RunIISummer20UL18-106X_privateMC_NANOGEN_v1",
        globber="merged*.root",
        use_xrootd=True
    )
]

nanoaodv15_run2_bkg = [
    # TTToHadronic
    DBSSample(dataset="/TTToHadronic_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODAPVv15-150X_mcRun2_asymptotic_preVFP_v1-v2/NANOAODSIM"),
    DBSSample(dataset="/TTToHadronic_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1-v2/NANOAODSIM"),
    DBSSample(dataset="/TTToHadronic_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1-v2/NANOAODSIM"),
    DBSSample(dataset="/TTToHadronic_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v2/NANOAODSIM"),
    # TTToSemiLeptonic
    DBSSample(dataset="/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODAPVv15-150X_mcRun2_asymptotic_preVFP_v1-v2/NANOAODSIM"),
    DBSSample(dataset="/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1-v2/NANOAODSIM"),
    DBSSample(dataset="/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1-v2/NANOAODSIM"),
    DBSSample(dataset="/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v2/NANOAODSIM"),
    # QCD (50 <= HT < 100): /QCD_HT50to100
    DBSSample(dataset="/QCD_HT50to100_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODAPVv15-150X_mcRun2_asymptotic_preVFP_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/QCD_HT50to100_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/QCD_HT50to100_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/QCD_HT50to100_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM"),
    # QCD (100 <= HT < 200): /QCD_HT100to200
    DBSSample(dataset="/QCD_HT100to200_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODAPVv15-150X_mcRun2_asymptotic_preVFP_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/QCD_HT100to200_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/QCD_HT100to200_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/QCD_HT100to200_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM"),
    # QCD (200 <= HT < 300): /QCD_HT200to300
    DBSSample(dataset="/QCD_HT200to300_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODAPVv15-150X_mcRun2_asymptotic_preVFP_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/QCD_HT200to300_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/QCD_HT200to300_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/QCD_HT200to300_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM"),
    # QCD (300 <= HT < 500): /QCD_HT300to500
    DBSSample(dataset="/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODAPVv15-150X_mcRun2_asymptotic_preVFP_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM"),
    # QCD (500 <= HT < 700): /QCD_HT500to700
    DBSSample(dataset="/QCD_HT500to700_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODAPVv15-150X_mcRun2_asymptotic_preVFP_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/QCD_HT500to700_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/QCD_HT500to700_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/QCD_HT500to700_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM"),
    # QCD (700 <= HT < 1000): /QCD_HT700to1000
    DBSSample(dataset="/QCD_HT700to1000_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODAPVv15-150X_mcRun2_asymptotic_preVFP_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/QCD_HT700to1000_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/QCD_HT700to1000_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/QCD_HT700to1000_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM"),
    # QCD (1000 <= HT < 1500): /QCD_HT1000to1500
    DBSSample(dataset="/QCD_HT1000to1500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODAPVv15-150X_mcRun2_asymptotic_preVFP_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/QCD_HT1000to1500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/QCD_HT1000to1500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/QCD_HT1000to1500_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM"),
    # QCD (1500 <= HT < 2000): /QCD_HT1500to2000
    DBSSample(dataset="/QCD_HT1500to2000_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODAPVv15-150X_mcRun2_asymptotic_preVFP_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/QCD_HT1500to2000_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/QCD_HT1500to2000_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/QCD_HT1500to2000_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM"),
    # QCD (2000 <= HT < Inf): /QCD_HT2000toInf
    DBSSample(dataset="/QCD_HT2000toInf_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODAPVv15-150X_mcRun2_asymptotic_preVFP_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/QCD_HT2000toInf_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/QCD_HT2000toInf_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/QCD_HT2000toInf_TuneCP5_PSWeights_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM"),
    # TTH (H to bb)
    DBSSample(dataset="/ttHTobb_M125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODAPVv15-150X_mcRun2_asymptotic_preVFP_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/ttHTobb_M125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/ttHTobb_M125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/ttHTobb_M125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM"),
    # TTH (H to non-bb)
    DBSSample(dataset="/ttHToNonbb_M125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODAPVv15-150X_mcRun2_asymptotic_preVFP_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/ttHToNonbb_M125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/ttHToNonbb_M125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/ttHToNonbb_M125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM"),
    # TTW
    DBSSample(dataset="/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer20UL16NanoAODAPVv15-150X_mcRun2_asymptotic_preVFP_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/TTWJetsToQQ_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM"),
    # TTWW
    DBSSample(dataset="/TTWW_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODAPVv15-150X_mcRun2_asymptotic_preVFP_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/TTWW_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/TTWW_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/TTWW_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM"),
    # TTWZ
    DBSSample(dataset="/TTWZ_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODAPVv15-150X_mcRun2_asymptotic_preVFP_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/TTWZ_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/TTWZ_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/TTWZ_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM"),
    # TTbb Hadronic
    #DBSSample(dataset=""),
    #DBSSample(dataset=""),
    #DBSSample(dataset=""),
    #DBSSample(dataset=""),
    # ST (t-channel, top): ST_t-channel_top_4f_InclusiveDecays
    DBSSample(dataset="/ST_t-channel_top_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/RunIISummer20UL16NanoAODAPVv15-150X_mcRun2_asymptotic_preVFP_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/ST_t-channel_top_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/ST_t-channel_top_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/ST_t-channel_top_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM"),
    # ST (t-channel, antitop): ST_t-channel_antitop_4f_InclusiveDecays
    DBSSample(dataset="/ST_t-channel_antitop_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/RunIISummer20UL16NanoAODAPVv15-150X_mcRun2_asymptotic_preVFP_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/ST_t-channel_antitop_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/ST_t-channel_antitop_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/ST_t-channel_antitop_4f_InclusiveDecays_TuneCP5_13TeV-powheg-madspin-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM"),
    # ST (tW, top): ST_tW_top_5f_inclusive
    DBSSample(dataset="/ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODAPVv15-150X_mcRun2_asymptotic_preVFP_v1-v2/NANOAODSIM"),
    DBSSample(dataset="/ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/ST_tW_top_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM"),
    # ST (tW, antitop): ST_tW_antitop_5f_inclusive
    DBSSample(dataset="/ST_tW_antitop_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODAPVv15-150X_mcRun2_asymptotic_preVFP_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/ST_tW_antitop_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/ST_tW_antitop_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/ST_tW_antitop_5f_inclusiveDecays_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM"),
    # WJetsToQQ (200 <= HT < 400): /WJetsToQQ_HT-200to400
    DBSSample(dataset="/WJetsToQQ_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODAPVv15-150X_mcRun2_asymptotic_preVFP_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/WJetsToQQ_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/WJetsToQQ_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/WJetsToQQ_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM"),
    # WJetsToQQ (400 <= HT < 600): /WJetsToQQ_HT-400to600
    DBSSample(dataset="/WJetsToQQ_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODAPVv15-150X_mcRun2_asymptotic_preVFP_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/WJetsToQQ_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/WJetsToQQ_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/WJetsToQQ_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM"),
    # WJetsToQQ (600 <= HT < 800): /WJetsToQQ_HT-600to800
    DBSSample(dataset="/WJetsToQQ_HT-600to800_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODAPVv15-150X_mcRun2_asymptotic_preVFP_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/WJetsToQQ_HT-600to800_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/WJetsToQQ_HT-600to800_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/WJetsToQQ_HT-600to800_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM"),
    # WJetsToQQ (800 <= HT < Inf): /WJetsToQQ_HT-800toInf
    DBSSample(dataset="/WJetsToQQ_HT-800toInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODAPVv15-150X_mcRun2_asymptotic_preVFP_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/WJetsToQQ_HT-800toInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/WJetsToQQ_HT-800toInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/WJetsToQQ_HT-800toInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM"),
    # ZJetsToQQ (200 <= HT < 400): /ZJetsToQQ_HT-200to400
    DBSSample(dataset="/ZJetsToQQ_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODAPVv15-150X_mcRun2_asymptotic_preVFP_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/ZJetsToQQ_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/ZJetsToQQ_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/ZJetsToQQ_HT-200to400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM"),
    # ZJetsToQQ (400 <= HT < 600): /ZJetsToQQ_HT-400to600
    DBSSample(dataset="/ZJetsToQQ_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODAPVv15-150X_mcRun2_asymptotic_preVFP_v1-v2/NANOAODSIM"),
    DBSSample(dataset="/ZJetsToQQ_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/ZJetsToQQ_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/ZJetsToQQ_HT-400to600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM"),
    # ZJetsToQQ (600 <= HT < 800): /ZJetsToQQ_HT-600to800
    DBSSample(dataset="/ZJetsToQQ_HT-600to800_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODAPVv15-150X_mcRun2_asymptotic_preVFP_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/ZJetsToQQ_HT-600to800_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/ZJetsToQQ_HT-600to800_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/ZJetsToQQ_HT-600to800_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM"),
    # ZJetsToQQ (800 <= HT < Inf): /ZJetsToQQ_HT-800toInf
    DBSSample(dataset="/ZJetsToQQ_HT-800toInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODAPVv15-150X_mcRun2_asymptotic_preVFP_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/ZJetsToQQ_HT-800toInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/ZJetsToQQ_HT-800toInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/ZJetsToQQ_HT-800toInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM"),
    # WW (WW to qqqq): /WWTo4Q
    DBSSample(dataset="/WWTo4Q_4f_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16NanoAODAPVv15-150X_mcRun2_asymptotic_preVFP_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/WWTo4Q_4f_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/WWTo4Q_4f_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/WWTo4Q_4f_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM"),
    # WW (WW to lnuqq): /WWTo1L1Nu2Q
    DBSSample(dataset="/WWTo1L1Nu2Q_4f_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16NanoAODAPVv15-150X_mcRun2_asymptotic_preVFP_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/WWTo1L1Nu2Q_4f_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/WWTo1L1Nu2Q_4f_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/WWTo1L1Nu2Q_4f_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM"),
    # WZ (W to qq, Z to ll): /WZTo2Q2L
    DBSSample(dataset="/WZTo2Q2L_mllmin4p0_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16NanoAODAPVv15-150X_mcRun2_asymptotic_preVFP_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/WZTo2Q2L_mllmin4p0_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/WZTo2Q2L_mllmin4p0_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/WZTo2Q2L_mllmin4p0_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM"),
    # WZ (W to lnu, Z to qq): /WZTo1L1Nu2Q
    DBSSample(dataset="/WZTo1L1Nu2Q_4f_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16NanoAODAPVv15-150X_mcRun2_asymptotic_preVFP_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/WZTo1L1Nu2Q_4f_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/WZTo1L1Nu2Q_4f_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/WZTo1L1Nu2Q_4f_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM"),
    # ZZ (ZZ to nunuqq): /ZZTo2Nu2Qu
    DBSSample(dataset="/ZZTo2Nu2Q_5f_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16NanoAODAPVv15-150X_mcRun2_asymptotic_preVFP_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/ZZTo2Nu2Q_5f_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/ZZTo2Nu2Q_5f_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/ZZTo2Nu2Q_5f_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM"),
    # ZZ (ZZ to qqqq): /ZZTo4Q
    DBSSample(dataset="/ZZTo4Q_5f_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16NanoAODAPVv15-150X_mcRun2_asymptotic_preVFP_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/ZZTo4Q_5f_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/ZZTo4Q_5f_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/ZZTo4Q_5f_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM"),
    # ZZ (ZZ to qqll): /ZZTo2Q2L
    DBSSample(dataset="/ZZTo2Q2L_mllmin4p0_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16NanoAODAPVv15-150X_mcRun2_asymptotic_preVFP_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/ZZTo2Q2L_mllmin4p0_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/ZZTo2Q2L_mllmin4p0_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/ZZTo2Q2L_mllmin4p0_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM"),
    # WWW
    DBSSample(dataset="/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16NanoAODAPVv15-150X_mcRun2_asymptotic_preVFP_v1_ext1-v1/NANOAODSIM"),
    DBSSample(dataset="/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1_ext1-v1/NANOAODSIM"),
    DBSSample(dataset="/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1_ext1-v1/NANOAODSIM"),
    DBSSample(dataset="/WWW_4F_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1_ext1-v1/NANOAODSIM"),
    # WWZ
    DBSSample(dataset="/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16NanoAODAPVv15-150X_mcRun2_asymptotic_preVFP_v1_ext1-v1/NANOAODSIM"),
    DBSSample(dataset="/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1_ext1-v1/NANOAODSIM"),
    DBSSample(dataset="/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1_ext1-v1/NANOAODSIM"),
    DBSSample(dataset="/WWZ_4F_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1_ext1-v1/NANOAODSIM"),
    # WZZ
    DBSSample(dataset="/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16NanoAODAPVv15-150X_mcRun2_asymptotic_preVFP_v1_ext1-v1/NANOAODSIM"),
    DBSSample(dataset="/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1_ext1-v1/NANOAODSIM"),
    DBSSample(dataset="/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1_ext1-v1/NANOAODSIM"),
    DBSSample(dataset="/WZZ_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1_ext1-v1/NANOAODSIM"),
    # ZZZ
    DBSSample(dataset="/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16NanoAODAPVv15-150X_mcRun2_asymptotic_preVFP_v1_ext1-v1/NANOAODSIM"),
    DBSSample(dataset="/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1_ext1-v1/NANOAODSIM"),
    DBSSample(dataset="/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1_ext1-v1/NANOAODSIM"),
    DBSSample(dataset="/ZZZ_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1_ext1-v1/NANOAODSIM"),
    # VH (H to non-bb)
    DBSSample(dataset="/VHToNonbb_M125_TuneCP5_13TeV-amcatnloFXFX_madspin_pythia8/RunIISummer20UL16NanoAODAPVv15-150X_mcRun2_asymptotic_preVFP_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/VHToNonbb_M125_TuneCP5_13TeV-amcatnloFXFX_madspin_pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/VHToNonbb_M125_TuneCP5_13TeV-amcatnloFXFX_madspin_pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/VHToNonbb_M125_TuneCP5_13TeV-amcatnloFXFX_madspin_pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM"),
    # W-H (W- to lnu): /WminusH_HToBB_WToLNu_M-125
    DBSSample(dataset="/WminusH_HToBB_WToLNu_M-125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODAPVv15-150X_mcRun2_asymptotic_preVFP_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/WminusH_HToBB_WToLNu_M-125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/WminusH_HToBB_WToLNu_M-125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/WminusH_HToBB_WToLNu_M-125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM"),
    # W+H (W+ to lnu): /WminusH_HToBB_WToLNu_M-125
    DBSSample(dataset="/WplusH_HToBB_WToLNu_M-125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODAPVv15-150X_mcRun2_asymptotic_preVFP_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/WplusH_HToBB_WToLNu_M-125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/WplusH_HToBB_WToLNu_M-125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/WplusH_HToBB_WToLNu_M-125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM"),
    # ZH (Z to qq): /ZH_HToBB_ZToQQ_M-125
    DBSSample(dataset="/ZH_HToBB_ZToQQ_M-125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODAPVv15-150X_mcRun2_asymptotic_preVFP_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/ZH_HToBB_ZToQQ_M-125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/ZH_HToBB_ZToQQ_M-125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/ZH_HToBB_ZToQQ_M-125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM"),
    # EWK W+ (W+ to qq)
    DBSSample(dataset="/EWKWplus2Jets_WToQQ_dipoleRecoilOn_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODAPVv15-150X_mcRun2_asymptotic_preVFP_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/EWKWplus2Jets_WToQQ_dipoleRecoilOn_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/EWKWplus2Jets_WToQQ_dipoleRecoilOn_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/EWKWplus2Jets_WToQQ_dipoleRecoilOn_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM"),
    # EWK W- (W- to qq)
    DBSSample(dataset="/EWKWminus2Jets_WToQQ_dipoleRecoilOn_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODAPVv15-150X_mcRun2_asymptotic_preVFP_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/EWKWminus2Jets_WToQQ_dipoleRecoilOn_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/EWKWminus2Jets_WToQQ_dipoleRecoilOn_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/EWKWminus2Jets_WToQQ_dipoleRecoilOn_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM"),
    # EWK Z (Z to ll)
    DBSSample(dataset="/EWKZ2Jets_ZToLL_M-50_TuneCP5_withDipoleRecoil_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODAPVv15-150X_mcRun2_asymptotic_preVFP_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/EWKZ2Jets_ZToLL_M-50_TuneCP5_withDipoleRecoil_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/EWKZ2Jets_ZToLL_M-50_TuneCP5_withDipoleRecoil_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/EWKZ2Jets_ZToLL_M-50_TuneCP5_withDipoleRecoil_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM"),
    # EWK Z (Z to nunu)
    DBSSample(dataset="/EWKZ2Jets_ZToNuNu_M-50_TuneCP5_withDipoleRecoil_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODAPVv15-150X_mcRun2_asymptotic_preVFP_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/EWKZ2Jets_ZToNuNu_M-50_TuneCP5_withDipoleRecoil_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/EWKZ2Jets_ZToNuNu_M-50_TuneCP5_withDipoleRecoil_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/EWKZ2Jets_ZToNuNu_M-50_TuneCP5_withDipoleRecoil_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM"),
    # EWK Z (Z to qq)
    DBSSample(dataset="/EWKZ2Jets_ZToQQ_dipoleRecoilOn_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODAPVv15-150X_mcRun2_asymptotic_preVFP_v1-v2/NANOAODSIM"),
    DBSSample(dataset="/EWKZ2Jets_ZToQQ_dipoleRecoilOn_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/EWKZ2Jets_ZToQQ_dipoleRecoilOn_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/EWKZ2Jets_ZToQQ_dipoleRecoilOn_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM"),
    # EWK WZ
    DBSSample(dataset="/WZJJ_EWK_InclusivePolarization_TuneCP5_13TeV_madgraph-madspin-pythia8/RunIISummer20UL16NanoAODAPVv15-150X_mcRun2_asymptotic_preVFP_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/WZJJ_EWK_InclusivePolarization_TuneCP5_13TeV_madgraph-madspin-pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/WZJJ_EWK_InclusivePolarization_TuneCP5_13TeV_madgraph-madspin-pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/WZJJ_EWK_InclusivePolarization_TuneCP5_13TeV_madgraph-madspin-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM"),
    #TTTo2L2Nu
    DBSSample(dataset="/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODAPVv15-150X_mcRun2_asymptotic_preVFP_v1-v2/NANOAODSIM"),
    DBSSample(dataset="/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1-v2/NANOAODSIM"),
    DBSSample(dataset="/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1-v2/NANOAODSIM"),
    DBSSample(dataset="/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v2/NANOAODSIM"),
    #ST_s-channel_4f_leptonDecays
    DBSSample(dataset="/ST_s-channel_4f_leptonDecays_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16NanoAODAPVv15-150X_mcRun2_asymptotic_preVFP_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/ST_s-channel_4f_leptonDecays_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/ST_s-channel_4f_leptonDecays_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/ST_s-channel_4f_leptonDecays_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM"),
    #WJetsToLNu_HT-70To100
    DBSSample(dataset="/WJetsToLNu_HT-70To100_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODAPVv15-150X_mcRun2_asymptotic_preVFP_v1_ext1-v1/NANOAODSIM"),
    DBSSample(dataset="/WJetsToLNu_HT-70To100_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1_ext1-v1/NANOAODSIM"),
    DBSSample(dataset="/WJetsToLNu_HT-70To100_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1_ext1-v1/NANOAODSIM"),
    DBSSample(dataset="/WJetsToLNu_HT-70To100_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1_ext1-v1/NANOAODSIM"),
    #WJetsToLNu_HT-100To200
    DBSSample(dataset="/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODAPVv15-150X_mcRun2_asymptotic_preVFP_v1_ext1-v1/NANOAODSIM"),
    DBSSample(dataset="/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1_ext1-v1/NANOAODSIM"),
    DBSSample(dataset="/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1_ext1-v1/NANOAODSIM"),
    DBSSample(dataset="/WJetsToLNu_HT-100To200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1_ext1-v1/NANOAODSIM"),
    #WJetsToLNu_HT-200To400
    DBSSample(dataset="/WJetsToLNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODAPVv15-150X_mcRun2_asymptotic_preVFP_v1_ext1-v1/NANOAODSIM"),
    DBSSample(dataset="/WJetsToLNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1_ext1-v1/NANOAODSIM"),
    DBSSample(dataset="/WJetsToLNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1_ext1-v1/NANOAODSIM"),
    DBSSample(dataset="/WJetsToLNu_HT-200To400_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1_ext1-v1/NANOAODSIM"),
    #WJetsToLNu_HT-400To600
    DBSSample(dataset="/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODAPVv15-150X_mcRun2_asymptotic_preVFP_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/WJetsToLNu_HT-400To600_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM"),
    #WJetsToLNu_HT-600To800
    DBSSample(dataset="/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODAPVv15-150X_mcRun2_asymptotic_preVFP_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/WJetsToLNu_HT-600To800_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM"),
    #WJetsToLNu_HT-800To1200
    DBSSample(dataset="/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODAPVv15-150X_mcRun2_asymptotic_preVFP_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/WJetsToLNu_HT-800To1200_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM"),
    #WJetsToLNu_HT-1200To2500
    DBSSample(dataset="/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODAPVv15-150X_mcRun2_asymptotic_preVFP_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/WJetsToLNu_HT-1200To2500_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM"),
    #WJetsToLNu_HT-2500ToInf
    DBSSample(dataset="/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODAPVv15-150X_mcRun2_asymptotic_preVFP_v1_ext2-v1/NANOAODSIM"),
    DBSSample(dataset="/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1_ext2-v1/NANOAODSIM"),
    DBSSample(dataset="/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1_ext2-v1/NANOAODSIM"),
    DBSSample(dataset="/WJetsToLNu_HT-2500ToInf_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1_ext2-v1/NANOAODSIM"),
    #WJetsToLNu
    DBSSample(dataset="/WJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16NanoAODAPVv15-150X_mcRun2_asymptotic_preVFP_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/WJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/WJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/WJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM"),
    #DYJetsToLL_M-10to50
    DBSSample(dataset="/DYJetsToLL_M-10to50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODAPVv15-150X_mcRun2_asymptotic_preVFP_v1-v2/NANOAODSIM"),
    DBSSample(dataset="/DYJetsToLL_M-10to50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/DYJetsToLL_M-10to50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1-v2/NANOAODSIM"),
    DBSSample(dataset="/DYJetsToLL_M-10to50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM"),
    #DYJetsToLL_M-50
    DBSSample(dataset="/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODAPVv15-150X_mcRun2_asymptotic_preVFP_v1-v5/NANOAODSIM"),
    DBSSample(dataset="/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1-v2/NANOAODSIM"),
    DBSSample(dataset="/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v2/NANOAODSIM"),
    #EWKWMinus2Jets_WToLNu_M-50
    DBSSample(dataset="/EWKWMinus2Jets_WToLNu_M-50_TuneCP5_withDipoleRecoil_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODAPVv15-150X_mcRun2_asymptotic_preVFP_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/EWKWMinus2Jets_WToLNu_M-50_TuneCP5_withDipoleRecoil_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/EWKWMinus2Jets_WToLNu_M-50_TuneCP5_withDipoleRecoil_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/EWKWMinus2Jets_WToLNu_M-50_TuneCP5_withDipoleRecoil_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM"),
    #EWKWPlus2Jets_WToLNu_M-50
    DBSSample(dataset="/EWKWPlus2Jets_WToLNu_M-50_TuneCP5_withDipoleRecoil_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODAPVv15-150X_mcRun2_asymptotic_preVFP_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/EWKWPlus2Jets_WToLNu_M-50_TuneCP5_withDipoleRecoil_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/EWKWPlus2Jets_WToLNu_M-50_TuneCP5_withDipoleRecoil_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/EWKWPlus2Jets_WToLNu_M-50_TuneCP5_withDipoleRecoil_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM"),
    #TTWJetsToLNu
    DBSSample(dataset="/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer20UL16NanoAODAPVv15-150X_mcRun2_asymptotic_preVFP_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/TTWJetsToLNu_TuneCP5_13TeV-amcatnloFXFX-madspin-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM"),
    #TTZToLLNuNu_M-10
    DBSSample(dataset="/TTZToLLNuNu_M-10_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16NanoAODAPVv15-150X_mcRun2_asymptotic_preVFP_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/TTZToLLNuNu_M-10_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/TTZToLLNuNu_M-10_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/TTZToLLNuNu_M-10_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM"),
    #TTbb_4f_TTTo2L2Nu
    #DBSSample(dataset=""),
    #DBSSample(dataset=""),
    #DBSSample(dataset=""),
    #DBSSample(dataset=""),
    #TTbb_4f_TTToSemiLeptonic
    #DBSSample(dataset=""),
    #DBSSample(dataset=""),
    #DBSSample(dataset=""),
    #DBSSample(dataset=""),
    #ttWJets
    #DBSSample(dataset=""),
    DBSSample(dataset="/ttWJets_TuneCP5_13TeV_madgraphMLM_pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/ttWJets_TuneCP5_13TeV_madgraphMLM_pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/ttWJets_TuneCP5_13TeV_madgraphMLM_pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM"),
    #ttZJets
    #DBSSample(dataset=""),
    DBSSample(dataset="/ttZJets_TuneCP5_13TeV_madgraphMLM_pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/ttZJets_TuneCP5_13TeV_madgraphMLM_pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/ttZJets_TuneCP5_13TeV_madgraphMLM_pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM"),
    #VBFWH_HToBB_WToLNu_M-125_dipoleRecoilOn
    DBSSample(dataset="/VBFWH_HToBB_WToLNu_M-125_dipoleRecoilOn_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODAPVv15-150X_mcRun2_asymptotic_preVFP_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/VBFWH_HToBB_WToLNu_M-125_dipoleRecoilOn_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/VBFWH_HToBB_WToLNu_M-125_dipoleRecoilOn_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/VBFWH_HToBB_WToLNu_M-125_dipoleRecoilOn_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM"),
    #WWJJToLNuLNu_EWK_noTop
    DBSSample(dataset="/WWJJToLNuLNu_EWK_noTop_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODAPVv15-150X_mcRun2_asymptotic_preVFP_v1-v2/NANOAODSIM"),
    DBSSample(dataset="/WWJJToLNuLNu_EWK_noTop_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/WWJJToLNuLNu_EWK_noTop_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/WWJJToLNuLNu_EWK_noTop_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM"),
    #WWTo2L2Nu
    DBSSample(dataset="/WWTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODAPVv15-150X_mcRun2_asymptotic_preVFP_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/WWTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/WWTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/WWTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM"),
    #WZTo1L3Nu_4f
    DBSSample(dataset="/WZTo1L3Nu_4f_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16NanoAODAPVv15-150X_mcRun2_asymptotic_preVFP_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/WZTo1L3Nu_4f_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/WZTo1L3Nu_4f_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/WZTo1L3Nu_4f_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM"),
    #WZTo3LNu
    DBSSample(dataset="/WZTo3LNu_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16NanoAODAPVv15-150X_mcRun2_asymptotic_preVFP_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/WZTo3LNu_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/WZTo3LNu_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/WZTo3LNu_TuneCP5_13TeV-amcatnloFXFX-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM"),
    #WminusH_HToBB_WToQQ_M-125
    DBSSample(dataset="/WminusH_HToBB_WToQQ_M-125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODAPVv15-150X_mcRun2_asymptotic_preVFP_v1-v2/NANOAODSIM"),
    DBSSample(dataset="/WminusH_HToBB_WToQQ_M-125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/WminusH_HToBB_WToQQ_M-125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/WminusH_HToBB_WToQQ_M-125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM"),
    #WplusH_HToBB_WToQQ_M-125
    DBSSample(dataset="/WplusH_HToBB_WToQQ_M-125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODAPVv15-150X_mcRun2_asymptotic_preVFP_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/WplusH_HToBB_WToQQ_M-125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/WplusH_HToBB_WToQQ_M-125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/WplusH_HToBB_WToQQ_M-125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM"),
    #ZH_HToBB_ZToLL_M-125
    DBSSample(dataset="/ZH_HToBB_ZToLL_M-125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODAPVv15-150X_mcRun2_asymptotic_preVFP_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/ZH_HToBB_ZToLL_M-125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/ZH_HToBB_ZToLL_M-125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/ZH_HToBB_ZToLL_M-125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM"),
    #ZH_HToBB_ZToBB_M-125
    DBSSample(dataset="/ZH_HToBB_ZToBB_M-125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODAPVv15-150X_mcRun2_asymptotic_preVFP_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/ZH_HToBB_ZToBB_M-125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/ZH_HToBB_ZToBB_M-125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1-v2/NANOAODSIM"),
    DBSSample(dataset="/ZH_HToBB_ZToBB_M-125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM"),
    #ZH_HToBB_ZToNuNu_M-125
    DBSSample(dataset="/ZH_HToBB_ZToNuNu_M-125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODAPVv15-150X_mcRun2_asymptotic_preVFP_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/ZH_HToBB_ZToNuNu_M-125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/ZH_HToBB_ZToNuNu_M-125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/ZH_HToBB_ZToNuNu_M-125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM"),
    #ZZJJTo4L
    DBSSample(dataset="/ZZJJTo4L_EWKnotop_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODAPVv15-150X_mcRun2_asymptotic_preVFP_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/ZZJJTo4L_EWKnotop_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/ZZJJTo4L_EWKnotop_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/ZZJJTo4L_EWKnotop_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM"),
    #ZZTo2L2Nu
    DBSSample(dataset="/ZZTo2L2Nu_TuneCP5_13TeV_powheg_pythia8/RunIISummer20UL16NanoAODAPVv15-150X_mcRun2_asymptotic_preVFP_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/ZZTo2L2Nu_TuneCP5_13TeV_powheg_pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/ZZTo2L2Nu_TuneCP5_13TeV_powheg_pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/ZZTo2L2Nu_TuneCP5_13TeV_powheg_pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM"),
    #ZZTo4L_M-1toInf
    DBSSample(dataset="/ZZTo4L_M-1toInf_TuneCP5_13TeV_powheg_pythia8/RunIISummer20UL16NanoAODAPVv15-150X_mcRun2_asymptotic_preVFP_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/ZZTo4L_M-1toInf_TuneCP5_13TeV_powheg_pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/ZZTo4L_M-1toInf_TuneCP5_13TeV_powheg_pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/ZZTo4L_M-1toInf_TuneCP5_13TeV_powheg_pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM"),
    #ggZH_HToBB_ZToLL_M-125
    DBSSample(dataset="/ggZH_HToBB_ZToLL_M-125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODAPVv15-150X_mcRun2_asymptotic_preVFP_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/ggZH_HToBB_ZToLL_M-125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/ggZH_HToBB_ZToLL_M-125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/ggZH_HToBB_ZToLL_M-125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM"),
    #ggZH_HToBB_ZToBB_M-125
    DBSSample(dataset="/ggZH_HToBB_ZToBB_M-125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODAPVv15-150X_mcRun2_asymptotic_preVFP_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/ggZH_HToBB_ZToBB_M-125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/ggZH_HToBB_ZToBB_M-125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/ggZH_HToBB_ZToBB_M-125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM"),
    #ggZH_HToBB_ZToNuNu_M-125
    DBSSample(dataset="/ggZH_HToBB_ZToNuNu_M-125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODAPVv15-150X_mcRun2_asymptotic_preVFP_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/ggZH_HToBB_ZToNuNu_M-125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/ggZH_HToBB_ZToNuNu_M-125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/ggZH_HToBB_ZToNuNu_M-125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM"),
    #ggZH_HToBB_ZToQQ_M-125
    DBSSample(dataset="/ggZH_HToBB_ZToQQ_M-125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODAPVv15-150X_mcRun2_asymptotic_preVFP_v1-v2/NANOAODSIM"),
    DBSSample(dataset="/ggZH_HToBB_ZToQQ_M-125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/ggZH_HToBB_ZToQQ_M-125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/ggZH_HToBB_ZToQQ_M-125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM"),
    #WZ
    DBSSample(dataset="/WZ_TuneCP5_13TeV-pythia8/RunIISummer20UL16NanoAODAPVv15-150X_mcRun2_asymptotic_preVFP_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/WZ_TuneCP5_13TeV-pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/WZ_TuneCP5_13TeV-pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/WZ_TuneCP5_13TeV-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM"),
    #WW
    DBSSample(dataset="/WW_TuneCP5_13TeV-pythia8/RunIISummer20UL16NanoAODAPVv15-150X_mcRun2_asymptotic_preVFP_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/WW_TuneCP5_13TeV-pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/WW_TuneCP5_13TeV-pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/WW_TuneCP5_13TeV-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM"),
    #ZZ
    DBSSample(dataset="/ZZ_TuneCP5_13TeV-pythia8/RunIISummer20UL16NanoAODAPVv15-150X_mcRun2_asymptotic_preVFP_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/ZZ_TuneCP5_13TeV-pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/ZZ_TuneCP5_13TeV-pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/ZZ_TuneCP5_13TeV-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM"),
    #GluGluHToZZTo4L_M125
    DBSSample(dataset="/GluGluHToZZTo4L_M125_TuneCP5_13TeV_powheg2_JHUGenV7011_pythia8/RunIISummer20UL16NanoAODAPVv15-150X_mcRun2_asymptotic_preVFP_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/GluGluHToZZTo4L_M125_TuneCP5_13TeV_powheg2_JHUGenV7011_pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/GluGluHToZZTo4L_M125_TuneCP5_13TeV_powheg2_JHUGenV7011_pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/GluGluHToZZTo4L_M125_TuneCP5_13TeV_powheg2_JHUGenV7011_pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM"),
    #SSWW
    DBSSample(dataset="/SSWW_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODAPVv15-150X_mcRun2_asymptotic_preVFP_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/SSWW_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/SSWW_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/SSWW_TuneCP5_13TeV-madgraph-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM"),
    #TWZToLL_tlept_Wlept_5f_DR
    DBSSample(dataset="/TWZToLL_tlept_Wlept_5f_DR_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16NanoAODAPVv15-150X_mcRun2_asymptotic_preVFP_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/TWZToLL_tlept_Wlept_5f_DR_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/TWZToLL_tlept_Wlept_5f_DR_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/TWZToLL_tlept_Wlept_5f_DR_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM"),
    #tZq_ll_4f_ckm_NLO
    DBSSample(dataset="/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16NanoAODAPVv15-150X_mcRun2_asymptotic_preVFP_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/tZq_ll_4f_ckm_NLO_TuneCP5_13TeV-amcatnlo-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM"),
    #GluGluToContinToZZTo2e2mu
    DBSSample(dataset="/GluGluToContinToZZTo2e2mu_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL16NanoAODAPVv15-150X_mcRun2_asymptotic_preVFP_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/GluGluToContinToZZTo2e2mu_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/GluGluToContinToZZTo2e2mu_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/GluGluToContinToZZTo2e2mu_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM"),
    #GluGluToContinToZZTo2e2tau
    DBSSample(dataset="/GluGluToContinToZZTo2e2tau_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL16NanoAODAPVv15-150X_mcRun2_asymptotic_preVFP_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/GluGluToContinToZZTo2e2tau_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/GluGluToContinToZZTo2e2tau_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/GluGluToContinToZZTo2e2tau_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM"),
    #GluGluToContinToZZTo2mu2tau
    DBSSample(dataset="/GluGluToContinToZZTo2mu2tau_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL16NanoAODAPVv15-150X_mcRun2_asymptotic_preVFP_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/GluGluToContinToZZTo2mu2tau_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/GluGluToContinToZZTo2mu2tau_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/GluGluToContinToZZTo2mu2tau_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM"),
    #GluGluToContinToZZTo4e
    DBSSample(dataset="/GluGluToContinToZZTo4e_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL16NanoAODAPVv15-150X_mcRun2_asymptotic_preVFP_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/GluGluToContinToZZTo4e_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/GluGluToContinToZZTo4e_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/GluGluToContinToZZTo4e_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM"),
    #GluGluToContinToZZTo4mu
    DBSSample(dataset="/GluGluToContinToZZTo4mu_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL16NanoAODAPVv15-150X_mcRun2_asymptotic_preVFP_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/GluGluToContinToZZTo4mu_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/GluGluToContinToZZTo4mu_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/GluGluToContinToZZTo4mu_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM"),
    #GluGluToContinToZZTo4tau
    DBSSample(dataset="/GluGluToContinToZZTo4tau_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL16NanoAODAPVv15-150X_mcRun2_asymptotic_preVFP_v1-v2/NANOAODSIM"),
    DBSSample(dataset="/GluGluToContinToZZTo4tau_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/GluGluToContinToZZTo4tau_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/GluGluToContinToZZTo4tau_TuneCP5_13TeV-mcfm701-pythia8/RunIISummer20UL18NanoAODv15-150X_mc2018_realistic_v1-v1/NANOAODSIM"),
    #HZJ_HToWWTo2L2Nu_ZTo2L_M-125
    #DBSSample(dataset=""),
    DBSSample(dataset="/HZJ_HToWWTo2L2Nu_ZTo2L_M-125_TuneCP5_13TeV-powheg-jhugen727-pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/HZJ_HToWWTo2L2Nu_ZTo2L_M-125_TuneCP5_13TeV-powheg-jhugen727-pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1-v1/NANOAODSIM"),
    #DBSSample(dataset=""),
    #GluGluZH_HToWWTo2L2Nu_M-125
    #DBSSample(dataset=""),
    DBSSample(dataset="/GluGluZH_HToWWTo2L2Nu_M-125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL16NanoAODv15-150X_mcRun2_asymptotic_v1-v1/NANOAODSIM"),
    DBSSample(dataset="/GluGluZH_HToWWTo2L2Nu_M-125_TuneCP5_13TeV-powheg-pythia8/RunIISummer20UL17NanoAODv15-150X_mc2017_realistic_v1-v1/NANOAODSIM"),
    #DBSSample(dataset=""),
]


nanoaodv15_run2_sig = [

    # c2v=1.0, c3=1.0 -- VBSWWH_OS
    DirectorySample(dataset="VBSWWH_OS_c2v1p0_c3_1p0_UL16APV", location="/ceph/cms/store/user/mmazza/SignalGeneration/VBSVVH_VBSCuts_13TeV_4f_LO_MG_2_9_18_c2v_1p0_c3_1p0_c2Vc3scan_slc7_amd64_gcc10_CMSSW_12_4_8/VBSWWH_OS_VBSCuts_13TeV_TuneCP5_RunIISummer20UL16APV_NANOv15", globber="*.root", use_xrootd=True),
    DirectorySample(dataset="VBSWWH_OS_c2v1p0_c3_1p0_UL16", location="/ceph/cms/store/user/mmazza/SignalGeneration/VBSVVH_VBSCuts_13TeV_4f_LO_MG_2_9_18_c2v_1p0_c3_1p0_c2Vc3scan_slc7_amd64_gcc10_CMSSW_12_4_8/VBSWWH_OS_VBSCuts_13TeV_TuneCP5_RunIISummer20UL16_NANOv15", globber="*.root", use_xrootd=True),
    DirectorySample(dataset="VBSWWH_OS_c2v1p0_c3_1p0_UL17", location="/ceph/cms/store/user/mmazza/SignalGeneration/VBSVVH_VBSCuts_13TeV_4f_LO_MG_2_9_18_c2v_1p0_c3_1p0_c2Vc3scan_slc7_amd64_gcc10_CMSSW_12_4_8/VBSWWH_OS_VBSCuts_13TeV_TuneCP5_RunIISummer20UL17_NANOv15", globber="*.root", use_xrootd=True),
    DirectorySample(dataset="VBSWWH_OS_c2v1p0_c3_1p0_UL18", location="/ceph/cms/store/user/mmazza/SignalGeneration/VBSVVH_VBSCuts_13TeV_4f_LO_MG_2_9_18_c2v_1p0_c3_1p0_c2Vc3scan_slc7_amd64_gcc10_CMSSW_12_4_8/VBSWWH_OS_VBSCuts_13TeV_TuneCP5_RunIISummer20UL18_NANOv15", globber="*.root", use_xrootd=True),
    # c2v=1.0, c3=1.0 -- VBSWWH_SS
    DirectorySample(dataset="VBSWWH_SS_c2v1p0_c3_1p0_UL16APV", location="/ceph/cms/store/user/mmazza/SignalGeneration/VBSVVH_VBSCuts_13TeV_4f_LO_MG_2_9_18_c2v_1p0_c3_1p0_c2Vc3scan_slc7_amd64_gcc10_CMSSW_12_4_8/VBSWWH_SS_VBSCuts_13TeV_TuneCP5_RunIISummer20UL16APV_NANOv15", globber="*.root", use_xrootd=True),
    DirectorySample(dataset="VBSWWH_SS_c2v1p0_c3_1p0_UL16", location="/ceph/cms/store/user/mmazza/SignalGeneration/VBSVVH_VBSCuts_13TeV_4f_LO_MG_2_9_18_c2v_1p0_c3_1p0_c2Vc3scan_slc7_amd64_gcc10_CMSSW_12_4_8/VBSWWH_SS_VBSCuts_13TeV_TuneCP5_RunIISummer20UL16_NANOv15", globber="*.root", use_xrootd=True),
    DirectorySample(dataset="VBSWWH_SS_c2v1p0_c3_1p0_UL17", location="/ceph/cms/store/user/mmazza/SignalGeneration/VBSVVH_VBSCuts_13TeV_4f_LO_MG_2_9_18_c2v_1p0_c3_1p0_c2Vc3scan_slc7_amd64_gcc10_CMSSW_12_4_8/VBSWWH_SS_VBSCuts_13TeV_TuneCP5_RunIISummer20UL17_NANOv15", globber="*.root", use_xrootd=True),
    DirectorySample(dataset="VBSWWH_SS_c2v1p0_c3_1p0_UL18", location="/ceph/cms/store/user/mmazza/SignalGeneration/VBSVVH_VBSCuts_13TeV_4f_LO_MG_2_9_18_c2v_1p0_c3_1p0_c2Vc3scan_slc7_amd64_gcc10_CMSSW_12_4_8/VBSWWH_SS_VBSCuts_13TeV_TuneCP5_RunIISummer20UL18_NANOv15", globber="*.root", use_xrootd=True),
    # c2v=1.0, c3=1.0 -- VBSWZH
    DirectorySample(dataset="VBSWZH_c2v1p0_c3_1p0_UL16APV", location="/ceph/cms/store/user/mmazza/SignalGeneration/VBSVVH_VBSCuts_13TeV_4f_LO_MG_2_9_18_c2v_1p0_c3_1p0_c2Vc3scan_slc7_amd64_gcc10_CMSSW_12_4_8/VBSWZH_VBSCuts_13TeV_TuneCP5_RunIISummer20UL16APV_NANOv15", globber="*.root", use_xrootd=True),
    DirectorySample(dataset="VBSWZH_c2v1p0_c3_1p0_UL16", location="/ceph/cms/store/user/mmazza/SignalGeneration/VBSVVH_VBSCuts_13TeV_4f_LO_MG_2_9_18_c2v_1p0_c3_1p0_c2Vc3scan_slc7_amd64_gcc10_CMSSW_12_4_8/VBSWZH_VBSCuts_13TeV_TuneCP5_RunIISummer20UL16_NANOv15", globber="*.root", use_xrootd=True),
    DirectorySample(dataset="VBSWZH_c2v1p0_c3_1p0_UL17", location="/ceph/cms/store/user/mmazza/SignalGeneration/VBSVVH_VBSCuts_13TeV_4f_LO_MG_2_9_18_c2v_1p0_c3_1p0_c2Vc3scan_slc7_amd64_gcc10_CMSSW_12_4_8/VBSWZH_VBSCuts_13TeV_TuneCP5_RunIISummer20UL17_NANOv15", globber="*.root", use_xrootd=True),
    DirectorySample(dataset="VBSWZH_c2v1p0_c3_1p0_UL18", location="/ceph/cms/store/user/mmazza/SignalGeneration/VBSVVH_VBSCuts_13TeV_4f_LO_MG_2_9_18_c2v_1p0_c3_1p0_c2Vc3scan_slc7_amd64_gcc10_CMSSW_12_4_8/VBSWZH_VBSCuts_13TeV_TuneCP5_RunIISummer20UL18_NANOv15", globber="*.root", use_xrootd=True),
    # c2v=1.0, c3=1.0 -- VBSZZH
    DirectorySample(dataset="VBSZZH_c2v1p0_c3_1p0_UL16APV", location="/ceph/cms/store/user/mmazza/SignalGeneration/VBSVVH_VBSCuts_13TeV_4f_LO_MG_2_9_18_c2v_1p0_c3_1p0_c2Vc3scan_slc7_amd64_gcc10_CMSSW_12_4_8/VBSZZH_VBSCuts_13TeV_TuneCP5_RunIISummer20UL16APV_NANOv15", globber="*.root", use_xrootd=True),
    DirectorySample(dataset="VBSZZH_c2v1p0_c3_1p0_UL16", location="/ceph/cms/store/user/mmazza/SignalGeneration/VBSVVH_VBSCuts_13TeV_4f_LO_MG_2_9_18_c2v_1p0_c3_1p0_c2Vc3scan_slc7_amd64_gcc10_CMSSW_12_4_8/VBSZZH_VBSCuts_13TeV_TuneCP5_RunIISummer20UL16_NANOv15", globber="*.root", use_xrootd=True),
    DirectorySample(dataset="VBSZZH_c2v1p0_c3_1p0_UL17", location="/ceph/cms/store/user/mmazza/SignalGeneration/VBSVVH_VBSCuts_13TeV_4f_LO_MG_2_9_18_c2v_1p0_c3_1p0_c2Vc3scan_slc7_amd64_gcc10_CMSSW_12_4_8/VBSZZH_VBSCuts_13TeV_TuneCP5_RunIISummer20UL17_NANOv15", globber="*.root", use_xrootd=True),
    DirectorySample(dataset="VBSZZH_c2v1p0_c3_1p0_UL18", location="/ceph/cms/store/user/mmazza/SignalGeneration/VBSVVH_VBSCuts_13TeV_4f_LO_MG_2_9_18_c2v_1p0_c3_1p0_c2Vc3scan_slc7_amd64_gcc10_CMSSW_12_4_8/VBSZZH_VBSCuts_13TeV_TuneCP5_RunIISummer20UL18_NANOv15", globber="*.root", use_xrootd=True),

    # c2v=1.5, c3=1.0 -- VBSWWH_OS
    DirectorySample(dataset="VBSWWH_OS_c2v1p5_c3_1p0_UL16APV", location="/ceph/cms/store/user/mmazza/SignalGeneration/VBSVVH_VBSCuts_13TeV_4f_LO_MG_2_9_18_c2v_1p5_c3_1p0_c2Vc3scan_slc7_amd64_gcc10_CMSSW_12_4_8/VBSWWH_OS_VBSCuts_13TeV_TuneCP5_RunIISummer20UL16APV_NANOv15", globber="*.root", use_xrootd=True),
    DirectorySample(dataset="VBSWWH_OS_c2v1p5_c3_1p0_UL16", location="/ceph/cms/store/user/mmazza/SignalGeneration/VBSVVH_VBSCuts_13TeV_4f_LO_MG_2_9_18_c2v_1p5_c3_1p0_c2Vc3scan_slc7_amd64_gcc10_CMSSW_12_4_8/VBSWWH_OS_VBSCuts_13TeV_TuneCP5_RunIISummer20UL16_NANOv15", globber="*.root", use_xrootd=True),
    DirectorySample(dataset="VBSWWH_OS_c2v1p5_c3_1p0_UL17", location="/ceph/cms/store/user/mmazza/SignalGeneration/VBSVVH_VBSCuts_13TeV_4f_LO_MG_2_9_18_c2v_1p5_c3_1p0_c2Vc3scan_slc7_amd64_gcc10_CMSSW_12_4_8/VBSWWH_OS_VBSCuts_13TeV_TuneCP5_RunIISummer20UL17_NANOv15", globber="*.root", use_xrootd=True),
    DirectorySample(dataset="VBSWWH_OS_c2v1p5_c3_1p0_UL18", location="/ceph/cms/store/user/mmazza/SignalGeneration/VBSVVH_VBSCuts_13TeV_4f_LO_MG_2_9_18_c2v_1p5_c3_1p0_c2Vc3scan_slc7_amd64_gcc10_CMSSW_12_4_8/VBSWWH_OS_VBSCuts_13TeV_TuneCP5_RunIISummer20UL18_NANOv15", globber="*.root", use_xrootd=True),
    # c2v=1.5, c3=1.0 -- VBSWWH_SS
    DirectorySample(dataset="VBSWWH_SS_c2v1p5_c3_1p0_UL16APV", location="/ceph/cms/store/user/mmazza/SignalGeneration/VBSVVH_VBSCuts_13TeV_4f_LO_MG_2_9_18_c2v_1p5_c3_1p0_c2Vc3scan_slc7_amd64_gcc10_CMSSW_12_4_8/VBSWWH_SS_VBSCuts_13TeV_TuneCP5_RunIISummer20UL16APV_NANOv15", globber="*.root", use_xrootd=True),
    DirectorySample(dataset="VBSWWH_SS_c2v1p5_c3_1p0_UL16", location="/ceph/cms/store/user/mmazza/SignalGeneration/VBSVVH_VBSCuts_13TeV_4f_LO_MG_2_9_18_c2v_1p5_c3_1p0_c2Vc3scan_slc7_amd64_gcc10_CMSSW_12_4_8/VBSWWH_SS_VBSCuts_13TeV_TuneCP5_RunIISummer20UL16_NANOv15", globber="*.root", use_xrootd=True),
    DirectorySample(dataset="VBSWWH_SS_c2v1p5_c3_1p0_UL17", location="/ceph/cms/store/user/mmazza/SignalGeneration/VBSVVH_VBSCuts_13TeV_4f_LO_MG_2_9_18_c2v_1p5_c3_1p0_c2Vc3scan_slc7_amd64_gcc10_CMSSW_12_4_8/VBSWWH_SS_VBSCuts_13TeV_TuneCP5_RunIISummer20UL17_NANOv15", globber="*.root", use_xrootd=True),
    DirectorySample(dataset="VBSWWH_SS_c2v1p5_c3_1p0_UL18", location="/ceph/cms/store/user/mmazza/SignalGeneration/VBSVVH_VBSCuts_13TeV_4f_LO_MG_2_9_18_c2v_1p5_c3_1p0_c2Vc3scan_slc7_amd64_gcc10_CMSSW_12_4_8/VBSWWH_SS_VBSCuts_13TeV_TuneCP5_RunIISummer20UL18_NANOv15", globber="*.root", use_xrootd=True),
    # c2v=1.5, c3=1.0 -- VBSWZH
    DirectorySample(dataset="VBSWZH_c2v1p5_c3_1p0_UL16APV", location="/ceph/cms/store/user/mmazza/SignalGeneration/VBSVVH_VBSCuts_13TeV_4f_LO_MG_2_9_18_c2v_1p5_c3_1p0_c2Vc3scan_slc7_amd64_gcc10_CMSSW_12_4_8/VBSWZH_VBSCuts_13TeV_TuneCP5_RunIISummer20UL16APV_NANOv15", globber="*.root", use_xrootd=True),
    DirectorySample(dataset="VBSWZH_c2v1p5_c3_1p0_UL16", location="/ceph/cms/store/user/mmazza/SignalGeneration/VBSVVH_VBSCuts_13TeV_4f_LO_MG_2_9_18_c2v_1p5_c3_1p0_c2Vc3scan_slc7_amd64_gcc10_CMSSW_12_4_8/VBSWZH_VBSCuts_13TeV_TuneCP5_RunIISummer20UL16_NANOv15", globber="*.root", use_xrootd=True),
    DirectorySample(dataset="VBSWZH_c2v1p5_c3_1p0_UL17", location="/ceph/cms/store/user/mmazza/SignalGeneration/VBSVVH_VBSCuts_13TeV_4f_LO_MG_2_9_18_c2v_1p5_c3_1p0_c2Vc3scan_slc7_amd64_gcc10_CMSSW_12_4_8/VBSWZH_VBSCuts_13TeV_TuneCP5_RunIISummer20UL17_NANOv15", globber="*.root", use_xrootd=True),
    DirectorySample(dataset="VBSWZH_c2v1p5_c3_1p0_UL18", location="/ceph/cms/store/user/mmazza/SignalGeneration/VBSVVH_VBSCuts_13TeV_4f_LO_MG_2_9_18_c2v_1p5_c3_1p0_c2Vc3scan_slc7_amd64_gcc10_CMSSW_12_4_8/VBSWZH_VBSCuts_13TeV_TuneCP5_RunIISummer20UL18_NANOv15", globber="*.root", use_xrootd=True),
    # c2v=1.5, c3=1.0 -- VBSZZH
    DirectorySample(dataset="VBSZZH_c2v1p5_c3_1p0_UL16APV", location="/ceph/cms/store/user/mmazza/SignalGeneration/VBSVVH_VBSCuts_13TeV_4f_LO_MG_2_9_18_c2v_1p5_c3_1p0_c2Vc3scan_slc7_amd64_gcc10_CMSSW_12_4_8/VBSZZH_VBSCuts_13TeV_TuneCP5_RunIISummer20UL16APV_NANOv15", globber="*.root", use_xrootd=True),
    DirectorySample(dataset="VBSZZH_c2v1p5_c3_1p0_UL16", location="/ceph/cms/store/user/mmazza/SignalGeneration/VBSVVH_VBSCuts_13TeV_4f_LO_MG_2_9_18_c2v_1p5_c3_1p0_c2Vc3scan_slc7_amd64_gcc10_CMSSW_12_4_8/VBSZZH_VBSCuts_13TeV_TuneCP5_RunIISummer20UL16_NANOv15", globber="*.root", use_xrootd=True),
    DirectorySample(dataset="VBSZZH_c2v1p5_c3_1p0_UL17", location="/ceph/cms/store/user/mmazza/SignalGeneration/VBSVVH_VBSCuts_13TeV_4f_LO_MG_2_9_18_c2v_1p5_c3_1p0_c2Vc3scan_slc7_amd64_gcc10_CMSSW_12_4_8/VBSZZH_VBSCuts_13TeV_TuneCP5_RunIISummer20UL17_NANOv15", globber="*.root", use_xrootd=True),
    DirectorySample(dataset="VBSZZH_c2v1p5_c3_1p0_UL18", location="/ceph/cms/store/user/mmazza/SignalGeneration/VBSVVH_VBSCuts_13TeV_4f_LO_MG_2_9_18_c2v_1p5_c3_1p0_c2Vc3scan_slc7_amd64_gcc10_CMSSW_12_4_8/VBSZZH_VBSCuts_13TeV_TuneCP5_RunIISummer20UL18_NANOv15", globber="*.root", use_xrootd=True),

    # c2v=1.0, c3=10.0 -- VBSWWH_OS
    DirectorySample(dataset="VBSWWH_OS_c2v1p0_c3_10p0_UL16APV", location="/ceph/cms/store/user/mmazza/SignalGeneration/VBSVVH_VBSCuts_13TeV_4f_LO_MG_2_9_18_c2v_1p0_c3_10p0_c2Vc3scan_slc7_amd64_gcc10_CMSSW_12_4_8/VBSWWH_OS_VBSCuts_13TeV_TuneCP5_RunIISummer20UL16APV_NANOv15", globber="*.root", use_xrootd=True),
    DirectorySample(dataset="VBSWWH_OS_c2v1p0_c3_10p0_UL16", location="/ceph/cms/store/user/mmazza/SignalGeneration/VBSVVH_VBSCuts_13TeV_4f_LO_MG_2_9_18_c2v_1p0_c3_10p0_c2Vc3scan_slc7_amd64_gcc10_CMSSW_12_4_8/VBSWWH_OS_VBSCuts_13TeV_TuneCP5_RunIISummer20UL16_NANOv15", globber="*.root", use_xrootd=True),
    DirectorySample(dataset="VBSWWH_OS_c2v1p0_c3_10p0_UL17", location="/ceph/cms/store/user/mmazza/SignalGeneration/VBSVVH_VBSCuts_13TeV_4f_LO_MG_2_9_18_c2v_1p0_c3_10p0_c2Vc3scan_slc7_amd64_gcc10_CMSSW_12_4_8/VBSWWH_OS_VBSCuts_13TeV_TuneCP5_RunIISummer20UL17_NANOv15", globber="*.root", use_xrootd=True),
    DirectorySample(dataset="VBSWWH_OS_c2v1p0_c3_10p0_UL18", location="/ceph/cms/store/user/mmazza/SignalGeneration/VBSVVH_VBSCuts_13TeV_4f_LO_MG_2_9_18_c2v_1p0_c3_10p0_c2Vc3scan_slc7_amd64_gcc10_CMSSW_12_4_8/VBSWWH_OS_VBSCuts_13TeV_TuneCP5_RunIISummer20UL18_NANOv15", globber="*.root", use_xrootd=True),
    # c2v=1.0, c3=10.0 -- VBSWWH_SS
    DirectorySample(dataset="VBSWWH_SS_c2v1p0_c3_10p0_UL16APV", location="/ceph/cms/store/user/mmazza/SignalGeneration/VBSVVH_VBSCuts_13TeV_4f_LO_MG_2_9_18_c2v_1p0_c3_10p0_c2Vc3scan_slc7_amd64_gcc10_CMSSW_12_4_8/VBSWWH_SS_VBSCuts_13TeV_TuneCP5_RunIISummer20UL16APV_NANOv15", globber="*.root", use_xrootd=True),
    DirectorySample(dataset="VBSWWH_SS_c2v1p0_c3_10p0_UL16", location="/ceph/cms/store/user/mmazza/SignalGeneration/VBSVVH_VBSCuts_13TeV_4f_LO_MG_2_9_18_c2v_1p0_c3_10p0_c2Vc3scan_slc7_amd64_gcc10_CMSSW_12_4_8/VBSWWH_SS_VBSCuts_13TeV_TuneCP5_RunIISummer20UL16_NANOv15", globber="*.root", use_xrootd=True),
    DirectorySample(dataset="VBSWWH_SS_c2v1p0_c3_10p0_UL17", location="/ceph/cms/store/user/mmazza/SignalGeneration/VBSVVH_VBSCuts_13TeV_4f_LO_MG_2_9_18_c2v_1p0_c3_10p0_c2Vc3scan_slc7_amd64_gcc10_CMSSW_12_4_8/VBSWWH_SS_VBSCuts_13TeV_TuneCP5_RunIISummer20UL17_NANOv15", globber="*.root", use_xrootd=True),
    DirectorySample(dataset="VBSWWH_SS_c2v1p0_c3_10p0_UL18", location="/ceph/cms/store/user/mmazza/SignalGeneration/VBSVVH_VBSCuts_13TeV_4f_LO_MG_2_9_18_c2v_1p0_c3_10p0_c2Vc3scan_slc7_amd64_gcc10_CMSSW_12_4_8/VBSWWH_SS_VBSCuts_13TeV_TuneCP5_RunIISummer20UL18_NANOv15", globber="*.root", use_xrootd=True),
    # c2v=1.0, c3=10.0 -- VBSWZH
    DirectorySample(dataset="VBSWZH_c2v1p0_c3_10p0_UL16APV", location="/ceph/cms/store/user/mmazza/SignalGeneration/VBSVVH_VBSCuts_13TeV_4f_LO_MG_2_9_18_c2v_1p0_c3_10p0_c2Vc3scan_slc7_amd64_gcc10_CMSSW_12_4_8/VBSWZH_VBSCuts_13TeV_TuneCP5_RunIISummer20UL16APV_NANOv15", globber="*.root", use_xrootd=True),
    DirectorySample(dataset="VBSWZH_c2v1p0_c3_10p0_UL16", location="/ceph/cms/store/user/mmazza/SignalGeneration/VBSVVH_VBSCuts_13TeV_4f_LO_MG_2_9_18_c2v_1p0_c3_10p0_c2Vc3scan_slc7_amd64_gcc10_CMSSW_12_4_8/VBSWZH_VBSCuts_13TeV_TuneCP5_RunIISummer20UL16_NANOv15", globber="*.root", use_xrootd=True),
    DirectorySample(dataset="VBSWZH_c2v1p0_c3_10p0_UL17", location="/ceph/cms/store/user/mmazza/SignalGeneration/VBSVVH_VBSCuts_13TeV_4f_LO_MG_2_9_18_c2v_1p0_c3_10p0_c2Vc3scan_slc7_amd64_gcc10_CMSSW_12_4_8/VBSWZH_VBSCuts_13TeV_TuneCP5_RunIISummer20UL17_NANOv15", globber="*.root", use_xrootd=True),
    DirectorySample(dataset="VBSWZH_c2v1p0_c3_10p0_UL18", location="/ceph/cms/store/user/mmazza/SignalGeneration/VBSVVH_VBSCuts_13TeV_4f_LO_MG_2_9_18_c2v_1p0_c3_10p0_c2Vc3scan_slc7_amd64_gcc10_CMSSW_12_4_8/VBSWZH_VBSCuts_13TeV_TuneCP5_RunIISummer20UL18_NANOv15", globber="*.root", use_xrootd=True),
    # c2v=1.0, c3=10.0 -- VBSZZH
    DirectorySample(dataset="VBSZZH_c2v1p0_c3_10p0_UL16APV", location="/ceph/cms/store/user/mmazza/SignalGeneration/VBSVVH_VBSCuts_13TeV_4f_LO_MG_2_9_18_c2v_1p0_c3_10p0_c2Vc3scan_slc7_amd64_gcc10_CMSSW_12_4_8/VBSZZH_VBSCuts_13TeV_TuneCP5_RunIISummer20UL16APV_NANOv15", globber="*.root", use_xrootd=True),
    DirectorySample(dataset="VBSZZH_c2v1p0_c3_10p0_UL16", location="/ceph/cms/store/user/mmazza/SignalGeneration/VBSVVH_VBSCuts_13TeV_4f_LO_MG_2_9_18_c2v_1p0_c3_10p0_c2Vc3scan_slc7_amd64_gcc10_CMSSW_12_4_8/VBSZZH_VBSCuts_13TeV_TuneCP5_RunIISummer20UL16_NANOv15", globber="*.root", use_xrootd=True),
    DirectorySample(dataset="VBSZZH_c2v1p0_c3_10p0_UL17", location="/ceph/cms/store/user/mmazza/SignalGeneration/VBSVVH_VBSCuts_13TeV_4f_LO_MG_2_9_18_c2v_1p0_c3_10p0_c2Vc3scan_slc7_amd64_gcc10_CMSSW_12_4_8/VBSZZH_VBSCuts_13TeV_TuneCP5_RunIISummer20UL17_NANOv15", globber="*.root", use_xrootd=True),
    DirectorySample(dataset="VBSZZH_c2v1p0_c3_10p0_UL18", location="/ceph/cms/store/user/mmazza/SignalGeneration/VBSVVH_VBSCuts_13TeV_4f_LO_MG_2_9_18_c2v_1p0_c3_10p0_c2Vc3scan_slc7_amd64_gcc10_CMSSW_12_4_8/VBSZZH_VBSCuts_13TeV_TuneCP5_RunIISummer20UL18_NANOv15", globber="*.root", use_xrootd=True),

]


nanoaodv15_run3_bkg = [
    DBSSample(dataset="/QCD_Bin-PT-50to80_TuneCP5_13p6TeV_pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"),
    DBSSample(dataset="/QCD_Bin-PT-80to120_TuneCP5_13p6TeV_pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"),
    DBSSample(dataset="/QCD_Bin-PT-120to170_TuneCP5_13p6TeV_pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"),
    DBSSample(dataset="/QCD_Bin-PT-170to300_TuneCP5_13p6TeV_pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"),
    DBSSample(dataset="/QCD_Bin-PT-300to470_TuneCP5_13p6TeV_pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"),
    DBSSample(dataset="/QCD_Bin-PT-470to600_TuneCP5_13p6TeV_pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"),
    DBSSample(dataset="/QCD_Bin-PT-600to800_TuneCP5_13p6TeV_pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"),
    DBSSample(dataset="/QCD_Bin-PT-800to1000_TuneCP5_13p6TeV_pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"),
    DBSSample(dataset="/QCD_Bin-PT-1000to1500_TuneCP5_13p6TeV_pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"),
    DBSSample(dataset="/QCD_Bin-PT-1500to2000_TuneCP5_13p6TeV_pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"),
    DBSSample(dataset="/QCD_Bin-PT-2000to2500_TuneCP5_13p6TeV_pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"),
    DBSSample(dataset="/QCD_Bin-PT-2500to3000_TuneCP5_13p6TeV_pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"),
    DBSSample(dataset="/QCD_Bin-PT-3000_TuneCP5_13p6TeV_pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"),
    DBSSample(dataset="/TTto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v3/NANOAODSIM"),
    DBSSample(dataset="/TTtoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"),
    DBSSample(dataset="/TTto4Q_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"),
    DBSSample(dataset="/TbarBQtoLNu-t-channel-4FS_TuneCP5_13p6TeV_powheg-madspin-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"),
    DBSSample(dataset="/TbarBQto2Q-t-channel-4FS_TuneCP5_13p6TeV_powheg-madspin-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"),
    DBSSample(dataset="/TBbarQto2Q-t-channel-4FS_TuneCP5_13p6TeV_powheg-madspin-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"),
    DBSSample(dataset="/TBbarQtoLNu-t-channel-4FS_TuneCP5_13p6TeV_powheg-madspin-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"),
    DBSSample(dataset="/TbarWplusto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"),
    DBSSample(dataset="/TbarWplusto4Q_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"),
    DBSSample(dataset="/TbarWplustoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"),
    DBSSample(dataset="/TWminusto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"),
    DBSSample(dataset="/TWminusto4Q_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"),
    DBSSample(dataset="/TWminustoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"),
    DBSSample(dataset="/TbarBtoLNu-s-channel_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"),
    DBSSample(dataset="/TBbartoLNu-s-channel_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"),
    DBSSample(dataset="/WtoLNu-2Jets_Bin-1J-PTLNu-40to100_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v3/NANOAODSIM"),
    DBSSample(dataset="/WtoLNu-2Jets_Bin-2J-PTLNu-40to100_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v3/NANOAODSIM"),
    DBSSample(dataset="/WtoLNu-2Jets_Bin-1J-PTLNu-100to200_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v3/NANOAODSIM"),
    DBSSample(dataset="/WtoLNu-2Jets_Bin-2J-PTLNu-100to200_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v3/NANOAODSIM"),
    DBSSample(dataset="/WtoLNu-2Jets_Bin-1J-PTLNu-200to400_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"),
    DBSSample(dataset="/WtoLNu-2Jets_Bin-2J-PTLNu-200to400_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"),
    DBSSample(dataset="/WtoLNu-2Jets_Bin-1J-PTLNu-400to600_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"),
    DBSSample(dataset="/WtoLNu-2Jets_Bin-2J-PTLNu-400to600_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"),
    DBSSample(dataset="/WtoLNu-2Jets_Bin-1J-PTLNu-600_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"),
    DBSSample(dataset="/WtoLNu-2Jets_Bin-2J-PTLNu-600_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"),
    DBSSample(dataset="/WtoLNu-4Jets_Bin-1J_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"),
    DBSSample(dataset="/WtoLNu-4Jets_Bin-2J_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"),
    DBSSample(dataset="/WtoLNu-4Jets_Bin-3J_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"),
    DBSSample(dataset="/WtoLNu-4Jets_Bin-4J_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"),
    DBSSample(dataset="/Wto2Q-3Jets_Bin-HT-100to400_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"),
    DBSSample(dataset="/Wto2Q-3Jets_Bin-HT-400to800_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"),
    DBSSample(dataset="/Wto2Q-3Jets_Bin-HT-800to1500_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"),
    DBSSample(dataset="/Wto2Q-3Jets_Bin-HT-1500to2500_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v3/NANOAODSIM"),
    DBSSample(dataset="/Wto2Q-3Jets_Bin-HT-2500_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"),
    DBSSample(dataset="/DYto2E_Bin-MLL-10to50_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"),
    DBSSample(dataset="/DYto2Mu_Bin-MLL-10to50_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"),
    DBSSample(dataset="/DYto2Tau_Bin-MLL-10to50_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"),
    DBSSample(dataset="/DYto2L-2Jets_Bin-1J-MLL-50-PTLL-40to100_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v3/NANOAODSIM"),
    DBSSample(dataset="/DYto2L-2Jets_Bin-1J-MLL-50-PTLL-100to200_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"),
    DBSSample(dataset="/DYto2L-2Jets_Bin-1J-MLL-50-PTLL-200to400_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"),
    DBSSample(dataset="/DYto2L-2Jets_Bin-1J-MLL-50-PTLL-400to600_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"),
    DBSSample(dataset="/DYto2L-2Jets_Bin-1J-MLL-50-PTLL-600_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"),
    DBSSample(dataset="/DYto2L-2Jets_Bin-2J-MLL-50-PTLL-40to100_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v3/NANOAODSIM"),
    DBSSample(dataset="/DYto2L-2Jets_Bin-2J-MLL-50-PTLL-100to200_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"),
    DBSSample(dataset="/DYto2L-2Jets_Bin-2J-MLL-50-PTLL-200to400_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"),
    DBSSample(dataset="/DYto2L-2Jets_Bin-2J-MLL-50-PTLL-400to600_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"),
    DBSSample(dataset="/DYto2L-2Jets_Bin-2J-MLL-50-PTLL-600_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"),
    DBSSample(dataset="/TTLNu-1Jets_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/RunIII2024Summer24NanoAODv15-mg35x_150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"),
    DBSSample(dataset="/TTW-WtoQQ-1Jets_TuneCP5_13p6TeV_amcatnloFXFXold-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"),
    DBSSample(dataset="/TTWW_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"),
    DBSSample(dataset="/TTWZ_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"),
    DBSSample(dataset="/TTLL_Bin-MLL-4to50_TuneCP5_13p6TeV_amcatnlo-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"),
    DBSSample(dataset="/TTBBto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"),
    DBSSample(dataset="/TTBBtoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"),
    DBSSample(dataset="/TTBBto4Q_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"),
    DBSSample(dataset="/TTH-HtoNon2B_Par-M-125_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"),
    DBSSample(dataset="/TTH-Hto2B_Par-M-125_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"),
    DBSSample(dataset="/TTLL_Bin-MLL-4to50_TuneCP5_13p6TeV_amcatnlo-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"),
    DBSSample(dataset="/TTLL_Bin-MLL-50_TuneCP5_13p6TeV_amcatnlo-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"),
    DBSSample(dataset="/WminusH-HtoNon2B_Par-M-125_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"),
    DBSSample(dataset="/WplusH-HtoNon2B_Par-M-125_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"),
    DBSSample(dataset="/ZH-HtoNon2B_Par-M-125_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"),
    DBSSample(dataset="/WWJJto2L2Nu-OS-noTop-EWK_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"),
    DBSSample(dataset="/WWJJto2L2Nu-SS-noTop-EWK_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"),
    DBSSample(dataset="/WWto4Q_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"),
    DBSSample(dataset="/WWtoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"),
    DBSSample(dataset="/WWto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"),
    DBSSample(dataset="/WWW-4F_TuneCP5_13p6TeV_amcatnlo-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"),
    DBSSample(dataset="/WWZ-4F_TuneCP5_13p6TeV_amcatnlo-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"),
    DBSSample(dataset="/WZtoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"),
    DBSSample(dataset="/WZtoL3Nu_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"),
    DBSSample(dataset="/WZto2L2Q_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"),
    DBSSample(dataset="/WZto3LNu_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"),
    DBSSample(dataset="/WZZ-5F_TuneCP5_13p6TeV_amcatnlo-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"),
    DBSSample(dataset="/WminusH-WtoLNu-Hto2B_Par-M-125_TuneCP5_13p6TeV_powhegMINLO-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"),
    DBSSample(dataset="/WminusH-Wto2Q-Hto2B_Par-M-125_TuneCP5_13p6TeV_powhegMINLO-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"),
    DBSSample(dataset="/WplusH-WtoLNu-Hto2B_Par-M-125_TuneCP5_13p6TeV_powhegMINLO-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"),
    DBSSample(dataset="/WplusH-Wto2Q-Hto2B_Par-M-125_TuneCP5_13p6TeV_powhegMINLO-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"),
    DBSSample(dataset="/ZH-Zto2L-Hto2B_Par-M-125_TuneCP5_13p6TeV_powhegMINLO-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"),
    DBSSample(dataset="/ZH-Zto2Nu-Hto2B_Par-M-125_TuneCP5_13p6TeV_powhegMINLO-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"),
    DBSSample(dataset="/ZH-Zto2Q-Hto2B_Par-M-125_TuneCP5_13p6TeV_powhegMINLO-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"),
    DBSSample(dataset="/ZZJJto4L-EWK_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"),
    DBSSample(dataset="/ZZJJto4L-QCD_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"),
    DBSSample(dataset="/ZZto2Nu2Q_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"),
    DBSSample(dataset="/ZZto4Q-1Jets_TuneCP5_13p6TeV_amcatnloFXFX-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"),
    DBSSample(dataset="/ZZto2L2Nu_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"),
    DBSSample(dataset="/ZZto2L2Q_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"),
    DBSSample(dataset="/ZZto4L_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"),
    DBSSample(dataset="/ZZZ-5F_TuneCP5_13p6TeV_amcatnlo-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"),
    DBSSample(dataset="/GluGluZH-Zto2L-Hto2B_Par-M-125_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"),
    DBSSample(dataset="/GluGluZH-Zto2Nu-Hto2B_Par-M-125_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"),
    DBSSample(dataset="/GluGluZH-Zto2Q-Hto2B_Par-M-125_TuneCP5_13p6TeV_powheg-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"),
    DBSSample(dataset="/WZ_TuneCP5_13p6TeV_pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"),
    DBSSample(dataset="/WW_TuneCP5_13p6TeV_pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"),
    DBSSample(dataset="/ZZ_TuneCP5_13p6TeV_pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"),
    DBSSample(dataset="/Zto2Q-4Jets_Bin-HT-100to400_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"),
    DBSSample(dataset="/Zto2Q-4Jets_Bin-HT-400to800_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"),
    DBSSample(dataset="/Zto2Q-4Jets_Bin-HT-800to1500_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"),
    DBSSample(dataset="/Zto2Q-4Jets_Bin-HT-1500to2500_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"),
    DBSSample(dataset="/Zto2Q-4Jets_Bin-HT-2500_TuneCP5_13p6TeV_madgraphMLM-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v3/NANOAODSIM"),
    DBSSample(dataset="/GluGluH-Hto2Zto4L_Par-M-125_TuneCP5_13p6TeV_powheg-jhugen-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"),
    DBSSample(dataset="/VBS-SSWW-TL_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"),
    DBSSample(dataset="/VBS-SSWW-TT_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"),
    DBSSample(dataset="/VBS-SSWW-LL_TuneCP5_13p6TeV_madgraph-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"),
    DBSSample(dataset="/TZQB-Zto2L-4FS_Bin-MLL-30_TuneCP5_13p6TeV_amcatnlo-pythia8/RunIII2024Summer24NanoAODv15-Madgraph_2_6_5_150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"),
    DBSSample(dataset="/GluGluToContinto2Zto2E2Mu_TuneCP5_13p6TeV_mcfm701-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"),
    DBSSample(dataset="/GluGluToContinto2Zto2E2Tau_TuneCP5_13p6TeV_mcfm701-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"),
    DBSSample(dataset="/GluGluToContinto2Zto2Mu2Tau_TuneCP5_13p6TeV_mcfm701-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"),
    DBSSample(dataset="/GluGlutoContinto2Zto4E_TuneCP5_13p6TeV_mcfm-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"),
    DBSSample(dataset="/GluGlutoContinto2Zto4Mu_TuneCP5_13p6TeV_mcfm-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"),
    DBSSample(dataset="/GluGlutoContinto2Zto4Tau_TuneCP5_13p6TeV_mcfm-pythia8/RunIII2024Summer24NanoAODv15-150X_mcRun3_2024_realistic_v2-v2/NANOAODSIM"),
]
