# generate_crisp_architecture.py
# High-Resolution (300 DPI), Crisp, De-blurred, and Shorter Aspect Ratio System Architecture Diagram
import os
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def build_crisp_architecture():
    out_dir = r'C:\Users\arunk\Projects\health-assistant\report_assets'
    os.makedirs(out_dir, exist_ok=True)

    # Balanced, compact widescreen canvas: 15.0 x 9.5 inches (300 DPI = 4500 x 2850 px)
    fig, ax = plt.subplots(figsize=(15.0, 9.5), dpi=300)
    ax.axis('off')

    # Background canvas
    canvas_bg = patches.Rectangle((0, 0), 15.0, 9.5, facecolor='#ffffff', edgecolor='none')
    ax.add_patch(canvas_bg)

    # Color Palette - Clean, Modern Medical Design
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

    def draw_card(x, y, w, h, bg_color, border_color, lw=2.0, rad=0.22):
        # Drop shadow for clean depth
        shadow = patches.FancyBboxPatch(
            (x + 0.035, y - 0.035), w, h,
            boxstyle=f'round,pad=0.06,rounding_size={rad}',
            facecolor='#e2e8f0', edgecolor='none', zorder=1
        )
        ax.add_patch(shadow)
        
        card = patches.FancyBboxPatch(
            (x, y), w, h,
            boxstyle=f'round,pad=0.06,rounding_size={rad}',
            facecolor=bg_color, edgecolor=border_color, linewidth=lw, zorder=2
        )
        ax.add_patch(card)

    def draw_badge(x, y, w, h, text, bg='#e0f2fe', border='#0284c7', text_color='#0369a1', fs=8.2, lw=1.2):
        badge = patches.FancyBboxPatch(
            (x - w/2, y - h/2), w, h,
            boxstyle='round,pad=0.04,rounding_size=0.12',
            facecolor=bg, edgecolor=border, linewidth=lw, zorder=5
        )
        ax.add_patch(badge)
        ax.text(x, y, text, ha='center', va='center', fontsize=fs, weight='bold',
                color=text_color, fontfamily='sans-serif', zorder=6, linespacing=1.2)

    # =========================================================================
    # TIER 1: CLIENT PRESENTATION & USER INTERACTION LAYER (Full Width Top Card)
    # =========================================================================
    t1_x, t1_y, t1_w, t1_h = 0.5, 6.45, 14.0, 2.75
    draw_card(t1_x, t1_y, t1_w, t1_h, c_tier1_bg, c_tier1_border, lw=2.2, rad=0.28)

    # Title & Subtitle
    ax.text(t1_x + 0.35, t1_y + t1_h - 0.34,
            'TIER 1: CLIENT PRESENTATION & USER INTERACTION LAYER (React 18 + Vite)',
            fontsize=12.0, weight='bold', color=c_tier1_border, fontfamily='sans-serif', zorder=3)
    ax.text(t1_x + 0.35, t1_y + t1_h - 0.58,
            'Responsive Single Page Application (SPA) hosting multimodal screening, digital twin simulations, and bilingual controls',
            fontsize=8.8, style='italic', color='#166534', fontfamily='sans-serif', zorder=3)

    # 4 Inner Columns in Tier 1
    t1_cols = [
        {
            'x': 0.72, 'w': 3.18,
            'title': 'Multi-Modal Ingestion',
            'bullets': [
                '• Mode 1: Lifestyle & Symptom Form',
                '• Mode 2: Clinical Lab Biomarkers',
                '• Mode 3: Medical Report OCR Upload',
                '• Automated field parsing & validation'
            ]
        },
        {
            'x': 4.14, 'w': 3.18,
            'title': 'Diagnostic Dashboard',
            'bullets': [
                '• 4-Class Severity Badge (Low–Critical)',
                '• Multi-Disease Risk (CAD, T2D, HTN)',
                '• TreeSHAP Feature Waterfall Plot',
                '• Evidence-based clinical guidance'
            ]
        },
        {
            'x': 7.56, 'w': 3.18,
            'title': 'Health Digital Twin',
            'bullets': [
                '• Interactive sensitivity sliders',
                '• Weight (±15 kg), sleep & exercise',
                '• Quit smoking (+16.5% protection)',
                '• Real-time risk reduction calculation'
            ]
        },
        {
            'x': 10.98, 'w': 3.28,
            'title': 'Admin Portal & Reports',
            'bullets': [
                '• Bilingual Engine (English & Tamil)',
                '• Live de-identified database view',
                '• Risk severity filtering & search',
                '• 1-Click official PDF clinical report'
            ]
        }
    ]

    for col in t1_cols:
        draw_card(col['x'], 6.58, col['w'], 1.95, c_tier1_sub_bg, c_tier1_sub_bd, lw=1.2, rad=0.16)
        # Header banner inside sub-card
        h_box = patches.FancyBboxPatch(
            (col['x'], 6.58 + 1.95 - 0.38), col['w'], 0.38,
            boxstyle='round,pad=0.03,rounding_size=0.10',
            facecolor='#e2e8f0', edgecolor='none', zorder=3
        )
        ax.add_patch(h_box)
        ax.text(col['x'] + col['w']/2, 6.58 + 1.95 - 0.19, col['title'],
                ha='center', va='center', fontsize=9.4, weight='bold', color='#0f2b5c', fontfamily='sans-serif', zorder=4)
        
        # Bullets
        for b_idx, bullet in enumerate(col['bullets']):
            ax.text(col['x'] + 0.15, 6.58 + 1.30 - b_idx * 0.32, bullet,
                    fontsize=8.3, color='#1e293b', fontfamily='sans-serif', zorder=4)

    # Connector between Tier 1 and Tier 2
    draw_badge(3.60, 6.10, 4.30, 0.35, 'JSON / REST HTTP Requests & Responses',
               bg='#e0f2fe', border='#0284c7', text_color='#0369a1', fs=8.5)
    # Up/Down Arrows
    ax.annotate('', xy=(3.60, 6.45), xytext=(3.60, 6.30),
                arrowprops=dict(arrowstyle='<->', lw=1.8, color='#0284c7'), zorder=4)
    ax.annotate('', xy=(3.60, 5.90), xytext=(3.60, 5.75),
                arrowprops=dict(arrowstyle='<->', lw=1.8, color='#0284c7'), zorder=4)

    # =========================================================================
    # MIDDLE ROW: TIER 2 (Left) & TIER 3 (Right)
    # =========================================================================
    m_y = 3.60
    m_h = 2.15

    # TIER 2 (FastAPI Gateway)
    t2_x, t2_w = 0.50, 6.20
    draw_card(t2_x, m_y, t2_w, m_h, c_tier2_bg, c_tier2_border, lw=2.0, rad=0.24)
    ax.text(t2_x + 0.30, m_y + m_h - 0.34,
            'TIER 2: API GATEWAY & CONTROLLER (FastAPI + ASGI Uvicorn)',
            fontsize=10.6, weight='bold', color=c_tier2_border, fontfamily='sans-serif', zorder=3)

    draw_card(t2_x + 0.20, m_y + 0.18, t2_w - 0.40, m_h - 0.66, c_tier2_sub_bg, c_tier2_sub_bd, lw=1.2, rad=0.14)
    t2_bullets = [
        '• POST /api/predict : Dispatches feature vectors to ML & XAI pipelines',
        '• GET /api/admin/records : Serves anonymized records for clinical audit',
        '• Pydantic v2 Schema Enforcement : Strict type checking & input validation',
        '• Security & Middleware : CORS handling, rate limiting & error handling'
    ]
    for b_idx, b in enumerate(t2_bullets):
        ax.text(t2_x + 0.36, m_y + m_h - 0.74 - b_idx * 0.33, b,
                fontsize=8.3, color='#1e293b', fontfamily='sans-serif', zorder=4)

    # TIER 3 (HIPAA Privacy)
    t3_x, t3_w = 8.30, 6.20
    draw_card(t3_x, m_y, t3_w, m_h, c_tier3_bg, c_tier3_border, lw=2.0, rad=0.24)
    ax.text(t3_x + 0.30, m_y + m_h - 0.34,
            'TIER 3: PRIVACY PRESERVATION ENGINE (HIPAA Safe Harbor)',
            fontsize=10.6, weight='bold', color=c_tier3_border, fontfamily='sans-serif', zorder=3)

    draw_card(t3_x + 0.20, m_y + 0.18, t3_w - 0.40, m_h - 0.66, c_tier3_sub_bg, c_tier3_sub_bd, lw=1.2, rad=0.14)
    t3_bullets = [
        '• Cryptographic Tokenizer : Non-reversible SHA-256 (e.g. ANON-8F92-4C1B)',
        '• k-Anonymity Generalizer : 5-Year Age Brackets & WHO BMI Categories',
        '• Zero-Storage Guarantee : Zero persistent Protected Health Info (PHI) on disk',
        '• Ephemeral RAM-bound execution preventing unauthorized forensic recovery'
    ]
    for b_idx, b in enumerate(t3_bullets):
        ax.text(t3_x + 0.36, m_y + m_h - 0.74 - b_idx * 0.33, b,
                fontsize=8.3, color='#1e293b', fontfamily='sans-serif', zorder=4)

    # Bridge Badge cleanly in the 1.60 wide gap between Tier 2 (end: 6.70) & Tier 3 (start: 8.30)
    badge_mid_x = 7.50
    draw_badge(badge_mid_x, m_y + m_h/2, 1.12, 0.56, 'Direct Sanitized\nPayload Hand-off',
               bg='#f8fafc', border='#64748b', text_color='#334155', fs=7.3)
    # Clear, visible arrows connecting Tier 2 and Tier 3
    ax.annotate('', xy=(badge_mid_x - 0.58, m_y + m_h/2), xytext=(6.70, m_y + m_h/2),
                arrowprops=dict(arrowstyle='<->', lw=1.8, color='#64748b'), zorder=4)
    ax.annotate('', xy=(8.30, m_y + m_h/2), xytext=(badge_mid_x + 0.58, m_y + m_h/2),
                arrowprops=dict(arrowstyle='<->', lw=1.8, color='#64748b'), zorder=4)

    # =========================================================================
    # CONNECTORS: Middle to Bottom
    # =========================================================================
    # Below Tier 2 -> Tier 4
    draw_badge(3.60, 3.20, 3.80, 0.34, 'Feature Vectors & ML Predictions',
               bg='#f3e8ff', border='#9333ea', text_color='#6b21a8', fs=8.2)
    ax.annotate('', xy=(3.60, 3.60), xytext=(3.60, 3.39),
                arrowprops=dict(arrowstyle='<->', lw=1.8, color='#9333ea'), zorder=4)
    ax.annotate('', xy=(3.60, 3.01), xytext=(3.60, 2.80),
                arrowprops=dict(arrowstyle='<->', lw=1.8, color='#9333ea'), zorder=4)

    # Below Tier 3 -> Tier 5
    draw_badge(11.40, 3.20, 3.50, 0.34, 'Anonymized Tokens (Zero PHI)',
               bg='#ffe4e6', border='#e11d48', text_color='#9f1239', fs=8.2)
    ax.annotate('', xy=(11.40, 3.60), xytext=(11.40, 3.39),
                arrowprops=dict(arrowstyle='->', lw=1.8, color='#e11d48'), zorder=4)
    ax.annotate('', xy=(11.40, 3.01), xytext=(11.40, 2.80),
                arrowprops=dict(arrowstyle='->', lw=1.8, color='#e11d48'), zorder=4)

    # =========================================================================
    # BOTTOM ROW: TIER 4 (Left) & TIER 5 (Right)
    # =========================================================================
    b_y = 0.40
    b_h = 2.40

    # TIER 4 (Machine Learning & XAI Engine)
    t4_x, t4_w = 0.50, 7.10
    draw_card(t4_x, b_y, t4_w, b_h, c_tier4_bg, c_tier4_border, lw=2.0, rad=0.24)
    ax.text(t4_x + 0.30, b_y + b_h - 0.34,
            'TIER 4: MACHINE LEARNING & EXPLAINABLE AI ENGINE (Python 3.11)',
            fontsize=10.6, weight='bold', color=c_tier4_border, fontfamily='sans-serif', zorder=3)

    # Two inner cards in Tier 4
    draw_card(t4_x + 0.18, b_y + 0.16, 3.28, b_h - 0.64, c_tier4_sub_bg, c_tier4_sub_bd, lw=1.2, rad=0.14)
    t4_left_bullets = [
        '• 150 Gradient-Boosted Trees (Depth: 6)',
        '• 99.86% Test Classification Accuracy',
        '• 99.79% Macro F1-Score across 4 classes',
        '• Multi-Disease Estimator: CAD, T2D, HTN %',
        '• Continuous composite risk scoring (0–100)'
    ]
    for b_idx, b in enumerate(t4_left_bullets):
        ax.text(t4_x + 0.30, b_y + b_h - 0.72 - b_idx * 0.32, b,
                fontsize=8.1, color='#1e293b', fontfamily='sans-serif', zorder=4)

    draw_card(t4_x + 3.64, b_y + 0.16, 3.28, b_h - 0.64, c_tier4_sub_bg, c_tier4_sub_bd, lw=1.2, rad=0.14)
    t4_right_bullets = [
        '• Computes exact Shapley values (phi_i)',
        '• Ranks top clinical risk & protective drivers',
        '• Completely resolves black-box opacity',
        '• Algorithmic Preventive Guidance Engine',
        '• Critical Single-Specialist Triage Engine'
    ]
    for b_idx, b in enumerate(t4_right_bullets):
        ax.text(t4_x + 3.76, b_y + b_h - 0.72 - b_idx * 0.32, b,
                fontsize=8.1, color='#1e293b', fontfamily='sans-serif', zorder=4)

    # TIER 5 (Data Storage & Warehouse)
    t5_x, t5_w = 9.10, 5.40
    draw_card(t5_x, b_y, t5_w, b_h, c_tier5_bg, c_tier5_border, lw=2.0, rad=0.24)
    ax.text(t5_x + 0.30, b_y + b_h - 0.34,
            'TIER 5: DATA STORAGE & EXPORT WAREHOUSE',
            fontsize=10.6, weight='bold', color=c_tier5_border, fontfamily='sans-serif', zorder=3)
    ax.text(t5_x + 0.30, b_y + b_h - 0.58,
            'In-memory RAM data store and clinical research warehouse',
            fontsize=8.2, style='italic', color='#92400e', fontfamily='sans-serif', zorder=3)

    draw_card(t5_x + 0.20, b_y + 0.16, t5_w - 0.40, b_h - 0.86, c_tier5_sub_bg, c_tier5_sub_bd, lw=1.2, rad=0.14)
    t5_bullets = [
        '• Live In-Memory Store (ANONYMIZED_DB_STORE)',
        '• Microsecond Query Latency (<0.01 ms response)',
        '• High Scalability: Holds 1,000,000+ records in 500 MB',
        '• Training Warehouse (healthcare_dataset.csv, 3,500 rows)',
        '• 1-Click CSV Audit Exporter for medical research'
    ]
    for b_idx, b in enumerate(t5_bullets):
        ax.text(t5_x + 0.34, b_y + b_h - 0.94 - b_idx * 0.30, b,
                fontsize=8.1, color='#1e293b', fontfamily='sans-serif', zorder=4)

    # Bridge Badge cleanly in the 1.50 wide gap between Tier 4 (end: 7.60) & Tier 5 (start: 9.10)
    badge_bot_x = 8.35
    draw_badge(badge_bot_x, b_y + b_h/2, 0.98, 0.52, 'CSV Sync /\nAudit Data',
               bg='#fef3c7', border='#d97706', text_color='#92400e', fs=7.3)
    # Clear, visible arrows connecting Tier 4 and Tier 5
    ax.annotate('', xy=(badge_bot_x - 0.51, b_y + b_h/2), xytext=(7.60, b_y + b_h/2),
                arrowprops=dict(arrowstyle='<->', lw=1.8, color='#d97706'), zorder=4)
    ax.annotate('', xy=(9.10, b_y + b_h/2), xytext=(badge_bot_x + 0.51, b_y + b_h/2),
                arrowprops=dict(arrowstyle='<->', lw=1.8, color='#d97706'), zorder=4)

    ax.set_xlim(0, 15.0)
    ax.set_ylim(0, 9.5)
    plt.tight_layout(pad=0.15)

    save_path = os.path.join(out_dir, 'fig_4_1_system_architecture_hd.png')
    plt.savefig(save_path, dpi=300, bbox_inches='tight', pad_inches=0.08)
    
    # Also save standard name
    std_path = os.path.join(out_dir, 'fig_4_1_system_architecture.png')
    plt.savefig(std_path, dpi=300, bbox_inches='tight', pad_inches=0.08)
    
    # Also save to downloads & artifacts
    dl_path = r'C:\Users\arunk\Downloads\fig_4_1_system_architecture_hd.png'
    plt.savefig(dl_path, dpi=300, bbox_inches='tight', pad_inches=0.08)

    art_path = r'C:\Users\arunk\.gemini\antigravity\brain\87427b1b-8625-473d-acdc-fff8d0537b70\fig_4_1_system_architecture_hd.png'
    plt.savefig(art_path, dpi=300, bbox_inches='tight', pad_inches=0.08)

    plt.close()
    print('Generated crisp HD architecture diagram successfully.')

if __name__ == '__main__':
    build_crisp_architecture()
