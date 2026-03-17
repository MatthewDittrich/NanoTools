# Channels and the respective datasets to skip

BKG_SKIP = {
    "4Lep": {
        "QCD_HT50to100_TuneCP5_PSWeights_13TeV-madgraph-pythia8",
        "QCD_HT100to200_TuneCP5_PSWeights_13TeV-madgraph-pythia8",
        "QCD_HT200to300_TuneCP5_PSWeights_13TeV-madgraph-pythia8",
        "QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8",
        "QCD_HT500to700_TuneCP5_PSWeights_13TeV-madgraph-pythia8",
        "QCD_HT700to1000_TuneCP5_PSWeights_13TeV-madgraph-pythia8",
        "QCD_HT1000to1500_TuneCP5_PSWeights_13TeV-madgraph-pythia8",
        "QCD_HT1500to2000_TuneCP5_PSWeights_13TeV-madgraph-pythia8",
        "QCD_HT2000toInf_TuneCP5_PSWeights_13TeV-madgraph-pythia8",
    },
    "3Lep": {
        "QCD_HT50to100_TuneCP5_PSWeights_13TeV-madgraph-pythia8",
        "QCD_HT100to200_TuneCP5_PSWeights_13TeV-madgraph-pythia8",
        "QCD_HT200to300_TuneCP5_PSWeights_13TeV-madgraph-pythia8",
        "QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8",
        "QCD_HT500to700_TuneCP5_PSWeights_13TeV-madgraph-pythia8",
        "QCD_HT700to1000_TuneCP5_PSWeights_13TeV-madgraph-pythia8",
        "QCD_HT1000to1500_TuneCP5_PSWeights_13TeV-madgraph-pythia8",
        "QCD_HT1500to2000_TuneCP5_PSWeights_13TeV-madgraph-pythia8",
        "QCD_HT2000toInf_TuneCP5_PSWeights_13TeV-madgraph-pythia8",
    },
    "2Lep2FJ": {
        "QCD_HT50to100_TuneCP5_PSWeights_13TeV-madgraph-pythia8",
        "QCD_HT100to200_TuneCP5_PSWeights_13TeV-madgraph-pythia8",
        "QCD_HT200to300_TuneCP5_PSWeights_13TeV-madgraph-pythia8",
        "QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8",
        "QCD_HT500to700_TuneCP5_PSWeights_13TeV-madgraph-pythia8",
        "QCD_HT700to1000_TuneCP5_PSWeights_13TeV-madgraph-pythia8",
        "QCD_HT1000to1500_TuneCP5_PSWeights_13TeV-madgraph-pythia8",
        "QCD_HT1500to2000_TuneCP5_PSWeights_13TeV-madgraph-pythia8",
        "QCD_HT2000toInf_TuneCP5_PSWeights_13TeV-madgraph-pythia8",
    },
    "2Lep1FJ": {
        "QCD_HT50to100_TuneCP5_PSWeights_13TeV-madgraph-pythia8",
        "QCD_HT100to200_TuneCP5_PSWeights_13TeV-madgraph-pythia8",
        "QCD_HT200to300_TuneCP5_PSWeights_13TeV-madgraph-pythia8",
        "QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8",
        "QCD_HT500to700_TuneCP5_PSWeights_13TeV-madgraph-pythia8",
        "QCD_HT700to1000_TuneCP5_PSWeights_13TeV-madgraph-pythia8",
        "QCD_HT1000to1500_TuneCP5_PSWeights_13TeV-madgraph-pythia8",
        "QCD_HT1500to2000_TuneCP5_PSWeights_13TeV-madgraph-pythia8",
        "QCD_HT2000toInf_TuneCP5_PSWeights_13TeV-madgraph-pythia8",
    },
    "1Lep1FJ": {
        "QCD_HT50to100_TuneCP5_PSWeights_13TeV-madgraph-pythia8",
        "QCD_HT100to200_TuneCP5_PSWeights_13TeV-madgraph-pythia8",
        "QCD_HT200to300_TuneCP5_PSWeights_13TeV-madgraph-pythia8",
        "QCD_HT300to500_TuneCP5_PSWeights_13TeV-madgraph-pythia8",
        "QCD_HT500to700_TuneCP5_PSWeights_13TeV-madgraph-pythia8",
        "QCD_HT700to1000_TuneCP5_PSWeights_13TeV-madgraph-pythia8",
        "QCD_HT1000to1500_TuneCP5_PSWeights_13TeV-madgraph-pythia8",
        "QCD_HT1500to2000_TuneCP5_PSWeights_13TeV-madgraph-pythia8",
        "QCD_HT2000toInf_TuneCP5_PSWeights_13TeV-madgraph-pythia8",
    },
    "0Lep3FJ": {
    },
    "0Lep2FJ": {
    },
    "0Lep1FJ": {
    },
    "0Lep0FJ": {
    }
}


DATA_SKIP = {
    "4Lep": {
        "MET",
        "JetHT",
        "JetMET",
        "JetMET0",
        "JetMET1",
    },
    "3Lep": {
        "MET",
        "JetHT",
        "JetMET",
        "JetMET0",
        "JetMET1",
    },
    "2Lep2FJ": {
    },
    "2Lep1FJ": {
    },
    "1Lep1FJ": {
    },
    "0Lep3FJ": {
        "MuonEG",
        "DoubleEG",
        "DoubleMuon",
        "SingleMuon",
        "EGamma",
        "SingleElectron",
        "Muon",
        "Muon0",
        "Muon1",
        "EGamma0",
        "EGamma1",
    },
    "0Lep2FJ": {
        "MuonEG",
        "DoubleEG",
        "DoubleMuon",
        "SingleMuon",
        "EGamma",
        "SingleElectron",
        "Muon",
        "Muon0",
        "Muon1",
        "EGamma0",
        "EGamma1",
    },
    "0Lep1FJ": {
        "MuonEG",
        "DoubleEG",
        "DoubleMuon",
        "SingleMuon",
        "EGamma",
        "SingleElectron",
        "Muon",
        "Muon0",
        "Muon1",
        "EGamma0",
        "EGamma1",
    },
    "0Lep0FJ": {
        "MuonEG",
        "DoubleEG",
        "DoubleMuon",
        "SingleMuon",
        "EGamma",
        "SingleElectron",
        "Muon",
        "Muon0",
        "Muon1",
        "EGamma0",
        "EGamma1",
    }
}
