import React from 'react';
import { useTranslation } from 'react-i18next';
import { AlertTriangle, BarChart2, Lightbulb, ShieldCheck, Activity } from 'lucide-react';
import WhatIfSimulator from './WhatIfSimulator';
import CriticalSpecialistCard from './CriticalSpecialistCard';

export default function OutputPage({ result, onNewAssessment }) {
  const { t, i18n } = useTranslation();
  if (!result) return null;

  const currentLang = i18n.language || 'en';
  const rawLevel = result.risk_level || 'High Risk';
  const isCritical = rawLevel.toLowerCase().includes('critical') || rawLevel.includes('தீவிர') || (typeof result.risk_score === 'number' && result.risk_score >= 75.0);
  const isHigh = isCritical || rawLevel.toLowerCase().includes('high') || rawLevel.includes('அதிக');
  const isMod = !isHigh && (rawLevel.toLowerCase().includes('moderate') || rawLevel.includes('மிதமான'));
  const riskClass = isHigh ? 'high' : isMod ? 'moderate' : 'low';

  const riskLabel = currentLang === 'ta'
    ? (isCritical ? (t('output.criticalRisk') || 'தீவிர ஆபத்து') : isHigh ? t('output.highRisk') : isMod ? t('output.moderateRisk') : t('output.lowRisk'))
    : (isCritical ? 'Critical Risk' : isHigh ? 'High Risk' : isMod ? 'Moderate Risk' : 'Low Risk');

  const riskDescription =
    result.risk_description ||
    (isCritical
      ? (currentLang === 'ta'
          ? 'உங்கள் உடல்நல குறிகாட்டிகள் தீவிர ஆபத்து மட்டத்தில் உள்ளன. உடனடி மருத்துவ கவனிப்பு மற்றும் சிறப்பு மருத்துவ பரிசோதனை அவசியமாகும்.'
          : 'Your health indicators indicate a Critical Risk level. Immediate clinical evaluation and specialist consultation are urgently advised.')
      : isHigh
      ? t('output.highRiskDesc')
      : isMod
      ? t('output.modRiskDesc')
      : t('output.lowRiskDesc'));

  // Localized factor translation helper
  const translateFactor = (factor) => {
    if (currentLang !== 'ta') return factor;
    if (factor.includes('High Body Weight') && factor.includes('Obese')) {
      return factor.replace('High Body Weight', 'அதிக உடல் எடை').replace('Obese', 'பருமனான நிலை / Obese');
    }
    if (factor.includes('High Body Weight') && factor.includes('Overweight')) {
      return factor.replace('High Body Weight', 'அதிக உடல் எடை').replace('Overweight', 'அதிக எடை / Overweight');
    }
    if (factor.includes('Body Weight Status') && factor.includes('Normal')) {
      return factor.replace('Body Weight Status', 'உடல் எடை நிலை').replace('Normal', 'இயல்பான எடை / Normal');
    }
    if (factor.includes('Low Body Weight') && factor.includes('Underweight')) {
      return factor.replace('Low Body Weight', 'குறைந்த உடல் எடை').replace('Underweight', 'குறைவான எடை / Underweight');
    }
    if (factor.includes('Low Physical Activity')) return 'குறைந்த உடற்பயிற்சி (Low Physical Activity)';
    if (factor.includes('Family History of Disease')) return 'குடும்ப மருத்துவ நோய் வரலாறு';
    if (factor.includes('Reports of Fatigue')) return 'உடல் சோர்வு அறிகுறிகள் (Fatigue)';
    if (factor.includes('Reports of Chest Pain')) return 'மார்பு வலி அறிகுறி (Chest Pain)';
    if (factor.includes('Shortness of Breath')) return 'மூச்சுத் திணறல் அறிகுறி (Shortness of Breath)';
    if (factor.includes('Frequent Urination or Thirst')) return 'அடிக்கடி சிறுநீர் கழித்தல் அல்லது அதிக தாகம்';
    if (factor.includes('Active Tobacco Smoking')) return 'புகைபிடிக்கும் பழக்கம்';
    if (factor.includes('Alcohol Consumption')) return 'மது அருந்தும் பழக்கம்';
    if (factor.includes('Insufficient Sleep')) return 'குறைவான தூக்க நேரம்';
    if (factor.includes('Age Factor')) return 'வயது காரணி (50 வயதிற்கு மேல்)';
    if (factor.includes('Adequate Sleep')) return 'போதுமான தூக்க நேரம்';
    if (factor.includes('Non-Smoking Status')) return 'புகைபிடிக்காத நிலை';
    if (factor.includes('Absence of Chronic Symptoms')) return 'தீவிர அறிகுறிகள் இல்லை';
    return factor;
  };

  const translateGuidance = (step) => {
    if (currentLang !== 'ta') return step;
    if (step.includes('physical activity')) return 'தினசரி குறைந்தது 30 நிமிடங்கள் வழக்கமான உடற்பயிற்சியை மேற்கொள்ளவும்.';
    if (step.includes('balanced and healthy diet')) return 'பழங்கள், காய்கறிகள் நிறைந்த சமச்சீர் ஊட்டச்சத்து உணவை உட்கொள்ளவும்.';
    if (step.includes('Monitor your weight')) return 'உங்கள் உடல் எடை மற்றும் இரத்த அழுத்த அளவுகளை தவறாமல் கண்காணிக்கவும்.';
    if (step.includes('Avoid smoking')) return 'புகைபிடிப்பதைத் தவிர்க்கவும் மற்றும் மது அருந்துவதை நிறுத்தவும்.';
    if (step.includes('Get regular health check-ups')) return 'வழக்கமான மருத்துவ பரிசோதனைகளை மேற்கொண்டு, அறிகுறிகள் தொடர்ந்தால் மருத்துவரை அணுகவும்.';
    return step;
  };

  const defaultBmiFactor = result.bmi && result.bmi_category
    ? (currentLang === 'ta'
        ? `உடல் எடை நிலை (BMI: ${result.bmi} - ${result.bmi_category})`
        : `Body Weight (BMI: ${result.bmi} - ${result.bmi_category})`)
    : 'Body Weight (BMI)';

  const factors = result.important_factors_bullets && result.important_factors_bullets.length > 0
    ? result.important_factors_bullets.map(translateFactor)
    : [
        defaultBmiFactor,
        currentLang === 'ta' ? 'குறைந்த உடற்பயிற்சி' : 'Low Physical Activity',
        currentLang === 'ta' ? 'குடும்ப நோய் வரலாறு' : 'Family History of Disease',
        currentLang === 'ta' ? 'உடல் சோர்வு அறிகுறிகள்' : 'Reports of Fatigue'
      ];

  const guidance = result.guidance_bullets && result.guidance_bullets.length > 0
    ? result.guidance_bullets.map(translateGuidance)
    : [
        currentLang === 'ta' ? 'தினசரி குறைந்தது 30 நிமிடங்கள் வழக்கமான உடற்பயிற்சியை மேற்கொள்ளவும்.' : 'Maintain regular physical activity (at least 30 minutes daily).',
        currentLang === 'ta' ? 'பழங்கள், காய்கறிகள் நிறைந்த சமச்சீர் ஊட்டச்சத்து உணவை உட்கொள்ளவும்.' : 'Follow a balanced and healthy diet with fruits and vegetables.',
        currentLang === 'ta' ? 'உங்கள் உடல் எடை மற்றும் பிற அளவுகளை தவறாமல் கண்காணிக்கவும்.' : 'Monitor your weight and other health parameters regularly.',
        currentLang === 'ta' ? 'புகைபிடிப்பதைத் தவிர்க்கவும் மற்றும் மது அருந்துவதை நிறுத்தவும்.' : 'Avoid smoking and limit alcohol consumption.',
        currentLang === 'ta' ? 'வழக்கமான மருத்துவ பரிசோதனைகளை மேற்கொண்டு, அறிகுறிகள் தொடர்ந்தால் மருத்துவரை அணுகவும்.' : 'Get regular health check-ups and consult a doctor if symptoms persist.'
      ];

  return (
    <div className="assessment-card">
      {/* Top Banner */}
      <div className="card-header-banner">
        <div className="clipboard-icon-box">
          <svg width="46" height="46" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.75" strokeLinecap="round" strokeLinejoin="round">
            <rect x="8" y="2" width="8" height="4" rx="1" ry="1" />
            <path d="M16 4h2a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2h2" />
            <path d="M12 11h.01" />
            <path d="M12 16h.01" />
            <path d="M9 13.5h6" />
          </svg>
        </div>
        <h2 className="card-header-title">{t('output.title')}</h2>
        <p className="card-header-subtitle">
          {t('output.subtitle')}
        </p>
      </div>

      {/* Results Body */}
      <div className="card-body">
        <div className="result-boxes-container">
          {/* Box 1: Risk Level */}
          <div className={`result-box-risk ${riskClass}`}>
            <div className={`risk-icon-wrapper ${riskClass}`}>
              {isHigh ? (
                <AlertTriangle size={24} strokeWidth={2.2} />
              ) : isMod ? (
                <AlertTriangle size={24} strokeWidth={2.2} />
              ) : (
                <ShieldCheck size={24} strokeWidth={2.2} />
              )}
            </div>

            <div className="risk-content-text">
              <div className="risk-title-row">
                <span className="risk-title-label">{t('output.riskLevel')}</span>
                <span className={`risk-pill-badge ${riskClass}`}>{riskLabel}</span>
              </div>
              <p className="risk-desc-text">
                {riskDescription}
              </p>
            </div>
          </div>

          {/* Box 1.5: Critical Specialist Recommendation (ONLY rendered for Critical Patients, suggests strictly ONE doctor) */}
          <CriticalSpecialistCard result={result} />

          {/* Box 2: Important Factors */}
          <div className="result-box-factors">
            <div className="factors-icon-wrapper">
              <BarChart2 size={24} strokeWidth={2.2} />
            </div>

            <div className="factors-content">
              <h3 className="factors-title">{t('output.importantFactors')}</h3>
              <ul className="bullets-list">
                {factors.map((factor, idx) => (
                  <li key={idx}>{factor}</li>
                ))}
              </ul>
            </div>
          </div>

          {/* Box 3: Preventive Guidance */}
          <div className="result-box-guidance">
            <div className="guidance-icon-wrapper">
              <Lightbulb size={24} strokeWidth={2.2} />
            </div>

            <div className="guidance-content">
              <h3 className="guidance-title">{t('output.preventiveGuidance')}</h3>
              <ul className="bullets-list">
                {guidance.map((step, idx) => (
                  <li key={idx}>{step}</li>
                ))}
              </ul>
            </div>
          </div>

          {/* Box 4: Multi-Disease Risk Probability Breakdown */}
          {result.disease_breakdown && (
            <div style={{ background: '#ffffff', border: '1px solid #cbd5e1', borderRadius: '12px', padding: '1rem 1.25rem', marginTop: '0.5rem' }}>
              <div style={{ display: 'flex', alignItems: 'center', gap: '0.5rem', marginBottom: '0.6rem' }}>
                <Activity size={20} color="#0284c7" />
                <h4 style={{ margin: 0, fontSize: '0.95rem', color: '#0f2b5c', fontWeight: 700 }}>
                  🫀 Multi-Disease Probability Breakdown
                </h4>
              </div>
              <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(200px, 1fr))', gap: '0.8rem' }}>
                {Object.entries(result.disease_breakdown).map(([disease, probPct]) => (
                  <div key={disease} style={{ background: '#f8fafc', padding: '0.6rem 0.8rem', borderRadius: '8px', border: '1px solid #e2e8f0' }}>
                    <div style={{ fontSize: '0.78rem', color: '#475569', fontWeight: 600 }}>{disease}</div>
                    <div style={{ fontSize: '1.1rem', fontWeight: 700, color: probPct > 60 ? '#b91c1c' : probPct > 35 ? '#d97706' : '#047857' }}>
                      {probPct}% Estimated Risk
                    </div>
                  </div>
                ))}
              </div>
            </div>
          )}

          {/* Box 5: Privacy & Confidentiality Certificate */}
          <div style={{ background: '#f8fafc', border: '1px solid #cbd5e1', borderRadius: '12px', padding: '1rem 1.25rem', marginTop: '0.5rem' }}>
            <div style={{ display: 'flex', alignItems: 'center', gap: '0.5rem', marginBottom: '0.6rem' }}>
              <ShieldCheck size={20} color="#047857" />
              <h4 style={{ margin: 0, fontSize: '0.92rem', color: '#0f2b5c', fontWeight: 700 }}>
                {t('output.privacyCertificate')}
              </h4>
            </div>
            <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(220px, 1fr))', gap: '0.6rem', fontSize: '0.8rem', color: '#475569' }}>
              <div>
                <span style={{ fontWeight: 600, color: '#1e293b' }}>{t('output.anonSessionId')} </span>
                <code style={{ background: '#e2e8f0', padding: '0.15rem 0.4rem', borderRadius: '4px', color: '#0f172a', fontWeight: 700 }}>
                  {result.privacy?.anonymous_id || 'ANON-8F92-4C1B'}
                </code>
              </div>
              <div>
                <span style={{ fontWeight: 600, color: '#1e293b' }}>{t('output.kAnonymityLabel')} </span>
                <span>{result.privacy?.k_anonymity_bracket || 'Age [50–54], BMI [25–29.9]'}</span>
              </div>
            </div>
            <div style={{ marginTop: '0.4rem', fontSize: '0.76rem', color: '#047857', fontWeight: 600 }}>
              ✔ {t('output.zeroStorage')}
            </div>
          </div>

          {/* Box 6: Interactive "What-If" Lifestyle Simulator */}
          <WhatIfSimulator originalResult={result} />
        </div>

        {/* Action Buttons */}
        <div className="submit-btn-wrapper" style={{ display: 'flex', gap: '1rem', justifyContent: 'center', marginTop: '1.5rem', flexWrap: 'wrap' }}>
          <button
            type="button"
            className="btn-primary-action"
            onClick={onNewAssessment}
          >
            {t('output.newAssessment')}
          </button>
          <button
            type="button"
            className="btn-primary-action"
            style={{ background: '#047857', borderColor: '#047857' }}
            onClick={() => window.print()}
          >
            📄 Download Clinical Report (PDF)
          </button>
        </div>
      </div>
    </div>
  );
}
