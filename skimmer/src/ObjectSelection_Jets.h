#ifndef OBJECTSELECTION_JETS_H
#define OBJECTSELECTION_JETS_H

// NanoTools
#include "Base.h"
#include "Config.h"
#include "Config.h" // gconf
#include "ElectronSelections.h"
#include "MuonSelections.h"
#include "Nano.h"

#include "arbol.h"
#include "arbusto.h"
#include "cutflow.h"
#include "hepcli.h"
#include <cmath>
// Custom skimmer
#include "JetId.h"
#include "ObjectSelection_Base.h"
#include "utilities.h" // Utilities::Variables
// ROOT
#include "TBranch.h"
#include "TString.h"
#include "TTree.h"

typedef std::vector<LorentzVector> LorentzVectors;
typedef std::vector<double> Doubles;
typedef std::vector<int> Integers;
typedef std::vector<unsigned int> Indices;

// Max array sizes (must match NanoCORE Nano.h)
#define JETID_NJET_MAX 250
#define JETID_NFATJET_MAX 18

class JetSelection : public ObjectSelection
{
  public:
    // JetId evaluator (correctionlib-based)
    std::unique_ptr<JetIdEvaluator> jetIdEval_;

    // TBranch pointers and arrays for NanoAODv15 variables not in NanoCORE
    // AK4 jets: multiplicity variables (UChar_t in NanoAODv15)
    TBranch *b_Jet_chMultiplicity_ = nullptr;
    TBranch *b_Jet_neMultiplicity_ = nullptr;
    UChar_t Jet_chMultiplicity_[JETID_NJET_MAX];
    UChar_t Jet_neMultiplicity_[JETID_NJET_MAX];

    // AK8 fat jets: energy fraction and multiplicity variables
    TBranch *b_FatJet_chHEF_ = nullptr;
    TBranch *b_FatJet_neHEF_ = nullptr;
    TBranch *b_FatJet_chEmEF_ = nullptr;
    TBranch *b_FatJet_neEmEF_ = nullptr;
    TBranch *b_FatJet_muEF_ = nullptr;
    TBranch *b_FatJet_chMultiplicity_ = nullptr;
    TBranch *b_FatJet_neMultiplicity_ = nullptr;
    float FatJet_chHEF_[JETID_NFATJET_MAX];
    float FatJet_neHEF_[JETID_NFATJET_MAX];
    float FatJet_chEmEF_[JETID_NFATJET_MAX];
    float FatJet_neEmEF_[JETID_NFATJET_MAX];
    float FatJet_muEF_[JETID_NFATJET_MAX];
    Short_t FatJet_chMultiplicity_[JETID_NFATJET_MAX];
    Short_t FatJet_neMultiplicity_[JETID_NFATJET_MAX];

    bool hasJetMultBranches_ = false;
    bool hasFatJetIdBranches_ = false;

    JetSelection(Arbusto &arbusto_ref, Nano &nt_ref, HEPCLI &cli_ref, Utilities::Variables &cutflow_globals_ref) : ObjectSelection(arbusto_ref, nt_ref, cli_ref, cutflow_globals_ref)
    {
    };

    // DeltaR calculation
    float deltaR(const LorentzVector &v1, const LorentzVector &v2)
    {
        float dEta = v1.eta() - v2.eta();
        float dPhi = v1.phi() - v2.phi();
        if (dPhi > M_PI) dPhi -= 2 * M_PI;
        if (dPhi < -M_PI) dPhi += 2 * M_PI;
        return std::sqrt(dEta * dEta + dPhi * dPhi);
    }

    // Veto Jets that overlap with a veto lepton
    bool passLeptonDRCut(const LorentzVector &jet, const LorentzVectors &leptons, double minDr = 0.4)
    {
        for (const auto &lep : leptons)
        {
            if (deltaR(jet, lep) <= minDr) return false;
        }
        return true;
    }

    // Initialize TTree branch addresses for NanoAODv15 variables not in NanoCORE
    void initTree(TTree *tree)
    {
        // Initialize correctionlib jet ID evaluator using year-aware JSON path
        std::string dsname = cli.input_tchain->GetCurrentFile()->GetName();
        std::string jsonPath = JetIdEvaluator::getJsonPath(gconf.year, dsname);
        if (jsonPath.empty() && gconf.year >= 2016 && gconf.year <= 2018)
        {
            std::cout << ">>> JetId: Using manual cut-based PUPPI jet ID for Run2 year " << gconf.year << std::endl;
        }
        else if (jsonPath.empty())
        {
            std::cout << ">>> WARNING: No jetid JSON available for year " << gconf.year << "; Jet_jetId/FatJet_jetId will not be computed." << std::endl;
        }
        else
        {
            std::cout << ">>> JetId JSON: " << jsonPath << std::endl;
        }
        jetIdEval_ = std::make_unique<JetIdEvaluator>(jsonPath, gconf.year);

        // AK4 jet multiplicity branches
        b_Jet_chMultiplicity_ = tree->GetBranch("Jet_chMultiplicity");
        if (b_Jet_chMultiplicity_)
        {
            b_Jet_chMultiplicity_->SetAddress(Jet_chMultiplicity_);
        }
        b_Jet_neMultiplicity_ = tree->GetBranch("Jet_neMultiplicity");
        if (b_Jet_neMultiplicity_)
        {
            b_Jet_neMultiplicity_->SetAddress(Jet_neMultiplicity_);
        }
        hasJetMultBranches_ = (b_Jet_chMultiplicity_ != nullptr && b_Jet_neMultiplicity_ != nullptr);

        // AK8 fat jet energy fraction and multiplicity branches
        b_FatJet_chHEF_ = tree->GetBranch("FatJet_chHEF");
        if (b_FatJet_chHEF_)
        {
            b_FatJet_chHEF_->SetAddress(FatJet_chHEF_);
        }
        b_FatJet_neHEF_ = tree->GetBranch("FatJet_neHEF");
        if (b_FatJet_neHEF_)
        {
            b_FatJet_neHEF_->SetAddress(FatJet_neHEF_);
        }
        b_FatJet_chEmEF_ = tree->GetBranch("FatJet_chEmEF");
        if (b_FatJet_chEmEF_)
        {
            b_FatJet_chEmEF_->SetAddress(FatJet_chEmEF_);
        }
        b_FatJet_neEmEF_ = tree->GetBranch("FatJet_neEmEF");
        if (b_FatJet_neEmEF_)
        {
            b_FatJet_neEmEF_->SetAddress(FatJet_neEmEF_);
        }
        b_FatJet_muEF_ = tree->GetBranch("FatJet_muEF");
        if (b_FatJet_muEF_)
        {
            b_FatJet_muEF_->SetAddress(FatJet_muEF_);
        }
        b_FatJet_chMultiplicity_ = tree->GetBranch("FatJet_chMultiplicity");
        if (b_FatJet_chMultiplicity_)
        {
            b_FatJet_chMultiplicity_->SetAddress(FatJet_chMultiplicity_);
        }
        b_FatJet_neMultiplicity_ = tree->GetBranch("FatJet_neMultiplicity");
        if (b_FatJet_neMultiplicity_)
        {
            b_FatJet_neMultiplicity_->SetAddress(FatJet_neMultiplicity_);
        }
        hasFatJetIdBranches_ = (b_FatJet_chHEF_ != nullptr && b_FatJet_neHEF_ != nullptr && b_FatJet_chEmEF_ != nullptr && b_FatJet_neEmEF_ != nullptr && b_FatJet_muEF_ != nullptr && b_FatJet_chMultiplicity_ != nullptr && b_FatJet_neMultiplicity_ != nullptr);
    }

    // Load the extra NanoAODv15 branches for the current entry
    void loadEntry(int entry)
    {
        if (b_Jet_chMultiplicity_)
        {
            b_Jet_chMultiplicity_->GetEntry(entry);
        }
        if (b_Jet_neMultiplicity_)
        {
            b_Jet_neMultiplicity_->GetEntry(entry);
        }
        if (b_FatJet_chHEF_)
        {
            b_FatJet_chHEF_->GetEntry(entry);
        }
        if (b_FatJet_neHEF_)
        {
            b_FatJet_neHEF_->GetEntry(entry);
        }
        if (b_FatJet_chEmEF_)
        {
            b_FatJet_chEmEF_->GetEntry(entry);
        }
        if (b_FatJet_neEmEF_)
        {
            b_FatJet_neEmEF_->GetEntry(entry);
        }
        if (b_FatJet_muEF_)
        {
            b_FatJet_muEF_->GetEntry(entry);
        }
        if (b_FatJet_chMultiplicity_)
        {
            b_FatJet_chMultiplicity_->GetEntry(entry);
        }
        if (b_FatJet_neMultiplicity_)
        {
            b_FatJet_neMultiplicity_->GetEntry(entry);
        }
    }

    // Compute Jet_jetId and FatJet_jetId using correctionlib and store in output branches
    void computeJetIds()
    {
        if (!jetIdEval_ || !jetIdEval_->isInitialized()) return;

        // Compute AK4 Jet_jetId
        if (hasJetMultBranches_)
        {
            std::vector<float> jetIds;
            unsigned int nJets = std::min(static_cast<unsigned int>(nt.nJet()), static_cast<unsigned int>(nt.Jet_eta().size()));
            for (unsigned int i = 0; i < nJets; i++)
            {
                int chMult = static_cast<int>(Jet_chMultiplicity_[i]);
                int neMult = static_cast<int>(Jet_neMultiplicity_[i]);
                int mult = chMult + neMult;
                float id = jetIdEval_->evalJetId(nt.Jet_eta().at(i), nt.Jet_chHEF().at(i), nt.Jet_neHEF().at(i), nt.Jet_chEmEF().at(i), nt.Jet_neEmEF().at(i), nt.Jet_muEF().at(i), chMult, neMult, mult);
                jetIds.push_back(id);
            }
            arbusto.setVecLeaf<float>("Jet_jetId", jetIds);
        }

        // Compute AK8 FatJet_jetId
        if (hasFatJetIdBranches_)
        {
            std::vector<float> fatJetIds;
            unsigned int nFatJets = std::min(static_cast<unsigned int>(nt.nFatJet()), static_cast<unsigned int>(nt.FatJet_eta().size()));
            for (unsigned int i = 0; i < nFatJets; i++)
            {
                int chMult = static_cast<int>(FatJet_chMultiplicity_[i]);
                int neMult = static_cast<int>(FatJet_neMultiplicity_[i]);
                int mult = chMult + neMult;
                float id = jetIdEval_->evalFatJetId(nt.FatJet_eta().at(i), FatJet_chHEF_[i], FatJet_neHEF_[i], FatJet_chEmEF_[i], FatJet_neEmEF_[i], FatJet_muEF_[i], chMult, neMult, mult);
                fatJetIds.push_back(id);
            }
            arbusto.setVecLeaf<float>("FatJet_jetId", fatJetIds);
        }
    }

    void selectVVHJets()
    {
        selectVVHAK4Jets();
        selectVVHAK8Jets();
    }

    void selectVVHAK4Jets()
    {
        LorentzVectors jet_p4s = {};
        LorentzVectors vvh_veto_lep_p4s = globals.getVal<LorentzVectors>("vvh_veto_lep_p4s");
        for (unsigned int jet_i = 0; jet_i < nt.nJet(); jet_i++)
        {
            LorentzVector jet_p4 = nt.Jet_p4().at(jet_i);
            if (jet_p4.pt() > 15) //&& passLeptonDRCut(jet_p4, vvh_veto_lep_p4s))
            {
                jet_p4s.push_back(jet_p4);
            }
        }
        globals.setVal<LorentzVectors>("vvh_veto_jet_p4s", jet_p4s);
        globals.setVal<int>("n_vvh_veto_jets", jet_p4s.size());
    }

    void selectVVHAK8Jets()
    {
        LorentzVectors fatjet_p4s = {};
        for (unsigned int fatjet_i = 0; fatjet_i < nt.nFatJet(); fatjet_i++)
        {
            LorentzVector fatjet_p4 = nt.FatJet_p4().at(fatjet_i);
            if (fatjet_p4.pt() > 200 && nt.FatJet_msoftdrop().at(fatjet_i) > 20)
            {
                fatjet_p4s.push_back(fatjet_p4);
            }
        }
        globals.setVal<LorentzVectors>("vvh_veto_fatjet_p4s", fatjet_p4s);
        globals.setVal<int>("n_vvh_veto_fatjets", fatjet_p4s.size());
    }
};
#endif
