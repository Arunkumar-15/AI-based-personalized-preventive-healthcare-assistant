# generate_vertical_architecture.py
# High-Resolution (300 DPI) Vertically Long (Portrait Orientation) System Architecture Diagram
# Tailored specifically for inserting into portrait Word documents (A4 / Letter 8.5" x 11.5")
import os
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def build_vertical_architecture():
    out_dir = r'C:\Users\arunk\Projects\health-assistant\report_assets'
    os.makedirs(out_dir, exist_ok=True)

    # Portrait Canvas: Width 8.6 inches, Height 12.2 inches (Portrait Ratio = 0.705)
    # 300 DPI = 2580 x 3660 pixels.
    fig, ax = plt.subplots(figsize=(8.6, 12.2), dpi=300)
    ax.axis('off')

    # White canvas background
    canvas_bg = patches.Rectangle((0, 0), 8.6, 12.2, facecolor='#ffffff', edgecolor='none')
    ax.add_patch(canvas_bg)

    # Color Palette
    c_tier1_border = '#15803d'  # Forest Green
    c_tier1_bg     = '#f0fdf4'
    c_tier1_sub_bg = '#ffffff'
    c_tier1_sub_bd = '#bbf7d0'

    c_tier2_border = '#1d4ed8'  # Cobalt Blue
    c_tier2_bg     = '#eff6ff'
    c_tier2_sub_bg = '#ffffff'
    c_tier2_sub_bd = '#bfdbfe'

    c_tier3_border = '#991b1b'  # Crimson Red
    c_tier3_bg     = '#fff1f2'
    c_tier3_sub_bg = '#ffffff'
    c_tier3_sub_bd = '#fecaca'

    c_tier4_border = '#7e22ce'  # Indigo Purple
    c_tier4_bg     = '#faf5ff'
    c_tier4_sub_bg = '#ffffff'
    c_tier4_sub_bd = '#e9d5ff'

    c_tier5_border = '#b45309'  # Warm Amber / Gold
    c_tier5_bg     = '#fffbeb'
    c_tier5_sub_bg = '#ffffff'
    c_tier5_sub_bd = '#fde68a'

    def draw_card(x, y, w, h, bg_color, border_color, lw=1.8, rad=0.20):
        shadow = patches.FancyBboxPatch(
            (x + 0.025, y - 0.025), w, h,
            boxstyle=f'round,pad=0.04,rounding_size={rad}',
            facecolor='#e2e8f0', edgecolor='none', zorder=1
        )
        ax.add_patch(shadow)
        card = patches.FancyBboxPatch(
            (x, y), w, h,
            boxstyle=f'round,pad=0.04,rounding_size={rad}',
            facecolor=bg_color, edgecolor=border_color, linewidth=lw, zorder=2
        )
        ax.add_patch(card)

    def draw_badge(x, y, w, h, text, bg='#e0f2fe', border='#0284c7', text_color='#0369a1', fs=7.3, lw=1.1):
        badge = patches.FancyBboxPatch(
            (x - w/2, y - h/2), w, h,
            boxstyle='round,pad=0.03,rounding_size=0.10',
            facecolor=bg, edgecolor=border, linewidth=lw, zorder=5
        )
        ax.add_patch(badge)
        ax.text(x, y, text, ha='center', va='center', fontsize=fs, weight='bold',
                color=text_color, fontfamily='sans-serif', zorder=6, linespacing=1.15)

    x_left = 0.45
    w_full = 7.70

    # =========================================================================
    # TIER 1: CLIENT PRESENTATION & USER INTERACTION LAYER (Top Card)
    # =========================================================================
    t1_y, t1_h = 9.25, 2.65
    draw_card(x_left, t1_y, w_full, t1_h, c_tier1_bg, c_tier1_border, lw=2.0, rad=0.22)

    ax.text(x_left + 0.20, t1_y + t1_h - 0.26,
            'TIER 1: CLIENT PRESENTATION & USER INTERACTION LAYER (React 18 + Vite)',
            fontsize=9.6, weight='bold', color=c_tier1_border, fontfamily='sans-serif', zorder=3)
    ax.text(x_left + 0.20, t1_y + t1_h - 0.46,
            'Responsive Single Page Application (SPA) hosting multimodal screening, digital twin & bilingual controls',
            fontsize=7.3, style='italic', color='#166534', fontfamily='sans-serif', zorder=3)

    col_w = (w_full - 0.30 - 3 * 0.12) / 4.0  # ~1.76 each
    t1_cols = [
        {
            'title': 'Multi-Modal Ingestion',
            'bullets': [
                '• Mode 1: Lifestyle & Symptoms',
                '• Mode 2: Clinical Biomarkers',
                '• Mode 3: Medical Report OCR',
                '• Field validation & parsing'
            ]
        },
        {
            'title': 'Diagnostic Dashboard',
            'bullets': [
                '• 4-Class Severity Badge',
                '• Multi-Disease Risk (CAD, T2D)',
                '• TreeSHAP Waterfall Plot',
                '• Evidence-based guidance'
            ]
        },
        {
            'title': 'Health Digital Twin',
            'bullets': [
                '• Sensitivity sliders (±15 kg)',
                '• Sleep & exercise tuning',
                '• Smoking cessation (+16.5%)',
                '• Real-time risk recalculation'
            ]
        },
        {
            'title': 'Admin & Reports',
            'bullets': [
                '• Bilingual Engine (EN & TA)',
                '• De-identified database view',
                '• Severity search & filtering',
                '• 1-Click official PDF export'
            ]
        }
    ]

    for idx, col in enumerate(t1_cols):
        cx = x_left + 0.15 + idx * (col_w + 0.12)
        cy = t1_y + 0.12
        ch = 1.95
        draw_card(cx, cy, col_w, ch, c_tier1_sub_bg, c_tier1_sub_bd, lw=1.1, rad=0.12)
        h_box = patches.FancyBboxPatch(
            (cx, cy + ch - 0.32), col_w, 0.32,
            boxstyle='round,pad=0.02,rounding_size=0.08',
            facecolor='#e2e8f0', edgecolor='none', zorder=3
        )
        ax.add_patch(h_box)
        ax.text(cx + col_w/2, cy + ch - 0.16, col['title'],
                ha='center', va='center', fontsize=7.4, weight='bold', color='#0f2b5c', fontfamily='sans-serif', zorder=4)
        for b_idx, b in enumerate(col['bullets']):
            ax.text(cx + 0.08, cy + 1.35 - b_idx * 0.35, b,
                    fontsize=6.5, color='#1e293b', fontfamily='sans-serif', zorder=4)

    # Connector Tier 1 -> Middle Row
    draw_badge(x_left + w_full/2, 9.00, 3.80, 0.28, 'JSON / REST HTTP Requests & Responses',
               bg='#e0f2fe', border='#0284c7', text_color='#0369a1', fs=7.2)
    ax.annotate('', xy=(x_left + w_full/2, 9.25), xytext=(x_left + w_full/2, 9.14),
                arrowprops=dict(arrowstyle='<->', lw=1.5, color='#0284c7'), zorder=4)
    ax.annotate('', xy=(x_left + w_full/2, 8.86), xytext=(x_left + w_full/2, 8.75),
                arrowprops=dict(arrowstyle='<->', lw=1.5, color='#0284c7'), zorder=4)

    # =========================================================================
    # MIDDLE ROW: TIER 2 (Left) & TIER 3 (Right) SIDE-BY-SIDE
    # =========================================================================
    m_y, m_h = 6.45, 2.30
    w_half = (w_full - 0.70) / 2.0  # 3.50 each

    # TIER 2 (API Gateway & Controller)
    t2_x = x_left
    draw_card(t2_x, m_y, w_half, m_h, c_tier2_bg, c_tier2_border, lw=1.8, rad=0.20)
    ax.text(t2_x + 0.16, m_y + m_h - 0.26,
            'TIER 2: API GATEWAY (FastAPI)',
            fontsize=8.8, weight='bold', color=c_tier2_border, fontfamily='sans-serif', zorder=3)

    draw_card(t2_x + 0.12, m_y + 0.12, w_half - 0.24, m_h - 0.44, c_tier2_sub_bg, c_tier2_sub_bd, lw=1.1, rad=0.12)
    t2_bullets = [
        '• POST /api/predict : Feature vector dispatch',
        '• GET /api/admin/records : Audit log queries',
        '• Pydantic v2 Schema : Strict type validation',
        '• Middleware : CORS, rate limiting & security'
    ]
    for b_idx, b in enumerate(t2_bullets):
        ax.text(t2_x + 0.22, m_y + m_h - 0.60 - b_idx * 0.38, b,
                fontsize=6.8, color='#1e293b', fontfamily='sans-serif', zorder=4)

    # TIER 3 (Privacy Preservation Engine)
    t3_x = x_left + w_half + 0.70
    draw_card(t3_x, m_y, w_half, m_h, c_tier3_bg, c_tier3_border, lw=1.8, rad=0.20)
    ax.text(t3_x + 0.16, m_y + m_h - 0.26,
            'TIER 3: PRIVACY ENGINE (HIPAA)',
            fontsize=8.8, weight='bold', color=c_tier3_border, fontfamily='sans-serif', zorder=3)

    draw_card(t3_x + 0.12, m_y + 0.12, w_half - 0.24, m_h - 0.44, c_tier3_sub_bg, c_tier3_sub_bd, lw=1.1, rad=0.12)
    t3_bullets = [
        '• Cryptographic Tokenizer : SHA-256 (ANON-8F92)',
        '• k-Anonymity Generalizer : 5-Yr Age & BMI',
        '• Zero-Storage Guarantee : Zero PHI on disk',
        '• Ephemeral RAM execution : Anti-forensic'
    ]
    for b_idx, b in enumerate(t3_bullets):
        ax.text(t3_x + 0.22, m_y + m_h - 0.60 - b_idx * 0.38, b,
                fontsize=6.8, color='#1e293b', fontfamily='sans-serif', zorder=4)

    # Badge between Tier 2 & Tier 3
    b_mid_x = t2_x + w_half + 0.35  # exactly center between the two
    draw_badge(b_mid_x, m_y + m_h/2, 0.66, 0.52, 'Sanitized\nPayload\nHand-off',
               bg='#f8fafc', border='#64748b', text_color='#334155', fs=6.2)
    ax.annotate('', xy=(b_mid_x - 0.34, m_y + m_h/2), xytext=(t2_x + w_half, m_y + m_h/2),
                arrowprops=dict(arrowstyle='<->', lw=1.4, color='#64748b'), zorder=4)
    ax.annotate('', xy=(t3_x, m_y + m_h/2), xytext=(b_mid_x + 0.34, m_y + m_h/2),
                arrowprops=dict(arrowstyle='<->', lw=1.4, color='#64748b'), zorder=4)

    # Connectors Middle Row -> Tier 4
    draw_badge(x_left + w_full/2, 6.18, 4.20, 0.28, 'Feature Vectors, ML Predictions & De-Identified Tokens',
               bg='#f3e8ff', border='#9333ea', text_color='#6b21a8', fs=7.0)
    ax.annotate('', xy=(t2_x + w_half/2, 6.45), xytext=(t2_x + w_half/2, 6.32),
                arrowprops=dict(arrowstyle='<->', lw=1.4, color='#9333ea'), zorder=4)
    ax.annotate('', xy=(t3_x + w_half/2, 6.45), xytext=(t3_x + w_half/2, 6.32),
                arrowprops=dict(arrowstyle='->', lw=1.4, color='#e11d48'), zorder=4)
    ax.annotate('', xy=(x_left + w_full/2, 6.04), xytext=(x_left + w_full/2, 5.90),
                arrowprops=dict(arrowstyle='->', lw=1.5, color='#9333ea'), zorder=4)

    # =========================================================================
    # TIER 4: MACHINE LEARNING & EXPLAINABLE AI ENGINE (Full Width Card)
    # =========================================================================
    t4_y, t4_h = 3.35, 2.55
    draw_card(x_left, t4_y, w_full, t4_h, c_tier4_bg, c_tier4_border, lw=2.0, rad=0.22)

    ax.text(x_left + 0.20, t4_y + t4_h - 0.26,
            'TIER 4: MACHINE LEARNING & EXPLAINABLE AI ENGINE (Python 3.11)',
            fontsize=9.6, weight='bold', color=c_tier4_border, fontfamily='sans-serif', zorder=3)

    t4_col_w = (w_full - 0.42) / 2.0  # 3.64 each
    # Sub-card Left: Model specs
    draw_card(x_left + 0.15, t4_y + 0.12, t4_col_w, t4_h - 0.44, c_tier4_sub_bg, c_tier4_sub_bd, lw=1.1, rad=0.12)
    # Title banner
    h_box_ml = patches.FancyBboxPatch(
        (x_left + 0.15, t4_y + t4_h - 0.74), t4_col_w, 0.30,
        boxstyle='round,pad=0.02,rounding_size=0.08',
        facecolor='#f3e8ff', edgecolor='none', zorder=3
    )
    ax.add_patch(h_box_ml)
    ax.text(x_left + 0.15 + t4_col_w/2, t4_y + t4_h - 0.59, 'Gradient Boosted Ensemble & Multi-Disease',
            ha='center', va='center', fontsize=7.4, weight='bold', color='#581c87', fontfamily='sans-serif', zorder=4)

    t4_left_bullets = [
        '• 150 Gradient-Boosted Trees (Depth: 6)',
        '• 99.86% Test Classification Accuracy',
        '• 99.79% Macro F1-Score across 4 classes',
        '• Multi-Disease Estimator: CAD, T2D, HTN %',
        '• Continuous composite risk scoring (0–100)'
    ]
    for b_idx, b in enumerate(t4_left_bullets):
        ax.text(x_left + 0.25, t4_y + t4_h - 0.95 - b_idx * 0.27, b,
                fontsize=6.9, color='#1e293b', fontfamily='sans-serif', zorder=4)

    # Sub-card Right: XAI & Specialist Referral
    draw_card(x_left + 0.15 + t4_col_w + 0.12, t4_y + 0.12, t4_col_w, t4_h - 0.44, c_tier4_sub_bg, c_tier4_sub_bd, lw=1.1, rad=0.12)
    h_box_xai = patches.FancyBboxPatch(
        (x_left + 0.15 + t4_col_w + 0.12, t4_y + t4_h - 0.74), t4_col_w, 0.30,
        boxstyle='round,pad=0.02,rounding_size=0.08',
        facecolor='#f3e8ff', edgecolor='none', zorder=3
    )
    ax.add_patch(h_box_xai)
    ax.text(x_left + 0.15 + t4_col_w + 0.12 + t4_col_w/2, t4_y + t4_h - 0.59, 'TreeSHAP & Critical Specialist Triage',
            ha='center', va='center', fontsize=7.4, weight='bold', color='#581c87', fontfamily='sans-serif', zorder=4)

    t4_right_bullets = [
        '• Computes exact Shapley values (phi_i)',
        '• Ranks top clinical risk & protective drivers',
        '• Completely resolves black-box opacity',
        '• Algorithmic Preventive Guidance Engine',
        '• Critical Single-Specialist Triage Engine'
    ]
    for b_idx, b in enumerate(t4_right_bullets):
        ax.text(x_left + 0.28 + t4_col_w + 0.12, t4_y + t4_h - 0.95 - b_idx * 0.27, b,
                fontsize=6.9, color='#1e293b', fontfamily='sans-serif', zorder=4)

    # Connector Tier 4 -> Tier 5
    draw_badge(x_left + w_full/2, 3.10, 3.90, 0.28, 'CSV Sync, Model Predictions & Clinical Audit Logging',
               bg='#fef3c7', border='#d97706', text_color='#92400e', fs=7.0)
    ax.annotate('', xy=(x_left + w_full/2, 3.35), xytext=(x_left + w_full/2, 3.24),
                arrowprops=dict(arrowstyle='<->', lw=1.5, color='#d97706'), zorder=4)
    ax.annotate('', xy=(x_left + w_full/2, 2.96), xytext=(x_left + w_full/2, 2.85),
                arrowprops=dict(arrowstyle='<->', lw=1.5, color='#d97706'), zorder=4)

    # =========================================================================
    # TIER 5: DATA STORAGE & EXPORT WAREHOUSE (Bottom Card)
    # =========================================================================
    t5_y, t5_h = 0.50, 2.35
    draw_card(x_left, t5_y, w_full, t5_h, c_tier5_bg, c_tier5_border, lw=2.0, rad=0.22)

    ax.text(x_left + 0.20, t5_y + t5_h - 0.26,
            'TIER 5: DATA STORAGE & EXPORT WAREHOUSE',
            fontsize=9.6, weight='bold', color=c_tier5_border, fontfamily='sans-serif', zorder=3)
    ax.text(x_left + 0.20, t5_y + t5_h - 0.46,
            'In-memory RAM data store and clinical research warehouse',
            fontsize=7.3, style='italic', color='#92400e', fontfamily='sans-serif', zorder=3)

    t5_col_w = (w_full - 0.42) / 2.0  # 3.64 each
    # Sub-card Left: Live In-Memory Store
    draw_card(x_left + 0.15, t5_y + 0.12, t5_col_w, t5_h - 0.64, c_tier5_sub_bg, c_tier5_sub_bd, lw=1.1, rad=0.12)
    h_box_store = patches.FancyBboxPatch(
        (x_left + 0.15, t5_y + t5_h - 0.94), t5_col_w, 0.30,
        boxstyle='round,pad=0.02,rounding_size=0.08',
        facecolor='#fef3c7', edgecolor='none', zorder=3
    )
    ax.add_patch(h_box_store)
    ax.text(x_left + 0.15 + t5_col_w/2, t5_y + t5_h - 0.79, 'Live In-Memory Clinical Store',
            ha='center', va='center', fontsize=7.4, weight='bold', color='#78350f', fontfamily='sans-serif', zorder=4)

    t5_left_bullets = [
        '• In-Memory Store (ANONYMIZED_DB_STORE)',
        '• Microsecond Query Latency (<0.01 ms)',
        '• Scalability: 1,000,000+ records in 500 MB',
        '• Ephemeral RAM protection (Zero PHI disk)'
    ]
    for b_idx, b in enumerate(t5_left_bullets):
        ax.text(x_left + 0.25, t5_y + t5_h - 1.15 - b_idx * 0.28, b,
                fontsize=6.9, color='#1e293b', fontfamily='sans-serif', zorder=4)

    # Sub-card Right: Research Warehouse
    draw_card(x_left + 0.15 + t5_col_w + 0.12, t5_y + 0.12, t5_col_w, t5_h - 0.64, c_tier5_sub_bg, c_tier5_sub_bd, lw=1.1, rad=0.12)
    h_box_ware = patches.FancyBboxPatch(
        (x_left + 0.15 + t5_col_w + 0.12, t5_y + t5_h - 0.94), t5_col_w, 0.30,
        boxstyle='round,pad=0.02,rounding_size=0.08',
        facecolor='#fef3c7', edgecolor='none', zorder=3
    )
    ax.add_patch(h_box_ware)
    ax.text(x_left + 0.15 + t5_col_w + 0.12 + t5_col_w/2, t5_y + t5_h - 0.79, 'Clinical Training & Audit Warehouse',
            ha='center', va='center', fontsize=7.4, weight='bold', color='#78350f', fontfamily='sans-serif', zorder=4)

    t5_right_bullets = [
        '• Training Warehouse (healthcare_dataset.csv)',
        '• 3,500 annotated clinical patient profiles',
        '• 1-Click CSV Audit Exporter for research',
        '• Complete longitudinal clinical trace'
    ]
    for b_idx, b in enumerate(t5_right_bullets):
        ax.text(x_left + 0.28 + t5_col_w + 0.12, t5_y + t5_h - 1.15 - b_idx * 0.28, b,
                fontsize=6.9, color='#1e293b', fontfamily='sans-serif', zorder=4)

    ax.set_xlim(0, 8.6)
    ax.set_ylim(0, 12.2)
    plt.tight_layout(pad=0.10)

    save_path = os.path.join(out_dir, 'fig_4_1_system_architecture_vertical.png')
    plt.savefig(save_path, dpi=300, bbox_inches='tight', pad_inches=0.08)

    dl_path = r'C:\Users\arunk\Downloads\fig_4_1_system_architecture_vertical.png'
    plt.savefig(dl_path, dpi=300, bbox_inches='tight', pad_inches=0.08)

    art_path = r'C:\Users\arunk\.gemini\antigravity\brain\87427b1b-8625-473d-acdc-fff8d0537b70\fig_4_1_system_architecture_vertical.png'
    plt.savefig(art_path, dpi=300, bbox_inches='tight', pad_inches=0.08)

    plt.close()
    print('Generated balanced vertical architecture diagram successfully.')

if __name__ == '__main__':
    build_vertical_architecture()
