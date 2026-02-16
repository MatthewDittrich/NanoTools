#ifndef JETID_H
#define JETID_H

#include "correction.h"
#include <string>
#include <memory>

// Jet ID JSON path on CVMFS for 2024 samples
#define JET_ID_JSON_2024 "/cvmfs/cms.cern.ch/rsync/cms-nanoAOD/jsonpog-integration/POG/JME/2024_Summer24/jetid.json.gz"

class JetIdEvaluator
{
private:
    std::unique_ptr<correction::CorrectionSet> cset_;
    correction::Correction::Ref ak4_tight_;
    correction::Correction::Ref ak4_tightLepVeto_;
    correction::Correction::Ref ak8_tight_;
    correction::Correction::Ref ak8_tightLepVeto_;

public:
    JetIdEvaluator(const std::string &json_path)
    {
        cset_ = correction::CorrectionSet::from_file(json_path);
        ak4_tight_ = cset_->at("AK4PUPPI_Tight");
        ak4_tightLepVeto_ = cset_->at("AK4PUPPI_TightLeptonVeto");
        ak8_tight_ = cset_->at("AK8PUPPI_Tight");
        ak8_tightLepVeto_ = cset_->at("AK8PUPPI_TightLeptonVeto");
    }

    // Evaluate AK4 jet ID bitmask: bit1 (2) = Tight, bit2 (4) = TightLeptonVeto
    float evalJetId(double eta, double chHEF, double neHEF, double chEmEF, double neEmEF,
                    double muEF, int chMult, int neMult, int mult) const
    {
        float id = 0.0f;
        id += 2.0f * ak4_tight_->evaluate({eta, chHEF, neHEF, chEmEF, neEmEF, muEF, chMult, neMult, mult});
        id += 4.0f * ak4_tightLepVeto_->evaluate({eta, chHEF, neHEF, chEmEF, neEmEF, muEF, chMult, neMult, mult});
        return id;
    }

    // Evaluate AK8 fat jet ID bitmask: bit1 (2) = Tight, bit2 (4) = TightLeptonVeto
    float evalFatJetId(double eta, double chHEF, double neHEF, double chEmEF, double neEmEF,
                       double muEF, int chMult, int neMult, int mult) const
    {
        float id = 0.0f;
        id += 2.0f * ak8_tight_->evaluate({eta, chHEF, neHEF, chEmEF, neEmEF, muEF, chMult, neMult, mult});
        id += 4.0f * ak8_tightLepVeto_->evaluate({eta, chHEF, neHEF, chEmEF, neEmEF, muEF, chMult, neMult, mult});
        return id;
    }
};

#endif
