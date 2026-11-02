import React, { useState, useMemo } from 'react';
import { 
  User, 
  HeartPulse, 
  Moon, 
  Flame, 
  Dna, 
  Stethoscope, 
  Sparkles, 
  ChevronRight, 
  AlertCircle 
} from 'lucide-react';

const PRESET_PROFILES = [
  {
    name: '1. Healthy & Active Profile',
    desc: '28yo, non-smoker, active exercise, normal BMI, 8h sleep',
    data: {
      age: 28,
      gender: 'Female',
      height_cm: 168,
      weight_kg: 60,
      smoking_habit: 'Non-smoker',
      alcohol_consumption: 'Occasional',
      physical_activity: 'Active',
      sleep_hours: 8.0,
      family_history: [],
      symptoms: [],
      other_symptom: ''
    }
  },
  {
    name: '2. High Cardiovascular Risk',
    desc: '56yo, regular smoker, chest pain, shortness of breath, hypertension family history',
    data: {
      age: 56,
      gender: 'Male',
      height_cm: 174,
      weight_kg: 89,
      smoking_habit: 'Regular Smoker',
      alcohol_consumption: 'Moderate',
      physical_activity: 'Sedentary',
      sleep_hours: 5.5,
      family_history: ['Heart Disease', 'Hypertension'],
      symptoms: ['Chest Pain', 'Shortness of Breath', 'Fatigue'],
      other_symptom: ''
    }
  },
  {
    name: '3. Metabolic & Diabetes Risk',
    desc: '47yo, BMI 32.1, excessive thirst, frequent urination, diabetes family history',
    data: {
      age: 47,
      gender: 'Male',
      height_cm: 170,
      weight_kg: 93,
      smoking_habit: 'Former Smoker',
      alcohol_consumption: 'None',
      physical_activity: 'Light',
      sleep_hours: 6.0,
      family_history: ['Diabetes'],
      symptoms: ['Excessive Thirst', 'Frequent Urination', 'Fatigue'],
      other_symptom: ''
    }
  },
  {
    name: '4. Moderate Lifestyle Strain',
    desc: '38yo, sedentary, occasional smoking, fatigue, irregular sleep',
    data: {
      age: 38,
      gender: 'Female',
      height_cm: 162,
      weight_kg: 72,
      smoking_habit: 'Occasional Smoker',
      alcohol_consumption: 'Moderate',
      physical_activity: 'Sedentary',
      sleep_hours: 5.0,
      family_history: ['Hypertension'],
      symptoms: ['Fatigue', 'Headache'],
      other_symptom: ''
    }
  }
];

const PREDEFINED_SYMPTOMS = [
  'Fatigue',
  'Chest Pain',
  'Excessive Thirst',
  'Frequent Urination',
  'Shortness of Breath',
  'Dizziness',
  'Headache'
];

const FAMILY_CONDITIONS = [
  'Hypertension',
  'Diabetes',
  'Heart Disease',
  'Stroke',
  'Cancer'
];

export default function BasicAssessmentForm({ onSubmit, isLoading }) {
  const [formData, setFormData] = useState({
    age: 42,
    gender: 'Male',
    height_cm: 172,
    weight_kg: 76,
    smoking_habit: 'Non-smoker',
    alcohol_consumption: 'Occasional',
    physical_activity: 'Light',
    sleep_hours: 7.0,
    family_history: ['Hypertension'],
    symptoms: ['Fatigue'],
    other_symptom: ''
  });

  const [hasOtherSymptom, setHasOtherSymptom] = useState(false);

  // Real-time BMI calculation
  const bmiInfo = useMemo(() => {
    const hM = formData.height_cm / 100;
    if (!hM || hM <= 0) return { bmi: 0, category: 'Unknown', pillClass: 'normal' };
    const val = Number((formData.weight_kg / (hM * hM)).toFixed(1));
    let cat = 'Normal Weight';
    let pill = 'normal';
    if (val < 18.5) { cat = 'Underweight'; pill = 'underweight'; }
    else if (val < 25) { cat = 'Normal Weight'; pill = 'normal'; }
    else if (val < 30) { cat = 'Overweight'; pill = 'overweight'; }
    else { cat = 'Obese'; pill = 'obese'; }
    return { bmi: val, category: cat, pillClass: pill };
  }, [formData.height_cm, formData.weight_kg]);

  const handleInputChange = (field, value) => {
    setFormData(prev => ({ ...prev, [field]: value }));
  };

  const handleSymptomToggle = (symptom) => {
    setFormData(prev => {
      const exists = prev.symptoms.includes(symptom);
      const updated = exists 
        ? prev.symptoms.filter(s => s !== symptom)
        : [...prev.symptoms, symptom];
      return { ...prev, symptoms: updated };
    });
  };

  const handleFamilyToggle = (condition) => {
    setFormData(prev => {
      const exists = prev.family_history.includes(condition);
      const updated = exists 
        ? prev.family_history.filter(c => c !== condition)
        : [...prev.family_history, condition];
      return { ...prev, family_history: updated };
    });
  };

  const handlePresetSelect = (preset) => {
    setFormData(preset.data);
    setHasOtherSymptom(Boolean(preset.data.other_symptom));
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    const payload = {
      ...formData,
      age: Number(formData.age),
      height_cm: Number(formData.height_cm),
      weight_kg: Number(formData.weight_kg),
      sleep_hours: Number(formData.sleep_hours),
      other_symptom: hasOtherSymptom ? formData.other_symptom : ''
    };
    onSubmit(payload);
  };

  return (
    <div>
      {/* Quick-Fill Sample Profiles */}
      <div className="presets-container">
        <div className="presets-header">
          <div className="presets-title">
            <Sparkles size={16} color="var(--primary-600)" />
            <span>Quick-Fill Sample Profiles for Testing</span>
          </div>
          <span style={{ fontSize: '0.75rem', color: 'var(--text-muted)' }}>Click to autofill data</span>
        </div>
        <div className="presets-grid">
          {PRESET_PROFILES.map((preset, idx) => (
            <button
              key={idx}
              type="button"
              className="preset-chip"
              onClick={() => handlePresetSelect(preset)}
            >
              <span className="preset-name">{preset.name}</span>
              <span className="preset-desc">{preset.desc}</span>
            </button>
          ))}
        </div>
      </div>

      <form onSubmit={handleSubmit} className="form-card">
        {/* Section 1: Demographics & Biometrics */}
        <div className="form-section-title">
          <User size={18} color="var(--primary-600)" />
          <span>1. Demographics & Biometrics</span>
        </div>
        <div className="form-grid">
          <div className="form-group">
            <label className="form-label" htmlFor="input-age">
              <span>Age (Years)</span>
              <span style={{ color: 'var(--primary-600)' }}>{formData.age} yrs</span>
            </label>
            <input
              id="input-age"
              type="number"
              min="18"
              max="95"
              className="form-input"
              value={formData.age}
              onChange={(e) => handleInputChange('age', e.target.value)}
              required
            />
          </div>

          <div className="form-group">
            <label className="form-label">Gender</label>
            <div className="segmented-control">
              {['Male', 'Female', 'Other'].map((g) => (
                <button
                  key={g}
                  type="button"
                  className={`segmented-btn ${formData.gender === g ? 'active' : ''}`}
                  onClick={() => handleInputChange('gender', g)}
                >
                  {g}
                </button>
              ))}
            </div>
          </div>

          <div className="form-group">
            <label className="form-label" htmlFor="input-height">
              <span>Height (cm)</span>
              <span>{formData.height_cm} cm</span>
            </label>
            <input
              id="input-height"
              type="number"
              min="120"
              max="220"
              className="form-input"
              value={formData.height_cm}
              onChange={(e) => handleInputChange('height_cm', e.target.value)}
              required
            />
          </div>

          <div className="form-group">
            <label className="form-label" htmlFor="input-weight">
              <span>Weight (kg) & BMI</span>
              <span className={`bmi-pill ${bmiInfo.pillClass}`}>
                BMI {bmiInfo.bmi} • {bmiInfo.category}
              </span>
            </label>
            <input
              id="input-weight"
              type="number"
              min="30"
              max="200"
              step="0.5"
              className="form-input"
              value={formData.weight_kg}
              onChange={(e) => handleInputChange('weight_kg', e.target.value)}
              required
            />
          </div>
        </div>

        {/* Section 2: Lifestyle & Habits */}
        <div className="form-section-title">
          <HeartPulse size={18} color="var(--primary-600)" />
          <span>2. Lifestyle & Daily Habits</span>
        </div>
        <div className="form-grid">
          <div className="form-group">
            <label className="form-label">Smoking Habit</label>
            <select
              className="form-select"
              value={formData.smoking_habit}
              onChange={(e) => handleInputChange('smoking_habit', e.target.value)}
            >
              <option value="Non-smoker">Non-smoker</option>
              <option value="Former Smoker">Former Smoker</option>
              <option value="Occasional Smoker">Occasional Smoker</option>
              <option value="Regular Smoker">Regular Smoker</option>
            </select>
          </div>

          <div className="form-group">
            <label className="form-label">Alcohol Consumption</label>
            <select
              className="form-select"
              value={formData.alcohol_consumption}
              onChange={(e) => handleInputChange('alcohol_consumption', e.target.value)}
            >
              <option value="None">None</option>
              <option value="Occasional">Occasional</option>
              <option value="Moderate">Moderate</option>
              <option value="Frequent">Frequent</option>
            </select>
          </div>

          <div className="form-group">
            <label className="form-label">Physical Activity</label>
            <select
              className="form-select"
              value={formData.physical_activity}
              onChange={(e) => handleInputChange('physical_activity', e.target.value)}
            >
              <option value="Sedentary">Sedentary (Desk bound / Minimal movement)</option>
              <option value="Light">Light (1-2 days active/week)</option>
              <option value="Moderate">Moderate (3-5 days cardio/strength)</option>
              <option value="Active">Active (6-7 days vigorous exercise)</option>
            </select>
          </div>

          <div className="form-group">
            <label className="form-label" htmlFor="input-sleep">
              <span>Sleep Duration</span>
              <span style={{ color: 'var(--primary-600)' }}>{formData.sleep_hours} hrs/night</span>
            </label>
            <input
              id="input-sleep"
              type="number"
              min="3"
              max="14"
              step="0.5"
              className="form-input"
              value={formData.sleep_hours}
              onChange={(e) => handleInputChange('sleep_hours', e.target.value)}
              required
            />
          </div>
        </div>

        {/* Section 3: Family Medical History */}
        <div className="form-section-title">
          <Dna size={18} color="var(--primary-600)" />
          <span>3. Family Medical History (Select all that apply)</span>
        </div>
        <div className="checklist-grid" style={{ marginBottom: '1.75rem' }}>
          {FAMILY_CONDITIONS.map((cond) => {
            const isSelected = formData.family_history.includes(cond);
            return (
              <label
                key={cond}
                className={`checkbox-card ${isSelected ? 'selected' : ''}`}
              >
                <input
                  type="checkbox"
                  checked={isSelected}
                  onChange={() => handleFamilyToggle(cond)}
                />
                <span className="checkbox-label">{cond}</span>
              </label>
            );
          })}
        </div>

        {/* Section 4: Predefined Symptom Checklist */}
        <div className="form-section-title">
          <Stethoscope size={18} color="var(--primary-600)" />
          <span>4. Symptom Checklist (Section 4 Specification)</span>
        </div>
        <div className="checklist-grid">
          {PREDEFINED_SYMPTOMS.map((symptom) => {
            const isSelected = formData.symptoms.includes(symptom);
            return (
              <label
                key={symptom}
                className={`checkbox-card ${isSelected ? 'selected' : ''}`}
              >
                <input
                  type="checkbox"
                  checked={isSelected}
                  onChange={() => handleSymptomToggle(symptom)}
                />
                <span className="checkbox-label">{symptom}</span>
              </label>
            );
          })}

          {/* Optional Other field */}
          <label className={`checkbox-card ${hasOtherSymptom ? 'selected' : ''}`}>
            <input
              type="checkbox"
              checked={hasOtherSymptom}
              onChange={(e) => setHasOtherSymptom(e.target.checked)}
            />
            <span className="checkbox-label">Other Symptoms</span>
          </label>
        </div>

        {hasOtherSymptom && (
          <div style={{ marginTop: '0.75rem' }}>
            <input
              type="text"
              placeholder="Describe any other symptoms (e.g. joint ache, palpitations, tremors)..."
              className="form-input"
              value={formData.other_symptom}
              onChange={(e) => handleInputChange('other_symptom', e.target.value)}
            />
          </div>
        )}

        {/* Form Submission */}
        <div style={{ marginTop: '2rem', display: 'flex', justifyContent: 'flex-end', gap: '1rem' }}>
          <button
            type="submit"
            className="btn btn-primary btn-lg"
            disabled={isLoading}
          >
            {isLoading ? (
              <span>Running XGBoost & SHAP Analysis...</span>
            ) : (
              <>
                <span>Run Preventive Screening</span>
                <ChevronRight size={18} />
              </>
            )}
          </button>
        </div>
      </form>
    </div>
  );
}
