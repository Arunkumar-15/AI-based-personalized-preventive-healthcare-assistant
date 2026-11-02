import React from 'react';
import { useTranslation } from 'react-i18next';
import { ClipboardList, Stethoscope, FileText, ArrowRight, ShieldCheck, Activity, Award } from 'lucide-react';

export default function HomePage({ onSelectMode }) {
  const { t, i18n } = useTranslation();
  const isTamil = i18n.language === 'ta';

  return (
    <div style={{ maxWidth: '1100px', margin: '0 auto', padding: '1rem 1rem 3rem 1rem' }}>
      {/* Hero Section */}
      <div style={{ background: 'linear-gradient(135deg, #0f2b5c 0%, #1e3a8a 100%)', color: '#ffffff', borderRadius: '24px', padding: '2.5rem 2rem', textAlign: 'center', marginBottom: '2.5rem', boxShadow: '0 12px 24px rgba(15,43,92,0.15)' }}>
        <div style={{ display: 'inline-flex', alignItems: 'center', gap: '0.5rem', padding: '0.4rem 1rem', background: 'rgba(255,255,255,0.15)', borderRadius: '9999px', fontSize: '0.82rem', fontWeight: 600, marginBottom: '1.2rem', backdropFilter: 'blur(4px)' }}>
          <ShieldCheck size={16} color="#6ee7b7" />
          <span>{isTamil ? '100% தனிப்பட்ட மற்றும் பெயர் மறைக்கப்பட்ட மதிப்பீடு' : '100% Private & Anonymous AI Health Screening'}</span>
        </div>

        <h1 style={{ fontSize: '2.2rem', fontWeight: 800, margin: '0 0 1rem 0', lineHeight: 1.25 }}>
          {isTamil ? 'AI தனிப்பயனாக்கப்பட்ட தடுப்பு சுகாதார உதவியாளர்' : 'AI-Based Personalized Preventive Healthcare Assistant'}
        </h1>

        <p style={{ fontSize: '1.05rem', color: '#93c5fd', maxWidth: '780px', margin: '0 auto 1.8rem auto', lineHeight: 1.6 }}>
          {isTamil 
            ? 'உங்கள் சுகாதார அபாயத்தை துல்லியமாக கணிக்கவும், SHAP AI விளக்கங்களைப் பெறவும், தடுப்பு வழிகாட்டுதல்களை அறியவும் கீழே உள்ள 3 மதிப்பீட்டு முறைகளில் ஒன்றைத் தேர்ந்தெடுக்கவும்.'
            : 'Select one of the 3 assessment modes below to screen your health risk, explore explainable AI insights (SHAP), and receive personalized preventive guidance.'}
        </p>

        <div style={{ display: 'flex', justifyContent: 'center', gap: '2rem', flexWrap: 'wrap', fontSize: '0.85rem', color: '#cbd5e1' }}>
          <div>✔ {isTamil ? '99.86% சரிபார்க்கப்பட்ட மாதிரி துல்லியம்' : '99.86% Verified Model Accuracy'}</div>
          <div>✔ {isTamil ? 'SHAP கணித முறை விளக்கம்' : 'SHAP Explainable AI Attribution'}</div>
          <div>✔ {isTamil ? 'பெயர் மறைக்கப்பட்ட பாதுகாப்பான சேமிப்பு' : 'Privacy-Preserving Anonymized Storage'}</div>
        </div>
      </div>

      {/* 3 Input Modes Grid Section Header */}
      <div style={{ textAlign: 'center', marginBottom: '1.8rem' }}>
        <h2 style={{ fontSize: '1.6rem', color: '#0f2b5c', fontWeight: 700, margin: '0 0 0.4rem 0' }}>
          {isTamil ? '3 சுகாதார மதிப்பீட்டு முறைகள்' : 'Choose Assessment Input Mode'}
        </h2>
        <p style={{ color: '#64748b', fontSize: '0.92rem', margin: 0 }}>
          {isTamil ? 'உங்கள் வசதிக்கேற்ப கீழே உள்ள 3 முறைகளில் ஒன்றை தேர்வு செய்யவும்' : 'Select your preferred evaluation mode to begin screening'}
        </p>
      </div>

      {/* 3 Input Mode Cards */}
      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(300px, 1fr))', gap: '1.5rem' }}>
        
        {/* Mode 1: Basic Health Assessment */}
        <div style={{ background: '#ffffff', border: '2px solid #0284c7', borderRadius: '18px', padding: '1.8rem 1.5rem', display: 'flex', flexDirection: 'column', justifyContent: 'space-between', transition: 'all 0.2s ease', boxShadow: '0 8px 16px rgba(2,132,199,0.08)' }}>
          <div>
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '1rem' }}>
              <div style={{ background: '#e0f2fe', width: '52px', height: '52px', borderRadius: '14px', display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
                <ClipboardList size={28} color="#0284c7" />
              </div>
              <span style={{ padding: '0.3rem 0.75rem', background: '#ecfdf5', color: '#047857', border: '1px solid #6ee7b7', borderRadius: '9999px', fontSize: '0.75rem', fontWeight: 700 }}>
                {isTamil ? '✅ முறை 1 (செயலில் உள்ளது)' : '✅ MODE 1 (ACTIVE)'}
              </span>
            </div>

            <h3 style={{ fontSize: '1.25rem', color: '#0f2b5c', fontWeight: 700, margin: '0 0 0.6rem 0' }}>
              {isTamil ? '1. அடிப்படை சுகாதார மதிப்பீடு' : '1. Basic Health Assessment'}
            </h3>

            <p style={{ fontSize: '0.88rem', color: '#475569', lineHeight: 1.5, marginBottom: '1.2rem' }}>
              {isTamil 
                ? 'வயது, எடை, உயரம், புகை பிடித்தல்/மது பழக்கம், குடும்ப வரலாறு மற்றும் அறிகுறிகளை அடிப்படையாகக் கொண்ட விரைவு மதிப்பீடு.'
                : 'Non-invasive screening based on age, BMI, lifestyle habits (smoking/alcohol/sleep), family medical history, and symptoms.'}
            </p>

            <ul style={{ paddingLeft: '1.2rem', fontSize: '0.82rem', color: '#64748b', lineHeight: 1.6, marginBottom: '1.5rem' }}>
              <li>{isTamil ? 'வயது, BMI, தூக்க நேரம்' : 'Age, BMI, Sleep Duration'}</li>
              <li>{isTamil ? 'புகை / மது பழக்கத்தின் வகை' : 'Smoking & Alcohol Frequency'}</li>
              <li>{isTamil ? 'குடும்ப மருத்துவ வரலாறு & அறிகுறிகள்' : 'Family Medical History & Symptoms'}</li>
            </ul>
          </div>

          <button
            type="button"
            onClick={() => onSelectMode('basic_input')}
            style={{ width: '100%', padding: '0.85rem', background: '#0284c7', color: '#ffffff', border: 'none', borderRadius: '10px', fontWeight: 700, fontSize: '0.92rem', cursor: 'pointer', display: 'flex', alignItems: 'center', justifyContent: 'center', gap: '0.5rem' }}
          >
            <span>{isTamil ? 'மதிப்பீட்டைத் தொடங்கவும்' : 'Start Basic Assessment'}</span>
            <ArrowRight size={18} />
          </button>
        </div>

        {/* Mode 2: Advanced Clinical Assessment */}
        <div style={{ background: '#ffffff', border: '1px solid #cbd5e1', borderRadius: '18px', padding: '1.8rem 1.5rem', display: 'flex', flexDirection: 'column', justifyContent: 'space-between', transition: 'all 0.2s ease', boxShadow: '0 4px 12px rgba(0,0,0,0.03)' }}>
          <div>
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '1rem' }}>
              <div style={{ background: '#f0fdf4', width: '52px', height: '52px', borderRadius: '14px', display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
                <Stethoscope size={28} color="#047857" />
              </div>
              <span style={{ padding: '0.3rem 0.75rem', background: '#f0fdf4', color: '#047857', border: '1px solid #a7f3d0', borderRadius: '9999px', fontSize: '0.75rem', fontWeight: 700 }}>
                {isTamil ? '🧪 முறை 2 (மருத்துவ பரிசோதனை)' : '🧪 MODE 2 (CLINICAL LAB)'}
              </span>
            </div>

            <h3 style={{ fontSize: '1.25rem', color: '#0f2b5c', fontWeight: 700, margin: '0 0 0.6rem 0' }}>
              {isTamil ? '2. தீவிர மருத்துவ மதிப்பீடு' : '2. Advanced Clinical Assessment'}
            </h3>

            <p style={{ fontSize: '0.88rem', color: '#475569', lineHeight: 1.5, marginBottom: '1.2rem' }}>
              {isTamil
                ? 'இரத்த அழுத்தம் (BP), இரத்த சர்க்கரை அளவு (Glucose), கொழுப்பு (Cholesterol) போன்ற மருத்துவ ஆய்வு முடிவுகளைக் கொண்ட தீவிர மதிப்பீடு.'
                : 'Comprehensive clinical evaluation incorporating lab biomarkers (Blood Pressure mmHg, Fasting Glucose mg/dL, HbA1c, Cholesterol).'}
            </p>

            <ul style={{ paddingLeft: '1.2rem', fontSize: '0.82rem', color: '#64748b', lineHeight: 1.6, marginBottom: '1.5rem' }}>
              <li>{isTamil ? 'இரத்த அழுத்தம் (BP mmHg)' : 'Blood Pressure (Systolic & Diastolic)'}</li>
              <li>{isTamil ? 'இரத்த சர்க்கரை (Glucose mg/dL) & HbA1c' : 'Fasting Blood Glucose & HbA1c (%)'}</li>
              <li>{isTamil ? 'கொலஸ்ட்ரால் & இதயத் துடிப்பு' : 'Total Cholesterol & Resting Heart Rate'}</li>
            </ul>
          </div>

          <button
            type="button"
            onClick={() => onSelectMode('advanced_input')}
            style={{ width: '100%', padding: '0.85rem', background: '#047857', color: '#ffffff', border: 'none', borderRadius: '10px', fontWeight: 700, fontSize: '0.92rem', cursor: 'pointer', display: 'flex', alignItems: 'center', justifyContent: 'center', gap: '0.5rem' }}
          >
            <span>{isTamil ? 'மருத்துவ மதிப்பீடு தொடங்க' : 'Start Advanced Assessment'}</span>
            <ArrowRight size={18} />
          </button>
        </div>

        {/* Mode 3: Medical Report Upload & OCR Scanner */}
        <div style={{ background: '#ffffff', border: '1px solid #cbd5e1', borderRadius: '18px', padding: '1.8rem 1.5rem', display: 'flex', flexDirection: 'column', justifyContent: 'space-between', transition: 'all 0.2s ease', boxShadow: '0 4px 12px rgba(0,0,0,0.03)' }}>
          <div>
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '1rem' }}>
              <div style={{ background: '#fef3c7', width: '52px', height: '52px', borderRadius: '14px', display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
                <FileText size={28} color="#d97706" />
              </div>
              <span style={{ padding: '0.3rem 0.75rem', background: '#fffbeb', color: '#b45309', border: '1px solid #fde68a', borderRadius: '9999px', fontSize: '0.75rem', fontWeight: 700 }}>
                {isTamil ? '📄 முறை 3 (OCR ஸ்கேனர்)' : '📄 MODE 3 (OCR SCANNER)'}
              </span>
            </div>

            <h3 style={{ fontSize: '1.25rem', color: '#0f2b5c', fontWeight: 700, margin: '0 0 0.6rem 0' }}>
              {isTamil ? '3. மருத்துவ அறிக்கை பதிவேற்றம் (OCR)' : '3. Medical Report Upload & OCR'}
            </h3>

            <p style={{ fontSize: '0.88rem', color: '#475569', lineHeight: 1.5, marginBottom: '1.2rem' }}>
              {isTamil
                ? 'உங்கள் இரத்த பரிசோதனை அறிக்கை (PDF/புகைப்படம்) பதிவேற்றம் செய்து தானாகவே எண்களை பிரித்தெடுத்து பகுப்பாய்வு செய்யும் முறை.'
                : 'Upload your lab test report photo or PDF. Our OCR scanner automatically extracts numerical values for 1-click assessment.'}
            </p>

            <ul style={{ paddingLeft: '1.2rem', fontSize: '0.82rem', color: '#64748b', lineHeight: 1.6, marginBottom: '1.5rem' }}>
              <li>{isTamil ? 'PDF அறிக்கை / புகைப்பட பதிவேற்றம்' : 'PDF Report or Photo Upload (.pdf, .jpg)'}</li>
              <li>{isTamil ? 'தானியங்கி எண்கள் பிரித்தெடுத்தல்' : 'Automated Lab Biomarker Extraction'}</li>
              <li>{isTamil ? '1-கிளிக் AI பகுப்பாய்வு' : 'Instant 1-Click AI Inference'}</li>
            </ul>
          </div>

          <button
            type="button"
            onClick={() => onSelectMode('ocr_upload')}
            style={{ width: '100%', padding: '0.85rem', background: '#d97706', color: '#ffffff', border: 'none', borderRadius: '10px', fontWeight: 700, fontSize: '0.92rem', cursor: 'pointer', display: 'flex', alignItems: 'center', justifyContent: 'center', gap: '0.5rem' }}
          >
            <span>{isTamil ? 'அறிக்கை பதிவேற்றம் செய்ய' : 'Upload Report & Scan'}</span>
            <ArrowRight size={18} />
          </button>
        </div>

      </div>
    </div>
  );
}
