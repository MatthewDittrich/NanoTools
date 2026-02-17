#ifndef JETID_H
#define JETID_H

#include "correction.h"
#include <cmath>
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
    bool hasCorrectionLib_ = false;
    int year_ = 0;

    // Manual cut-based PUPPI jet ID for Run2 (2016-2018)
    // Returns bitmask: 1*tight + 2*tight + 4*tightLepVeto (same format as correctionlib)
    float evalManualPuppiId(double eta, double chHEF, double neHEF, double chEmEF, double neEmEF, double muEF,
                            int chMult, int neMult, int mult) const
    {
        double absEta = std::abs(eta);
        bool tight = false;
        bool tightLepVeto = false;

        if (year_ == 2016)
        {
            // 2016 Tight
            if (absEta <= 2.4)
                tight = (chMult > 0 && chHEF > 0 && mult > 1 && neEmEF < 0.9 && neHEF < 0.9);
            else if (absEta <= 2.7)
                tight = (neEmEF < 0.99 && neHEF < 0.98);
            else if (absEta <= 3.0)
                tight = (neMult >= 1);
            else
                tight = (neEmEF < 0.90 && neMult > 2);

            // 2016 TightLepVeto (adds CEMF<0.8, MUF<0.8 in |eta|<=2.4 only)
            if (absEta <= 2.4)
                tightLepVeto = tight && (chEmEF < 0.8 && muEF < 0.8);
            else
                tightLepVeto = tight;
        }
        else // 2017, 2018
        {
            // 2017/2018 Tight
            if (absEta <= 2.6)
                tight = (chMult > 0 && chHEF > 0 && mult > 1 && neEmEF < 0.9 && neHEF < 0.9);
            else if (absEta <= 2.7)
                tight = (neEmEF < 0.99 && neHEF < 0.9);
            else if (absEta <= 3.0)
                tight = (neHEF < 0.9999);
            else
                tight = (neEmEF < 0.90 && neMult > 2);

            // 2017/2018 TightLepVeto (adds CEMF<0.8, MUF<0.8 in |eta|<=2.7)
            if (absEta <= 2.6)
                tightLepVeto = tight && (chEmEF < 0.8 && muEF < 0.8);
            else if (absEta <= 2.7)
                tightLepVeto = tight && (chEmEF < 0.8 && muEF < 0.8);
            else
                tightLepVeto = tight;
        }

        float t = tight ? 1.0f : 0.0f;
        float tlv = tightLepVeto ? 1.0f : 0.0f;
        return 1.0f * t + 2.0f * t + 4.0f * tlv;
    }

  public:
    // Default constructor: uninitialized
    JetIdEvaluator() : initialized_(false), hasCorrectionLib_(false), year_(0) {}

    JetIdEvaluator(const std::string &json_path, int year) : year_(year)
    {
        if (!json_path.empty())
        {
            cset_ = correction::CorrectionSet::from_file(json_path);
            ak4_tight_ = cset_->at("AK4PUPPI_Tight");
            ak4_tightLepVeto_ = cset_->at("AK4PUPPI_TightLeptonVeto");
            ak8_tight_ = cset_->at("AK8PUPPI_Tight");
            ak8_tightLepVeto_ = cset_->at("AK8PUPPI_TightLeptonVeto");
            hasCorrectionLib_ = true;
            initialized_ = true;
        }
        else if (year >= 2016 && year <= 2018)
        {
            // Run2: use manual cut-based ID (no correctionlib JSON available)
            hasCorrectionLib_ = false;
            initialized_ = true;
        }
        else
        {
            initialized_ = false;
        }
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
        if (hasCorrectionLib_)
        {
            float tight = ak4_tight_->evaluate({eta, chHEF, neHEF, chEmEF, neEmEF, muEF, chMult, neMult, mult});
            float tightLepVeto = ak4_tightLepVeto_->evaluate({eta, chHEF, neHEF, chEmEF, neEmEF, muEF, chMult, neMult, mult});
            return 1.0f * tight + 2.0f * tight + 4.0f * tightLepVeto;
        }
        return evalManualPuppiId(eta, chHEF, neHEF, chEmEF, neEmEF, muEF, chMult, neMult, mult);
    }

    // Evaluate AK8 fat jet ID bitmask: bit0 (1) = Loose, bit1 (2) = Tight, bit2 (4) = TightLeptonVeto
    // Tight implies Loose, so bit0 is set whenever Tight passes.
    // AK8 recipe: "use the corresponding AK4 jet ID" — same PUPPI cuts apply.
    float evalFatJetId(double eta, double chHEF, double neHEF, double chEmEF, double neEmEF, double muEF, int chMult, int neMult, int mult) const
    {
        if (!initialized_) return 0.0f;
        if (hasCorrectionLib_)
        {
            float tight = ak8_tight_->evaluate({eta, chHEF, neHEF, chEmEF, neEmEF, muEF, chMult, neMult, mult});
            float tightLepVeto = ak8_tightLepVeto_->evaluate({eta, chHEF, neHEF, chEmEF, neEmEF, muEF, chMult, neMult, mult});
            return 1.0f * tight + 2.0f * tight + 4.0f * tightLepVeto;
        }
        return evalManualPuppiId(eta, chHEF, neHEF, chEmEF, neEmEF, muEF, chMult, neMult, mult);
    }
};

#endif
