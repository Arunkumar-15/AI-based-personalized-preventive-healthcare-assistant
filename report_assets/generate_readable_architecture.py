# generate_readable_architecture.py
# Publication-Grade, Ultra-Clear, Highly Readable System Architecture Diagram (Figure 4.1)
# 1. Height is shorter and balanced (10.2" x 10.6" - near square/slightly portrait)
# 2. Large, bold, highly legible typography
# 3. Clean spacing: Zero text overflows, zero border collisions, spacious arrow gaps
# 4. 300 DPI Ultra HD Vector Rendering
import os
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def build_readable_architecture():
    out_dir = r'C:\Users\arunk\Projects\health-assistant\report_assets'
    os.makedirs(out_dir, exist_ok=True)

    # Shorter, perfectly proportioned portrait canvas: 10.2 x 10.6 inches
    # 300 DPI = 3060 x 3180 pixels
    fig, ax = plt.subplots(figsize=(10.2, 10.6), dpi=300)
    ax.axis('off')

    # White canvas background
    canvas_bg = patches.Rectangle((0, 0), 10.2, 10.6, facecolor='#ffffff', edgecolor='none')
    ax.add_patch(canvas_bg)

    # Color Palette - High contrast, accessible, publication standard
    c_tier1_border = '#15803d'  # Emerald / Forest Green
    c_tier1_bg     = '#f0fdf4'
    c_tier1_sub_bg = '#ffffff'
    c_tier1_sub_bd = '#86efac'

    c_tier2_border = '#1d4ed8'  # Cobalt Blue
    c_tier2_bg     = '#eff6ff'
    c_tier2_sub_bg = '#ffffff'
    c_tier2_sub_bd = '#93c5fd'

    c_tier3_border = '#991b1b'  # Crimson Red
    c_tier3_bg     = '#fff1f2'
    c_tier3_sub_bg = '#ffffff'
    c_tier3_sub_bd = '#fca5a5'

    c_tier4_border = '#7e22ce'  # Indigo Purple
    c_tier4_bg     = '#faf5ff'
    c_tier4_sub_bg = '#ffffff'
    c_tier4_sub_bd = '#d8b4fe'

    c_tier5_border = '#b45309'  # Warm Amber / Gold
    c_tier5_bg     = '#fffbeb'
    c_tier5_sub_bg = '#ffffff'
    c_tier5_sub_bd = '#fcd34d'

    def draw_card(x, y, w, h, bg_color, border_color, lw=2.0, rad=0.20):
        shadow = patches.FancyBboxPatch(
            (x + 0.025, y - 0.025), w, h,
            boxstyle=f'round,pad=0.04,rounding_size={rad}',
            facecolor='#cbd5e1', edgecolor='none', zorder=1
        )
        ax.add_patch(shadow)
        card = patches.FancyBboxPatch(
            (x, y), w, h,
            boxstyle=f'round,pad=0.04,rounding_size={rad}',
            facecolor=bg_color, edgecolor=border_color, linewidth=lw, zorder=2
        )
        ax.add_patch(card)

    def draw_badge(x, y, w, h, text, bg='#e0f2fe', border='#0284c7', text_color='#0369a1', fs=8.3, lw=1.2):
        badge = patches.FancyBboxPatch(
            (x - w/2, y - h/2), w, h,
            boxstyle='round,pad=0.03,rounding_size=0.10',
            facecolor=bg, edgecolor=border, linewidth=lw, zorder=5
        )
        ax.add_patch(badge)
        ax.text(x, y, text, ha='center', va='center', fontsize=fs, weight='bold',
                color=text_color, fontfamily='sans-serif', zorder=6, linespacing=1.2)

    x_left = 0.40
    w_full = 9.40

    # =========================================================================
    # TIER 1: CLIENT PRESENTATION & USER INTERACTION LAYER (Top Full-Width Card)
    # =========================================================================
    t1_y, t1_h = 7.70, 2.55
    draw_card(x_left, t1_y, w_full, t1_h, c_tier1_bg, c_tier1_border, lw=2.2, rad=0.24)

    # Title & Subtitle
    ax.text(x_left + 0.22, t1_y + t1_h - 0.28,
            'TIER 1: CLIENT PRESENTATION & USER INTERACTION LAYER (React 18 + Vite)',
            fontsize=11.0, weight='bold', color=c_tier1_border, fontfamily='sans-serif', zorder=3)
    ax.text(x_left + 0.22, t1_y + t1_h - 0.50,
            'Responsive Single Page Application (SPA) hosting multimodal screening, digital twin simulations & bilingual controls',
            fontsize=8.3, style='italic', color='#166534', fontfamily='sans-serif', zorder=3)

    # 4 Inner Columns in Tier 1
    col_w = (w_full - 0.32 - 3 * 0.12) / 4.0  # ~2.18 each
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
                '• 1-Click official PDF report'
            ]
        }
    ]

    for idx, col in enumerate(t1_cols):
        cx = x_left + 0.16 + idx * (col_w + 0.12)
        cy = t1_y + 0.12
        ch = 1.80
        draw_card(cx, cy, col_w, ch, c_tier1_sub_bg, c_tier1_sub_bd, lw=1.2, rad=0.14)
        h_box = patches.FancyBboxPatch(
            (cx, cy + ch - 0.34), col_w, 0.34,
            boxstyle='round,pad=0.02,rounding_size=0.08',
            facecolor='#e2e8f0', edgecolor='none', zorder=3
        )
        ax.add_patch(h_box)
        ax.text(cx + col_w/2, cy + ch - 0.17, col['title'],
                ha='center', va='center', fontsize=8.6, weight='bold', color='#0f2b5c', fontfamily='sans-serif', zorder=4)
        for b_idx, b in enumerate(col['bullets']):
            ax.text(cx + 0.08, cy + 1.18 - b_idx * 0.31, b,
                    fontsize=8.0, color='#0f172a', fontfamily='sans-serif', zorder=4)

    # Connector Tier 1 -> Tier 2
    draw_badge(2.45, 7.42, 4.00, 0.32, 'JSON / REST HTTP Requests & Responses',
               bg='#e0f2fe', border='#0284c7', text_color='#0369a1', fs=8.3)
    ax.annotate('', xy=(2.45, 7.70), xytext=(2.45, 7.58),
                arrowprops=dict(arrowstyle='<->', lw=1.8, color='#0284c7'), zorder=4)
    ax.annotate('', xy=(2.45, 7.26), xytext=(2.45, 7.12),
                arrowprops=dict(arrowstyle='<->', lw=1.8, color='#0284c7'), zorder=4)

    # =========================================================================
    # MIDDLE ROW: TIER 2 (Left) & TIER 3 (Right)
    # =========================================================================
    m_y, m_h = 4.65, 2.45
    w_m_card = 4.05  # each card

    # TIER 2: API Gateway & Controller (from x=0.40 to 4.45)
    t2_x = x_left
    draw_card(t2_x, m_y, w_m_card, m_h, c_tier2_bg, c_tier2_border, lw=2.0, rad=0.22)
    ax.text(t2_x + 0.18, m_y + m_h - 0.30,
            'TIER 2: API GATEWAY & CONTROLLER (FastAPI)',
            fontsize=9.4, weight='bold', color=c_tier2_border, fontfamily='sans-serif', zorder=3)

    draw_card(t2_x + 0.14, m_y + 0.12, w_m_card - 0.28, m_h - 0.48, c_tier2_sub_bg, c_tier2_sub_bd, lw=1.2, rad=0.14)
    t2_bullets = [
        '• POST /api/predict : Feature vector dispatch',
        '• GET /api/admin/records : Audit log queries',
        '• Pydantic v2 Schema : Strict type validation',
        '• Security Middleware : CORS, rate limits & errors'
    ]
    for b_idx, b in enumerate(t2_bullets):
        ax.text(t2_x + 0.22, m_y + m_h - 0.68 - b_idx * 0.38, b,
                fontsize=8.0, color='#0f172a', fontfamily='sans-serif', zorder=4)

    # TIER 3: Privacy Preservation Engine (from x=5.75 to 9.80)
    t3_x = x_left + w_m_card + 1.30  # 0.40 + 4.05 + 1.30 = 5.75
    draw_card(t3_x, m_y, w_m_card, m_h, c_tier3_bg, c_tier3_border, lw=2.0, rad=0.22)
    ax.text(t3_x + 0.18, m_y + m_h - 0.30,
            'TIER 3: PRIVACY ENGINE (HIPAA Safe Harbor)',
            fontsize=9.4, weight='bold', color=c_tier3_border, fontfamily='sans-serif', zorder=3)

    draw_card(t3_x + 0.14, m_y + 0.12, w_m_card - 0.28, m_h - 0.48, c_tier3_sub_bg, c_tier3_sub_bd, lw=1.2, rad=0.14)
    t3_bullets = [
        '• Cryptographic Tokenizer : SHA-256 (ANON-8F92)',
        '• k-Anonymity : 5-Yr Age & WHO BMI Brackets',
        '• Zero-Storage Guarantee : Zero PHI on disk',
        '• Ephemeral RAM Execution : Prevents forensics'
    ]
    for b_idx, b in enumerate(t3_bullets):
        ax.text(t3_x + 0.22, m_y + m_h - 0.68 - b_idx * 0.38, b,
                fontsize=8.0, color='#0f172a', fontfamily='sans-serif', zorder=4)

    # Bridge Badge cleanly centered in the 1.30 wide gap (x=4.45 to 5.75)
    b_mid_x = ( (t2_x + w_m_card) + t3_x ) / 2.0  # (4.45 + 5.75)/2 = 5.10
    draw_badge(b_mid_x, m_y + m_h/2, 0.82, 0.58, 'Direct Sanitized\nPayload Hand-off',
               bg='#f8fafc', border='#64748b', text_color='#334155', fs=7.3)
    # Visible, clear arrows connecting to Tier 2 and Tier 3 with plenty of room
    ax.annotate('', xy=(b_mid_x - 0.43, m_y + m_h/2), xytext=(t2_x + w_m_card, m_y + m_h/2),
                arrowprops=dict(arrowstyle='<->', lw=1.6, color='#64748b'), zorder=4)
    ax.annotate('', xy=(t3_x, m_y + m_h/2), xytext=(b_mid_x + 0.43, m_y + m_h/2),
                arrowprops=dict(arrowstyle='<->', lw=1.6, color='#64748b'), zorder=4)

    # =========================================================================
    # CONNECTORS: Middle Row -> Bottom Row
    # =========================================================================
    # Below Tier 2 -> Tier 4
    draw_badge(2.45, 4.38, 3.80, 0.32, 'Feature Vectors & ML Predictions',
               bg='#f3e8ff', border='#9333ea', text_color='#6b21a8', fs=8.2)
    ax.annotate('', xy=(2.45, 4.65), xytext=(2.45, 4.54),
                arrowprops=dict(arrowstyle='<->', lw=1.8, color='#9333ea'), zorder=4)
    ax.annotate('', xy=(2.45, 4.22), xytext=(2.45, 4.08),
                arrowprops=dict(arrowstyle='<->', lw=1.8, color='#9333ea'), zorder=4)

    # Below Tier 3 -> Tier 5
    draw_badge(7.75, 4.38, 3.50, 0.32, 'Anonymized Tokens (Zero PHI)',
               bg='#ffe4e6', border='#e11d48', text_color='#9f1239', fs=8.2)
    ax.annotate('', xy=(7.75, 4.65), xytext=(7.75, 4.54),
                arrowprops=dict(arrowstyle='->', lw=1.8, color='#e11d48'), zorder=4)
    ax.annotate('', xy=(7.75, 4.22), xytext=(7.75, 4.08),
                arrowprops=dict(arrowstyle='->', lw=1.8, color='#e11d48'), zorder=4)

    # =========================================================================
    # BOTTOM ROW: TIER 4 (Left) & TIER 5 (Right)
    # =========================================================================
    b_y, b_h = 0.45, 3.60

    # TIER 4: Machine Learning & Explainable AI Engine (from x=0.40 to 5.75, width 5.35)
    t4_x, t4_w = x_left, 5.35
    draw_card(t4_x, b_y, t4_w, b_h, c_tier4_bg, c_tier4_border, lw=2.2, rad=0.24)
    ax.text(t4_x + 0.18, b_y + b_h - 0.30,
            'TIER 4: MACHINE LEARNING & EXPLAINABLE AI (Python 3.11)',
            fontsize=9.6, weight='bold', color=c_tier4_border, fontfamily='sans-serif', zorder=3)

    t4_col_w = (t4_w - 0.40) / 2.0  # 2.47 each
    # Sub-card Left: Model specs
    draw_card(t4_x + 0.14, b_y + 0.14, t4_col_w, b_h - 0.52, c_tier4_sub_bg, c_tier4_sub_bd, lw=1.2, rad=0.14)
    h_box_ml = patches.FancyBboxPatch(
        (t4_x + 0.14, b_y + b_h - 0.88), t4_col_w, 0.34,
        boxstyle='round,pad=0.02,rounding_size=0.08',
        facecolor='#f3e8ff', edgecolor='none', zorder=3
    )
    ax.add_patch(h_box_ml)
    ax.text(t4_x + 0.14 + t4_col_w/2, b_y + b_h - 0.71, 'Gradient Boosted Trees & Metrics',
            ha='center', va='center', fontsize=8.0, weight='bold', color='#581c87', fontfamily='sans-serif', zorder=4)

    t4_left_bullets = [
        '• 150 Boosted Trees (Depth: 6)',
        '• 99.86% Test Classification Acc.',
        '• 99.79% Macro F1 across 4 classes',
        '• Multi-Disease: CAD, T2D, HTN %',
        '• Continuous composite risk (0–100)'
    ]
    for b_idx, b in enumerate(t4_left_bullets):
        ax.text(t4_x + 0.20, b_y + b_h - 1.15 - b_idx * 0.44, b,
                fontsize=7.8, color='#0f172a', fontfamily='sans-serif', zorder=4)

    # Sub-card Right: XAI & Specialist Referral
    draw_card(t4_x + 0.14 + t4_col_w + 0.12, b_y + 0.14, t4_col_w, b_h - 0.52, c_tier4_sub_bg, c_tier4_sub_bd, lw=1.2, rad=0.14)
    h_box_xai = patches.FancyBboxPatch(
        (t4_x + 0.14 + t4_col_w + 0.12, b_y + b_h - 0.88), t4_col_w, 0.34,
        boxstyle='round,pad=0.02,rounding_size=0.08',
        facecolor='#f3e8ff', edgecolor='none', zorder=3
    )
    ax.add_patch(h_box_xai)
    ax.text(t4_x + 0.14 + t4_col_w + 0.12 + t4_col_w/2, b_y + b_h - 0.71, 'TreeSHAP & Specialist Triage',
            ha='center', va='center', fontsize=8.0, weight='bold', color='#581c87', fontfamily='sans-serif', zorder=4)

    t4_right_bullets = [
        '• TreeSHAP: Exact Shapley values (phi)',
        '• Ranks top clinical risk & drivers',
        '• Resolves black-box opacity',
        '• Algorithmic Preventive Guidance',
        '• Critical Single-Specialist Triage'
    ]
    for b_idx, b in enumerate(t4_right_bullets):
        ax.text(t4_x + 0.22 + t4_col_w + 0.12, b_y + b_h - 1.15 - b_idx * 0.44, b,
                fontsize=7.8, color='#0f172a', fontfamily='sans-serif', zorder=4)

    # TIER 5: Data Storage & Warehouse (from x=6.80 to 9.80, width 3.00)
    t5_x, t5_w = x_left + t4_w + 1.05, 3.00  # 0.40 + 5.35 + 1.05 = 6.80
    draw_card(t5_x, b_y, t5_w, b_h, c_tier5_bg, c_tier5_border, lw=2.2, rad=0.24)
    ax.text(t5_x + 0.16, b_y + b_h - 0.30,
            'TIER 5: STORAGE & WAREHOUSE',
            fontsize=9.2, weight='bold', color=c_tier5_border, fontfamily='sans-serif', zorder=3)
    ax.text(t5_x + 0.16, b_y + b_h - 0.52,
            'In-memory RAM & clinical dataset',
            fontsize=7.6, style='italic', color='#92400e', fontfamily='sans-serif', zorder=3)

    draw_card(t5_x + 0.12, b_y + 0.14, t5_w - 0.24, b_h - 0.74, c_tier5_sub_bg, c_tier5_sub_bd, lw=1.2, rad=0.14)
    t5_bullets = [
        '• Live In-Memory Clinical Store',
        '  (ANONYMIZED_DB_STORE in RAM)',
        '• Microsecond Latency (<0.01 ms)',
        '• Holds 1,000,000+ records in 500 MB',
        '• Training Warehouse: 3,500 rows',
        '  (healthcare_dataset.csv)',
        '• 1-Click CSV Audit Exporter'
    ]
    for b_idx, b in enumerate(t5_bullets):
        ax.text(t5_x + 0.18, b_y + b_h - 0.98 - b_idx * 0.36, b,
                fontsize=7.8, color='#0f172a', fontfamily='sans-serif', zorder=4)

    # Bridge Badge cleanly centered in the 1.05 wide gap (x=5.75 to 6.80)
    b_bot_x = ( (t4_x + t4_w) + t5_x ) / 2.0  # (5.75 + 6.80)/2 = 6.275
    draw_badge(b_bot_x, b_y + b_h/2, 0.68, 0.54, 'CSV Sync /\nAudit Data',
               bg='#fef3c7', border='#d97706', text_color='#92400e', fs=7.3)
    ax.annotate('', xy=(b_bot_x - 0.36, b_y + b_h/2), xytext=(t4_x + t4_w, b_y + b_h/2),
                arrowprops=dict(arrowstyle='<->', lw=1.6, color='#d97706'), zorder=4)
    ax.annotate('', xy=(t5_x, b_y + b_h/2), xytext=(b_bot_x + 0.36, b_y + b_h/2),
                arrowprops=dict(arrowstyle='<->', lw=1.6, color='#d97706'), zorder=4)

    ax.set_xlim(0, 10.2)
    ax.set_ylim(0, 10.6)
    plt.tight_layout(pad=0.10)

    save_path = os.path.join(out_dir, 'fig_4_1_system_architecture_clear.png')
    plt.savefig(save_path, dpi=300, bbox_inches='tight', pad_inches=0.08)

    dl_path = r'C:\Users\arunk\Downloads\fig_4_1_system_architecture_clear.png'
    plt.savefig(dl_path, dpi=300, bbox_inches='tight', pad_inches=0.08)

    art_path = r'C:\Users\arunk\.gemini\antigravity\brain\87427b1b-8625-473d-acdc-fff8d0537b70\fig_4_1_system_architecture_clear.png'
    plt.savefig(art_path, dpi=300, bbox_inches='tight', pad_inches=0.08)

    plt.close()
    print('Generated perfectly readable architecture diagram successfully.')

if __name__ == '__main__':
    build_readable_architecture()
