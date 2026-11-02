import React, { useState } from 'react';
import { useTranslation } from 'react-i18next';
import { FileText, UploadCloud, ArrowLeft, CheckCircle, Cpu } from 'lucide-react';

export default function ReportUploadPage({ onSubmit, onBack }) {
  const { t, i18n } = useTranslation();
  const isTamil = i18n.language === 'ta';

  const [selectedFile, setSelectedFile] = useState(null);
  const [isScanning, setIsScanning] = useState(false);
  const [ocrData, setOcrData] = useState(null);

  const handleFileChange = (e) => {
    if (e.target.files && e.target.files[0]) {
      setSelectedFile(e.target.files[0]);
    }
  };

  const handleRunOCR = () => {
    if (!selectedFile) return;
    setIsScanning(true);

    // Simulate OCR Extraction Animation (1.5 seconds)
    setTimeout(() => {
      setIsScanning(false);
      setOcrData({
        fileName: selectedFile.name,
        extractedDate: new Date().toLocaleDateString(),
        biomarkers: {
          systolic_bp: 138,
          diastolic_bp: 90,
          fasting_glucose: 132,
          hba1c: 7.1,
          total_cholesterol: 224,
          resting_heart_rate: 82
        }
      });
    }, 1500);
  };

  const handleFinalSubmit = () => {
    const payload = {
      age: 52,
      gender: 'Male',
      height_cm: 175,
      weight_kg: 92,
      smoking_habit: 'Regular Smoker',
      alcohol_consumption: 'Moderate',
      physical_activity: 'Sedentary',
      sleep_hours: 6.0,
      family_history: ['Heart Disease', 'Diabetes'],
      symptoms: ['Chest Pain', 'Fatigue']
    };
    onSubmit(payload);
  };

  return (
    <div className="assessment-card" style={{ maxWidth: '850px', margin: '0 auto' }}>
      <div className="card-header-banner" style={{ background: 'linear-gradient(135deg, #b45309 0%, #d97706 100%)' }}>
        <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', marginBottom: '0.8rem' }}>
          <button
            type="button"
            onClick={onBack}
            style={{ background: 'rgba(255,255,255,0.2)', border: 'none', color: '#ffffff', padding: '0.4rem 0.8rem', borderRadius: '8px', cursor: 'pointer', display: 'inline-flex', alignItems: 'center', gap: '0.4rem', fontSize: '0.85rem', fontWeight: 600 }}
          >
            <ArrowLeft size={16} />
            <span>{isTamil ? 'முகப்புக்கு திரும்ப' : 'Back to Home'}</span>
          </button>
          <div style={{ padding: '0.3rem 0.75rem', background: '#fffbeb', border: '1px solid #fde68a', borderRadius: '9999px', fontSize: '0.78rem', color: '#b45309', fontWeight: 600 }}>
            {isTamil ? '📄 முறை 3: OCR ஸ்கேனர்' : '📄 Mode 3: OCR Scanner'}
          </div>
        </div>

        <h2 className="card-header-title">{isTamil ? '3. மருத்துவ அறிக்கை பதிவேற்றம் & OCR ஸ்கேனர்' : '3. Medical Report Upload & OCR Scanner'}</h2>
        <p className="card-header-subtitle">
          {isTamil ? 'உங்கள் இரத்த பரிசோதனை அறிக்கையை (PDF/புகைப்படம்) பதிவேற்றி தானாகவே பகுப்பாய்வு செய்யுங்கள்' : 'Upload your lab report photo or PDF. Our OCR engine automatically extracts numerical biomarkers.'}
        </p>
      </div>

      <div className="card-body">
        {/* Upload Drop Zone */}
        <div style={{ border: '2px dashed #d97706', borderRadius: '16px', padding: '2.5rem 1.5rem', textAlign: 'center', background: '#fffbeb', marginBottom: '1.5rem' }}>
          <UploadCloud size={48} color="#d97706" style={{ marginBottom: '0.8rem' }} />
          <h3 style={{ margin: '0 0 0.4rem 0', color: '#78350f', fontSize: '1.15rem' }}>
            {isTamil ? 'மருத்துவ அறிக்கையை இங்கே பதிவேற்றவும்' : 'Upload Blood Test Report (PDF or Photo)'}
          </h3>
          <p style={{ margin: '0 0 1.2rem 0', fontSize: '0.85rem', color: '#92400e' }}>
            {isTamil ? 'ஆதரிக்கப்படும் வடிவங்கள்: PDF, PNG, JPG (அதிகபட்சம் 10MB)' : 'Supported Formats: .pdf, .png, .jpg (Max 10MB)'}
          </p>

          <input
            type="file"
            accept=".pdf,.png,.jpg,.jpeg"
            onChange={handleFileChange}
            style={{ display: 'none' }}
            id="lab-report-input"
          />
          <label
            htmlFor="lab-report-input"
            style={{ display: 'inline-flex', alignItems: 'center', gap: '0.5rem', padding: '0.7rem 1.5rem', background: '#d97706', color: '#ffffff', borderRadius: '10px', fontWeight: 700, cursor: 'pointer', fontSize: '0.9rem' }}
          >
            <FileText size={18} />
            <span>{selectedFile ? selectedFile.name : (isTamil ? 'கோப்பைத் தேர்ந்தெடுக்கவும்' : 'Choose File')}</span>
          </label>
        </div>

        {/* Scan Action */}
        {selectedFile && !ocrData && (
          <div style={{ textAlign: 'center', marginBottom: '1.5rem' }}>
            <button
              type="button"
              onClick={handleRunOCR}
              disabled={isScanning}
              style={{ padding: '0.85rem 2rem', background: '#b45309', color: '#ffffff', border: 'none', borderRadius: '10px', fontWeight: 700, cursor: 'pointer', display: 'inline-flex', alignItems: 'center', gap: '0.6rem' }}
            >
              <Cpu size={20} />
              <span>{isScanning ? (isTamil ? 'OCR ஸ்கேன் செய்யப்படுகிறது...' : 'Scanning Report with OCR...') : (isTamil ? 'அறிக்கையை OCR ஸ்கேன் செய்க' : 'Run OCR Scan')}</span>
            </button>
          </div>
        )}

        {/* Extracted Biomarkers Preview */}
        {ocrData && (
          <div style={{ background: '#f0fdf4', border: '1px solid #a7f3d0', borderRadius: '14px', padding: '1.25rem 1.5rem', marginBottom: '1.5rem' }}>
            <div style={{ display: 'flex', alignItems: 'center', gap: '0.5rem', marginBottom: '1rem', color: '#047857', fontWeight: 700 }}>
              <CheckCircle size={22} />
              <h4 style={{ margin: 0, fontSize: '1.05rem' }}>
                {isTamil ? 'OCR வெற்றிகரமாக பிரித்தெடுக்கப்பட்ட ஆய்வு அளவுகள்' : 'OCR Successfully Extracted Biomarkers'}
              </h4>
            </div>

            <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(200px, 1fr))', gap: '0.8rem', marginBottom: '1.2rem' }}>
              <div style={{ background: '#ffffff', padding: '0.6rem 0.8rem', borderRadius: '8px', border: '1px solid #cbd5e1' }}>
                <span style={{ fontSize: '0.78rem', color: '#64748b' }}>Blood Pressure</span>
                <div style={{ fontSize: '1rem', fontWeight: 700, color: '#0f2b5c' }}>{ocrData.biomarkers.systolic_bp}/{ocrData.biomarkers.diastolic_bp} mmHg</div>
              </div>
              <div style={{ background: '#ffffff', padding: '0.6rem 0.8rem', borderRadius: '8px', border: '1px solid #cbd5e1' }}>
                <span style={{ fontSize: '0.78rem', color: '#64748b' }}>Fasting Glucose</span>
                <div style={{ fontSize: '1rem', fontWeight: 700, color: '#0f2b5c' }}>{ocrData.biomarkers.fasting_glucose} mg/dL</div>
              </div>
              <div style={{ background: '#ffffff', padding: '0.6rem 0.8rem', borderRadius: '8px', border: '1px solid #cbd5e1' }}>
                <span style={{ fontSize: '0.78rem', color: '#64748b' }}>HbA1c</span>
                <div style={{ fontSize: '1rem', fontWeight: 700, color: '#0f2b5c' }}>{ocrData.biomarkers.hba1c}%</div>
              </div>
              <div style={{ background: '#ffffff', padding: '0.6rem 0.8rem', borderRadius: '8px', border: '1px solid #cbd5e1' }}>
                <span style={{ fontSize: '0.78rem', color: '#64748b' }}>Total Cholesterol</span>
                <div style={{ fontSize: '1rem', fontWeight: 700, color: '#0f2b5c' }}>{ocrData.biomarkers.total_cholesterol} mg/dL</div>
              </div>
            </div>

            <button
              type="button"
              onClick={handleFinalSubmit}
              style={{ width: '100%', padding: '0.85rem', background: '#047857', color: '#ffffff', border: 'none', borderRadius: '10px', fontWeight: 700, fontSize: '0.95rem', cursor: 'pointer' }}
            >
              {isTamil ? 'பிரித்தெடுக்கப்பட்ட அறிக்கையை பகுப்பாய்வு செய்க (Run AI Inference)' : 'Run AI Inference on Extracted Report'}
            </button>
          </div>
        )}
      </div>
    </div>
  );
}
