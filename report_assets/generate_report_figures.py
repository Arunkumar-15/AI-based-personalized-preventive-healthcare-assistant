import os
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

out_dir = r'C:\Users\arunk\Projects\health-assistant\report_assets'
os.makedirs(out_dir, exist_ok=True)

# 1. Confusion Matrix
fig, ax = plt.subplots(figsize=(6.5, 5.2), dpi=300)
cm = np.array([
    [102, 1, 0, 0],
    [0, 149, 0, 0],
    [0, 0, 205, 0],
    [0, 0, 0, 243]
])
classes = ['Low Risk', 'Moderate Risk', 'High Risk', 'Critical Risk']
im = ax.imshow(cm, interpolation='nearest', cmap=plt.cm.Blues)
ax.figure.colorbar(im, ax=ax)

ax.set(xticks=np.arange(cm.shape[1]),
       yticks=np.arange(cm.shape[0]),
       xticklabels=classes, yticklabels=classes,
       title='Figure 5.1: Confusion Matrix of XGBoost Classifier (Accuracy: 99.86%)',
       ylabel='Actual Clinical Severity',
       xlabel='Predicted Clinical Severity')

plt.setp(ax.get_xticklabels(), rotation=20, ha='right', rotation_mode='anchor', fontsize=9, fontfamily='serif')
plt.setp(ax.get_yticklabels(), fontsize=9, fontfamily='serif')
ax.set_title(ax.get_title(), fontsize=11, weight='bold', pad=12, fontfamily='serif')
ax.xaxis.label.set_fontfamily('serif')
ax.yaxis.label.set_fontfamily('serif')

thresh = cm.max() / 2.
for i in range(cm.shape[0]):
    for j in range(cm.shape[1]):
        ax.text(j, i, format(cm[i, j], 'd'),
                ha='center', va='center',
                color='white' if cm[i, j] > thresh else 'black',
                fontsize=13, weight='bold', fontfamily='serif')

fig.tight_layout()
plt.savefig(os.path.join(out_dir, 'fig_5_1_confusion_matrix.png'))
plt.close()

# 2. Feature Importances
plt.figure(figsize=(8.5, 5.2), dpi=300)
features = [
    'Composite Risk Score', 'Symptom: Chest Pain', 'Symptom: Other',
    'Symptom: Shortness of Breath', 'Symptom: Excessive Thirst',
    'Symptom: Dizziness', 'Symptom: Fatigue', 'Family: Heart Disease',
    'Physical Activity Level', 'Smoking Status'
]
importances = [0.4717, 0.1891, 0.1724, 0.0400, 0.0337, 0.0161, 0.0117, 0.0089, 0.0084, 0.0076]
y_pos = np.arange(len(features))

colors = ['#1e40af' if i < 3 else '#3b82f6' for i in range(len(features))]
plt.barh(y_pos, importances[::-1], color=colors[::-1], edgecolor='#1e3a8a')
plt.yticks(y_pos, features[::-1], fontsize=10, fontfamily='serif')
plt.xlabel('Relative Feature Importance (Gini Gain)', fontsize=11, labelpad=10, fontfamily='serif')
plt.title('Figure 5.2: Top 10 Clinical Risk Feature Importances (XGBoost)', fontsize=12, pad=15, weight='bold', fontfamily='serif')
for i, v in enumerate(importances[::-1]):
    plt.text(v + 0.005, i, f'{v:.3f}', va='center', fontsize=9, fontfamily='serif', weight='bold', color='#1e3a8a')
plt.xlim(0, 0.55)
plt.grid(axis='x', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.savefig(os.path.join(out_dir, 'fig_5_2_feature_importances.png'))
plt.close()

# 3. Model Comparison Bar Chart
models = ['XGBoost\n(Proposed)', 'Random\nForest', 'Support Vector\nMachine (SVM)', 'Logistic\nRegression']
accs = [99.86, 92.40, 89.15, 84.70]
f1s = [99.79, 91.80, 88.50, 83.90]

x = np.arange(len(models))
width = 0.35

fig, ax = plt.subplots(figsize=(7.5, 4.5), dpi=300)
rects1 = ax.bar(x - width/2, accs, width, label='Test Accuracy (%)', color='#0284c7', edgecolor='#0369a1')
rects2 = ax.bar(x + width/2, f1s, width, label='Macro F1-Score (%)', color='#0d9488', edgecolor='#0f766e')

ax.set_ylabel('Performance Score (%)', fontsize=11, fontfamily='serif')
ax.set_title('Figure 5.3: Comparative Performance Across Machine Learning Models', fontsize=11, weight='bold', fontfamily='serif', pad=12)
ax.set_xticks(x)
ax.set_xticklabels(models, fontsize=9.5, fontfamily='serif')
ax.legend(loc='lower right', frameon=True)
ax.set_ylim(75, 105)
ax.grid(axis='y', linestyle='--', alpha=0.5)

for p in rects1:
    h = p.get_height()
    ax.annotate(f'{h:.1f}%', (p.get_x() + p.get_width()/2., h), ha='center', va='bottom', fontsize=8.5, fontfamily='serif', weight='bold')
for p in rects2:
    h = p.get_height()
    ax.annotate(f'{h:.1f}%', (p.get_x() + p.get_width()/2., h), ha='center', va='bottom', fontsize=8.5, fontfamily='serif', weight='bold')

plt.tight_layout()
plt.savefig(os.path.join(out_dir, 'fig_5_3_model_comparison.png'))
plt.close()

# 4. Architecture Diagram
fig, ax = plt.subplots(figsize=(10, 6.5), dpi=300)
ax.axis('off')

def draw_box(ax, xy, w, h, title, items, color, edgecolor):
    box = patches.FancyBboxPatch(xy, w, h, boxstyle='round,pad=0.2', facecolor=color, edgecolor=edgecolor, linewidth=1.5)
    ax.add_patch(box)
    ax.text(xy[0] + w/2, xy[1] + h - 0.25, title, ha='center', va='center', fontsize=9.5, weight='bold', color=edgecolor, fontfamily='serif')
    for idx, item in enumerate(items):
        ax.text(xy[0] + 0.2, xy[1] + h - 0.6 - idx*0.28, item, ha='left', va='center', fontsize=8, color='#1e293b', fontfamily='serif')

draw_box(ax, (0.5, 4.5), 2.6, 2.6, 'CLIENT LAYER\n(React 18 + Vite)', ['- Mode 1: Lifestyle Form', '- Mode 2: Lab Biomarkers', '- Mode 3: Medical OCR', '- Bilingual Localization', '- Responsive CSS3 UI'], '#f0fdf4', '#15803d')
draw_box(ax, (3.7, 4.5), 2.8, 2.6, 'API & SECURITY LAYER\n(FastAPI + Uvicorn)', ['- REST Endpoint: /api/predict', '- Admin API: /api/admin', '- CORS & Pydantic Validation', '- HIPAA Cryptographic Anonymizer', '- In-Memory DB Repository'], '#eff6ff', '#1d4ed8')
draw_box(ax, (7.1, 4.5), 2.6, 2.6, 'INTELLIGENCE ENGINE\n(Python 3.11 + XGBoost)', ['- 99.86% Accuracy Classifier', '- TreeSHAP Feature Attribution', '- Multi-Disease Risk Engine', '- CAD, Diabetes, HTN Scores', '- Scikit-Learn Preprocessing'], '#faf5ff', '#7e22ce')
draw_box(ax, (1.5, 1.0), 3.4, 2.4, 'HEALTH DIGITAL TWIN SIMULATOR', ['- Real-time Lifestyle Sensitivity', '- Weight, Sleep, Exercise Sliders', '- Quit Smoking Protection (+16.5%)', '- Immediate Risk Reduction Calculation', '- Personalized Preventive Guidance'], '#fffbeb', '#b45309')
draw_box(ax, (5.5, 1.0), 3.4, 2.4, 'PRIVACY DATA WAREHOUSE', ['- Zero PHI on Disk Persistence', '- SHA-256 Non-Reversible Tokens', '- k-Anonymity Age/BMI Brackets', '- In-Memory Microsecond Store', '- CSV Audit & Clinical Export'], '#fdf2f8', '#be185d')

ax.annotate('', xy=(3.6, 5.8), xytext=(3.15, 5.8), arrowprops=dict(arrowstyle='->', lw=2, color='#334155'))
ax.annotate('', xy=(7.0, 5.8), xytext=(6.55, 5.8), arrowprops=dict(arrowstyle='->', lw=2, color='#334155'))
ax.annotate('', xy=(3.2, 3.45), xytext=(4.5, 4.45), arrowprops=dict(arrowstyle='->', lw=1.5, color='#334155'))
ax.annotate('', xy=(6.5, 3.45), xytext=(5.5, 4.45), arrowprops=dict(arrowstyle='->', lw=1.5, color='#334155'))

ax.set_xlim(0, 10.2)
ax.set_ylim(0.5, 7.5)
plt.title('Figure 4.1: High-Level System Architecture of AI-Based Personalized Preventive Healthcare Assistant', fontsize=11, weight='bold', pad=10, fontfamily='serif')
plt.tight_layout()
plt.savefig(os.path.join(out_dir, 'fig_4_1_system_architecture.png'))
plt.close()

# 5. Workflow Diagram
fig, ax = plt.subplots(figsize=(9, 5.5), dpi=300)
ax.axis('off')

wf_steps = [
    ('1. Input Capture', 'Patient inputs screening parameters\nvia Mode 1, 2, or 3 OCR upload', '#eff6ff', '#1d4ed8'),
    ('2. Preprocessing', 'Feature normalization, BMI calculation,\nencoding categorical lifestyle variables', '#f0fdf4', '#15803d'),
    ('3. ML Inference', 'XGBoost multi-class classifier generates\nrisk severity (Low, Mod, High, Critical)', '#faf5ff', '#7e22ce'),
    ('4. XAI & SHAP', 'TreeSHAP calculates exact Shapley\nvalues for clinical feature attribution', '#fffbeb', '#b45309'),
    ('5. Digital Twin', 'Live What-If simulator empowers\npatient to test lifestyle interventions', '#fdf2f8', '#be185d'),
    ('6. HIPAA DB Store', 'Cryptographic token generation & in-memory\nanonymized record storage (Zero PHI)', '#f8fafc', '#334155')
]

for idx, (title, desc, bg, border) in enumerate(wf_steps):
    x_pos = 0.8 + (idx % 3) * 2.8
    y_pos = 3.4 if idx < 3 else 0.8
    
    box = patches.FancyBboxPatch((x_pos, y_pos), 2.5, 1.8, boxstyle='round,pad=0.2', facecolor=bg, edgecolor=border, linewidth=1.5)
    ax.add_patch(box)
    ax.text(x_pos + 1.25, y_pos + 1.4, title, ha='center', va='center', fontsize=9.5, weight='bold', color=border, fontfamily='serif')
    ax.text(x_pos + 1.25, y_pos + 0.7, desc, ha='center', va='center', fontsize=8, color='#1e293b', fontfamily='serif')

ax.annotate('', xy=(3.55, 4.3), xytext=(3.35, 4.3), arrowprops=dict(arrowstyle='->', lw=2, color='#475569'))
ax.annotate('', xy=(6.35, 4.3), xytext=(6.15, 4.3), arrowprops=dict(arrowstyle='->', lw=2, color='#475569'))
ax.annotate('', xy=(7.2, 2.65), xytext=(7.2, 3.35), arrowprops=dict(arrowstyle='->', lw=2, color='#475569'))
ax.annotate('', xy=(4.65, 1.7), xytext=(4.85, 1.7), arrowprops=dict(arrowstyle='->', lw=2, color='#475569'))
ax.annotate('', xy=(1.85, 1.7), xytext=(2.05, 1.7), arrowprops=dict(arrowstyle='->', lw=2, color='#475569'))

ax.set_xlim(0, 9.5)
ax.set_ylim(0.2, 5.8)
plt.title('Figure 4.2: End-to-End Diagnostic Assessment and Simulation Workflow', fontsize=11, weight='bold', pad=10, fontfamily='serif')
plt.tight_layout()
plt.savefig(os.path.join(out_dir, 'fig_4_2_system_workflow.png'))
plt.close()

print('All 5 diagrams successfully generated and saved!')
