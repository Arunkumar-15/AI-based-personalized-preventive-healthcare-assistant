import React, { useState } from 'react';
import { useTranslation } from 'react-i18next';
import { User, ShieldCheck, ArrowRight, Heart, Lock, Mail } from 'lucide-react';

export default function LoginPage({ onLogin }) {
  const { t, i18n } = useTranslation();
  const isTamil = i18n.language === 'ta';

  const [activeTab, setActiveTab] = useState('user'); // 'user' | 'admin'
  
  // User Form State
  const [userEmail, setUserEmail] = useState('');
  
  // Admin Form State
  const [adminUsername, setAdminUsername] = useState('');
  const [adminPassword, setAdminPassword] = useState('');
  
  const [errorMsg, setErrorMsg] = useState('');

  const handleUserSubmit = (e) => {
    e.preventDefault();
    setErrorMsg('');
    const emailVal = userEmail.trim();

    if (!emailVal || !emailVal.includes('@')) {
      setErrorMsg(isTamil ? 'செல்லுபடியாகும் மின்னஞ்சல் முகவரியை உள்ளிடவும்' : 'Please enter a valid email address.');
      return;
    }

    onLogin({
      name: emailVal.split('@')[0],
      email: emailVal,
      role: 'Patient'
    });
  };

  const handleAdminSubmit = (e) => {
    e.preventDefault();
    setErrorMsg('');

    if (adminUsername.trim().toLowerCase() === 'admin' && adminPassword === 'admin123') {
      onLogin({
        name: 'Admin',
        email: 'admin@healthcare.ai',
        role: 'Admin'
      });
    } else {
      setErrorMsg(isTamil ? 'நிர்வாகி பயனர்பெயர் அல்லது கடவுச்சொல் தவறானது (Use admin / admin123)' : 'Invalid Admin Credentials. (Username: admin | Password: admin123)');
    }
  };

  return (
    <div style={{ maxWidth: '440px', margin: '2.5rem auto', padding: '0 1rem' }}>
      <div style={{ background: '#ffffff', border: '1px solid #cbd5e1', borderRadius: '24px', padding: '2.2rem 2rem', boxShadow: '0 12px 32px rgba(15,43,92,0.1)' }}>
        
        {/* Header */}
        <div style={{ textAlign: 'center', marginBottom: '1.6rem' }}>
          <div style={{ width: '56px', height: '56px', background: 'linear-gradient(135deg, #0f2b5c 0%, #0284c7 100%)', borderRadius: '16px', color: '#ffffff', display: 'flex', alignItems: 'center', justifyContent: 'center', margin: '0 auto 1rem auto', boxShadow: '0 8px 16px rgba(2,132,199,0.2)' }}>
            <Heart size={28} />
          </div>
          <h2 style={{ fontSize: '1.5rem', fontWeight: 800, color: '#0f2b5c', margin: '0 0 0.4rem 0' }}>
            {isTamil ? 'AI சுகாதார உதவியாளர் உள்நுழைவு' : 'AI Healthcare Portal Login'}
          </h2>
          <p style={{ fontSize: '0.85rem', color: '#64748b', margin: 0 }}>
            {isTamil ? 'பயனர்கள் மின்னஞ்சல் மூலமாகவும், நிர்வாகி பயனர்பெயர்/கடவுச்சொல் மூலமாகவும் உள்நுழையலாம்' : 'Users sign in via Email only. Admins log in with Username & Password.'}
          </p>
        </div>

        {/* Tab Switcher: User Sign In vs Admin Login */}
        <div style={{ display: 'flex', background: '#f1f5f9', padding: '0.3rem', borderRadius: '12px', marginBottom: '1.5rem' }}>
          <button
            type="button"
            onClick={() => { setActiveTab('user'); setErrorMsg(''); }}
            style={{ flex: 1, padding: '0.6rem', border: 'none', borderRadius: '9px', background: activeTab === 'user' ? '#ffffff' : 'transparent', color: activeTab === 'user' ? '#0284c7' : '#64748b', fontWeight: 700, fontSize: '0.85rem', cursor: 'pointer', display: 'flex', alignItems: 'center', justifyContent: 'center', gap: '0.4rem', boxShadow: activeTab === 'user' ? '0 2px 6px rgba(0,0,0,0.06)' : 'none' }}
          >
            <Mail size={16} />
            <span>{isTamil ? 'பயனர் உள்நுழைவு (Email)' : 'User Sign In'}</span>
          </button>
          <button
            type="button"
            onClick={() => { setActiveTab('admin'); setErrorMsg(''); }}
            style={{ flex: 1, padding: '0.6rem', border: 'none', borderRadius: '9px', background: activeTab === 'admin' ? '#ffffff' : 'transparent', color: activeTab === 'admin' ? '#047857' : '#64748b', fontWeight: 700, fontSize: '0.85rem', cursor: 'pointer', display: 'flex', alignItems: 'center', justifyContent: 'center', gap: '0.4rem', boxShadow: activeTab === 'admin' ? '0 2px 6px rgba(0,0,0,0.06)' : 'none' }}
          >
            <Lock size={16} />
            <span>{isTamil ? 'நிர்வாகி (Admin)' : 'Admin Login'}</span>
          </button>
        </div>

        {/* Error Alert */}
        {errorMsg && (
          <div style={{ background: '#fef2f2', border: '1px solid #fca5a5', color: '#b91c1c', padding: '0.65rem 0.85rem', borderRadius: '10px', fontSize: '0.82rem', marginBottom: '1.2rem', fontWeight: 600 }}>
            {errorMsg}
          </div>
        )}

        {/* FORM 1: User Sign In (Email Only) */}
        {activeTab === 'user' && (
          <form onSubmit={handleUserSubmit}>
            <div style={{ marginBottom: '1.5rem' }}>
              <label style={{ display: 'block', fontSize: '0.82rem', fontWeight: 600, color: '#1e293b', marginBottom: '0.4rem' }}>
                {isTamil ? 'மின்னஞ்சல் முகவரி (Email Address)' : 'Email Address'}
              </label>
              <input
                type="email"
                value={userEmail}
                onChange={(e) => setUserEmail(e.target.value)}
                placeholder="e.g. user@gmail.com"
                required
                style={{ width: '100%', padding: '0.75rem 0.85rem', border: '1px solid #cbd5e1', borderRadius: '10px', fontSize: '0.9rem', outline: 'none' }}
              />
              <span style={{ display: 'block', fontSize: '0.75rem', color: '#64748b', marginTop: '0.35rem' }}>
                {isTamil ? 'கடவுச்சொல் தேவையில்லை — மின்னஞ்சலை உள்ளிட்டு உள்நுழையவும்' : 'No password required — enter your email to start assessment'}
              </span>
            </div>

            <button
              type="submit"
              style={{ width: '100%', padding: '0.85rem', background: '#0284c7', color: '#ffffff', border: 'none', borderRadius: '10px', fontWeight: 700, fontSize: '0.95rem', cursor: 'pointer', display: 'flex', alignItems: 'center', justifyContent: 'center', gap: '0.5rem' }}
            >
              <span>{isTamil ? 'மதிப்பீட்டிற்கு உள்நுழைக' : 'Sign In'}</span>
              <ArrowRight size={18} />
            </button>
          </form>
        )}

        {/* FORM 2: Admin Login (Username & Password) */}
        {activeTab === 'admin' && (
          <form onSubmit={handleAdminSubmit}>
            <div style={{ marginBottom: '1rem' }}>
              <label style={{ display: 'block', fontSize: '0.82rem', fontWeight: 600, color: '#1e293b', marginBottom: '0.4rem' }}>
                {isTamil ? 'நிர்வாகி பயனர்பெயர் (Admin Username)' : 'Admin Username'}
              </label>
              <input
                type="text"
                value={adminUsername}
                onChange={(e) => setAdminUsername(e.target.value)}
                placeholder="e.g. admin"
                required
                style={{ width: '100%', padding: '0.75rem 0.85rem', border: '1px solid #cbd5e1', borderRadius: '10px', fontSize: '0.9rem', outline: 'none' }}
              />
            </div>

            <div style={{ marginBottom: '1.5rem' }}>
              <label style={{ display: 'block', fontSize: '0.82rem', fontWeight: 600, color: '#1e293b', marginBottom: '0.4rem' }}>
                {isTamil ? 'நிர்வாகி கடவுச்சொல் (Admin Password)' : 'Admin Password'}
              </label>
              <input
                type="password"
                value={adminPassword}
                onChange={(e) => setAdminPassword(e.target.value)}
                placeholder="••••••••"
                required
                style={{ width: '100%', padding: '0.75rem 0.85rem', border: '1px solid #cbd5e1', borderRadius: '10px', fontSize: '0.9rem', outline: 'none' }}
              />
              <span style={{ display: 'block', fontSize: '0.74rem', color: '#047857', marginTop: '0.35rem', fontWeight: 600 }}>
                🔑 Default Admin: <code>admin</code> / <code>admin123</code>
              </span>
            </div>

            <button
              type="submit"
              style={{ width: '100%', padding: '0.85rem', background: '#047857', color: '#ffffff', border: 'none', borderRadius: '10px', fontWeight: 700, fontSize: '0.95rem', cursor: 'pointer', display: 'flex', alignItems: 'center', justifyContent: 'center', gap: '0.5rem' }}
            >
              <span>{isTamil ? 'நிர்வாகி உள்நுழைவு' : 'Admin Login'}</span>
              <ArrowRight size={18} />
            </button>
          </form>
        )}

        <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'center', gap: '0.4rem', marginTop: '1.5rem', fontSize: '0.76rem', color: '#047857', fontWeight: 600 }}>
          <ShieldCheck size={16} />
          <span>{isTamil ? '100% பாதுகாப்பான & பெயர் மறைக்கப்பட்ட தரவு' : '100% Privacy & De-Identified Storage'}</span>
        </div>

      </div>
    </div>
  );
}
