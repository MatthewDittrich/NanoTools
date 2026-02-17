#ifndef JETID_H
#define JETID_H

#include "correction.h"
#include <iostream>
#include <memory>
#include <string>

class JetIdEvaluator
{
  private:
    std::unique_ptr<correction::CorrectionSet> cset_;
    correction::Correction::Ref ak4_tight_;
    correction::Correction::Ref ak4_tightLepVeto_;
    correction::Correction::Ref ak8_tight_;
    correction::Correction::Ref ak8_tightLepVeto_;
    bool initialized_ = false;

  public:
    // Default constructor: uninitialized (for Run2 where no JSON exists)
    JetIdEvaluator() : initialized_(false) {}

    JetIdEvaluator(const std::string &json_path)
    {
        if (json_path.empty())
        {
            initialized_ = false;
            return;
        }
        cset_ = correction::CorrectionSet::from_file(json_path);
        ak4_tight_ = cset_->at("AK4PUPPI_Tight");
        ak4_tightLepVeto_ = cset_->at("AK4PUPPI_TightLeptonVeto");
        ak8_tight_ = cset_->at("AK8PUPPI_Tight");
        ak8_tightLepVeto_ = cset_->at("AK8PUPPI_TightLeptonVeto");
        initialized_ = true;
    }

    bool isInitialized() const { return initialized_; }

    // Map year + dataset name to the correct jetid JSON path on CVMFS.
    // Returns empty string for Run2 (2016-2018) where no jetid JSON is available.
    static std::string getJsonPath(int year, const std::string &dsname)
    {
        const std::string base = "/cvmfs/cms.cern.ch/rsync/cms-nanoAOD/jsonpog-integration/POG/JME/";
        switch (year)
        {
        case 2022:
            // Run2022E/F/G or EE campaign → Summer22EE
            if (dsname.find("EE") != std::string::npos || dsname.find("Run2022E") != std::string::npos || dsname.find("Run2022F") != std::string::npos || dsname.find("Run2022G") != std::string::npos)
                return base + "2022_Summer22EE/jetid.json.gz";
            return base + "2022_Summer22/jetid.json.gz";
        case 2023:
            // Run2023D or BPix campaign → Summer23BPix
            if (dsname.find("BPix") != std::string::npos || dsname.find("Run2023D") != std::string::npos)
                return base + "2023_Summer23BPix/jetid.json.gz";
            return base + "2023_Summer23/jetid.json.gz";
        case 2024:
            return base + "2024_Summer24/jetid.json.gz";
        default:
            // Run2 (2016-2018) or unknown: no jetid JSON available
            return "";
        }
    }

    // Evaluate AK4 jet ID bitmask: bit0 (1) = Loose, bit1 (2) = Tight, bit2 (4) = TightLeptonVeto
    // Tight implies Loose, so bit0 is set whenever Tight passes.
    float evalJetId(double eta, double chHEF, double neHEF, double chEmEF, double neEmEF, double muEF, int chMult, int neMult, int mult) const
    {
        if (!initialized_) return 0.0f;
        float tight = ak4_tight_->evaluate({eta, chHEF, neHEF, chEmEF, neEmEF, muEF, chMult, neMult, mult});
        float tightLepVeto = ak4_tightLepVeto_->evaluate({eta, chHEF, neHEF, chEmEF, neEmEF, muEF, chMult, neMult, mult});
        return 1.0f * tight + 2.0f * tight + 4.0f * tightLepVeto;
    }

    // Evaluate AK8 fat jet ID bitmask: bit0 (1) = Loose, bit1 (2) = Tight, bit2 (4) = TightLeptonVeto
    // Tight implies Loose, so bit0 is set whenever Tight passes.
    float evalFatJetId(double eta, double chHEF, double neHEF, double chEmEF, double neEmEF, double muEF, int chMult, int neMult, int mult) const
    {
        if (!initialized_) return 0.0f;
        float tight = ak8_tight_->evaluate({eta, chHEF, neHEF, chEmEF, neEmEF, muEF, chMult, neMult, mult});
        float tightLepVeto = ak8_tightLepVeto_->evaluate({eta, chHEF, neHEF, chEmEF, neEmEF, muEF, chMult, neMult, mult});
        return 1.0f * tight + 2.0f * tight + 4.0f * tightLepVeto;
    }
};

#endif
