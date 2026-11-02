import React, { useState } from 'react';
import { Sliders, RefreshCw, Activity, Heart, Award } from 'lucide-react';

export default function WhatIfSimulator({ originalResult, onSimulate }) {
  const [weightDelta, setWeightDelta] = useState(0);
  const [quitSmoking, setQuitSmoking] = useState(false);
  const [sleepHours, setSleepHours] = useState(7.0);
  const [exerciseDays, setExerciseDays] = useState(3);

  const baseScore = originalResult.risk_score || 65.0;

  const rawSmoking = (
    originalResult?.smoking_habit || 
    originalResult?.user_inputs?.smoking_habit || 
    ''
  ).toString().toLowerCase();

  const isNonSmoker = rawSmoking === 'non-smoker' || rawSmoking === 'no' || rawSmoking === 'none' || rawSmoking === 'never';

  // Sensitivity calculation logic
  let reduction = 0;
  if (weightDelta < 0) {
    reduction += Math.abs(weightDelta) * 2.2;
  } else if (weightDelta > 0) {
    reduction -= weightDelta * 1.8;
  }

  if (!isNonSmoker && quitSmoking) {
    reduction += 16.5;
  }

  if (sleepHours >= 7.0 && sleepHours <= 8.5) {
    reduction += 8.0;
  } else if (sleepHours < 6.0) {
    reduction -= 6.0;
  }

  reduction += (exerciseDays - 1) * 4.5;

  const simulatedScore = Math.min(95.0, Math.max(8.0, baseScore - reduction));
  const riskDiff = (baseScore - simulatedScore).toFixed(1);
  const isBetter = baseScore > simulatedScore;

  return (
    <div style={{ background: '#ffffff', border: '1px solid #cbd5e1', borderRadius: '16px', padding: '1.25rem 1.5rem', marginTop: '1.5rem', boxShadow: '0 4px 12px rgba(0,0,0,0.03)' }}>
      <div style={{ display: 'flex', alignItems: 'center', gap: '0.6rem', marginBottom: '0.8rem' }}>
        <Sliders size={22} color="#0284c7" />
        <h3 style={{ margin: 0, fontSize: '1.1rem', color: '#0f2b5c', fontWeight: 700 }}>
          🔮 Interactive "What-If" Lifestyle Simulator (Health Digital Twin)
        </h3>
      </div>
      <p style={{ margin: '0 0 1rem 0', fontSize: '0.85rem', color: '#64748b' }}>
        Adjust live lifestyle sliders below to simulate real-time risk reduction and observe how positive changes protect your health.
      </p>

      {/* Sliders Grid */}
      <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(240px, 1fr))', gap: '1.2rem', marginBottom: '1.2rem' }}>
        {/* Weight Adjustment */}
        <div style={{ background: '#f8fafc', padding: '0.85rem 1rem', borderRadius: '10px', border: '1px solid #e2e8f0' }}>
          <label style={{ display: 'flex', justifyContent: 'space-between', fontSize: '0.82rem', fontWeight: 600, color: '#1e293b', marginBottom: '0.4rem' }}>
            <span>Weight Adjustment</span>
            <span style={{ color: weightDelta < 0 ? '#047857' : weightDelta > 0 ? '#b91c1c' : '#475569' }}>
              {weightDelta > 0 ? `+${weightDelta} kg` : `${weightDelta} kg`}
            </span>
          </label>
          <input
            type="range"
            min="-15"
            max="15"
            step="1"
            value={weightDelta}
            onChange={(e) => setWeightDelta(Number(e.target.value))}
            style={{ width: '100%', accentColor: '#0284c7' }}
          />
        </div>

        {/* Quit Smoking (Hidden if User Selected Non-Smoker / No) */}
        {!isNonSmoker && (
          <div style={{ background: '#f8fafc', padding: '0.85rem 1rem', borderRadius: '10px', border: '1px solid #e2e8f0', display: 'flex', flexDirection: 'column', justifyContent: 'center' }}>
            <label style={{ display: 'flex', alignItems: 'center', gap: '0.6rem', fontSize: '0.85rem', fontWeight: 600, color: '#1e293b', cursor: 'pointer' }}>
              <input
                type="checkbox"
                checked={quitSmoking}
                onChange={(e) => setQuitSmoking(e.target.checked)}
                style={{ width: '18px', height: '18px', accentColor: '#047857' }}
              />
              <span>Quit Tobacco Smoking (+16.5% protection)</span>
            </label>
          </div>
        )}

        {/* Sleep Hours */}
        <div style={{ background: '#f8fafc', padding: '0.85rem 1rem', borderRadius: '10px', border: '1px solid #e2e8f0' }}>
          <label style={{ display: 'flex', justifyContent: 'space-between', fontSize: '0.82rem', fontWeight: 600, color: '#1e293b', marginBottom: '0.4rem' }}>
            <span>Target Sleep Duration</span>
            <span style={{ color: '#0284c7' }}>{sleepHours} Hours/night</span>
          </label>
          <input
            type="range"
            min="4"
            max="10"
            step="0.5"
            value={sleepHours}
            onChange={(e) => setSleepHours(Number(e.target.value))}
            style={{ width: '100%', accentColor: '#0284c7' }}
          />
        </div>

        {/* Exercise Days */}
        <div style={{ background: '#f8fafc', padding: '0.85rem 1rem', borderRadius: '10px', border: '1px solid #e2e8f0' }}>
          <label style={{ display: 'flex', justifyContent: 'space-between', fontSize: '0.82rem', fontWeight: 600, color: '#1e293b', marginBottom: '0.4rem' }}>
            <span>Weekly Exercise Days</span>
            <span style={{ color: '#047857' }}>{exerciseDays} Days/week</span>
          </label>
          <input
            type="range"
            min="0"
            max="7"
            step="1"
            value={exerciseDays}
            onChange={(e) => setExerciseDays(Number(e.target.value))}
            style={{ width: '100%', accentColor: '#047857' }}
          />
        </div>
      </div>

      {/* Simulated Results Comparison Box */}
      <div style={{ background: isBetter ? '#ecfdf5' : '#fef2f2', border: `1px solid ${isBetter ? '#6ee7b7' : '#fca5a5'}`, borderRadius: '12px', padding: '1rem 1.25rem', display: 'flex', alignItems: 'center', justifyContent: 'space-between', flexWrap: 'wrap', gap: '1rem' }}>
        <div>
          <div style={{ fontSize: '0.78rem', color: '#475569', fontWeight: 600 }}>BASELINE RISK SCORE</div>
          <div style={{ fontSize: '1.25rem', fontWeight: 700, color: '#1e293b' }}>{baseScore.toFixed(1)} / 100</div>
        </div>

        <div style={{ textAlign: 'center' }}>
          <div style={{ fontSize: '0.78rem', color: '#475569', fontWeight: 600 }}>SIMULATED FUTURE RISK</div>
          <div style={{ fontSize: '1.6rem', fontWeight: 800, color: isBetter ? '#047857' : '#b91c1c' }}>
            {simulatedScore.toFixed(1)} / 100
          </div>
        </div>

        <div style={{ textAlign: 'right' }}>
          <span style={{ display: 'inline-flex', alignItems: 'center', gap: '0.3rem', padding: '0.35rem 0.8rem', background: isBetter ? '#047857' : '#b91c1c', color: '#ffffff', borderRadius: '9999px', fontSize: '0.82rem', fontWeight: 700 }}>
            <Award size={16} />
            {isBetter ? `-${riskDiff}% Risk Reduction!` : `+${Math.abs(riskDiff)}% Risk Increase`}
          </span>
        </div>
      </div>
    </div>
  );
}
