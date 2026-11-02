import React, { useState } from 'react';
import { useTranslation } from 'react-i18next';
import { Stethoscope, ArrowLeft, ShieldCheck } from 'lucide-react';

export default function AdvancedAssessmentPage({ onSubmit, onBack }) {
  const { t, i18n } = useTranslation();
  const isTamil = i18n.language === 'ta';

  const [formData, setFormData] = useState({
    age: '',
    gender: 'Male',
    height_cm: '',
    weight_kg: '',
    systolic_bp: '',
    diastolic_bp: '',
    fasting_glucose: '',
    hba1c: '',
    total_cholesterol: '',
    hdl_cholesterol: '',
    ldl_cholesterol: '',
    resting_heart_rate: '',
    smoking_habit: 'Non-smoker',
    alcohol_consumption: 'None',
    physical_activity: 'Moderate',
    sleep_hours: '',
    family_history: [],
    symptoms: []
  });

  const handleSubmit = (e) => {
    e.preventDefault();
    const cleanPayload = {
      age: Number(formData.age) || 45,
      gender: formData.gender || 'Male',
      height_cm: Number(formData.height_cm) || 170,
      weight_kg: Number(formData.weight_kg) || 70,
      systolic_bp: Number(formData.systolic_bp) || 120,
      diastolic_bp: Number(formData.diastolic_bp) || 80,
      fasting_glucose: Number(formData.fasting_glucose) || 95,
      hba1c: Number(formData.hba1c) || 5.4,
      total_cholesterol: Number(formData.total_cholesterol) || 180,
      hdl_cholesterol: Number(formData.hdl_cholesterol) || 50,
      ldl_cholesterol: Number(formData.ldl_cholesterol) || 100,
      resting_heart_rate: Number(formData.resting_heart_rate) || 72,
      smoking_habit: formData.smoking_habit,
      alcohol_consumption: formData.alcohol_consumption,
      physical_activity: formData.physical_activity,
      sleep_hours: Number(formData.sleep_hours) || 7.0,
      family_history: formData.family_history,
      symptoms: formData.symptoms
    };
    onSubmit(cleanPayload);
  };

  return (
    <div className="assessment-card" style={{ maxWidth: '850px', margin: '0 auto' }}>
      <div className="card-header-banner">
        <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', marginBottom: '0.8rem' }}>
          <button
            type="button"
            onClick={onBack}
            style={{ background: 'rgba(255,255,255,0.2)', border: 'none', color: '#ffffff', padding: '0.4rem 0.8rem', borderRadius: '8px', cursor: 'pointer', display: 'inline-flex', alignItems: 'center', gap: '0.4rem', fontSize: '0.85rem', fontWeight: 600 }}
          >
            <ArrowLeft size={16} />
            <span>{isTamil ? 'முகப்புக்கு திரும்ப' : 'Back to Home'}</span>
          </button>
          <div style={{ padding: '0.3rem 0.75rem', background: '#ecfdf5', border: '1px solid #6ee7b7', borderRadius: '9999px', fontSize: '0.78rem', color: '#047857', fontWeight: 600 }}>
            {isTamil ? '🧪 முறை 2: தீவிர மருத்துவ மதிப்பீடு' : '🧪 Mode 2: Advanced Clinical Assessment'}
          </div>
        </div>

        <h2 className="card-header-title">{isTamil ? '2. தீவிர மருத்துவ சுகாதார மதிப்பீடு' : '2. Advanced Clinical Health Assessment'}</h2>
        <p className="card-header-subtitle">
          {isTamil ? 'இரத்த அழுத்தம், சர்க்கரை அளவு மற்றும் கொழுப்பைக் கொண்ட விரிவான பகுப்பாய்வு' : 'Comprehensive evaluation incorporating clinical lab biomarkers (BP, Fasting Glucose, Cholesterol)'}
        </p>
      </div>

      <form onSubmit={handleSubmit} className="card-body">
        {/* Section 1: Demographics */}
        <h4 style={{ color: '#0f2b5c', borderBottom: '1px solid #e2e8f0', paddingBottom: '0.4rem', marginBottom: '1rem' }}>
          {isTamil ? 'பிரிவு 1: அடிப்படை விவரங்கள்' : 'Section 1: Demographics & Body Metrics'}
        </h4>
        <div className="form-two-col-grid">
          <div className="input-field-group">
            <label className="input-label">{t('form.age')}</label>
            <input
              type="number"
              className="text-input"
              value={formData.age}
              onChange={(e) => setFormData({ ...formData, age: e.target.value })}
              placeholder={isTamil ? 'எ.கா. 45' : 'e.g. 45'}
              required
            />
          </div>
          <div className="input-field-group">
            <label className="input-label">{t('form.gender')}</label>
            <select
              className="select-input"
              value={formData.gender}
              onChange={(e) => setFormData({ ...formData, gender: e.target.value })}
            >
              <option value="Male">{t('form.male')}</option>
              <option value="Female">{t('form.female')}</option>
              <option value="Other">{t('form.other')}</option>
            </select>
          </div>
          <div className="input-field-group">
            <label className="input-label">{t('form.height')}</label>
            <input
              type="number"
              className="text-input"
              value={formData.height_cm}
              onChange={(e) => setFormData({ ...formData, height_cm: e.target.value })}
              placeholder={isTamil ? 'எ.கா. 170' : 'e.g. 170'}
              required
            />
          </div>
          <div className="input-field-group">
            <label className="input-label">{t('form.weight')}</label>
            <input
              type="number"
              className="text-input"
              value={formData.weight_kg}
              onChange={(e) => setFormData({ ...formData, weight_kg: e.target.value })}
              placeholder={isTamil ? 'எ.கா. 70' : 'e.g. 70'}
              required
            />
          </div>
        </div>

        {/* Section 2: Clinical Biomarkers */}
        <h4 style={{ color: '#0f2b5c', borderBottom: '1px solid #e2e8f0', paddingBottom: '0.4rem', margin: '1.5rem 0 1rem 0' }}>
          🧪 {isTamil ? 'பிரிவு 2: மருத்துவ ஆய்வு அளவுருக்கள் (Clinical Biomarkers)' : 'Section 2: Clinical Laboratory Biomarkers'}
        </h4>

        <div className="form-two-col-grid">
          <div className="input-field-group">
            <label className="input-label">Systolic Blood Pressure (mmHg)</label>
            <input
              type="number"
              className="text-input"
              value={formData.systolic_bp}
              onChange={(e) => setFormData({ ...formData, systolic_bp: e.target.value })}
              placeholder="e.g. 120"
            />
          </div>
          <div className="input-field-group">
            <label className="input-label">Diastolic Blood Pressure (mmHg)</label>
            <input
              type="number"
              className="text-input"
              value={formData.diastolic_bp}
              onChange={(e) => setFormData({ ...formData, diastolic_bp: e.target.value })}
              placeholder="e.g. 80"
            />
          </div>
          <div className="input-field-group">
            <label className="input-label">Fasting Blood Glucose (mg/dL)</label>
            <input
              type="number"
              className="text-input"
              value={formData.fasting_glucose}
              onChange={(e) => setFormData({ ...formData, fasting_glucose: e.target.value })}
              placeholder="e.g. 95"
            />
          </div>
          <div className="input-field-group">
            <label className="input-label">HbA1c (%)</label>
            <input
              type="number"
              step="0.1"
              className="text-input"
              value={formData.hba1c}
              onChange={(e) => setFormData({ ...formData, hba1c: e.target.value })}
              placeholder="e.g. 5.4"
            />
          </div>
          <div className="input-field-group">
            <label className="input-label">Total Cholesterol (mg/dL)</label>
            <input
              type="number"
              className="text-input"
              value={formData.total_cholesterol}
              onChange={(e) => setFormData({ ...formData, total_cholesterol: e.target.value })}
              placeholder="e.g. 180"
            />
          </div>
          <div className="input-field-group">
            <label className="input-label">Resting Heart Rate (BPM)</label>
            <input
              type="number"
              className="text-input"
              value={formData.resting_heart_rate}
              onChange={(e) => setFormData({ ...formData, resting_heart_rate: e.target.value })}
              placeholder="e.g. 72"
            />
          </div>
        </div>

        {/* Submit */}
        <div className="submit-btn-wrapper" style={{ marginTop: '2rem' }}>
          <button type="submit" className="btn-primary-action" style={{ background: '#047857', borderColor: '#047857' }}>
            {isTamil ? 'மருத்துவ பகுப்பாய்வு செய்க' : 'Run Advanced Clinical Assessment'}
          </button>
        </div>
      </form>
    </div>
  );
}
