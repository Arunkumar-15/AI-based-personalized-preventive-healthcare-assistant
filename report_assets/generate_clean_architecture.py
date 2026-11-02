import os
import matplotlib.pyplot as plt
import matplotlib.patches as patches

out_dir = r'C:\Users\arunk\Projects\health-assistant\report_assets'
os.makedirs(out_dir, exist_ok=True)

# Set high-resolution figure with spacious canvas (15 inches by 10.5 inches)
fig, ax = plt.subplots(figsize=(15, 10.5), dpi=300)
ax.axis('off')

# Clean neutral background
bg = patches.Rectangle((0, 0), 15, 10.5, facecolor='#ffffff', edgecolor='none')
ax.add_patch(bg)

# Sophisticated color palette
C_TIER1_BG = '#f0fdf4'
C_TIER1_BORDER = '#15803d'

C_TIER2_BG = '#eff6ff'
C_TIER2_BORDER = '#1d4ed8'

C_TIER3_BG = '#fdf2f8'
C_TIER3_BORDER = '#be185d'

C_TIER4_BG = '#faf5ff'
C_TIER4_BORDER = '#7e22ce'

C_TIER5_BG = '#fffbeb'
C_TIER5_BORDER = '#b45309'

def draw_tier_container(x, y, w, h, title, subtitle, bg_color, border_color):
    """Draws a main architectural tier boundary container"""
    rect = patches.FancyBboxPatch(
        (x, y), w, h,
        boxstyle="round,pad=0.2,rounding_size=0.25",
        facecolor=bg_color, edgecolor=border_color, linewidth=2.0
    )
    ax.add_patch(rect)
    
    # Title badge
    ax.text(x + 0.35, y + h - 0.40, title, 
            fontsize=12, weight='bold', color=border_color, fontfamily='serif')
    
    # Subtitle
    if subtitle:
        ax.text(x + 0.35, y + h - 0.72, subtitle, 
                fontsize=9.5, style='italic', color='#475569', fontfamily='serif')

def draw_module_box(x, y, w, h, header, bullet_items, fill_c='#ffffff', border_c='#cbd5e1'):
    """Draws an inner modular component box with clean padding and typography"""
    box = patches.FancyBboxPatch(
        (x, y), w, h,
        boxstyle="round,pad=0.15,rounding_size=0.18",
        facecolor=fill_c, edgecolor=border_c, linewidth=1.2
    )
    ax.add_patch(box)
    
    # Header bar
    header_box = patches.FancyBboxPatch(
        (x + 0.05, y + h - 0.50), w - 0.10, 0.45,
        boxstyle="round,pad=0.08,rounding_size=0.12",
        facecolor='#f1f5f9', edgecolor='none'
    )
    ax.add_patch(header_box)
    
    ax.text(x + w / 2, y + h - 0.28, header, 
            ha='center', va='center', fontsize=9.5, weight='bold', color='#0f172a', fontfamily='serif')
    
    # Bullet text with generous line spacing
    start_y = y + h - 0.78
    line_spacing = 0.28
    for idx, item in enumerate(bullet_items):
        ax.text(x + 0.20, start_y - (idx * line_spacing), item, 
                fontsize=8.5, color='#334155', fontfamily='serif')

# ==================== MAIN FIGURE TITLE ====================
ax.text(7.5, 10.05, 'Figure 4.1: High-Level System Architecture of AI-Based Personalized Preventive Healthcare Assistant', 
        ha='center', va='center', fontsize=14, weight='bold', color='#0f172a', fontfamily='serif')

# ==================== TIER 1: CLIENT PRESENTATION LAYER ====================
draw_tier_container(
    0.6, 6.7, 13.8, 3.0, 
    'TIER 1: CLIENT PRESENTATION & USER INTERACTION LAYER (React 18 + Vite)', 
    'Responsive Single-Page Application (SPA) hosting multi-modal screening, digital twin simulations, and bilingual controls',
    C_TIER1_BG, C_TIER1_BORDER
)

draw_module_box(
    0.9, 7.0, 3.2, 2.1, 
    'Multi-Modal Ingestion', 
    [
        '• Mode 1: Lifestyle & Symptom Form',
        '• Mode 2: Clinical Lab Biomarkers',
        '• Mode 3: Medical Report OCR Upload',
        '• Automated field parsing & presets'
    ]
)

draw_module_box(
    4.3, 7.0, 3.2, 2.1, 
    'Diagnostic Dashboard', 
    [
        '• 4-Class Severity Badge (Low-Critical)',
        '• Multi-Disease Risk (CAD, T2D, HTN)',
        '• TreeSHAP Feature Waterfall Plot',
        '• Evidence-based clinical guidance'
    ]
)

draw_module_box(
    7.7, 7.0, 3.2, 2.1, 
    'Health Digital Twin', 
    [
        '• Interactive sensitivity sliders',
        '• Weight (±15 kg), sleep & exercise',
        '• Quit smoking (+16.5% protection)',
        '• Real-time risk reduction calculation'
    ]
)

draw_module_box(
    11.1, 7.0, 3.0, 2.1, 
    'Admin Portal & Reports', 
    [
        '• Bilingual Engine (English & Tamil)',
        '• Live de-identified database view',
        '• Risk severity filtering & search',
        '• 1-Click official PDF clinical report'
    ]
)

# ==================== TIER 2: API GATEWAY & SECURITY LAYER ====================
draw_tier_container(
    0.6, 3.8, 6.7, 2.2, 
    'TIER 2: API GATEWAY & CONTROLLER (FastAPI + ASGI Uvicorn)', 
    'Asynchronous REST API routing, request validation, and service orchestration',
    C_TIER2_BG, C_TIER2_BORDER
)

draw_module_box(
    0.9, 4.05, 6.1, 1.45, 
    'REST Endpoints & Validation Gateway', 
    [
        '• POST /api/predict : Dispatches feature vectors to ML & XAI pipelines',
        '• GET /api/admin/records : Serves anonymized records for clinical audit',
        '• Pydantic v2 Schema Enforcement : Type checking & input sanitization',
        '• Security & Middleware : CORS handling, rate limiting & error handling'
    ]
)

# ==================== TIER 3: PRIVACY PRESERVATION ENGINE ====================
draw_tier_container(
    7.7, 3.8, 6.7, 2.2, 
    'TIER 3: PRIVACY PRESERVATION ENGINE (HIPAA Safe Harbor)', 
    'De-identification, cryptographic pseudonymization, and zero-disk memory safeguards',
    C_TIER3_BG, C_TIER3_BORDER
)

draw_module_box(
    8.0, 4.05, 6.1, 1.45, 
    'HIPAA Compliance & De-Identification Engine', 
    [
        '• Cryptographic Tokenizer : Non-reversible SHA-256 (e.g. ANON-8F92-4C1B)',
        '• k-Anonymity Generalizer : 5-Year Age Brackets & WHO BMI Categories',
        '• Zero-Storage Guarantee : Zero persistent Protected Health Info (PHI) on disk',
        '• Ephemeral RAM-bound execution preventing unauthorized forensic recovery'
    ]
)

# ==================== TIER 4: MACHINE LEARNING & XAI ENGINE ====================
draw_tier_container(
    0.6, 0.5, 7.8, 2.65, 
    'TIER 4: MACHINE LEARNING & EXPLAINABLE AI ENGINE (Python 3.11)', 
    'High-accuracy gradient boosting prediction and game-theoretic feature attribution',
    C_TIER4_BG, C_TIER4_BORDER
)

draw_module_box(
    0.9, 0.75, 3.6, 1.85, 
    'XGBoost Predictive Engine', 
    [
        '• 150 Gradient Boosted Trees (Max depth: 6)',
        '• 99.86% Test Classification Accuracy',
        '• 99.79% Macro F1-Score across 4 classes',
        '• Multi-Disease Estimator: CAD %, T2D %, HTN %',
        '• Continuous composite risk scoring (0–100)'
    ]
)

draw_module_box(
    4.7, 0.75, 3.4, 1.85, 
    'TreeSHAP Attribution & Guidance', 
    [
        '• Computes exact Shapley values (phi_i)',
        '• Ranks top clinical risk & protective drivers',
        '• Completely resolves black-box opacity',
        '• Algorithmic Preventive Guidance Engine',
        '• Personalized dietary, habit & checkup advice'
    ]
)

# ==================== TIER 5: DATA PERSISTENCE & AUDIT WAREHOUSE ====================
draw_tier_container(
    8.8, 0.5, 5.6, 2.65, 
    'TIER 5: DATA STORAGE & EXPORT WAREHOUSE', 
    'In-memory RAM data store and clinical research warehouse',
    C_TIER5_BG, C_TIER5_BORDER
)

draw_module_box(
    9.1, 0.75, 5.0, 1.85, 
    'In-Memory Store & Clinical Dataset', 
    [
        '• Live In-Memory Store (ANONYMIZED_DB_STORE)',
        '• Microsecond Query Latency (<0.01 ms response)',
        '• High Scalability: Holds 1,000,000+ records in 500 MB RAM',
        '• Training Warehouse (healthcare_dataset.csv, 3,500 rows)',
        '• 1-Click CSV Audit Exporter for medical research'
    ]
)

# ==================== CONNECTIVE DATA FLOW ARROWS ====================
def draw_flow_arrow(start_x, start_y, end_x, end_y, label, text_offset=(0, 0), color='#1d4ed8'):
    ax.annotate(
        '', xy=(end_x, end_y), xytext=(start_x, start_y),
        arrowprops=dict(arrowstyle='<->', lw=2.0, color=color, mutation_scale=15)
    )
    if label:
        mid_x = (start_x + end_x) / 2 + text_offset[0]
        mid_y = (start_y + end_y) / 2 + text_offset[1]
        ax.text(
            mid_x, mid_y, label, ha='center', va='center',
            fontsize=8.5, weight='bold', color=color, fontfamily='serif',
            bbox=dict(boxstyle='round,pad=0.25', facecolor='#ffffff', edgecolor=color, lw=1.0)
        )

# Arrow 1: Tier 1 <-> Tier 2 (HTTP REST Ingestion)
draw_flow_arrow(3.8, 6.7, 3.8, 6.0, 'JSON / REST HTTP Requests & Responses', text_offset=(0, 0), color='#1d4ed8')

# Arrow 2: Tier 2 <-> Tier 3 (Internal De-Identification)
draw_flow_arrow(7.3, 4.9, 7.7, 4.9, 'Direct Sanitized\nPayload Hand-off', text_offset=(0, 0.40), color='#475569')

# Arrow 3: Tier 2 <-> Tier 4 (Feature Vectors & Predictions)
draw_flow_arrow(3.8, 3.8, 3.8, 3.15, 'Feature Vectors & ML Predictions', text_offset=(0, 0), color='#7e22ce')

# Arrow 4: Tier 3 -> Tier 5 (Anonymized Tokens)
draw_flow_arrow(11.4, 3.8, 11.4, 3.15, 'Anonymized Tokens (Zero PHI)', text_offset=(0, 0), color='#be185d')

# Arrow 5: Tier 4 <-> Tier 5 (Model Training & DB Sync)
draw_flow_arrow(8.4, 1.8, 8.8, 1.8, 'CSV Sync / Audit Data', text_offset=(0, 0.32), color='#b45309')

ax.set_xlim(0, 15)
ax.set_ylim(0, 10.5)
plt.tight_layout()

save_path = os.path.join(out_dir, 'fig_4_1_system_architecture.png')
plt.savefig(save_path, bbox_inches='tight')
plt.close()
print('Clean, non-overlapping architecture diagram generated successfully at:', save_path)
