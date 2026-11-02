import React from 'react';
import { useTranslation } from 'react-i18next';
import { ChevronDown, User, LogOut, ShieldCheck } from 'lucide-react';

export default function Navbar({ onGoHome, onOpenAbout, onOpenContact, onOpenAdmin, onLogout, currentUser, language, setLanguage }) {
  const { t, i18n } = useTranslation();

  const handleLanguageChange = (e) => {
    const newLang = e.target.value;
    setLanguage(newLang);
    i18n.changeLanguage(newLang);
  };

  return (
    <header className="top-navbar">
      <div className="navbar-brand" onClick={onGoHome}>
        <div className="brand-heart-icon">
          <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2.5" strokeLinecap="round" strokeLinejoin="round">
            <path d="M19 14c1.49-1.46 3-3.21 3-5.5A5.5 5.5 0 0 0 16.5 3c-1.76 0-3 .5-4.5 2-1.5-1.5-2.74-2-4.5-2A5.5 5.5 0 0 0 2 8.5c0 2.3 1.5 4.05 3 5.5l7 7Z" />
            <path d="M3.22 12H9.5l1.5-3 2 6 1.5-3h6.28" />
          </svg>
        </div>
        <span className="brand-title">{t('nav.brand')}</span>
      </div>

      <div className="navbar-right">
        {currentUser && (
          <button type="button" className="nav-link" onClick={onGoHome}>
            {t('nav.home')}
          </button>
        )}

        <button type="button" className="nav-link" onClick={onOpenAbout}>
          {t('nav.about')}
        </button>

        <button type="button" className="nav-link" onClick={onOpenContact}>
          {t('nav.contact')}
        </button>

        {/* Admin Portal Button */}
        {currentUser && (currentUser.role === 'Admin' || currentUser.role === 'Doctor' || currentUser.name.includes('Admin')) && (
          <button
            type="button"
            className="nav-link"
            onClick={onOpenAdmin}
            style={{ color: '#047857', fontWeight: 700, display: 'flex', alignItems: 'center', gap: '0.3rem' }}
          >
            <ShieldCheck size={16} />
            <span>Admin DB</span>
          </button>
        )}

        {/* User Profile Badge & Logout */}
        {currentUser ? (
          <div style={{ display: 'flex', alignItems: 'center', gap: '0.6rem', paddingLeft: '0.5rem', borderLeft: '1px solid #cbd5e1' }}>
            <div style={{ fontSize: '0.8rem', color: '#0f2b5c', fontWeight: 700, display: 'flex', alignItems: 'center', gap: '0.3rem', background: '#f1f5f9', padding: '0.3rem 0.65rem', borderRadius: '9999px' }}>
              <User size={14} color="#0284c7" />
              <span>{currentUser.name}</span>
            </div>

            <button
              type="button"
              onClick={onLogout}
              title="Sign Out"
              style={{ background: '#fef2f2', border: '1px solid #fca5a5', color: '#b91c1c', padding: '0.3rem 0.6rem', borderRadius: '8px', cursor: 'pointer', display: 'flex', alignItems: 'center', gap: '0.3rem', fontSize: '0.78rem', fontWeight: 700 }}
            >
              <LogOut size={14} />
              <span>Logout</span>
            </button>
          </div>
        ) : null}

        <div className="lang-select-wrapper">
          <select
            className="lang-select"
            value={language}
            onChange={handleLanguageChange}
          >
            <option value="en">English</option>
            <option value="ta">தமிழ் (Tamil)</option>
          </select>
          <ChevronDown size={14} className="lang-select-arrow" />
        </div>
      </div>
    </header>
  );
}
