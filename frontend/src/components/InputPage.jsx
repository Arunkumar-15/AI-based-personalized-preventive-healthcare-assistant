import React, { useState } from 'react';
import { useTranslation } from 'react-i18next';

export default function InputPage({ onSubmit, isLoading }) {
  const { t } = useTranslation();
  
  const [formData, setFormData] = useState({
    age: '',
    gender: '',
    height_cm: '',
    weight_kg: '',
    smoking: 'No',
    smoking_frequency: 'Regular', // 'Regular' | 'Occasional'
    alcohol: 'No',
    alcohol_frequency: 'Occasional', // 'Regular' | 'Occasional'
    physical_activity: '',
    sleep_hours: '',
    family_history: [],
    symptoms: []
  });

  const handleInputChange = (field, value) => {
    setFormData(prev => ({ ...prev, [field]: value }));
  };

  const handleFamilyToggle = (item) => {
    setFormData(prev => {
      if (item === 'None') {
        // If clicking None, clear other selections and set only None
        const isNoneSelected = prev.family_history.includes('None');
        return { ...prev, family_history: isNoneSelected ? [] : ['None'] };
      } else {
        // If clicking a disease, remove 'None' and toggle the disease
        const withoutNone = prev.family_history.filter(f => f !== 'None');
        const exists = withoutNone.includes(item);
        const updated = exists
          ? withoutNone.filter(f => f !== item)
          : [...withoutNone, item];
        return { ...prev, family_history: updated };
      }
    });
  };

  const handleSymptomToggle = (item) => {
    setFormData(prev => {
      const exists = prev.symptoms.includes(item);
      const updated = exists
        ? prev.symptoms.filter(s => s !== item)
        : [...prev.symptoms, item];
      return { ...prev, symptoms: updated };
    });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    
    // Map smoking habit
    let finalSmoking = 'Non-smoker';
    if (formData.smoking === 'Yes') {
      finalSmoking = formData.smoking_frequency === 'Regular' ? 'Regular Smoker' : 'Occasional Smoker';
    }

    // Map alcohol consumption
    let finalAlcohol = 'None';
    if (formData.alcohol === 'Yes') {
      finalAlcohol = formData.alcohol_frequency === 'Regular' ? 'Frequent' : 'Moderate';
    }

    // Filter family history
    const cleanFamilyHistory = formData.family_history.filter(f => f !== 'None');

    const payload = {
      age: Number(formData.age) || 45,
      gender: formData.gender || 'Male',
      height_cm: Number(formData.height_cm) || 170,
      weight_kg: Number(formData.weight_kg) || 75,
      smoking_habit: finalSmoking,
      alcohol_consumption: finalAlcohol,
      physical_activity: formData.physical_activity || 'Moderate',
      sleep_hours: Number(formData.sleep_hours) || 7.0,
      family_history: cleanFamilyHistory,
      symptoms: formData.symptoms,
      other_symptom: cleanFamilyHistory.includes('Other') ? 'Other family condition' : ''
    };
    onSubmit(payload);
  };

  const familyHistoryItems = [
    { id: 'None', label: t('form.noneFamily') },
    { id: 'Heart Disease', label: t('form.heartDisease') },
    { id: 'Diabetes', label: t('form.diabetes') },
    { id: 'Hypertension', label: t('form.hypertension') },
    { id: 'Other', label: t('form.otherFamily') }
  ];

  const leftSymptoms = [
    { id: 'Fatigue', label: t('form.fatigue') },
    { id: 'Chest Pain', label: t('form.chestPain') },
    { id: 'Shortness of Breath', label: t('form.shortnessOfBreath') }
  ];

  const rightSymptoms = [
    { id: 'Excessive Thirst', label: t('form.excessiveThirst') },
    { id: 'Frequent Urination', label: t('form.frequentUrination') },
    { id: 'Dizziness', label: t('form.dizziness') }
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
        <h2 className="card-header-title">{t('form.title')}</h2>
        <p className="card-header-subtitle">
          {t('form.subtitle')}
        </p>
        <div style={{ display: 'inline-flex', alignItems: 'center', gap: '0.4rem', marginTop: '0.6rem', padding: '0.3rem 0.75rem', background: '#ecfdf5', border: '1px solid #6ee7b7', borderRadius: '9999px', fontSize: '0.78rem', color: '#047857', fontWeight: 600 }}>
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
            <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/>
            <path d="M9 12l2 2 4-4"/>
          </svg>
          <span>{t('form.privacyBadge')}</span>
        </div>
      </div>

      {/* Form Body */}
      <form onSubmit={handleSubmit} className="card-body">
        {/* Row 1: Age & Gender */}
        <div className="form-two-col-grid">
          <div className="input-field-group">
            <label className="input-label">{t('form.age')}</label>
            <input
              type="number"
              placeholder="e.g. 45"
              className="text-input"
              value={formData.age}
              onChange={(e) => handleInputChange('age', e.target.value)}
              required
            />
          </div>

          <div className="input-field-group">
            <label className="input-label">{t('form.gender')}</label>
            <select
              className="select-input"
              value={formData.gender}
              onChange={(e) => handleInputChange('gender', e.target.value)}
              required
            >
              <option value="" disabled>{t('form.selectGender')}</option>
              <option value="Male">{t('form.male')}</option>
              <option value="Female">{t('form.female')}</option>
              <option value="Other">{t('form.other')}</option>
            </select>
          </div>
        </div>

        {/* Row 2: Height & Weight */}
        <div className="form-two-col-grid">
          <div className="input-field-group">
            <label className="input-label">{t('form.height')}</label>
            <input
              type="number"
              placeholder="e.g. 175"
              className="text-input"
              value={formData.height_cm}
              onChange={(e) => handleInputChange('height_cm', e.target.value)}
              required
            />
          </div>

          <div className="input-field-group">
            <label className="input-label">{t('form.weight')}</label>
            <input
              type="number"
              placeholder="e.g. 75"
              className="text-input"
              value={formData.weight_kg}
              onChange={(e) => handleInputChange('weight_kg', e.target.value)}
              required
            />
          </div>
        </div>

        {/* Lifestyle Section */}
        <h3 className="form-section-heading">{t('nav.about') === 'About' ? 'Lifestyle Information' : 'வாழ்க்கை முறை விவரங்கள்'}</h3>

        {/* Row 3: Smoking & Alcohol Radio Options */}
        <div className="form-two-col-grid">
          {/* Smoking Block */}
          <div className="input-field-group">
            <label className="input-label">{t('form.smoking')}</label>
            <div className="radio-options-row">
              <label className="radio-label">
                <input
                  type="radio"
                  name="smoking"
                  value="Yes"
                  checked={formData.smoking === 'Yes'}
                  onChange={() => handleInputChange('smoking', 'Yes')}
                />
                <span>{t('form.yes')}</span>
              </label>
              <label className="radio-label">
                <input
                  type="radio"
                  name="smoking"
                  value="No"
                  checked={formData.smoking === 'No'}
                  onChange={() => handleInputChange('smoking', 'No')}
                />
                <span>{t('form.no')}</span>
              </label>
            </div>

            {/* Sub-selection if Smoking == Yes */}
            {formData.smoking === 'Yes' && (
              <div style={{ marginTop: '0.65rem', padding: '0.5rem 0.75rem', background: '#f1f5f9', borderRadius: '8px', border: '1px solid #cbd5e1' }}>
                <span style={{ fontSize: '0.78rem', fontWeight: 700, color: '#0f2b5c', display: 'block', marginBottom: '0.35rem' }}>
                  {t('form.smokingFrequency')}:
                </span>
                <div style={{ display: 'flex', gap: '1rem' }}>
                  <label className="radio-label" style={{ fontSize: '0.82rem' }}>
                    <input
                      type="radio"
                      name="smoking_freq"
                      value="Regular"
                      checked={formData.smoking_frequency === 'Regular'}
                      onChange={() => handleInputChange('smoking_frequency', 'Regular')}
                    />
                    <span>{t('form.regular')}</span>
                  </label>
                  <label className="radio-label" style={{ fontSize: '0.82rem' }}>
                    <input
                      type="radio"
                      name="smoking_freq"
                      value="Occasional"
                      checked={formData.smoking_frequency === 'Occasional'}
                      onChange={() => handleInputChange('smoking_frequency', 'Occasional')}
                    />
                    <span>{t('form.occasional')}</span>
                  </label>
                </div>
              </div>
            )}
          </div>

          {/* Alcohol Block */}
          <div className="input-field-group">
            <label className="input-label">{t('form.alcohol')}</label>
            <div className="radio-options-row">
              <label className="radio-label">
                <input
                  type="radio"
                  name="alcohol"
                  value="Yes"
                  checked={formData.alcohol === 'Yes'}
                  onChange={() => handleInputChange('alcohol', 'Yes')}
                />
                <span>{t('form.yes')}</span>
              </label>
              <label className="radio-label">
                <input
                  type="radio"
                  name="alcohol"
                  value="No"
                  checked={formData.alcohol === 'No'}
                  onChange={() => handleInputChange('alcohol', 'No')}
                />
                <span>{t('form.no')}</span>
              </label>
            </div>

            {/* Sub-selection if Alcohol == Yes */}
            {formData.alcohol === 'Yes' && (
              <div style={{ marginTop: '0.65rem', padding: '0.5rem 0.75rem', background: '#f1f5f9', borderRadius: '8px', border: '1px solid #cbd5e1' }}>
                <span style={{ fontSize: '0.78rem', fontWeight: 700, color: '#0f2b5c', display: 'block', marginBottom: '0.35rem' }}>
                  {t('form.alcoholFrequency')}:
                </span>
                <div style={{ display: 'flex', gap: '1rem' }}>
                  <label className="radio-label" style={{ fontSize: '0.82rem' }}>
                    <input
                      type="radio"
                      name="alcohol_freq"
                      value="Regular"
                      checked={formData.alcohol_frequency === 'Regular'}
                      onChange={() => handleInputChange('alcohol_frequency', 'Regular')}
                    />
                    <span>{t('form.regular')}</span>
                  </label>
                  <label className="radio-label" style={{ fontSize: '0.82rem' }}>
                    <input
                      type="radio"
                      name="alcohol_freq"
                      value="Occasional"
                      checked={formData.alcohol_frequency === 'Occasional'}
                      onChange={() => handleInputChange('alcohol_frequency', 'Occasional')}
                    />
                    <span>{t('form.occasional')}</span>
                  </label>
                </div>
              </div>
            )}
          </div>
        </div>

        {/* Row 4: Physical Activity & Sleep Hours */}
        <div className="form-two-col-grid">
          <div className="input-field-group">
            <label className="input-label">{t('form.physicalActivity')}</label>
            <select
              className="select-input"
              value={formData.physical_activity}
              onChange={(e) => handleInputChange('physical_activity', e.target.value)}
              required
            >
              <option value="" disabled>{t('form.physicalActivity')}</option>
              <option value="Sedentary">{t('form.sedentary')}</option>
              <option value="Light">{t('form.light')}</option>
              <option value="Moderate">{t('form.moderate')}</option>
              <option value="Active">{t('form.active')}</option>
            </select>
          </div>

          <div className="input-field-group">
            <label className="input-label">{t('form.sleepHours')}</label>
            <input
              type="number"
              step="0.5"
              placeholder="e.g. 7.0"
              className="text-input"
              value={formData.sleep_hours}
              onChange={(e) => handleInputChange('sleep_hours', e.target.value)}
              required
            />
          </div>
        </div>

        {/* Family History */}
        <h3 className="form-section-heading">{t('form.familyHistory')}</h3>
        <div className="checkbox-inline-row">
          {familyHistoryItems.map((item) => (
            <label key={item.id} className="checkbox-item-label">
              <input
                type="checkbox"
                checked={formData.family_history.includes(item.id)}
                onChange={() => handleFamilyToggle(item.id)}
              />
              <span>{item.label}</span>
            </label>
          ))}
        </div>

        {/* Symptoms */}
        <h3 className="form-section-heading">{t('form.symptoms')}</h3>
        <div className="checkbox-two-col-grid">
          <div style={{ display: 'flex', flexDirection: 'column', gap: '0.75rem' }}>
            {leftSymptoms.map((sym) => (
              <label key={sym.id} className="checkbox-item-label">
                <input
                  type="checkbox"
                  checked={formData.symptoms.includes(sym.id)}
                  onChange={() => handleSymptomToggle(sym.id)}
                />
                <span>{sym.label}</span>
              </label>
            ))}
          </div>

          <div style={{ display: 'flex', flexDirection: 'column', gap: '0.75rem' }}>
            {rightSymptoms.map((sym) => (
              <label key={sym.id} className="checkbox-item-label">
                <input
                  type="checkbox"
                  checked={formData.symptoms.includes(sym.id)}
                  onChange={() => handleSymptomToggle(sym.id)}
                />
                <span>{sym.label}</span>
              </label>
            ))}
          </div>
        </div>

        {/* Submit Button */}
        <div className="submit-btn-wrapper">
          <button
            type="submit"
            className="btn-primary-action"
            disabled={isLoading}
          >
            {isLoading ? t('form.submitting') : t('form.submit')}
          </button>
        </div>
      </form>
    </div>
  );
}
