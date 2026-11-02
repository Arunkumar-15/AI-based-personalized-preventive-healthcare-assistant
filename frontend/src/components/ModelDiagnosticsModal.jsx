import React, { useEffect, useState } from 'react';
import { X, Cpu, CheckCircle, Database, BarChart3, AlertCircle } from 'lucide-react';
import { fetchModelMetrics } from '../services/api';

export default function ModelDiagnosticsModal({ isOpen, onClose }) {
  const [metrics, setMetrics] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  useEffect(() => {
    if (isOpen && !metrics) {
      setLoading(true);
      fetchModelMetrics()
        .then(data => {
          setMetrics(data);
          setLoading(false);
        })
        .catch(err => {
          setError(err.message);
          setLoading(false);
        });
    }
  }, [isOpen, metrics]);

  if (!isOpen) return null;

  return (
    <div className="modal-backdrop" onClick={onClose}>
      <div className="modal-card" onClick={e => e.stopPropagation()}>
        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', borderBottom: '1px solid var(--border-subtle)', paddingBottom: '1rem' }}>
          <div style={{ display: 'flex', alignItems: 'center', gap: '0.625rem' }}>
            <Cpu size={22} color="var(--primary-600)" />
            <div>
              <h3 style={{ fontSize: '1.125rem', fontWeight: 800, color: 'var(--text-primary)' }}>
                XGBoost Model Diagnostics & Evaluation
              </h3>
              <p style={{ fontSize: '0.75rem', color: 'var(--text-muted)' }}>
                Section 5 Specification • Real Dataset Evaluation Metrics
              </p>
            </div>
          </div>
          <button
            type="button"
            className="btn btn-outline btn-sm"
            onClick={onClose}
            style={{ padding: '0.25rem 0.5rem' }}
          >
            <X size={18} />
          </button>
        </div>

        {loading ? (
          <div style={{ padding: '3rem', textAlign: 'center', color: 'var(--text-muted)' }}>
            Loading model performance metrics from backend...
          </div>
        ) : error ? (
          <div style={{ padding: '2rem', textAlign: 'center', color: '#dc2626' }}>
            <AlertCircle size={32} style={{ margin: '0 auto 0.5rem auto' }} />
            <p>Could not load model metrics: {error}</p>
          </div>
        ) : metrics ? (
          <div>
            {/* KPI Grid */}
            <div className="metrics-kpi-grid">
              <div className="kpi-card">
                <div className="kpi-val">{(metrics.accuracy * 100).toFixed(1)}%</div>
                <div className="kpi-label">Accuracy</div>
              </div>

              <div className="kpi-card">
                <div className="kpi-val">{(metrics.precision_macro * 100).toFixed(1)}%</div>
                <div className="kpi-label">Precision (Macro)</div>
              </div>

              <div className="kpi-card">
                <div className="kpi-val">{(metrics.recall_macro * 100).toFixed(1)}%</div>
                <div className="kpi-label">Recall (Macro)</div>
              </div>

              <div className="kpi-card">
                <div className="kpi-val">{(metrics.f1_macro * 100).toFixed(1)}%</div>
                <div className="kpi-label">F1-Score (Macro)</div>
              </div>
            </div>

            {/* Dataset split stats */}
            <div style={{ background: 'var(--bg-muted)', padding: '0.75rem 1rem', borderRadius: 'var(--radius-md)', display: 'flex', justifyContent: 'space-between', fontSize: '0.8125rem', color: 'var(--text-secondary)' }}>
              <span>Training Samples: <strong>{metrics.train_samples}</strong> (80% Stratified)</span>
              <span>Test Samples: <strong>{metrics.test_samples}</strong> (20% Holdout)</span>
              <span>Active Features: <strong>{metrics.features_count}</strong></span>
            </div>

            {/* Confusion Matrix */}
            {metrics.confusion_matrix && (
              <div style={{ marginTop: '1.5rem' }}>
                <h4 style={{ fontSize: '0.875rem', fontWeight: 700, color: 'var(--text-primary)', display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
                  <BarChart3 size={16} color="var(--primary-600)" />
                  Confusion Matrix (Evaluated on {metrics.test_samples} Test Samples)
                </h4>
                <table className="cm-table">
                  <thead>
                    <tr>
                      <th>Actual \ Predicted</th>
                      {metrics.confusion_matrix.labels?.map((lbl) => (
                        <th key={lbl}>{lbl}</th>
                      ))}
                    </tr>
                  </thead>
                  <tbody>
                    {metrics.confusion_matrix.matrix?.map((row, rIdx) => {
                      const actualLabel = metrics.confusion_matrix.labels[rIdx];
                      return (
                        <tr key={actualLabel}>
                          <th style={{ textAlign: 'left' }}>{actualLabel}</th>
                          {row.map((cell, cIdx) => (
                            <td key={cIdx} className={rIdx === cIdx ? 'diagonal' : ''}>
                              {cell}
                            </td>
                          ))}
                        </tr>
                      );
                    })}
                  </tbody>
                </table>
              </div>
            )}

            {/* Top Feature Importances */}
            {metrics.feature_importances && (
              <div style={{ marginTop: '1.5rem' }}>
                <h4 style={{ fontSize: '0.875rem', fontWeight: 700, color: 'var(--text-primary)', marginBottom: '0.75rem' }}>
                  Top XGBoost Global Feature Importances
                </h4>
                <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fill, minmax(220px, 1fr))', gap: '0.5rem' }}>
                  {metrics.feature_importances.slice(0, 8).map((f, idx) => (
                    <div key={idx} style={{ background: 'var(--bg-app)', border: '1px solid var(--border-subtle)', padding: '0.5rem 0.75rem', borderRadius: 'var(--radius-sm)', display: 'flex', justifyContent: 'space-between', fontSize: '0.75rem' }}>
                      <span style={{ fontWeight: 600, color: 'var(--text-secondary)' }}>{f.feature}</span>
                      <span style={{ fontWeight: 700, color: 'var(--primary-600)', fontFamily: 'var(--font-mono)' }}>
                        {(f.importance * 100).toFixed(1)}%
                      </span>
                    </div>
                  ))}
                </div>
              </div>
            )}
          </div>
        ) : null}

        <div style={{ marginTop: '1.5rem', display: 'flex', justifyContent: 'flex-end' }}>
          <button type="button" className="btn btn-outline" onClick={onClose}>
            Close Diagnostics
          </button>
        </div>
      </div>
    </div>
  );
}
