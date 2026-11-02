import React from 'react';
import { ShieldAlert, ShieldCheck, AlertTriangle, Flame, Activity } from 'lucide-react';

export default function RiskOverviewCard({ result }) {
  if (!result) return null;

  const { risk_level, risk_score, risk_category, probabilities, bmi, bmi_category } = result;

  const getRiskDetails = (level) => {
    switch (level) {
      case 'Low':
        return {
          icon: <ShieldCheck size={26} color="var(--risk-low-solid)" />,
          badgeClass: 'low',
          barColor: 'var(--risk-low-solid)',
          sub: 'Risk indicators are balanced within safe clinical benchmarks.'
        };
      case 'Moderate':
        return {
          icon: <AlertTriangle size={26} color="var(--risk-mod-solid)" />,
          badgeClass: 'moderate',
          barColor: 'var(--risk-mod-solid)',
          sub: 'Moderate physiological strain detected. Targeted lifestyle adjustments recommended.'
        };
      case 'High':
        return {
          icon: <Flame size={26} color="var(--risk-high-solid)" />,
          badgeClass: 'high',
          barColor: 'var(--risk-high-solid)',
          sub: 'Elevated multi-factor risk detected. Diagnostic screening advised.'
        };
      case 'Critical':
        return {
          icon: <ShieldAlert size={26} color="var(--risk-crit-solid)" />,
          badgeClass: 'critical',
          barColor: 'var(--risk-crit-solid)',
          sub: 'High-acuity risk markers present. Medical consultation strongly recommended.'
        };
      default:
        return {
          icon: <Activity size={26} />,
          badgeClass: 'low',
          barColor: 'var(--primary-600)',
          sub: ''
        };
    }
  };

  const details = getRiskDetails(risk_level);

  return (
    <div className="risk-card">
      <div>
        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start' }}>
          <div>
            <span style={{ fontSize: '0.75rem', fontWeight: 700, color: 'var(--text-muted)', textTransform: 'uppercase', letterSpacing: '0.05em' }}>
              Overall Health Screening
            </span>
            <h3 style={{ fontSize: '1.25rem', fontWeight: 800, color: 'var(--text-primary)', marginTop: '0.25rem' }}>
              {risk_category}
            </h3>
          </div>

          <div className={`risk-level-badge ${details.badgeClass}`}>
            {details.icon}
            <span>{risk_level} Risk</span>
          </div>
        </div>

        {/* Score Display */}
        <div className="score-display">
          <span className="score-number" style={{ color: details.barColor }}>
            {risk_score}
          </span>
          <span className="score-scale">/ 100</span>
        </div>

        <p style={{ fontSize: '0.8125rem', color: 'var(--text-secondary)', marginBottom: '0.5rem' }}>
          {details.sub}
        </p>

        {/* Progress Bar */}
        <div className="progress-track">
          <div
            className="progress-fill"
            style={{
              width: `${Math.min(100, Math.max(5, risk_score))}%`,
              backgroundColor: details.barColor
            }}
          />
        </div>

        {/* Probability Breakdown */}
        <div style={{ marginTop: '1.25rem' }}>
          <span style={{ fontSize: '0.75rem', fontWeight: 700, color: 'var(--text-secondary)', textTransform: 'uppercase', letterSpacing: '0.04em' }}>
            Model Class Probabilities
          </span>
          <div style={{ display: 'grid', gridTemplateColumns: 'repeat(4, 1fr)', gap: '0.5rem', marginTop: '0.5rem' }}>
            {probabilities && Object.entries(probabilities).map(([cls, prob]) => (
              <div key={cls} style={{ background: 'var(--bg-muted)', padding: '0.5rem', borderRadius: 'var(--radius-sm)', textAlign: 'center' }}>
                <div style={{ fontSize: '0.6875rem', fontWeight: 600, color: 'var(--text-muted)' }}>{cls}</div>
                <div style={{ fontSize: '0.875rem', fontWeight: 800, color: 'var(--text-primary)', fontFamily: 'var(--font-mono)' }}>
                  {(prob * 100).toFixed(1)}%
                </div>
              </div>
            ))}
          </div>
        </div>
      </div>

      {/* Biometric quick pill footer */}
      <div style={{ marginTop: '1.5rem', paddingTop: '1rem', borderTop: '1px solid var(--border-subtle)', display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
        <span style={{ fontSize: '0.8125rem', color: 'var(--text-muted)' }}>Screening Biometrics:</span>
        <span className={`bmi-pill ${bmi >= 30 ? 'obese' : bmi >= 25 ? 'overweight' : bmi < 18.5 ? 'underweight' : 'normal'}`}>
          BMI: {bmi} ({bmi_category})
        </span>
      </div>
    </div>
  );
}
