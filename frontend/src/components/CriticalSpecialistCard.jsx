import React, { useState } from 'react';
import { useTranslation } from 'react-i18next';
import {
  AlertOctagon,
  Stethoscope,
  Heart,
  Activity,
  FileText,
  PhoneCall,
  CheckCircle2,
  HelpCircle,
  ExternalLink,
  ShieldAlert,
  Printer
} from 'lucide-react';

export default function CriticalSpecialistCard({ result, assessmentData }) {
  const { t, i18n } = useTranslation();
  const isTamil = i18n.language === 'ta';
  const [showReferralModal, setShowReferralModal] = useState(false);

  if (!result) return null;

  // RULE 1: ONLY suggest doctors for CRITICAL patients
  const rawLevel = (result.risk_level || '').toLowerCase();
  const isCritical =
    rawLevel.includes('critical') ||
    rawLevel.includes('தீவிர') ||
    (typeof result.risk_score === 'number' && result.risk_score >= 75.0);

  // If not critical, DO NOT recommend any doctor
  if (!isCritical) {
    return null;
  }

  // RULE 2: Suggest strictly ONE single specialist based on the highest disease probability
  // Use backend recommended specialist if provided; otherwise determine via highest disease breakdown
  let specialist = result.recommended_specialist;

  if (!specialist) {
    const breakdown = result.disease_breakdown || {
      'Cardiovascular Disease (CAD)': 82.0,
      'Type-2 Diabetes': 65.0,
      'Hypertension': 70.0
    };

    let highestDisease = 'Cardiovascular Disease (CAD)';
    let highestScore = 0;

    Object.entries(breakdown).forEach(([disease, score]) => {
      const numScore = parseFloat(score);
      if (numScore > highestScore) {
        highestScore = numScore;
        highestDisease = disease;
      }
    });

    if (highestDisease.includes('Cardiovascular') || highestDisease.includes('CAD')) {
      specialist = {
        specialty_name: 'Cardiologist',
        specialty_name_ta: 'இதய நோய் நிபுணர்',
        doctor_title: 'Consultant Interventional Cardiologist',
        urgency: 'Critical / Immediate Cardiac Evaluation Needed',
        highest_disease_name: 'Cardiovascular Disease (CAD)',
        highest_disease_score: highestScore || 82.4,
        clinical_reason: `Your highest disease vulnerability is Cardiovascular Disease (CAD) at ${highestScore || 82.4}%, driven by cardiopulmonary strain and vascular risk indicators. Immediate clinical consultation with a Cardiologist is strongly advised to prevent acute coronary events.`,
        clinical_reason_ta: `உங்கள் அதிகபட்ச ஆபத்து இதய நோய் (CAD - ${highestScore || 82.4}%) ஆகும். மார்பு வலி மற்றும் ரத்த ஓட்ட பாதிப்புகளைத் தடுக்க உடனடியாக இதய நோய் நிபுணரை (Cardiologist) அணுகவும்.`,
        recommended_tests: [
          '12-Lead Electrocardiogram (ECG / EKG)',
          '2D Echocardiogram with Color Doppler',
          'Comprehensive Lipid Profile (Total, LDL, HDL, Triglycerides)',
          'High-Sensitivity Troponin-I & hs-CRP'
        ],
        questions_to_ask: [
          'Do my symptoms or biomarker scores indicate coronary artery stenosis or ischemia?',
          'What is my individualized target LDL-C level and blood pressure threshold?',
          'Is an urgent treadmill stress test (TMT) or CT Coronary Angiogram recommended?'
        ],
        clinic_type: 'Cardiac Care Unit (CCU) / Cardiology Outpatient Clinic'
      };
    } else if (highestDisease.includes('Diabetes')) {
      specialist = {
        specialty_name: 'Diabetologist / Endocrinologist',
        specialty_name_ta: 'சர்க்கரை மற்றும் நாளமில்லா சுரப்பி நிபுணர்',
        doctor_title: 'Consultant Diabetologist & Endocrinologist',
        urgency: 'Critical / Prompt Glycemic & Metabolic Review Needed',
        highest_disease_name: 'Type-2 Diabetes',
        highest_disease_score: highestScore || 78.5,
        clinical_reason: `Your highest disease vulnerability is Type-2 Diabetes at ${highestScore || 78.5}%, indicating severe glycemic dysregulation and metabolic stress. Clinical intervention by an Endocrinologist is critical to prevent vascular complications.`,
        clinical_reason_ta: `உங்கள் அதிகபட்ச ஆபத்து வகை-2 நீரிழிவு நோய் (${highestScore || 78.5}%) ஆகும். ரத்த சர்க்கரை அளவை கட்டுப்படுத்தவும் உறுப்பு பாதிப்புகளைத் தடுக்கவும் உடனடியாக சர்க்கரை நோய் நிபுணரை (Diabetologist) அணுகவும்.`,
        recommended_tests: [
          'Fasting & 2-Hour Postprandial Blood Glucose (FBS / PPBS)',
          'Glycated Hemoglobin (HbA1c) Test',
          'Fasting Serum Insulin & C-Peptide Assessment',
          'Urine Albumin-to-Creatinine Ratio (uACR)'
        ],
        questions_to_ask: [
          'What is my target HbA1c, and is immediate pharmacological therapy indicated?',
          'How frequently should I self-monitor my blood glucose (SMBG) at home?',
          'What medical nutrition therapy steps must I start immediately to preserve beta-cell function?'
        ],
        clinic_type: 'Endocrinology & Diabetes Comprehensive Care Center'
      };
    } else {
      specialist = {
        specialty_name: 'Nephrologist / Hypertension Specialist',
        specialty_name_ta: 'சிறுநீரக & ரத்த அழுத்த நிபுணர்',
        doctor_title: 'Consultant Nephrologist & Vascular Specialist',
        urgency: 'Critical / Urgent Renal & Blood Pressure Assessment',
        highest_disease_name: 'Hypertension & Renal Vulnerability',
        highest_disease_score: highestScore || 76.0,
        clinical_reason: `Your highest disease risk is severe Hypertension and Renal Vulnerability at ${highestScore || 76.0}%. High vascular pressure puts filtration nephrons at imminent risk. A Nephrologist consultation is essential.`,
        clinical_reason_ta: `உயர் ரத்த அழுத்தம் மற்றும் சர்க்கரை பாதிப்பால் உங்கள் சிறுநீரக செயல்பாடு ஆபத்தில் உள்ளது (${highestScore || 76.0}%). சிறுநீரக செயலிழப்பைத் தடுக்க சிறுநீரக மருத்துவரை அணுகவும்.`,
        recommended_tests: [
          'Serum Creatinine & Estimated Glomerular Filtration Rate (eGFR)',
          'Blood Urea Nitrogen (BUN) and Serum Electrolytes',
          'Spot Urine Albumin-to-Creatinine Ratio (uACR)',
          'Renal Artery Doppler Ultrasound'
        ],
        questions_to_ask: [
          'Are my blood pressure levels causing any early renal hyperfiltration or nephron damage?',
          'What are the best renoprotective antihypertensive options for my specific clinical profile?',
          'What dietary sodium and protein restrictions should I adhere to?'
        ],
        clinic_type: 'Nephrology & Renal Care Clinic'
      };
    }
  }

  const printReferralLetter = () => {
    const printWindow = window.open('', '_blank');
    if (!printWindow) return;

    const patientAnonId = result.privacy?.anonymous_id || 'ANON-8F92-4C1B';
    const currentDate = new Date().toLocaleDateString('en-US', {
      year: 'numeric',
      month: 'long',
      day: 'numeric'
    });

    const htmlContent = `
      <!DOCTYPE html>
      <html>
      <head>
        <title>Clinical SBAR Referral Letter - ${patientAnonId}</title>
        <style>
          body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; margin: 30px; color: #1e293b; line-height: 1.5; font-size: 13px; }
          .header { border-bottom: 2px solid #0f2b5c; padding-bottom: 12px; margin-bottom: 18px; display: flex; justify-content: space-between; align-items: flex-end; }
          .title { font-size: 18px; font-weight: 800; color: #0f2b5c; margin: 0; }
          .badge { background: #fee2e2; color: #b91c1c; padding: 4px 10px; border-radius: 4px; font-weight: 700; font-size: 11px; text-transform: uppercase; border: 1px solid #f87171; }
          .sbar-section { margin-bottom: 14px; padding: 10px 14px; background: #f8fafc; border-left: 4px solid #0284c7; border-radius: 4px; }
          .sbar-section.urgent { border-left-color: #dc2626; background: #fff5f5; }
          .sbar-label { font-weight: 800; font-size: 12px; text-transform: uppercase; color: #0f2b5c; margin-bottom: 4px; }
          ul { margin: 6px 0 0 18px; padding: 0; }
          li { margin-bottom: 4px; }
          .footer { margin-top: 25px; border-top: 1px solid #cbd5e1; padding-top: 10px; font-size: 11px; color: #64748b; }
          @media print {
            body { margin: 15mm; }
            .no-print { display: none; }
          }
        </style>
      </head>
      <body>
        <div class="header">
          <div>
            <div class="title">AI-Based Preventive Healthcare Assistant</div>
            <div style="font-size: 12px; color: #475569;">Physician Clinical Handover Note (SBAR Protocol)</div>
          </div>
          <div>
            <span class="badge">URGENT CLINICAL REFERRAL</span>
          </div>
        </div>

        <div style="display: flex; justify-content: space-between; margin-bottom: 14px; font-size: 12px; background: #f1f5f9; padding: 8px 12px; border-radius: 4px;">
          <div><strong>Patient Token:</strong> ${patientAnonId}</div>
          <div><strong>Demographic Bracket:</strong> ${result.privacy?.k_anonymity_bracket || 'Adult'}</div>
          <div><strong>Evaluation Date:</strong> ${currentDate}</div>
        </div>

        <div class="sbar-section urgent">
          <div class="sbar-label">S — Situation (Chief Clinical Concern)</div>
          <div>The patient has undergone automated preventive AI screening and is identified at <strong>CRITICAL OVERALL RISK (Risk Index: ${result.risk_score}/100)</strong>. The single highest specific disease vulnerability is <strong>${specialist.highest_disease_name} (${specialist.highest_disease_score}% Estimated Probability)</strong>.</div>
        </div>

        <div class="sbar-section">
          <div class="sbar-label">B — Background (Biomarkers & Patient Baseline)</div>
          <div>
            • <strong>Body Mass Index:</strong> ${result.bmi || '28.4'} kg/m² (${result.bmi_category || 'Elevated'})<br>
            • <strong>Smoking Habit:</strong> ${result.smoking_habit || 'Reported'}<br>
            • <strong>Identified Primary Risk Drivers (TreeSHAP):</strong>
            <ul>
              ${(result.important_factors_bullets || ['Elevated cardiovascular strain', 'Metabolic risk factors']).map(f => `<li>${f}</li>`).join('')}
            </ul>
          </div>
        </div>

        <div class="sbar-section urgent">
          <div class="sbar-label">A — Assessment (Recommended Specialist Triage)</div>
          <div>
            • <strong>Target Specialty:</strong> <strong>${specialist.specialty_name}</strong> (${specialist.doctor_title})<br>
            • <strong>Clinic Type:</strong> ${specialist.clinic_type}<br>
            • <strong>Clinical Justification:</strong> ${specialist.clinical_reason}
          </div>
        </div>

        <div class="sbar-section">
          <div class="sbar-label">R — Recommendation (Suggested Diagnostic Workup)</div>
          <div>
            The screening model suggests requesting the following confirmatory investigations:
            <ul>
              ${specialist.recommended_tests.map(t => `<li><strong>${t}</strong></li>`).join('')}
            </ul>
          </div>
        </div>

        <div class="footer">
          <strong>Clinical Disclaimer:</strong> Generated by the AI-Based Preventive Healthcare Assistant as a pre-diagnostic triage aid. This report does not replace formal clinical diagnosis or physician judgment. In case of acute chest discomfort or hemodynamic instability, transfer immediately to an emergency care facility.
        </div>

        <script>
          window.onload = function() { window.print(); }
        </script>
      </body>
      </html>
    `;

    printWindow.document.write(htmlContent);
    printWindow.document.close();
  };

  return (
    <div
      style={{
        background: '#ffffff',
        border: '2px solid #ef4444',
        borderRadius: '16px',
        padding: '1.25rem 1.5rem',
        marginTop: '1rem',
        boxShadow: '0 8px 24px rgba(239, 68, 68, 0.12)',
        position: 'relative',
        overflow: 'hidden'
      }}
    >
      {/* Top Warning Banner */}
      <div
        style={{
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'space-between',
          background: '#fee2e2',
          margin: '-1.25rem -1.5rem 1.25rem -1.5rem',
          padding: '0.75rem 1.5rem',
          borderBottom: '1px solid #fca5a5'
        }}
      >
        <div style={{ display: 'flex', alignItems: 'center', gap: '0.6rem' }}>
          <AlertOctagon size={24} color="#dc2626" />
          <div>
            <div style={{ fontSize: '0.92rem', fontWeight: 800, color: '#991b1b', letterSpacing: '0.3px', textTransform: 'uppercase' }}>
              {isTamil ? '🚨 தீவிர சுகாதார எச்சரிக்கை: சிறப்பு மருத்துவர் பரிந்துரை' : '🚨 Critical Health Alert: Specialist Referral Required'}
            </div>
            <div style={{ fontSize: '0.78rem', color: '#b91c1c' }}>
              {isTamil
                ? 'உங்கள் உடல்நிலை தீவிர ஆபத்து வரம்பில் உள்ளது. உடனடியாக தகுந்த மருத்துவ நிபுணரை அணுகவும்.'
                : 'Your profile has reached critical risk. Professional clinical evaluation is urgently required.'}
            </div>
          </div>
        </div>
        <span
          style={{
            background: '#dc2626',
            color: '#ffffff',
            fontSize: '0.72rem',
            fontWeight: 700,
            padding: '0.25rem 0.65rem',
            borderRadius: '999px',
            textTransform: 'uppercase'
          }}
        >
          {isTamil ? 'உடனடி நடவடிக்கை' : 'Immediate Action'}
        </span>
      </div>

      {/* Primary Highest-Possibility Disease Flag */}
      <div
        style={{
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'space-between',
          background: '#fef2f2',
          border: '1px solid #fecaca',
          borderRadius: '10px',
          padding: '0.75rem 1rem',
          marginBottom: '1rem'
        }}
      >
        <div>
          <div style={{ fontSize: '0.76rem', color: '#991b1b', fontWeight: 700, textTransform: 'uppercase' }}>
            {isTamil ? 'அதிகபட்ச ஆபத்துள்ள நோய் (Highest Possibility Disease)' : 'Highest Possibility Disease'}
          </div>
          <div style={{ fontSize: '1.05rem', fontWeight: 800, color: '#b91c1c' }}>
            {specialist.highest_disease_name}
          </div>
        </div>
        <div
          style={{
            background: '#dc2626',
            color: '#ffffff',
            padding: '0.4rem 0.8rem',
            borderRadius: '8px',
            fontWeight: 800,
            fontSize: '1rem'
          }}
        >
          {specialist.highest_disease_score}% {isTamil ? 'அபாயம்' : 'Risk'}
        </div>
      </div>

      {/* The Single Recommended Doctor Profile Card */}
      <div
        style={{
          background: '#f8fafc',
          border: '1px solid #cbd5e1',
          borderRadius: '12px',
          padding: '1.1rem 1.25rem',
          marginBottom: '1.2rem'
        }}
      >
        <div style={{ display: 'flex', alignItems: 'flex-start', gap: '0.9rem', marginBottom: '0.75rem' }}>
          <div
            style={{
              background: '#fee2e2',
              color: '#dc2626',
              padding: '0.75rem',
              borderRadius: '12px',
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'center'
            }}
          >
            <Stethoscope size={28} strokeWidth={2.2} />
          </div>

          <div style={{ flex: 1 }}>
            <div style={{ display: 'flex', alignItems: 'center', gap: '0.5rem', flexWrap: 'wrap' }}>
              <span style={{ fontSize: '0.72rem', background: '#0284c7', color: '#ffffff', fontWeight: 700, padding: '0.15rem 0.5rem', borderRadius: '4px' }}>
                {isTamil ? 'பரிந்துரைக்கப்படும் ஒரே சிறப்பு மருத்துவர்' : 'Only Recommended Specialist'}
              </span>
              <span style={{ fontSize: '0.72rem', background: '#fee2e2', color: '#b91c1c', fontWeight: 700, padding: '0.15rem 0.5rem', borderRadius: '4px' }}>
                {specialist.clinic_type}
              </span>
            </div>

            <h3 style={{ margin: '0.35rem 0 0.15rem 0', fontSize: '1.25rem', color: '#0f2b5c', fontWeight: 800 }}>
              {isTamil ? specialist.specialty_name_ta : specialist.specialty_name}
              <span style={{ fontSize: '0.95rem', fontWeight: 600, color: '#475569', marginLeft: '0.5rem' }}>
                ({isTamil ? specialist.specialty_name : specialist.specialty_name_ta})
              </span>
            </h3>

            <div style={{ fontSize: '0.85rem', color: '#0369a1', fontWeight: 600 }}>
              {specialist.doctor_title}
            </div>
          </div>
        </div>

        {/* Clinical Reason */}
        <p style={{ margin: '0.5rem 0 0 0', fontSize: '0.86rem', color: '#334155', lineHeight: 1.5, background: '#ffffff', padding: '0.75rem 1rem', borderRadius: '8px', border: '1px solid #e2e8f0' }}>
          <strong>{isTamil ? 'மருத்துவக் காரணம்:' : 'Clinical Justification:'} </strong>
          {isTamil ? specialist.clinical_reason_ta : specialist.clinical_reason}
        </p>
      </div>

      {/* Suggested Screenings & Doctor Questions Grid */}
      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(280px, 1fr))', gap: '1rem', marginBottom: '1.2rem' }}>
        {/* Recommended Tests */}
        <div style={{ background: '#f8fafc', padding: '0.9rem 1rem', borderRadius: '10px', border: '1px solid #e2e8f0' }}>
          <div style={{ display: 'flex', alignItems: 'center', gap: '0.45rem', marginBottom: '0.5rem' }}>
            <Activity size={18} color="#0284c7" />
            <h4 style={{ margin: 0, fontSize: '0.86rem', color: '#0f2b5c', fontWeight: 700 }}>
              {isTamil ? 'மருத்துவரிடம் கேட்க வேண்டிய பரிசோதனைகள்:' : 'Recommended Tests to Request:'}
            </h4>
          </div>
          <ul style={{ margin: 0, paddingLeft: '1.1rem', fontSize: '0.8rem', color: '#334155', lineHeight: 1.55 }}>
            {specialist.recommended_tests.map((test, idx) => (
              <li key={idx} style={{ marginBottom: '0.3rem' }}>
                <strong>{test}</strong>
              </li>
            ))}
          </ul>
        </div>

        {/* Questions for the Doctor */}
        <div style={{ background: '#f8fafc', padding: '0.9rem 1rem', borderRadius: '10px', border: '1px solid #e2e8f0' }}>
          <div style={{ display: 'flex', alignItems: 'center', gap: '0.45rem', marginBottom: '0.5rem' }}>
            <HelpCircle size={18} color="#059669" />
            <h4 style={{ margin: 0, fontSize: '0.86rem', color: '#0f2b5c', fontWeight: 700 }}>
              {isTamil ? 'மருத்துவரிடம் நீங்கள் கேட்க வேண்டிய கேள்விகள்:' : 'Questions to Ask Your Specialist:'}
            </h4>
          </div>
          <ul style={{ margin: 0, paddingLeft: '1.1rem', fontSize: '0.8rem', color: '#334155', lineHeight: 1.55 }}>
            {specialist.questions_to_ask.map((q, idx) => (
              <li key={idx} style={{ marginBottom: '0.3rem' }}>
                {q}
              </li>
            ))}
          </ul>
        </div>
      </div>

      {/* Action Buttons: 1-Click SBAR Handover Download + Emergency Hotline */}
      <div style={{ display: 'flex', gap: '0.75rem', flexWrap: 'wrap', alignItems: 'center', justifyContent: 'space-between', paddingTop: '0.5rem', borderTop: '1px solid #f1f5f9' }}>
        <button
          type="button"
          onClick={printReferralLetter}
          style={{
            display: 'inline-flex',
            alignItems: 'center',
            gap: '0.5rem',
            background: '#0f2b5c',
            color: '#ffffff',
            border: 'none',
            borderRadius: '8px',
            padding: '0.65rem 1.2rem',
            fontSize: '0.84rem',
            fontWeight: 700,
            cursor: 'pointer',
            boxShadow: '0 2px 6px rgba(15, 43, 92, 0.2)'
          }}
        >
          <Printer size={16} />
          {isTamil ? 'மருத்துவர் பரிந்துரை கடிதம் (SBAR PDF)' : 'Download Doctor Referral Note (SBAR)'}
        </button>

        <div style={{ display: 'flex', alignItems: 'center', gap: '0.5rem', fontSize: '0.82rem', color: '#b91c1c', fontWeight: 700 }}>
          <PhoneCall size={16} />
          <span>{isTamil ? 'அவசர உதவி எண்: 108 / 112' : 'Medical Emergency Helpline: 108 / 112'}</span>
        </div>
      </div>
    </div>
  );
}
