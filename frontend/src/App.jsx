import React, { useState } from 'react';
import { useTranslation } from 'react-i18next';
import Navbar from './components/Navbar';
import LoginPage from './components/LoginPage';
import HomePage from './components/HomePage';
import InputPage from './components/InputPage';
import AdvancedAssessmentPage from './components/AdvancedAssessmentPage';
import ReportUploadPage from './components/ReportUploadPage';
import OutputPage from './components/OutputPage';
import AdminDashboard from './components/AdminDashboard';
import { submitAssessment } from './services/api';
import { X, Info, Mail, ShieldAlert } from 'lucide-react';

export default function App() {
  const { t, i18n } = useTranslation();
  const [currentUser, setCurrentUser] = useState(null); // null if logged out
  const [currentView, setCurrentView] = useState('login'); // 'login', 'home', 'basic_input', 'advanced_input', 'ocr_upload', 'output', 'admin_db'
  const [assessmentResult, setAssessmentResult] = useState(null);
  const [isLoading, setIsLoading] = useState(false);
  const [errorMsg, setErrorMsg] = useState(null);
  const [language, setLanguage] = useState(i18n.language || 'en');
  const [activeModal, setActiveModal] = useState(null); // 'about', 'contact', null

  const handleLogin = (user) => {
    setCurrentUser(user);
    if (user.role === 'Admin') {
      setCurrentView('admin_db');
    } else {
      setCurrentView('home');
    }
    window.scrollTo({ top: 0, behavior: 'smooth' });
  };

  const handleLogout = () => {
    setCurrentUser(null);
    setCurrentView('login');
    setAssessmentResult(null);
    setErrorMsg(null);
    window.scrollTo({ top: 0, behavior: 'smooth' });
  };

  const handleAssessmentSubmit = async (formData) => {
    setIsLoading(true);
    setErrorMsg(null);
    try {
      const payload = {
        ...formData,
        language: language
      };
      const res = await submitAssessment(payload);
      setAssessmentResult(res);
      setCurrentView('output');
      window.scrollTo({ top: 0, behavior: 'smooth' });
    } catch (err) {
      console.error(err);
      setErrorMsg(
        err.message || 'Unable to communicate with the FastAPI backend. Ensure the backend is active.'
      );
    } finally {
      setIsLoading(false);
    }
  };

  const handleGoHome = () => {
    if (currentUser) {
      setCurrentView('home');
    } else {
      setCurrentView('login');
    }
    setAssessmentResult(null);
    setErrorMsg(null);
    window.scrollTo({ top: 0, behavior: 'smooth' });
  };

  return (
    <div className="app-wrapper">
      {/* Top Navbar */}
      <Navbar
        onGoHome={handleGoHome}
        onOpenAbout={() => setActiveModal('about')}
        onOpenContact={() => setActiveModal('contact')}
        onOpenAdmin={() => setCurrentView('admin_db')}
        onLogout={handleLogout}
        currentUser={currentUser}
        language={language}
        setLanguage={setLanguage}
      />

      {/* Main Container */}
      <main className="main-container">
        {/* Error notification if connection failed */}
        {errorMsg && (
          <div style={{ position: 'fixed', top: '5rem', left: '50%', transform: 'translateX(-50%)', zIndex: 100, background: '#fef2f2', border: '1px solid #f87171', color: '#991b1b', padding: '0.875rem 1.5rem', borderRadius: '10px', boxShadow: '0 10px 25px rgba(0,0,0,0.1)', display: 'flex', alignItems: 'center', gap: '0.75rem', maxWidth: '90%', fontSize: '0.875rem' }}>
            <ShieldAlert size={20} color="#dc2626" />
            <span>{errorMsg}</span>
            <button
              onClick={() => setErrorMsg(null)}
              style={{ background: 'none', border: 'none', color: '#991b1b', cursor: 'pointer', fontWeight: 'bold', marginLeft: '0.5rem' }}
            >
              ✕
            </button>
          </div>
        )}

        {/* View Switcher */}
        {currentView === 'login' && (
          <LoginPage onLogin={handleLogin} />
        )}

        {currentView === 'home' && (
          <HomePage onSelectMode={(mode) => setCurrentView(mode)} />
        )}

        {currentView === 'basic_input' && (
          <InputPage onSubmit={handleAssessmentSubmit} isLoading={isLoading} />
        )}

        {currentView === 'advanced_input' && (
          <AdvancedAssessmentPage onSubmit={handleAssessmentSubmit} onBack={handleGoHome} />
        )}

        {currentView === 'ocr_upload' && (
          <ReportUploadPage onSubmit={handleAssessmentSubmit} onBack={handleGoHome} />
        )}

        {currentView === 'output' && (
          <OutputPage result={assessmentResult} onNewAssessment={handleGoHome} />
        )}

        {currentView === 'admin_db' && (
          <AdminDashboard onBack={handleGoHome} />
        )}
      </main>

      {/* About Modal */}
      {activeModal === 'about' && (
        <div className="simple-modal-backdrop" onClick={() => setActiveModal(null)}>
          <div className="simple-modal-card" onClick={(e) => e.stopPropagation()}>
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '1rem' }}>
              <div style={{ display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
                <Info size={22} color="var(--blue-primary)" />
                <h3 style={{ fontSize: '1.2rem', fontWeight: 700, color: '#0f2b5c' }}>
                  {language === 'ta' ? 'AI சுகாதார உதவியாளர் பற்றி' : 'About AI Healthcare Assistant'}
                </h3>
              </div>
              <button
                type="button"
                className="simple-modal-close"
                onClick={() => setActiveModal(null)}
              >
                <X size={18} />
              </button>
            </div>
            <p style={{ fontSize: '0.875rem', color: '#475569', lineHeight: 1.6, marginBottom: '1rem' }}>
              {language === 'ta'
                ? 'இந்த AI சுகாதார உதவியாளர் 3 வெவ்வேறு மதிப்பீட்டு முறைகள் மூலம் சுகாதார அபாயங்களை கணிக்க உதவுகிறது. ஒவ்வொரு முறைக்கும் தேவையான உள்ளீடுகள் கீழே கொடுக்கப்பட்டுள்ளன:'
                : 'This AI-Powered Healthcare Assistant provides personalized risk screening across 3 assessment modes. Below are the required inputs for each mode:'}
            </p>

            <div style={{ display: 'flex', flexDirection: 'column', gap: '0.75rem', fontSize: '0.825rem' }}>
              <div style={{ background: '#f8fafc', border: '1px solid #e2e8f0', borderRadius: '10px', padding: '0.75rem 0.9rem' }}>
                <strong style={{ color: '#0284c7' }}>
                  {language === 'ta' ? '📝 1. அடிப்படை சுகாதார மதிப்பீடு (தேவையான உள்ளீடுகள்):' : '📝 1. Basic Health Assessment (Required Inputs):'}
                </strong>
                <span style={{ color: '#334155', display: 'block', marginTop: '0.25rem', lineHeight: 1.5 }}>
                  {language === 'ta'
                    ? 'வயது, பாலினம், உயரம், எடை (BMI), பழக்கவழக்கங்கள் (புகை/மது/உடற்பயிற்சி/தூக்கம்), குடும்ப மருத்துவ வரலாறு மற்றும் அறிகுறிகள் (சோர்வு, மார்பு வலி, மூச்சுத் திணறல்).'
                    : 'Demographics (Age, Gender, Height, Weight), Lifestyle Habits (Smoking, Alcohol, Physical Activity, Sleep), Family History, and Symptoms (Fatigue, Chest Pain, Shortness of Breath, etc.).'}
                </span>
              </div>

              <div style={{ background: '#f8fafc', border: '1px solid #e2e8f0', borderRadius: '10px', padding: '0.75rem 0.9rem' }}>
                <strong style={{ color: '#047857' }}>
                  {language === 'ta' ? '🧪 2. தீவிர மருத்துவ மதிப்பீடு (தேவையான உள்ளீடுகள்):' : '🧪 2. Advanced Clinical Assessment (Required Inputs):'}
                </strong>
                <span style={{ color: '#334155', display: 'block', marginTop: '0.25rem', lineHeight: 1.5 }}>
                  {language === 'ta'
                    ? 'மருத்துவ ஆய்வு அளவுகள்: இரத்த அழுத்தம் (BP mmHg), இரத்த சர்க்கரை (Glucose mg/dL), HbA1c (%), கொழுப்பு (Cholesterol mg/dL), இதயத் துடிப்பு (BPM) மற்றும் அடிப்படை விவரங்கள்.'
                    : 'Clinical Lab Biomarkers: Blood Pressure (Systolic/Diastolic mmHg), Fasting Glucose (mg/dL), HbA1c (%), Total Cholesterol (mg/dL), Resting Heart Rate (BPM), and Demographics.'}
                </span>
              </div>

              <div style={{ background: '#f8fafc', border: '1px solid #e2e8f0', borderRadius: '10px', padding: '0.75rem 0.9rem' }}>
                <strong style={{ color: '#d97706' }}>
                  {language === 'ta' ? '📄 3. மருத்துவ அறிக்கை பதிவேற்றம் (தேவையான கோப்புகள்):' : '📄 3. Medical Report Upload & OCR (Required Files):'}
                </strong>
                <span style={{ color: '#334155', display: 'block', marginTop: '0.25rem', lineHeight: 1.5 }}>
                  {language === 'ta'
                    ? 'இரத்த பரிசோதனை அறிக்கை கோப்பு (PDF அல்லது photo .jpg, .png). OCR கணினி தானாகவே ஆய்வக எண்களை பிரித்தெடுத்து பகுப்பாய்வு செய்யும்.'
                    : 'Blood Test Lab Report File: Digital PDF document or Photo (.jpg, .png). The OCR engine automatically extracts numerical biomarkers for assessment.'}
                </span>
              </div>
            </div>
          </div>
        </div>
      )}

      {/* Contact Modal */}
      {activeModal === 'contact' && (
        <div className="simple-modal-backdrop" onClick={() => setActiveModal(null)}>
          <div className="simple-modal-card" onClick={(e) => e.stopPropagation()}>
            <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '1rem' }}>
              <div style={{ display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
                <Mail size={22} color="var(--blue-primary)" />
                <h3 style={{ fontSize: '1.2rem', fontWeight: 700, color: '#0f2b5c' }}>
                  {language === 'ta' ? 'தொடர்பு கொள்ள' : 'Contact Support & Inquiry'}
                </h3>
              </div>
              <button
                type="button"
                className="simple-modal-close"
                onClick={() => setActiveModal(null)}
              >
                <X size={18} />
              </button>
            </div>
            <p style={{ fontSize: '0.875rem', color: '#475569', lineHeight: 1.6 }}>
              {language === 'ta'
                ? 'மேலும் தகவல்களுக்கு அல்லது திட்ட விளக்கத்திற்கு எங்களை தொடர்பு கொள்ளவும்.'
                : 'For technical inquiries, research collaboration, or project evaluation details, contact our AI Healthcare Engineering Team.'}
            </p>
          </div>
        </div>
      )}
    </div>
  );
}
