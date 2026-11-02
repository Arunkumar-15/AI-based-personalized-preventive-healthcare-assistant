# generate_workflow_pipeline.py
# High-Resolution (300 DPI), Publication-Grade 7-Step Clinical Workflow & Processing Pipeline Diagram
# (Figure 4.2: End-to-End Clinical Data Flow / Processing Pipeline)
import os
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def build_workflow_pipeline():
    out_dir = r'C:\Users\arunk\Projects\health-assistant\report_assets'
    os.makedirs(out_dir, exist_ok=True)

    # Balanced canvas: 12.0 x 13.0 inches (300 DPI = 3600 x 3900 pixels)
    fig, ax = plt.subplots(figsize=(12.0, 13.0), dpi=300)
    ax.axis('off')

    # White canvas background
    canvas_bg = patches.Rectangle((0, 0), 12.0, 13.0, facecolor='#ffffff', edgecolor='none')
    ax.add_patch(canvas_bg)

    # Professional Medical Color Palette
    c1_border = '#0284c7'  # Sky / Cobalt
    c1_bg     = '#f0f9ff'
    c1_badge  = '#0369a1'
    c1_text   = '#0c4a6e'

    c2_border = '#16a34a'  # Mint Green
    c2_bg     = '#f0fdf4'
    c2_badge  = '#15803d'
    c2_text   = '#14532d'

    c3_border = '#9333ea'  # Purple
    c3_bg     = '#faf5ff'
    c3_badge  = '#7e22ce'
    c3_text   = '#581c87'

    c4_border = '#d97706'  # Amber / Warm Gold
    c4_bg     = '#fffbeb'
    c4_badge  = '#b45309'
    c4_text   = '#78350f'

    c5_border = '#e11d48'  # Rose / Coral
    c5_bg     = '#fff1f2'
    c5_badge  = '#be123c'
    c5_text   = '#881337'

    c6_border = '#0d9488'  # Teal / Cyan
    c6_bg     = '#f0fdfa'
    c6_badge  = '#0f766e'
    c6_text   = '#134e4a'

    c7_border = '#64748b'  # Slate / Navy
    c7_bg     = '#f8fafc'
    c7_badge  = '#334155'
    c7_text   = '#0f172a'

    def draw_card(x, y, w, h, bg_color, border_color, lw=2.0, rad=0.22):
        shadow = patches.FancyBboxPatch(
            (x + 0.035, y - 0.035), w, h,
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

    def draw_num_badge(x, y, num_str, bg_color):
        w, h = 0.38, 0.38
        badge = patches.FancyBboxPatch(
            (x, y), w, h,
            boxstyle='round,pad=0.02,rounding_size=0.10',
            facecolor=bg_color, edgecolor='none', zorder=4
        )
        ax.add_patch(badge)
        ax.text(x + w/2, y + h/2, num_str, ha='center', va='center',
                fontsize=11.0, weight='bold', color='#ffffff', fontfamily='sans-serif', zorder=5)

    def draw_pill_badge(x, y, w, h, text, bg='#ffffff', border='#64748b', text_color='#334155', fs=7.5, lw=1.2):
        badge = patches.FancyBboxPatch(
            (x - w/2, y - h/2), w, h,
            boxstyle='round,pad=0.03,rounding_size=0.10',
            facecolor=bg, edgecolor=border, linewidth=lw, zorder=6
        )
        ax.add_patch(badge)
        ax.text(x, y, text, ha='center', va='center', fontsize=fs, weight='bold',
                color=text_color, fontfamily='sans-serif', zorder=7, linespacing=1.15)

    # Layout Dimensions
    x_left = 0.45
    card_w = 2.90
    gap_x  = 1.20
    c1_x   = x_left                      # 0.45 to 3.35
    c2_x   = c1_x + card_w + gap_x       # 4.55 to 7.45
    c3_x   = c2_x + card_w + gap_x       # 8.65 to 11.55

    # =========================================================================
    # ROW 1: STEPS 1, 2, 3
    # =========================================================================
    r1_y = 8.15
    r1_h = 4.35

    # --- STEP 1: Multi-Modal Patient Intake ---
    draw_card(c1_x, r1_y, card_w, r1_h, c1_bg, c1_border, lw=2.0)
    draw_num_badge(c1_x + 0.16, r1_y + r1_h - 0.54, '1', c1_badge)
    ax.text(c1_x + 0.64, r1_y + r1_h - 0.35, 'Multi-Modal Patient Intake',
            fontsize=9.2, weight='bold', color=c1_text, fontfamily='sans-serif', zorder=4)
    ax.plot([c1_x + 0.16, c1_x + card_w - 0.16], [r1_y + r1_h - 0.68, r1_y + r1_h - 0.68],
            linestyle=':', color=c1_border, lw=1.2, zorder=3)

    c1_content = [
        ('• Mode 1: Non-Invasive Screening', True, 0),
        ('  - Demographics, Habits, Symptoms', False, 0.10),
        ('• Mode 2: Clinical Lab Biomarkers', True, 0),
        ('  - Blood Pressure, Glucose, HbA1c', False, 0.10),
        ('• Mode 3: Medical Document OCR', True, 0),
        ('  - Automated PDF/Text extraction', False, 0.10),
        ('• Bilingual UI: English or Tamil', True, 0)
    ]
    cur_y = r1_y + r1_h - 1.04
    for text, is_header, indent in c1_content:
        fs = 7.9 if is_header else 7.2
        clr = '#0f172a' if is_header else '#334155'
        wt = 'bold' if is_header else 'normal'
        ax.text(c1_x + 0.16 + indent, cur_y, text, fontsize=fs, weight=wt, color=clr, fontfamily='sans-serif', zorder=4)
        cur_y -= 0.42 if is_header else 0.34

    # Connector 1 -> 2 (Gap from 3.35 to 4.55 = 1.20 in)
    b1_x = (c1_x + card_w + c2_x) / 2.0  # 3.95
    b1_y = r1_y + r1_h / 2.0
    bw1, bh1 = 0.86, 0.44
    draw_pill_badge(b1_x, b1_y, bw1, bh1, 'Raw\nPayload', bg='#f0f9ff', border=c1_border, text_color=c1_badge, fs=7.5)
    ax.annotate('', xy=(b1_x - bw1/2 - 0.02, b1_y), xytext=(c1_x + card_w, b1_y),
                arrowprops=dict(arrowstyle='-', lw=1.8, color=c1_border), zorder=4)
    ax.annotate('', xy=(c2_x, b1_y), xytext=(b1_x + bw1/2 + 0.02, b1_y),
                arrowprops=dict(arrowstyle='->', lw=1.8, color=c1_border), zorder=4)

    # --- STEP 2: Preprocessing & Validation ---
    draw_card(c2_x, r1_y, card_w, r1_h, c2_bg, c2_border, lw=2.0)
    draw_num_badge(c2_x + 0.16, r1_y + r1_h - 0.54, '2', c2_badge)
    ax.text(c2_x + 0.64, r1_y + r1_h - 0.35, 'Preprocessing & Validation',
            fontsize=9.2, weight='bold', color=c2_text, fontfamily='sans-serif', zorder=4)
    ax.plot([c2_x + 0.16, c2_x + card_w - 0.16], [r1_y + r1_h - 0.68, r1_y + r1_h - 0.68],
            linestyle=':', color=c2_border, lw=1.2, zorder=3)

    c2_content = [
        ('• Pydantic v2 Schema Enforcement', True, 0),
        ('  - Boundary & type sanitization', False, 0.10),
        ('• Continuous Feature Engineering', True, 0),
        ('  - BMI = Weight(kg) / Height(m)²', False, 0.10),
        ('• Categorical Integer Encoding', True, 0),
        ('  - Smoking, Alcohol, Activity level', False, 0.10),
        ('• Binary Symptom Vectorization', True, 0)
    ]
    cur_y = r1_y + r1_h - 1.04
    for text, is_header, indent in c2_content:
        fs = 7.9 if is_header else 7.2
        clr = '#0f172a' if is_header else '#334155'
        wt = 'bold' if is_header else 'normal'
        ax.text(c2_x + 0.16 + indent, cur_y, text, fontsize=fs, weight=wt, color=clr, fontfamily='sans-serif', zorder=4)
        cur_y -= 0.42 if is_header else 0.34

    # Connector 2 -> 3 (Gap from 7.45 to 8.65 = 1.20 in)
    b2_x = (c2_x + card_w + c3_x) / 2.0  # 8.05
    b2_y = r1_y + r1_h / 2.0
    bw2, bh2 = 0.86, 0.44
    draw_pill_badge(b2_x, b2_y, bw2, bh2, 'Feature\nVector', bg='#f0fdf4', border=c2_border, text_color=c2_badge, fs=7.5)
    ax.annotate('', xy=(b2_x - bw2/2 - 0.02, b2_y), xytext=(c2_x + card_w, b2_y),
                arrowprops=dict(arrowstyle='-', lw=1.8, color=c2_border), zorder=4)
    ax.annotate('', xy=(c3_x, b2_y), xytext=(b2_x + bw2/2 + 0.02, b2_y),
                arrowprops=dict(arrowstyle='->', lw=1.8, color=c2_border), zorder=4)

    # --- STEP 3: XGBoost Predictive Engine ---
    draw_card(c3_x, r1_y, card_w, r1_h, c3_bg, c3_border, lw=2.0)
    draw_num_badge(c3_x + 0.16, r1_y + r1_h - 0.54, '3', c3_badge)
    ax.text(c3_x + 0.64, r1_y + r1_h - 0.35, 'XGBoost Predictive Engine',
            fontsize=9.2, weight='bold', color=c3_text, fontfamily='sans-serif', zorder=4)
    ax.plot([c3_x + 0.16, c3_x + card_w - 0.16], [r1_y + r1_h - 0.68, r1_y + r1_h - 0.68],
            linestyle=':', color=c3_border, lw=1.2, zorder=3)

    c3_content = [
        ('• 150 Gradient-Boosted Trees (Depth 6)', True, 0),
        ('• Softmax Probability Distribution', True, 0),
        ('• 4-Class Clinical Severity Output:', True, 0),
        ('  - Low, Moderate, High, Critical', False, 0.10),
        ('• 99.86% Test Classification Acc.', True, 0),
        ('• Multi-Disease Risk Estimators:', True, 0),
        ('  - CAD %, Type-2 Diabetes %, HTN %', False, 0.10)
    ]
    cur_y = r1_y + r1_h - 1.04
    for text, is_header, indent in c3_content:
        fs = 7.9 if is_header else 7.2
        clr = '#0f172a' if is_header else '#334155'
        wt = 'bold' if is_header else 'normal'
        ax.text(c3_x + 0.16 + indent, cur_y, text, fontsize=fs, weight=wt, color=clr, fontfamily='sans-serif', zorder=4)
        cur_y -= 0.40 if is_header else 0.32

    # =========================================================================
    # ROW 2: STEPS 4, 5, 6
    # =========================================================================
    r2_y = 2.45
    r2_h = 4.80

    # --- STEP 4: TreeSHAP Attribution (XAI) ---
    draw_card(c1_x, r2_y, card_w, r2_h, c4_bg, c4_border, lw=2.0)
    draw_num_badge(c1_x + 0.16, r2_y + r2_h - 0.54, '4', c4_badge)
    ax.text(c1_x + 0.64, r2_y + r2_h - 0.35, 'TreeSHAP Attribution (XAI)',
            fontsize=9.2, weight='bold', color=c4_text, fontfamily='sans-serif', zorder=4)
    ax.plot([c1_x + 0.16, c1_x + card_w - 0.16], [r2_y + r2_h - 0.68, r2_y + r2_h - 0.68],
            linestyle=':', color=c4_border, lw=1.2, zorder=3)

    c4_content = [
        ('• Polynomial-Time TreeSHAP Algorithm', True, 0),
        ('• Computes exact Shapley values (phi_i)', True, 0),
        ('• Ranks Patient Specific Risk Drivers:', True, 0),
        ('  - e.g. High Systolic BP, Obese BMI', False, 0.10),
        ('• Identifies Protective Factors:', True, 0),
        ('  - e.g. Normal Sleep, Non-smoker', False, 0.10),
        ('• Completely resolves Black Box Opacity', True, 0),
        ('• Critical Specialist Triage Engine', True, 0)
    ]
    cur_y = r2_y + r2_h - 1.04
    for text, is_header, indent in c4_content:
        fs = 7.9 if is_header else 7.2
        clr = '#78350f' if 'Specialist' in text else ('#0f172a' if is_header else '#334155')
        wt = 'bold' if is_header else 'normal'
        ax.text(c1_x + 0.16 + indent, cur_y, text, fontsize=fs, weight=wt, color=clr, fontfamily='sans-serif', zorder=4)
        cur_y -= 0.40 if is_header else 0.32

    # Connector 4 -> 5 (Gap from 3.35 to 4.55 = 1.20 in)
    b4_x = (c1_x + card_w + c2_x) / 2.0  # 3.95
    b4_y = r2_y + r2_h * 0.58
    bw4, bh4 = 0.88, 0.44
    draw_pill_badge(b4_x, b4_y, bw4, bh4, 'Baseline\nDrivers', bg='#fffbeb', border=c4_border, text_color=c4_badge, fs=7.5)
    ax.annotate('', xy=(b4_x - bw4/2 - 0.02, b4_y), xytext=(c1_x + card_w, b4_y),
                arrowprops=dict(arrowstyle='-', lw=1.8, color=c4_border), zorder=4)
    ax.annotate('', xy=(c2_x, b4_y), xytext=(b4_x + bw4/2 + 0.02, b4_y),
                arrowprops=dict(arrowstyle='->', lw=1.8, color=c4_border), zorder=4)

    # --- STEP 5: Health Digital Twin Simulator ---
    draw_card(c2_x, r2_y, card_w, r2_h, c5_bg, c5_border, lw=2.0)
    draw_num_badge(c2_x + 0.16, r2_y + r2_h - 0.54, '5', c5_badge)
    ax.text(c2_x + 0.64, r2_y + r2_h - 0.35, 'Health Digital Twin Simulator',
            fontsize=8.9, weight='bold', color=c5_text, fontfamily='sans-serif', zorder=4)
    ax.plot([c2_x + 0.16, c2_x + card_w - 0.16], [r2_y + r2_h - 0.68, r2_y + r2_h - 0.68],
            linestyle=':', color=c5_border, lw=1.2, zorder=3)

    c5_content = [
        ('• "What-If" Sensitivity Analysis', True, 0),
        ('• Interactive Behavioral Sliders:', True, 0),
        ('  - Weight delta: -15 kg to +15 kg', False, 0.10),
        ('  - Sleep duration: 4 to 10 hours', False, 0.10),
        ('  - Exercise frequency: 0 to 7 days', False, 0.10),
        ('• Quit Smoking (+16.5% protection)', True, 0),
        ('  - Hidden automatically if non-smoker', False, 0.10),
        ('• Live Risk Reduction Percentage Badge', True, 0)
    ]
    cur_y = r2_y + r2_h - 1.04
    for text, is_header, indent in c5_content:
        fs = 7.9 if is_header else 7.2
        clr = '#0f172a' if is_header else '#334155'
        wt = 'bold' if is_header else 'normal'
        ax.text(c2_x + 0.16 + indent, cur_y, text, fontsize=fs, weight=wt, color=clr, fontfamily='sans-serif', zorder=4)
        cur_y -= 0.38 if is_header else 0.30

    # --- STEP 6: HIPAA De-Identification & DB ---
    draw_card(c3_x, r2_y, card_w, r2_h, c6_bg, c6_border, lw=2.0)
    draw_num_badge(c3_x + 0.16, r2_y + r2_h - 0.54, '6', c6_badge)
    ax.text(c3_x + 0.64, r2_y + r2_h - 0.35, 'HIPAA De-Identification & DB',
            fontsize=8.9, weight='bold', color=c6_text, fontfamily='sans-serif', zorder=4)
    ax.plot([c3_x + 0.16, c3_x + card_w - 0.16], [r2_y + r2_h - 0.68, r2_y + r2_h - 0.68],
            linestyle=':', color=c6_border, lw=1.2, zorder=3)

    c6_content = [
        ('• Salted SHA-256 Cryptographic Token', True, 0),
        ('  - Non-reversible ID (e.g. ANON-8F92)', False, 0.10),
        ('• k-Anonymity Generalization:', True, 0),
        ('  - 5 Year Age Brackets (e.g. 50-54)', False, 0.10),
        ('  - WHO Clinical BMI Intervals', False, 0.10),
        ('• Zero-Storage Guarantee (Zero disk PHI)', True, 0),
        ('• In-Memory RAM Store (<0.01 ms latency)', True, 0)
    ]
    cur_y = r2_y + r2_h - 1.04
    for text, is_header, indent in c6_content:
        fs = 7.9 if is_header else 7.2
        clr = '#0f172a' if is_header else '#334155'
        wt = 'bold' if is_header else 'normal'
        ax.text(c3_x + 0.16 + indent, cur_y, text, fontsize=fs, weight=wt, color=clr, fontfamily='sans-serif', zorder=4)
        cur_y -= 0.42 if is_header else 0.34

    # =========================================================================
    # CONNECTORS: ROW 1 TO ROW 2
    # =========================================================================
    # Connector Step 3 -> Step 4 (Class Probabilities & Model Trees)
    start_3_4 = (c3_x + 0.40, r1_y)
    end_3_4   = (c1_x + card_w * 0.75, r2_y + r2_h)
    mid_3_4_x = (start_3_4[0] + end_3_4[0]) / 2.0
    mid_3_4_y = (start_3_4[1] + end_3_4[1]) / 2.0
    ax.annotate('', xy=end_3_4, xytext=start_3_4,
                arrowprops=dict(arrowstyle='->', lw=1.8, color='#7e22ce'), zorder=4)
    draw_pill_badge(mid_3_4_x, mid_3_4_y, 3.20, 0.30, 'Class Probabilities & Model Trees',
                    bg='#faf5ff', border=c3_border, text_color=c3_badge, fs=7.8)

    # Connector Step 3 -> Step 6 (Asynchronous Ingestion)
    c3_6_x = c3_x + card_w * 0.55
    ax.annotate('', xy=(c3_6_x, r2_y + r2_h), xytext=(c3_6_x, r1_y),
                arrowprops=dict(arrowstyle='->', lw=1.8, color='#0d9488'), zorder=4)
    draw_pill_badge(c3_6_x, (r1_y + r2_y + r2_h)/2.0, 2.30, 0.30, 'Asynchronous Ingestion',
                    bg='#f0fdfa', border=c6_border, text_color=c6_badge, fs=7.8)

    # =========================================================================
    # ROW 3: STEP 7 (Full Width Bottom Card)
    # =========================================================================
    r3_y = 0.40
    r3_h = 1.35
    w_full = (c3_x + card_w) - c1_x

    draw_card(c1_x, r3_y, w_full, r3_h, c7_bg, c7_border, lw=2.0)

    # Header for Step 7
    ax.text(c1_x + w_full/2, r3_y + r3_h - 0.32,
            'STEP 7: CLINICAL EMPOWERMENT & CONTINUOUS PREVENTIVE CARE',
            ha='center', va='center', fontsize=11.2, weight='bold', color=c7_text, fontfamily='sans-serif', zorder=4)

    # Dotted divider
    ax.plot([c1_x + 0.30, c1_x + w_full - 0.30], [r3_y + r3_h - 0.54, r3_y + r3_h - 0.54],
            linestyle=':', color=c7_border, lw=1.2, zorder=3)

    row7_1 = '• 1-Click Official Clinical PDF Report Download      • Personalized Dietary & Exercise Regimen      • Critical Specialist Referral'
    row7_2 = '• Administrative Repository & Severity Filtering      • Longitudinal Preventive Re-Assessment & Progress Tracking'
    ax.text(c1_x + w_full/2, r3_y + 0.50, row7_1, ha='center', va='center',
            fontsize=8.3, weight='bold', color='#1e293b', fontfamily='sans-serif', zorder=4)
    ax.text(c1_x + w_full/2, r3_y + 0.22, row7_2, ha='center', va='center',
            fontsize=8.3, weight='bold', color='#1e293b', fontfamily='sans-serif', zorder=4)

    # =========================================================================
    # CONNECTORS: ROW 2 TO ROW 3
    # =========================================================================
    # Step 5 -> Step 7 (Simulated Sensitivity Outcomes)
    c5_7_x = c2_x + card_w * 0.55
    ax.annotate('', xy=(c5_7_x, r3_y + r3_h), xytext=(c5_7_x, r2_y),
                arrowprops=dict(arrowstyle='->', lw=1.8, color=c5_border), zorder=4)
    draw_pill_badge(c5_7_x, (r2_y + r3_y + r3_h)/2.0, 3.00, 0.30, 'Simulated Sensitivity Outcomes',
                    bg='#fff1f2', border=c5_border, text_color=c5_badge, fs=7.6)

    # Step 6 -> Step 7 (De-Identified Audit)
    c6_7_x = c3_x + card_w * 0.55
    ax.annotate('', xy=(c6_7_x, r3_y + r3_h), xytext=(c6_7_x, r2_y),
                arrowprops=dict(arrowstyle='->', lw=1.8, color=c6_border), zorder=4)
    draw_pill_badge(c6_7_x, (r2_y + r3_y + r3_h)/2.0, 2.00, 0.30, 'De-Identified Audit',
                    bg='#f0fdfa', border=c6_border, text_color=c6_badge, fs=7.6)

    ax.set_xlim(0, 12.0)
    ax.set_ylim(0, 13.0)
    plt.tight_layout(pad=0.10)

    save_path = os.path.join(out_dir, 'fig_4_2_clinical_workflow_pipeline.png')
    plt.savefig(save_path, dpi=300, bbox_inches='tight', pad_inches=0.08)

    dl_path = r'C:\Users\arunk\Downloads\fig_4_2_clinical_workflow_pipeline.png'
    plt.savefig(dl_path, dpi=300, bbox_inches='tight', pad_inches=0.08)

    art_path = r'C:\Users\arunk\.gemini\antigravity\brain\87427b1b-8625-473d-acdc-fff8d0537b70\fig_4_2_clinical_workflow_pipeline.png'
    plt.savefig(art_path, dpi=300, bbox_inches='tight', pad_inches=0.08)

    plt.close()
    print('Generated crisp, publication-grade clinical workflow pipeline diagram successfully.')

if __name__ == '__main__':
    build_workflow_pipeline()
