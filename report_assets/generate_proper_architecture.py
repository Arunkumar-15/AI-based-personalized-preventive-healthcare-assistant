import os
import matplotlib.pyplot as plt
import matplotlib.patches as patches

out_dir = r'C:\Users\arunk\Projects\health-assistant\report_assets'
os.makedirs(out_dir, exist_ok=True)

# Create a clean, professional layered software architecture diagram
fig, ax = plt.subplots(figsize=(12, 8.5), dpi=300)
ax.axis('off')

# Background canvas
bg = patches.Rectangle((0, 0), 12, 8.5, facecolor='#f8fafc', edgecolor='none')
ax.add_patch(bg)

# Palette
c_pres_bg = '#f0fdf4'
c_pres_border = '#16a34a'
c_api_bg = '#eff6ff'
c_api_border = '#2563eb'
c_ml_bg = '#faf5ff'
c_ml_border = '#9333ea'
c_sec_bg = '#fff1f2'
c_sec_border = '#e11d48'
c_db_bg = '#fffbeb'
c_db_border = '#d97706'

def draw_layer_card(x, y, w, h, title, subtitle, bg_color, border_color):
    card = patches.FancyBboxPatch((x, y), w, h, boxstyle='round,pad=0.15', facecolor=bg_color, edgecolor=border_color, linewidth=1.8)
    ax.add_patch(card)
    ax.text(x + 0.25, y + h - 0.32, title, fontsize=11, weight='bold', color=border_color, fontfamily='serif')
    if subtitle:
        ax.text(x + 0.25, y + h - 0.58, subtitle, fontsize=8.5, style='italic', color='#475569', fontfamily='serif')

def draw_sub_component(x, y, w, h, title, items, fill_c='#ffffff', border_c='#cbd5e1'):
    box = patches.FancyBboxPatch((x, y), w, h, boxstyle='round,pad=0.1', facecolor=fill_c, edgecolor=border_c, linewidth=1.2)
    ax.add_patch(box)
    ax.text(x + w/2, y + h - 0.22, title, ha='center', va='center', fontsize=9, weight='bold', color='#1e293b', fontfamily='serif')
    for idx, it in enumerate(items):
        ax.text(x + 0.15, y + h - 0.45 - idx*0.22, it, fontsize=7.8, color='#334155', fontfamily='serif')

# Header
ax.text(6.0, 8.1, 'Figure 4.1: High-Level System Architecture of AI-Based Personalized Preventive Healthcare Assistant', 
        ha='center', va='center', fontsize=12.5, weight='bold', color='#0f172a', fontfamily='serif')

# ==================== LAYER 1: CLIENT PRESENTATION LAYER ====================
draw_layer_card(0.5, 5.2, 11.0, 2.5, 'TIER 1: CLIENT PRESENTATION LAYER (React 18 + Vite)', 'Responsive User Experience & Interactive Diagnostic Interfaces', c_pres_bg, c_pres_border)

# 4 Components in Tier 1
draw_sub_component(0.8, 5.4, 2.4, 1.7, 'Multi-Modal Ingestion', 
                   ['- Mode 1: Lifestyle & Habits', '- Mode 2: Lab Biomarkers', '- Mode 3: Medical OCR Report', '- Form validation & presets'])

draw_sub_component(3.5, 5.4, 2.5, 1.7, 'Diagnostic Dashboard', 
                   ['- 4-Tier Risk Badge (Low-Crit)', '- Multi-Disease % (CAD, T2D, HTN)', '- SHAP Waterfall Attribution', '- Clinical Guidance Cards'])

draw_sub_component(6.3, 5.4, 2.5, 1.7, 'Health Digital Twin', 
                   ['- What-If Sensitivity Sliders', '- Weight (+/-15kg), Sleep, Exercise', '- Quit Smoking (+16.5% protect)', '- Real-Time Risk Reduction %'])

draw_sub_component(9.1, 5.4, 2.1, 1.7, 'Support & Admin UI', 
                   ['- Bilingual (English / Tamil)', '- Admin Clinical Records View', '- Severity Filtering & Search', '- 1-Click PDF Report Export'])

# ==================== LAYER 2: API GATEWAY & SECURITY TIER ====================
draw_layer_card(0.5, 3.4, 5.3, 1.45, 'TIER 2: API GATEWAY & CONTROLLER (FastAPI + Uvicorn)', 'Asynchronous REST Ingestion & Schema Dispatch', c_api_bg, c_api_border)
draw_sub_component(0.8, 3.55, 4.7, 0.95, 'REST Endpoints & Validation', 
                   ['- POST /api/predict (Inference & XAI)   - GET /api/admin/records (DB)', 
                    '- Pydantic Schema Validation           - CORS & Security Headers'], fill_c='#ffffff')

# ==================== LAYER 3: PRIVACY & ANONYMIZATION ENGINE ====================
draw_layer_card(6.2, 3.4, 5.3, 1.45, 'TIER 3: PRIVACY PRESERVATION ENGINE (HIPAA Safe Harbor)', 'De-identification & Zero-Storage Cryptographic Module', c_sec_bg, c_sec_border)
draw_sub_component(6.5, 3.55, 4.7, 0.95, 'HIPAA Compliance & De-Identification', 
                   ['- Salted SHA-256 Tokenization (e.g. ANON-8F92-4C1B)', 
                    '- k-Anonymity Binning: 5-Year Age Brackets & WHO BMI Intervals', 
                    '- Zero Persistent Protected Health Information (PHI) on Disk'], fill_c='#ffffff')

# ==================== LAYER 4: INTELLIGENCE & XAI ENGINE ====================
draw_layer_card(0.5, 0.5, 6.2, 2.5, 'TIER 4: MACHINE LEARNING & EXPLAINABILITY ENGINE', 'Gradient Boosting Prediction & Game-Theoretic Feature Attribution', c_ml_bg, c_ml_border)

draw_sub_component(0.8, 0.7, 2.7, 1.8, 'XGBoost Classification', 
                   ['- 150 Gradient Boosted Trees', '- Max Depth: 6 | Softmax loss', '- 99.86% Test Classification Acc', '- 4-Class Output (Low-Critical)', '- Multi-Disease Scoring (CAD, T2D)'])

draw_sub_component(3.8, 0.7, 2.6, 1.8, 'TreeSHAP & Guidance', 
                   ['- Exact Shapley attributions (phi_i)', '- Identifies Top Risk Drivers', '- Resolves Black-Box Dilemma', '- Evidence-Based Recommendations', '- Diet, Exercise & Checkup Logic'])

# ==================== LAYER 5: STORAGE & DATA MANAGEMENT TIER ====================
draw_layer_card(7.1, 0.5, 4.4, 2.5, 'TIER 5: DATA STORAGE & EXPORT', 'In-Memory Repository & Audit Warehouse', c_db_bg, c_db_border)

draw_sub_component(7.4, 0.7, 3.8, 1.8, 'In-Memory DB & CSV Storage', 
                   ['- Live RAM Store (ANONYMIZED_DB_STORE)', '- Microsecond Latency (<0.01 ms)', '- Capable of 1M+ Records in 500MB', '- Training Warehouse (3,500 CSV)', '- CSV Clinical Audit & Research Export'])

# Connective Flow Arrows
# Tier 1 to Tier 2
ax.annotate('', xy=(3.15, 4.88), xytext=(3.15, 5.2), arrowprops=dict(arrowstyle='<->', lw=2, color='#2563eb'))
ax.text(3.3, 5.0, 'JSON / REST HTTP', fontsize=7.5, style='italic', color='#1e40af', fontfamily='serif')

# Tier 2 to Tier 3
ax.annotate('', xy=(6.2, 4.1), xytext=(5.8, 4.1), arrowprops=dict(arrowstyle='<->', lw=1.8, color='#475569'))

# Tier 2 to Tier 4
ax.annotate('', xy=(3.15, 3.0), xytext=(3.15, 3.4), arrowprops=dict(arrowstyle='<->', lw=2, color='#9333ea'))
ax.text(3.3, 3.18, 'Feature Vectors & Predictions', fontsize=7.5, style='italic', color='#6b21a8', fontfamily='serif')

# Tier 3 to Tier 5
ax.annotate('', xy=(8.8, 3.0), xytext=(8.8, 3.4), arrowprops=dict(arrowstyle='->', lw=2, color='#e11d48'))
ax.text(9.0, 3.18, 'De-Identified Token Payloads', fontsize=7.5, style='italic', color='#9f1239', fontfamily='serif')

# Tier 4 to Tier 5
ax.annotate('', xy=(7.1, 1.6), xytext=(6.7, 1.6), arrowprops=dict(arrowstyle='<->', lw=1.8, color='#475569'))

ax.set_xlim(0, 12)
ax.set_ylim(0, 8.5)
plt.tight_layout()

save_path = os.path.join(out_dir, 'fig_4_1_system_architecture.png')
plt.savefig(save_path)
plt.close()
print('Successfully generated publication-grade Figure 4.1 at:', save_path)
