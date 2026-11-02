import React, { useState } from 'react';
import { HelpCircle, TrendingUp, TrendingDown, Layers } from 'lucide-react';

export default function ShapWaterfallChart({ result }) {
  const [activeTab, setActiveTab] = useState('drivers'); // 'drivers', 'protective', 'all'

  if (!result) return null;

  const { top_risk_factors, top_protective_factors, all_shap_factors } = result;

  let displayFactors = [];
  if (activeTab === 'drivers') {
    displayFactors = top_risk_factors || [];
  } else if (activeTab === 'protective') {
    displayFactors = top_protective_factors || [];
  } else {
    displayFactors = (all_shap_factors || []).slice(0, 10);
  }

  // Calculate max absolute SHAP for responsive bar scaling
  const maxShap = Math.max(
    ...((all_shap_factors || []).map(f => Math.abs(f.shap_value))),
    1.0
  );

  return (
    <div className="shap-card">
      <div className="shap-header">
        <div>
          <span style={{ fontSize: '0.75rem', fontWeight: 700, color: 'var(--text-muted)', textTransform: 'uppercase', letterSpacing: '0.05em' }}>
            Explainable AI (SHAP TreeExplainer)
          </span>
          <h3 style={{ fontSize: '1.125rem', fontWeight: 800, color: 'var(--text-primary)' }}>
            Feature Contribution Analysis
          </h3>
        </div>

        <div className="shap-tabs">
          <button
            type="button"
            className={`shap-tab-btn ${activeTab === 'drivers' ? 'active' : ''}`}
            onClick={() => setActiveTab('drivers')}
          >
            <TrendingUp size={13} style={{ display: 'inline', marginRight: 4 }} />
            Risk Drivers ({top_risk_factors?.length || 0})
          </button>

          <button
            type="button"
            className={`shap-tab-btn ${activeTab === 'protective' ? 'active' : ''}`}
            onClick={() => setActiveTab('protective')}
          >
            <TrendingDown size={13} style={{ display: 'inline', marginRight: 4 }} />
            Protective ({top_protective_factors?.length || 0})
          </button>

          <button
            type="button"
            className={`shap-tab-btn ${activeTab === 'all' ? 'active' : ''}`}
            onClick={() => setActiveTab('all')}
          >
            <Layers size={13} style={{ display: 'inline', marginRight: 4 }} />
            Top 10 Overall
          </button>
        </div>
      </div>

      <p style={{ fontSize: '0.8125rem', color: 'var(--text-muted)', marginBottom: '1rem' }}>
        SHAP values illustrate how each biometric factor influenced the XGBoost decision boundary relative to baseline.
      </p>

      {/* Factor Rows */}
      <div style={{ display: 'flex', flexDirection: 'column', gap: '0.25rem' }}>
        {displayFactors.length === 0 ? (
          <div style={{ padding: '2rem', textAlign: 'center', color: 'var(--text-muted)', fontSize: '0.875rem' }}>
            No significant factors in this category.
          </div>
        ) : (
          displayFactors.map((factor, idx) => {
            const isRiskUp = factor.shap_value > 0;
            const barWidthPercent = Math.min(100, Math.max(8, (Math.abs(factor.shap_value) / maxShap) * 100));

            return (
              <div key={idx} className="shap-factor-row">
                <div className="shap-factor-name">
                  <span>{factor.feature_name}</span>
                  <span className="shap-factor-sub">
                    Value: <strong>{factor.feature_value}</strong>
                  </span>
                </div>

                <div className="shap-bar-container">
                  <div
                    className={`shap-bar ${isRiskUp ? 'risk-up' : 'protective'}`}
                    style={{ width: `${barWidthPercent}%` }}
                    title={factor.clinical_note}
                  />
                </div>

                <div className={`shap-factor-val ${isRiskUp ? 'risk-up' : 'protective'}`}>
                  {isRiskUp ? `+${factor.shap_value.toFixed(3)}` : factor.shap_value.toFixed(3)}
                </div>
              </div>
            );
          })
        )}
      </div>

      {/* Key Insights Callout */}
      {top_risk_factors && top_risk_factors.length > 0 && (
        <div style={{ marginTop: '1.25rem', padding: '0.875rem 1rem', background: 'var(--bg-muted)', borderRadius: 'var(--radius-md)', border: '1px solid var(--border-subtle)' }}>
          <div style={{ display: 'flex', alignItems: 'center', gap: '0.5rem', fontSize: '0.8125rem', fontWeight: 700, color: 'var(--text-primary)' }}>
            <HelpCircle size={15} color="var(--primary-600)" />
            <span>Primary Explanatory Insight:</span>
          </div>
          <p style={{ fontSize: '0.8125rem', color: 'var(--text-secondary)', marginTop: '0.25rem' }}>
            {top_risk_factors[0]?.clinical_note || 'Multiple lifestyle indicators influence this classification.'}
          </p>
        </div>
      )}
    </div>
  );
}
