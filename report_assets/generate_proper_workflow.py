import os
import matplotlib.pyplot as plt
import matplotlib.patches as patches

out_dir = r'C:\Users\arunk\Projects\health-assistant\report_assets'
os.makedirs(out_dir, exist_ok=True)

# Create high-resolution figure with comfortable dimensions (15 inches x 10.5 inches)
fig, ax = plt.subplots(figsize=(15, 10.5), dpi=300)
ax.axis('off')

# Clean background
bg = patches.Rectangle((0, 0), 15, 10.5, facecolor='#f8fafc', edgecolor='none')
ax.add_patch(bg)

# Palette
C_STAGE_BORDER = '#334155'

def draw_step_card(x, y, w, h, step_num, title, desc_items, header_c, bg_c='#ffffff', border_c='#cbd5e1'):
    """Draws a professional workflow step card with distinct header badge"""
    # Outer Card
    card = patches.FancyBboxPatch(
        (x, y), w, h,
        boxstyle="round,pad=0.15,rounding_size=0.18",
        facecolor=bg_c, edgecolor=border_c, linewidth=1.6
    )
    ax.add_patch(card)
    
    # Step Number Badge
    badge = patches.FancyBboxPatch(
        (x + 0.15, y + h - 0.48), 0.60, 0.38,
        boxstyle="round,pad=0.08,rounding_size=0.10",
        facecolor=header_c, edgecolor='none'
    )
    ax.add_patch(badge)
    ax.text(x + 0.45, y + h - 0.29, str(step_num), 
            ha='center', va='center', fontsize=9.5, weight='bold', color='#ffffff', fontfamily='serif')
    
    # Title Text
    ax.text(x + 0.90, y + h - 0.29, title, 
            ha='left', va='center', fontsize=10.5, weight='bold', color=header_c, fontfamily='serif')
    
    # Divider line
    ax.plot([x + 0.2, x + w - 0.2], [y + h - 0.58, y + h - 0.58], color=border_c, lw=0.8, linestyle='--')
    
    # Bullet Items
    start_y = y + h - 0.82
    line_sp = 0.24
    for idx, item in enumerate(desc_items):
        ax.text(x + 0.22, start_y - (idx * line_sp), item, 
                fontsize=8.2, color='#1e293b', fontfamily='serif')

def draw_arrow(start_x, start_y, end_x, end_y, label="", color='#475569', rad=0.0):
    """Draws a clean directed workflow arrow with optional label"""
    conn = f"arc3,rad={rad}" if rad != 0 else "arc3"
    ax.annotate(
        '', xy=(end_x, end_y), xytext=(start_x, start_y),
        arrowprops=dict(arrowstyle='->', lw=2.0, color=color, mutation_scale=15, connectionstyle=conn)
    )
    if label:
        mid_x = (start_x + end_x) / 2
        mid_y = (start_y + end_y) / 2
        ax.text(
            mid_x, mid_y, label, ha='center', va='center',
            fontsize=7.8, weight='bold', color=color, fontfamily='serif',
            bbox=dict(boxstyle='round,pad=0.2', facecolor='#ffffff', edgecolor=color, lw=0.8)
        )

# ==================== MAIN FIGURE TITLE ====================
ax.text(7.5, 10.05, 'Figure 4.2: End-to-End Diagnostic Assessment and Simulation Workflow', 
        ha='center', va='center', fontsize=13.5, weight='bold', color='#0f172a', fontfamily='serif')

# ==================== ROW 1: INGESTION, PREPROCESSING & INFERENCE ====================
# Step 1: Multi-Modal Intake
draw_step_card(
    0.6, 6.6, 4.2, 2.8, 1, 
    'Multi-Modal Patient Intake',
    [
        '• Mode 1: Non-Invasive Screening',
        '  - Demographics, Habits, Symptoms',
        '• Mode 2: Clinical Lab Biomarkers',
        '  - Blood Pressure, Glucose, HbA1c',
        '• Mode 3: Medical Document OCR',
        '  - Automated PDF/Scan text extraction',
        '• Bilingual UI: English or Tamil'
    ],
    header_c='#1d4ed8', bg_c='#eff6ff', border_c='#93c5fd'
)

# Step 2: Preprocessing & Feature Engineering
draw_step_card(
    5.4, 6.6, 4.2, 2.8, 2, 
    'Preprocessing & Validation',
    [
        '• Pydantic v2 Schema Enforcement',
        '  - Boundary & type sanitization',
        '• Continuous Feature Engineering',
        '  - BMI = Weight(kg) / Height(m)²',
        '• Categorical Integer Label Encoding',
        '  - Smoking, Alcohol, Activity level',
        '• Binary Clinical Symptom Vectorization'
    ],
    header_c='#15803d', bg_c='#f0fdf4', border_c='#86efac'
)

# Step 3: XGBoost Predictive Inference
draw_step_card(
    10.2, 6.6, 4.2, 2.8, 3, 
    'XGBoost Predictive Engine',
    [
        '• 150 Gradient-Boosted Trees (Max depth 6)',
        '• Softmax Probability Distribution',
        '• 4-Class Clinical Severity Output:',
        '  - Low, Moderate, High, Critical Risk',
        '• 99.86% Test Classification Accuracy',
        '• Multi-Disease Calibrated Estimators:',
        '  - CAD %, Type-2 Diabetes %, HTN %'
    ],
    header_c='#7e22ce', bg_c='#faf5ff', border_c='#d8b4fe'
)

# ==================== ROW 2: EXPLAINABILITY, DIGITAL TWIN & PERSISTENCE ====================
# Step 4: Explainable AI & SHAP
draw_step_card(
    0.6, 2.6, 4.2, 2.8, 4, 
    'TreeSHAP Attribution (XAI)',
    [
        '• Polynomial-Time TreeSHAP Algorithm',
        '• Computes exact Shapley values (phi_i)',
        '• Ranks Patient-Specific Risk Drivers:',
        '  - e.g. High Systolic BP, Obese BMI',
        '• Identifies Protective Factors:',
        '  - e.g. Normal Sleep, Non-smoker status',
        '• Completely resolves Black-Box Opacity'
    ],
    header_c='#b45309', bg_c='#fffbeb', border_c='#fde68a'
)

# Step 5: Health Digital Twin Simulator
draw_step_card(
    5.4, 2.6, 4.2, 2.8, 5, 
    'Health Digital Twin Simulator',
    [
        '• "What-If" Sensitivity Analysis',
        '• Interactive Behavioral Sliders:',
        '  - Weight delta: -15 kg to +15 kg',
        '  - Sleep duration: 4 to 10 hours',
        '  - Exercise frequency: 0 to 7 days',
        '• Quit Smoking (+16.5% protection)',
        '  - Hidden automatically if non-smoker',
        '• Live Risk Reduction Percentage Badge'
    ],
    header_c='#be185d', bg_c='#fdf2f8', border_c='#fbcfe8'
)

# Step 6: HIPAA Privacy & In-Memory DB
draw_step_card(
    10.2, 2.6, 4.2, 2.8, 6, 
    'HIPAA De-Identification & DB',
    [
        '• Salted SHA-256 Cryptographic Token',
        '  - Non-reversible ID (e.g. ANON-8F92)',
        '• k-Anonymity Generalization:',
        '  - 5-Year Age Brackets (e.g. 50–54)',
        '  - WHO Clinical BMI Intervals',
        '• Zero-Storage Guarantee (Zero disk PHI)',
        '• In-Memory RAM Store (<0.01 ms latency)'
    ],
    header_c='#0f766e', bg_c='#f0fdfa', border_c='#99f6e4'
)

# ==================== ROW 3: FINAL DELIVERABLES ====================
final_box = patches.FancyBboxPatch(
    (2.8, 0.4), 9.4, 1.4,
    boxstyle="round,pad=0.15,rounding_size=0.18",
    facecolor='#f8fafc', edgecolor='#64748b', linewidth=1.8
)
ax.add_patch(final_box)

ax.text(7.5, 1.45, 'STEP 7: CLINICAL EMPOWERMENT & CONTINUOUS PREVENTIVE CARE', 
        ha='center', va='center', fontsize=10.5, weight='bold', color='#0f172a', fontfamily='serif')
ax.text(7.5, 1.15, '• 1-Click Official Clinical PDF Report Download   • Personalized Dietary & Exercise Regimen', 
        ha='center', va='center', fontsize=8.8, color='#334155', fontfamily='serif')
ax.text(7.5, 0.80, '• Administrative Repository & Severity Filtering   • Longitudinal Preventive Re-Assessment', 
        ha='center', va='center', fontsize=8.8, color='#334155', fontfamily='serif')

# ==================== LOGICAL WORKFLOW ARROWS ====================
# 1 -> 2
draw_arrow(4.8, 8.0, 5.4, 8.0, label='Raw Payload', color='#1d4ed8')

# 2 -> 3
draw_arrow(9.6, 8.0, 10.2, 8.0, label='Feature Vector', color='#15803d')

# 3 -> 4 (Down & Left to XAI)
draw_arrow(11.0, 6.6, 3.8, 5.4, label='Class Probabilities & Model Trees', color='#7e22ce')

# 3 -> 6 (Down to HIPAA DB in parallel)
draw_arrow(12.3, 6.6, 12.3, 5.4, label='Asynchronous Ingestion', color='#0f766e')

# 4 -> 5 (XAI to Digital Twin)
draw_arrow(4.8, 4.0, 5.4, 4.0, label='Baseline Drivers', color='#b45309')

# 5 -> 7 (Digital Twin to Clinical Empowerment)
draw_arrow(7.5, 2.6, 7.5, 1.8, label='Simulated Sensitivity Outcomes', color='#be185d')

# 6 -> 7 (HIPAA DB to Clinical Empowerment)
draw_arrow(11.5, 2.6, 10.5, 1.8, label='De-Identified Audit', color='#0f766e')

ax.set_xlim(0, 15)
ax.set_ylim(0, 10.5)
plt.tight_layout()

save_path = os.path.join(out_dir, 'fig_4_2_system_workflow.png')
plt.savefig(save_path, bbox_inches='tight')
plt.close()
print('Proper workflow diagram Figure 4.2 generated successfully at:', save_path)
