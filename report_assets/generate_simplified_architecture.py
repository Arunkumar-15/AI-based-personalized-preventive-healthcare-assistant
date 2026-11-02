import os
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle

out_dir = r'C:\Users\arunk\Projects\health-assistant\report_assets'
os.makedirs(out_dir, exist_ok=True)

# 16 x 12 inches at 400 DPI gives ultra-high pixel density (6400 x 4800 px) - Razor-sharp clarity!
fig, ax = plt.subplots(figsize=(16, 12), dpi=400)
ax.axis('off')

# Set background to pristine crisp white
bg = patches.Rectangle((0, 0), 16, 12, facecolor='#ffffff', edgecolor='none')
ax.add_patch(bg)

FONT_FAMILY = 'Segoe UI'

# Modern, accessible healthcare tech color palette
C_TIER1_BORDER = '#059669'  # Emerald Green
C_TIER1_BG = '#ecfdf5'
C_TIER1_TITLE = '#065f46'
C_TIER1_CARD_BORDER = '#10b981'
C_TIER1_HEADER_BG = '#d1fae5'

C_TIER2_BORDER = '#2563eb'  # Royal Blue
C_TIER2_BG = '#eff6ff'
C_TIER2_TITLE = '#1e40af'
C_TIER2_CARD_BORDER = '#3b82f6'
C_TIER2_HEADER_BG = '#dbeafe'

C_TIER3_BORDER = '#e11d48'  # Crimson / Rose (Security)
C_TIER3_BG = '#fff1f2'
C_TIER3_TITLE = '#9f1239'
C_TIER3_CARD_BORDER = '#f43f5e'
C_TIER3_HEADER_BG = '#ffe4e6'

C_TIER4_BORDER = '#7c3aed'  # Violet / Purple (AI & Intelligence)
C_TIER4_BG = '#faf5ff'
C_TIER4_TITLE = '#5b21b6'
C_TIER4_CARD_BORDER = '#8b5cf6'
C_TIER4_HEADER_BG = '#ede9fe'

C_TIER5_BORDER = '#d97706'  # Amber / Bronze (Storage)
C_TIER5_BG = '#fffbeb'
C_TIER5_TITLE = '#92400e'
C_TIER5_CARD_BORDER = '#f59e0b'
C_TIER5_HEADER_BG = '#fef3c7'

def draw_shadow(x, y, w, h, radius=0.20):
    """Draw subtle shadow behind containers for depth"""
    shadow = FancyBboxPatch(
        (x + 0.05, y - 0.05), w, h,
        boxstyle=f"round,pad=0.0,rounding_size={radius}",
        facecolor='#cbd5e1', edgecolor='none', alpha=0.40, zorder=1
    )
    ax.add_patch(shadow)

def draw_tier_container(x, y, w, h, tier_badge, title, subtitle, bg_color, border_color, title_color, badge_y_offset=0.45):
    draw_shadow(x, y, w, h, radius=0.20)
    container = FancyBboxPatch(
        (x, y), w, h,
        boxstyle="round,pad=0.0,rounding_size=0.20",
        facecolor=bg_color, edgecolor=border_color, linewidth=2.0, zorder=2
    )
    ax.add_patch(container)
    
    # Tier Badge Pill
    badge_w = 1.50
    badge_h = 0.34
    badge_y = y + h - badge_y_offset
    badge = FancyBboxPatch(
        (x + 0.32, badge_y), badge_w, badge_h,
        boxstyle="round,pad=0.0,rounding_size=0.10",
        facecolor=border_color, edgecolor='none', zorder=3
    )
    ax.add_patch(badge)
    ax.text(
        x + 0.32 + badge_w / 2, badge_y + badge_h / 2, tier_badge,
        ha='center', va='center', fontsize=9.8, weight='bold', color='#ffffff',
        fontfamily=FONT_FAMILY, zorder=4
    )
    
    # Main Tier Title
    ax.text(
        x + 0.32 + badge_w + 0.22, badge_y + badge_h - 0.06, title,
        ha='left', va='center', fontsize=12.2, weight='bold', color=title_color,
        fontfamily=FONT_FAMILY, zorder=4
    )
    
    # Subtitle
    if subtitle:
        ax.text(
            x + 0.32 + badge_w + 0.22, badge_y - 0.12, subtitle,
            ha='left', va='center', fontsize=9.0, style='italic', color='#475569',
            fontfamily=FONT_FAMILY, zorder=4
        )

def draw_card(x, y, w, h, title, items, card_border='#cbd5e1', header_bg='#f8fafc', title_color='#0f172a', bullet_color='#3b82f6', header_h=0.34):
    # Inner card
    card = FancyBboxPatch(
        (x, y), w, h,
        boxstyle="round,pad=0.0,rounding_size=0.14",
        facecolor='#ffffff', edgecolor=card_border, linewidth=1.3, zorder=3
    )
    ax.add_patch(card)
    
    # Card Header Strip
    header_strip = FancyBboxPatch(
        (x, y + h - header_h), w, header_h,
        boxstyle="round,pad=0.0,rounding_size=0.14",
        facecolor=header_bg, edgecolor='none', zorder=4
    )
    ax.add_patch(header_strip)
    
    # Header Bottom Divider
    ax.plot([x, x + w], [y + h - header_h, y + h - header_h], color=card_border, lw=1.0, zorder=5)
    
    # Header Title
    ax.text(
        x + w / 2, y + h - header_h / 2, title,
        ha='center', va='center', fontsize=10.0, weight='bold', color=title_color,
        fontfamily=FONT_FAMILY, zorder=6
    )
    
    # Content Items with circular bullet icons
    total_items = len(items)
    content_h = h - header_h - 0.14
    spacing = content_h / total_items if total_items > 0 else 0.25
    start_y = y + h - header_h - 0.10 - (spacing / 2)
    
    for idx, text in enumerate(items):
        cur_y = start_y - (idx * spacing)
        # Vector Bullet Circle
        bullet = Circle((x + 0.22, cur_y), radius=0.040, facecolor=bullet_color, edgecolor='none', zorder=6)
        ax.add_patch(bullet)
        # Bullet Text
        ax.text(
            x + 0.36, cur_y, text,
            ha='left', va='center', fontsize=8.9, color='#1e293b',
            fontfamily=FONT_FAMILY, zorder=6
        )

# ==================== MAIN FIGURE TITLE ====================
ax.text(
    8.0, 11.65, 'Figure 4.1: High-Level System Architecture of AI-Based Personalized Preventive Healthcare Assistant',
    ha='center', va='center', fontsize=15.5, weight='bold', color='#0f172a',
    fontfamily=FONT_FAMILY
)
ax.text(
    8.0, 11.32, 'Modular Multi-Tier Framework: Client Presentation, Secure Gateway, HIPAA Privacy Engine, Explainable AI & In-Memory Storage',
    ha='center', va='center', fontsize=10.2, color='#64748b',
    fontfamily=FONT_FAMILY
)

# ==================== TIER 1: CLIENT PRESENTATION LAYER ====================
draw_tier_container(
    0.6, 8.35, 14.8, 2.65,
    'TIER 1', 'CLIENT PRESENTATION & INTERACTION LAYER',
    'Responsive Single-Page Application (React 18 + Vite + Tailwind CSS)',
    C_TIER1_BG, C_TIER1_BORDER, C_TIER1_TITLE, badge_y_offset=0.45
)

t1_w = 3.38
t1_gap = 0.26
t1_start_x = 0.85
t1_y = 8.50
t1_h = 1.76

draw_card(
    t1_start_x + 0 * (t1_w + t1_gap), t1_y, t1_w, t1_h,
    'Multi-Modal Ingestion',
    [
        'Mode 1: Lifestyle & Symptom Form',
        'Mode 2: Clinical Lab Biomarkers',
        'Mode 3: Medical Report OCR Upload',
        'Pre-configured test case presets'
    ],
    card_border=C_TIER1_CARD_BORDER, header_bg=C_TIER1_HEADER_BG, title_color=C_TIER1_TITLE, bullet_color=C_TIER1_BORDER
)

draw_card(
    t1_start_x + 1 * (t1_w + t1_gap), t1_y, t1_w, t1_h,
    'Diagnostic Risk Dashboard',
    [
        '4-Tier Severity Badge (Low to Critical)',
        'Multi-Disease Risk (CAD, T2D, HTN)',
        'Continuous Risk Score Index (0–100)',
        'Real-time alert indicators & guidance'
    ],
    card_border=C_TIER1_CARD_BORDER, header_bg=C_TIER1_HEADER_BG, title_color=C_TIER1_TITLE, bullet_color=C_TIER1_BORDER
)

draw_card(
    t1_start_x + 2 * (t1_w + t1_gap), t1_y, t1_w, t1_h,
    'Health Digital Twin Simulator',
    [
        'Interactive Sensitivity Sliders',
        'Weight (±15 kg), Sleep & Exercise',
        'Quit Smoking Effect (+16.5% Gain)',
        'Instant Risk Delta Reduction %'
    ],
    card_border=C_TIER1_CARD_BORDER, header_bg=C_TIER1_HEADER_BG, title_color=C_TIER1_TITLE, bullet_color=C_TIER1_BORDER
)

draw_card(
    t1_start_x + 3 * (t1_w + t1_gap), t1_y, t1_w, t1_h,
    'Clinical Portal & Reporting',
    [
        'Bilingual Support (English & Tamil)',
        '1-Click Official PDF Medical Report',
        'De-identified record audit table',
        'Severity-based search & filtering'
    ],
    card_border=C_TIER1_CARD_BORDER, header_bg=C_TIER1_HEADER_BG, title_color=C_TIER1_TITLE, bullet_color=C_TIER1_BORDER
)

# ==================== TIER 2: API GATEWAY & CONTROLLER ====================
draw_tier_container(
    0.6, 5.45, 14.8, 2.25,
    'TIER 2', 'API GATEWAY & CONTROLLER SERVICE',
    'High-Speed Asynchronous Microservice Gateway (FastAPI + ASGI Uvicorn)',
    C_TIER2_BG, C_TIER2_BORDER, C_TIER2_TITLE, badge_y_offset=0.45
)

t2_w = 4.60
t2_gap = 0.25
t2_start_x = 0.85
t2_y = 5.60
t2_h = 1.36

draw_card(
    t2_start_x + 0 * (t2_w + t2_gap), t2_y, t2_w, t2_h,
    'REST Ingestion Endpoints',
    [
        'POST /api/predict : Multi-modal inference & XAI',
        'GET /api/admin/records : De-identified audit feed',
        'GET /api/health : Microservice liveness & status'
    ],
    card_border=C_TIER2_CARD_BORDER, header_bg=C_TIER2_HEADER_BG, title_color=C_TIER2_TITLE, bullet_color=C_TIER2_BORDER
)

draw_card(
    t2_start_x + 1 * (t2_w + t2_gap), t2_y, t2_w, t2_h,
    'Request Validation & Sanitization',
    [
        'Pydantic v2 strict schema enforcement',
        'Clinical range bounds & outlier detection',
        'Automated BMI & categorical encoding'
    ],
    card_border=C_TIER2_CARD_BORDER, header_bg=C_TIER2_HEADER_BG, title_color=C_TIER2_TITLE, bullet_color=C_TIER2_BORDER
)

draw_card(
    t2_start_x + 2 * (t2_w + t2_gap), t2_y, t2_w, t2_h,
    'Security Middleware & Controller',
    [
        'Strict Cross-Origin Resource Sharing (CORS)',
        'Rate-limiting & Denial-of-Service shielding',
        'Standardized JSON error & exception handling'
    ],
    card_border=C_TIER2_CARD_BORDER, header_bg=C_TIER2_HEADER_BG, title_color=C_TIER2_TITLE, bullet_color=C_TIER2_BORDER
)

# ==================== TIER 3 & TIER 4 (SIDE BY SIDE) ====================
# Tier 3 (Left) - Privacy Preservation Engine
t3_x = 0.6
t3_w = 7.15
t3_y = 2.35
t3_h = 2.35

draw_tier_container(
    t3_x, t3_y, t3_w, t3_h,
    'TIER 3', 'PRIVACY PRESERVATION ENGINE',
    'HIPAA Safe Harbor Compliance & Cryptographic Safeguards',
    C_TIER3_BG, C_TIER3_BORDER, C_TIER3_TITLE, badge_y_offset=0.45
)

draw_card(
    t3_x + 0.25, t3_y + 0.15, t3_w - 0.5, 1.48,
    'Cryptographic Anonymization Safeguards',
    [
        'Salted SHA-256 Tokenization (e.g., ANON-8F92-4C1B)',
        'k-Anonymity Generalization: 5-Year Age & WHO BMI Bins',
        'Zero-Disk PHI Storage: No identifiable patient data on disk',
        'Ephemeral RAM-only execution preventing forensic recovery'
    ],
    card_border=C_TIER3_CARD_BORDER, header_bg=C_TIER3_HEADER_BG, title_color=C_TIER3_TITLE, bullet_color=C_TIER3_BORDER
)

# Tier 4 (Right) - Machine Learning & XAI Engine
t4_x = 8.25
t4_w = 7.15
t4_y = 2.35
t4_h = 2.35

draw_tier_container(
    t4_x, t4_y, t4_w, t4_h,
    'TIER 4', 'MACHINE LEARNING & EXPLAINABILITY ENGINE',
    'Gradient Boosting Prediction & Game-Theoretic TreeSHAP',
    C_TIER4_BG, C_TIER4_BORDER, C_TIER4_TITLE, badge_y_offset=0.45
)

draw_card(
    t4_x + 0.25, t4_y + 0.15, t4_w - 0.5, 1.48,
    'XGBoost Predictive Core & TreeSHAP Explainer',
    [
        '150-Tree XGBoost Classifier (99.86% Test Accuracy)',
        'TreeSHAP Attribution: Exact Shapley values (phi_i) per feature',
        'Multi-Disease Estimator: Individual CAD %, T2D %, HTN %',
        'Algorithmic Guidance Engine: Personalized clinical diet & habits'
    ],
    card_border=C_TIER4_CARD_BORDER, header_bg=C_TIER4_HEADER_BG, title_color=C_TIER4_TITLE, bullet_color=C_TIER4_BORDER
)

# ==================== TIER 5: DATA STORAGE & AUDIT WAREHOUSE ====================
draw_tier_container(
    0.6, 0.22, 14.8, 1.43,
    'TIER 5', 'DATA PERSISTENCE & CLINICAL RESEARCH WAREHOUSE',
    'High-Speed Ephemeral RAM Store & Curated 3,500-Patient Training Dataset',
    C_TIER5_BG, C_TIER5_BORDER, C_TIER5_TITLE, badge_y_offset=0.40
)

t5_w = 4.60
t5_gap = 0.25
t5_start_x = 0.85
t5_y = 0.32
t5_h = 0.72

draw_card(
    t5_start_x + 0 * (t5_w + t5_gap), t5_y, t5_w, t5_h,
    'Live In-Memory RAM Store',
    [
        'ANONYMIZED_DB_STORE in Python memory',
        'Sub-millisecond latency (<0.01 ms response)'
    ],
    card_border=C_TIER5_CARD_BORDER, header_bg=C_TIER5_HEADER_BG, title_color=C_TIER5_TITLE, bullet_color=C_TIER5_BORDER, header_h=0.26
)

draw_card(
    t5_start_x + 1 * (t5_w + t5_gap), t5_y, t5_w, t5_h,
    'Clinical Training Warehouse',
    [
        'healthcare_dataset.csv (3,500 patient records)',
        'Stratified clinical splits for model training'
    ],
    card_border=C_TIER5_CARD_BORDER, header_bg=C_TIER5_HEADER_BG, title_color=C_TIER5_TITLE, bullet_color=C_TIER5_BORDER, header_h=0.26
)

draw_card(
    t5_start_x + 2 * (t5_w + t5_gap), t5_y, t5_w, t5_h,
    'Clinical Audit & Research Export',
    [
        'Zero-PHI anonymized research audit trail',
        '1-Click CSV export for medical validation'
    ],
    card_border=C_TIER5_CARD_BORDER, header_bg=C_TIER5_HEADER_BG, title_color=C_TIER5_TITLE, bullet_color=C_TIER5_BORDER, header_h=0.26
)

# ==================== CONNECTIVE FLOW ARROWS ====================
def draw_bidirectional_arrow(x1, y1, x2, y2, label='', color='#2563eb', label_pos=0.5):
    arrow = FancyArrowPatch(
        (x1, y1), (x2, y2),
        arrowstyle='<|-|>',
        mutation_scale=16,
        linewidth=2.2,
        color=color,
        zorder=10
    )
    ax.add_patch(arrow)
    if label:
        lx = x1 + (x2 - x1) * label_pos
        ly = y1 + (y2 - y1) * label_pos
        ax.text(
            lx, ly, label,
            ha='center', va='center',
            fontsize=9.2, weight='bold', color=color,
            fontfamily=FONT_FAMILY,
            bbox=dict(boxstyle='round,pad=0.28', facecolor='#ffffff', edgecolor=color, lw=1.2),
            zorder=11
        )

def draw_single_arrow(x1, y1, x2, y2, label='', color='#475569', label_pos=0.5):
    arrow = FancyArrowPatch(
        (x1, y1), (x2, y2),
        arrowstyle='-|>',
        mutation_scale=16,
        linewidth=2.2,
        color=color,
        zorder=10
    )
    ax.add_patch(arrow)
    if label:
        lx = x1 + (x2 - x1) * label_pos
        ly = y1 + (y2 - y1) * label_pos
        ax.text(
            lx, ly, label,
            ha='center', va='center',
            fontsize=8.8, weight='bold', color=color,
            fontfamily=FONT_FAMILY,
            bbox=dict(boxstyle='round,pad=0.24', facecolor='#ffffff', edgecolor=color, lw=1.2),
            zorder=11
        )

# Flow 1: Tier 1 <-> Tier 2 (HTTP REST Ingestion)
draw_bidirectional_arrow(8.0, 8.35, 8.0, 7.70, 'JSON / RESTful HTTPS Requests & Real-Time Diagnostic Results', color='#2563eb')

# Flow 2: Tier 2 -> Tier 3 (Raw Screening Payload)
draw_single_arrow(4.17, 5.45, 4.17, 4.70, 'Raw Screening Payload', color='#e11d48')

# Flow 3: Tier 3 -> Tier 4 (De-Identified Feature Vectors)
draw_single_arrow(7.75, 3.24, 8.25, 3.24, 'De-Identified\nFeature Vector', color='#6b21a8')

# Flow 4: Tier 4 -> Tier 2 (ML Predictions & SHAP Explanation)
draw_single_arrow(11.82, 4.70, 11.82, 5.45, 'Predictions & TreeSHAP Explanations', color='#7c3aed')

# Flow 5: Tier 3 & Tier 4 -> Tier 5 (Persistence)
draw_single_arrow(4.17, 2.35, 4.17, 1.65, 'Anonymized Tokens (Zero PHI)', color='#e11d48')
draw_single_arrow(11.82, 2.35, 11.82, 1.65, 'Audit Logs & Model Metrics', color='#d97706')

ax.set_xlim(0, 16)
ax.set_ylim(0, 12)
plt.tight_layout()

save_path = os.path.join(out_dir, 'fig_4_1_system_architecture.png')
plt.savefig(save_path, bbox_inches='tight', dpi=400)
plt.close()

print(f"High-clarity, simplified architecture diagram generated successfully at: {save_path}")
