import React from 'react';
import { 
  Stethoscope, 
  Utensils, 
  Dumbbell, 
  Moon, 
  ShieldCheck, 
  AlertCircle, 
  CheckCircle2, 
  ArrowRight 
} from 'lucide-react';

export default function PreventiveGuidance({ guidance, disclaimer }) {
  if (!guidance || guidance.length === 0) return null;

  const getCategoryIcon = (category) => {
    switch (category) {
      case 'clinical':
        return <Stethoscope size={18} color="#0284c7" />;
      case 'diet':
        return <Utensils size={18} color="#16a34a" />;
      case 'activity':
        return <Dumbbell size={18} color="#f97316" />;
      case 'lifestyle':
        return <Moon size={18} color="#7c3aed" />;
      default:
        return <ShieldCheck size={18} color="#0284c7" />;
    }
  };

  const getPriorityBadge = (priority) => {
    switch (priority) {
      case 'critical':
        return <span style={{ background: '#fee2e2', color: '#991b1b', fontSize: '0.6875rem', fontWeight: 700, padding: '0.2rem 0.5rem', borderRadius: '999px', textTransform: 'uppercase' }}>Urgent Action</span>;
      case 'high':
        return <span style={{ background: '#ffedd5', color: '#9a3412', fontSize: '0.6875rem', fontWeight: 700, padding: '0.2rem 0.5rem', borderRadius: '999px', textTransform: 'uppercase' }}>Priority Recommendation</span>;
      case 'medium':
        return <span style={{ background: '#fef3c7', color: '#92400e', fontSize: '0.6875rem', fontWeight: 700, padding: '0.2rem 0.5rem', borderRadius: '999px', textTransform: 'uppercase' }}>Recommended</span>;
      default:
        return <span style={{ background: '#e0f2fe', color: '#0369a1', fontSize: '0.6875rem', fontWeight: 700, padding: '0.2rem 0.5rem', borderRadius: '999px', textTransform: 'uppercase' }}>Wellness Tip</span>;
    }
  };

  return (
    <div className="guidance-section">
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', flexWrap: 'wrap', gap: '0.5rem' }}>
        <div>
          <span style={{ fontSize: '0.75rem', fontWeight: 700, color: 'var(--text-muted)', textTransform: 'uppercase', letterSpacing: '0.05em' }}>
            Section 7 • Evidence-Based Action Plan
          </span>
          <h3 style={{ fontSize: '1.25rem', fontWeight: 800, color: 'var(--text-primary)' }}>
            Personalized Preventive Guidance
          </h3>
        </div>
        <span style={{ fontSize: '0.8125rem', color: 'var(--text-muted)' }}>
          {guidance.length} Tailored Preventive Actions
        </span>
      </div>

      <p style={{ fontSize: '0.8125rem', color: 'var(--text-secondary)', marginTop: '0.375rem' }}>
        Synthesized dynamically from your XGBoost risk level and key individual SHAP contributing factors.
      </p>

      {/* Guidance Cards Grid */}
      <div className="guidance-grid">
        {guidance.map((item) => (
          <div key={item.id} className={`guidance-card ${item.priority}`}>
            <div className="guidance-header">
              <div className="guidance-title">
                {getCategoryIcon(item.category)}
                <span>{item.title}</span>
              </div>
              {getPriorityBadge(item.priority)}
            </div>

            <p style={{ fontSize: '0.8125rem', color: 'var(--text-secondary)', lineHeight: 1.4 }}>
              {item.description}
            </p>

            {item.target_factor && (
              <div style={{ fontSize: '0.75rem', color: 'var(--text-muted)', fontWeight: 600 }}>
                Targeting: <span style={{ color: 'var(--primary-700)' }}>{item.target_factor}</span>
              </div>
            )}

            {/* Action steps */}
            <ul className="guidance-steps">
              {item.action_steps.map((step, sIdx) => (
                <li key={sIdx} className="guidance-step-item">
                  <CheckCircle2 size={15} color="var(--primary-600)" style={{ flexShrink: 0, marginTop: 2 }} />
                  <span>{step}</span>
                </li>
              ))}
            </ul>
          </div>
        ))}
      </div>
    </div>
  );
}
