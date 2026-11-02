import React from 'react';
import { AlertCircle } from 'lucide-react';

export default function MedicalDisclaimer({ text }) {
  const defaultText =
    "Clinical Notice: PreventiveCare AI is an automated statistical screening tool designed for preventive wellness " +
    "and risk pattern identification. It does NOT provide clinical diagnosis, medical treatment, or individualized medical advice. " +
    "Always consult a board-certified healthcare provider for the diagnosis and management of medical conditions.";

  return (
    <div className="disclaimer-banner">
      <AlertCircle size={20} color="var(--primary-600)" style={{ flexShrink: 0, marginTop: 2 }} />
      <div>
        <strong style={{ color: 'var(--text-primary)', display: 'block', marginBottom: '0.125rem' }}>
          Preventive Health Screening Notice
        </strong>
        <span>{text || defaultText}</span>
      </div>
    </div>
  );
}
