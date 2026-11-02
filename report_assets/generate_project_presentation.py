import os
import pptx
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor

template_path = r'C:\Users\arunk\.gemini\antigravity\brain\87427b1b-8625-473d-acdc-fff8d0537b70\.user_uploaded\media_1793375585008_a52c90a9.pptx'
output_project_path = r'C:\Users\arunk\Projects\health-assistant\AI_Personalized_Preventive_Healthcare_Assistant_Presentation.pptx'
output_downloads_path = r'C:\Users\arunk\Downloads\AI_Personalized_Preventive_Healthcare_Assistant_Presentation.pptx'

prs = pptx.Presentation(template_path)

def update_footer(slide, tag_text="AI PERSONALIZED PREVENTIVE HEALTHCARE ASSISTANT"):
    """Update footer tag if present."""
    for sh in slide.shapes:
        if sh.has_text_frame and "AI PLACEMENT INTELLIGENCE PLATFORM" in sh.text:
            p = sh.text_frame.paragraphs[0]
            orig_sz = p.runs[0].font.size.pt if p.runs and p.runs[0].font.size else 9.0
            orig_c = p.runs[0].font.color.rgb if p.runs and p.runs[0].font.color and hasattr(p.runs[0].font.color, 'rgb') else RGBColor(97, 115, 134)
            p.text = tag_text
            p.runs[0].font.size = Pt(orig_sz)
            p.runs[0].font.bold = True
            p.runs[0].font.color.rgb = orig_c

# ==============================================================================
# SLIDE 1: TITLE SLIDE
# ==============================================================================
s1 = prs.slides[0]
# Title box (Shape 2)
s1_title_shape = s1.shapes[2]
tf1 = s1_title_shape.text_frame
tf1.paragraphs[0].text = "AI-BASED PERSONALIZED PREVENTIVE"
tf1.paragraphs[0].runs[0].font.size = Pt(36.0)
tf1.paragraphs[0].runs[0].font.bold = True
tf1.paragraphs[0].runs[0].font.color.rgb = RGBColor(255, 255, 255)

tf1.paragraphs[1].text = "HEALTHCARE ASSISTANT"
tf1.paragraphs[1].runs[0].font.size = Pt(36.0)
tf1.paragraphs[1].runs[0].font.bold = True
tf1.paragraphs[1].runs[0].font.color.rgb = RGBColor(255, 255, 255)

# Subtitle (Shape 3)
s1_sub_shape = s1.shapes[3]
tf1_sub = s1_sub_shape.text_frame
tf1_sub.paragraphs[0].text = "An AI-powered, explainable & privacy-preserving platform for proactive health risk assessment & prevention"
tf1_sub.paragraphs[0].runs[0].font.size = Pt(17.0)
tf1_sub.paragraphs[0].runs[0].font.color.rgb = RGBColor(211, 224, 234)

# ==============================================================================
# SLIDE 2: ABSTRACT
# ==============================================================================
s2 = prs.slides[1]
update_footer(s2)

# Lead sentence (Shape 6)
s2.shapes[6].text_frame.paragraphs[0].text = "A centralized web platform that turns preventive healthcare into a proactive, explainable, and privacy-preserving process."
s2.shapes[6].text_frame.paragraphs[0].runs[0].font.size = Pt(19.0)
s2.shapes[6].text_frame.paragraphs[0].runs[0].font.bold = True
s2.shapes[6].text_frame.paragraphs[0].runs[0].font.color.rgb = RGBColor(16, 36, 58)

# 4 Bullets (Shapes 8, 10, 12, 14)
s2_bullets = [
    "Multi-modal screening ingests lifestyle habits, clinical lab biomarkers, and medical report OCR data.",
    "XGBoost classifier achieves 99.86% accuracy across 4 severity tiers (Low, Moderate, High, Critical).",
    "TreeSHAP explainability reveals patient-specific risk drivers, and the Digital Twin simulates lifestyle interventions.",
    "Patient, clinical and admin interfaces support assessment, personalized guidance, and zero-disk HIPAA compliance."
]
bullet_shape_indices = [8, 10, 12, 14]
for s_idx, b_text in zip(bullet_shape_indices, s2_bullets):
    p = s2.shapes[s_idx].text_frame.paragraphs[0]
    p.text = b_text
    p.runs[0].font.size = Pt(15.0)
    p.runs[0].font.bold = False
    p.runs[0].font.color.rgb = RGBColor(24, 48, 71)

# ==============================================================================
# SLIDE 3: PROJECT OBJECTIVES
# ==============================================================================
s3 = prs.slides[2]
update_footer(s3)

objectives_data = [
    (7, 8, "Multi-Modal Ingestion", "Capture demographic, clinical biomarker, and OCR report data."),
    (10, 11, "Early Detection", "Screen chronic disease risks (CAD, T2D, HTN) before acute symptoms."),
    (13, 14, "High-Accuracy ML", "Train XGBoost achieving 99.86% multi-class risk classification."),
    (16, 17, "Explainable AI", "Provide exact TreeSHAP values for transparent clinical drivers."),
    (19, 20, "Digital Twin", "Interactive sensitivity modeling for personalized lifestyle interventions."),
    (22, 23, "HIPAA Privacy", "Guarantee zero disk PHI storage with salted SHA-256 pseudonymization."),
    (25, 26, "Bilingual Access", "Provide localized dual-language interface in English and Tamil."),
    (28, 29, "Clinical Reporting", "Generate 1-click official PDF medical reports and audit trail logs.")
]

for t_idx, d_idx, title_text, desc_text in objectives_data:
    p_t = s3.shapes[t_idx].text_frame.paragraphs[0]
    p_t.text = title_text
    p_t.runs[0].font.size = Pt(15.5)
    p_t.runs[0].font.bold = True
    p_t.runs[0].font.color.rgb = RGBColor(16, 36, 58)
    
    p_d = s3.shapes[d_idx].text_frame.paragraphs[0]
    p_d.text = desc_text
    p_d.runs[0].font.size = Pt(12.0)
    p_d.runs[0].font.bold = False
    p_d.runs[0].font.color.rgb = RGBColor(97, 115, 134)

# ==============================================================================
# SLIDE 4: PROPOSED SYSTEM METHODOLOGY
# ==============================================================================
s4 = prs.slides[3]
update_footer(s4)

s4_tb = s4.shapes[6].text_frame
methodology_items = [
    ("Multi-Modal Screening Ingestion:", " Captures patient data via Lifestyle Forms (Mode 1), Clinical Lab Biomarkers (Mode 2), and OCR Report Upload (Mode 3)."),
    ("Pydantic Validation & Normalization:", " Enforces strict schema validation, calculates WHO BMI categories, and normalizes feature vectors."),
    ("Cryptographic De-Identification:", " Applies non-reversible salted SHA-256 pseudonymization and k-anonymity binning before processing."),
    ("XGBoost Risk Stratification:", " 150 gradient-boosted decision trees classify patient risk into 4 calibrated severity tiers (Low to Critical)."),
    ("TreeSHAP Feature Attribution:", " Computes exact Shapley values to identify top clinical risk drivers and protective factors for each patient."),
    ("Digital Twin Lifestyle Simulation:", " Evaluates What-If lifestyle interventions (weight, sleep, smoking cessation) in real time.")
]

para_indices = [1, 3, 5, 7, 9, 11]
for p_idx, (b_title, n_text) in zip(para_indices, methodology_items):
    p = s4_tb.paragraphs[p_idx]
    p.text = ""
    r1 = p.add_run()
    r1.text = b_title
    r1.font.bold = True
    r1.font.size = Pt(13.0)
    r1.font.color.rgb = RGBColor(24, 48, 71)
    
    r2 = p.add_run()
    r2.text = n_text
    r2.font.bold = False
    r2.font.size = Pt(13.0)
    r2.font.color.rgb = RGBColor(97, 115, 134)

# ==============================================================================
# SLIDE 5: SYSTEM ARCHITECTURE
# ==============================================================================
s5 = prs.slides[4]
update_footer(s5)

# Top User Roles (Shape 7)
p = s5.shapes[7].text_frame.paragraphs[0]
p.text = "PATIENT  •  CLINICIAN  •  ADMIN"
p.runs[0].font.size = Pt(14.0)
p.runs[0].font.bold = True
p.runs[0].font.color.rgb = RGBColor(255, 255, 255)

# API Request label (Shape 8)
p = s5.shapes[8].text_frame.paragraphs[0]
p.text = "HTTPS / REST REQUESTS"
p.runs[0].font.size = Pt(10.0)
p.runs[0].font.bold = True
p.runs[0].font.color.rgb = RGBColor(24, 167, 161)

# Presentation tier (Shape 11)
p = s5.shapes[11].text_frame.paragraphs[0]
p.text = "PRESENTATION  |  React 18 + Vite + Tailwind CSS"
p.runs[0].font.size = Pt(14.5)
p.runs[0].font.bold = True
p.runs[0].font.color.rgb = RGBColor(24, 48, 71)

# REST API Calls label (Shape 12)
p = s5.shapes[12].text_frame.paragraphs[0]
p.text = "ASYNC FASTAPI CALLS"
p.runs[0].font.size = Pt(10.0)
p.runs[0].font.bold = True
p.runs[0].font.color.rgb = RGBColor(24, 167, 161)

# Backend tier (Shape 15)
p = s5.shapes[15].text_frame.paragraphs[0]
p.text = "GATEWAY & API  |  FastAPI + ASGI Uvicorn"
p.runs[0].font.size = Pt(14.5)
p.runs[0].font.bold = True
p.runs[0].font.color.rgb = RGBColor(24, 48, 71)

# Column 1: DATA PERSISTENCE
p = s5.shapes[16].text_frame.paragraphs[0]
p.text = "DATA PERSISTENCE"
p.runs[0].font.size = Pt(9.5)
p.runs[0].font.bold = True
p.runs[0].font.color.rgb = RGBColor(24, 167, 161)

p = s5.shapes[19].text_frame.paragraphs[0]
p.text = "RAM STORE"
p.runs[0].font.size = Pt(11.0)
p.runs[0].font.bold = True
p.runs[0].font.color.rgb = RGBColor(255, 255, 255)

tf21 = s5.shapes[21].text_frame
tf21.paragraphs[0].text = "In-Memory DB (<0.01 ms)"
tf21.paragraphs[0].runs[0].font.size = Pt(12.0)
tf21.paragraphs[0].runs[0].font.bold = True
tf21.paragraphs[0].runs[0].font.color.rgb = RGBColor(24, 48, 71)

tf21.paragraphs[1].text = "3,500 CSV Training Corpus"
tf21.paragraphs[1].runs[0].font.size = Pt(11.5)
tf21.paragraphs[1].runs[0].font.bold = False
tf21.paragraphs[1].runs[0].font.color.rgb = RGBColor(97, 115, 134)

# Column 2: PRIVACY ENGINE
p = s5.shapes[22].text_frame.paragraphs[0]
p.text = "PRIVACY ENGINE"
p.runs[0].font.size = Pt(9.5)
p.runs[0].font.bold = True
p.runs[0].font.color.rgb = RGBColor(24, 167, 161)

p = s5.shapes[25].text_frame.paragraphs[0]
p.text = "HIPAA SAFE HARBOR"
p.runs[0].font.size = Pt(10.5)
p.runs[0].font.bold = True
p.runs[0].font.color.rgb = RGBColor(255, 255, 255)

tf27 = s5.shapes[27].text_frame
tf27.paragraphs[0].text = "Salted SHA-256 Tokens"
tf27.paragraphs[0].runs[0].font.size = Pt(12.0)
tf27.paragraphs[0].runs[0].font.bold = True
tf27.paragraphs[0].runs[0].font.color.rgb = RGBColor(24, 48, 71)

p_extra = tf27.paragraphs[1] if len(tf27.paragraphs) > 1 else tf27.add_paragraph()
p_extra.text = "Zero Persistent PHI on Disk"
p_extra.runs[0].font.size = Pt(11.5)
p_extra.runs[0].font.bold = False
p_extra.runs[0].font.color.rgb = RGBColor(97, 115, 134)

# Column 3: PREDICTIVE AI & XAI
p = s5.shapes[28].text_frame.paragraphs[0]
p.text = "PREDICTIVE AI & XAI"
p.runs[0].font.size = Pt(9.5)
p.runs[0].font.bold = True
p.runs[0].font.color.rgb = RGBColor(24, 167, 161)

p = s5.shapes[31].text_frame.paragraphs[0]
p.text = "Intelligence & XAI Layer"
p.runs[0].font.size = Pt(11.0)
p.runs[0].font.bold = True
p.runs[0].font.color.rgb = RGBColor(255, 255, 255)

tf33 = s5.shapes[33].text_frame
tf33.paragraphs[0].text = "XGBoost Core (99.86% Acc)"
tf33.paragraphs[0].runs[0].font.size = Pt(12.0)
tf33.paragraphs[0].runs[0].font.bold = True
tf33.paragraphs[0].runs[0].font.color.rgb = RGBColor(24, 48, 71)

tf33.paragraphs[1].text = "TreeSHAP Attributions & Multi-Disease Risk (CAD, T2D, HTN)"
tf33.paragraphs[1].runs[0].font.size = Pt(10.5)
tf33.paragraphs[1].runs[0].font.bold = False
tf33.paragraphs[1].runs[0].font.color.rgb = RGBColor(97, 115, 134)

# Bottom text (Shape 34)
s5.shapes[34].top = Inches(6.36)
s5.shapes[34].height = Inches(0.40)
p = s5.shapes[34].text_frame.paragraphs[0]
p.text = "Responses, SHAP waterfall plots & What-If digital twin simulations return asynchronously to the user dashboard"
p.runs[0].font.size = Pt(10.5)
p.runs[0].font.bold = True
p.runs[0].font.color.rgb = RGBColor(24, 167, 161)

# ==============================================================================
# SLIDE 6: PLATFORM MODULES
# ==============================================================================
s6 = prs.slides[5]
update_footer(s6)

# Top box (Shape 7)
tf7 = s6.shapes[7].text_frame
tf7.paragraphs[0].text = "AI PERSONALIZED PREVENTIVE"
tf7.paragraphs[0].runs[0].font.size = Pt(13.0)
tf7.paragraphs[0].runs[0].font.bold = True
tf7.paragraphs[0].runs[0].font.color.rgb = RGBColor(255, 255, 255)

tf7.paragraphs[1].text = "HEALTHCARE ASSISTANT"
tf7.paragraphs[1].runs[0].font.size = Pt(13.0)
tf7.paragraphs[1].runs[0].font.bold = True
tf7.paragraphs[1].runs[0].font.color.rgb = RGBColor(255, 255, 255)

# Left Module (Shape 10) - High contrast dark text on light badge
p = s6.shapes[10].text_frame.paragraphs[0]
p.text = "PATIENT SCREENING"
p.runs[0].font.size = Pt(11.5)
p.runs[0].font.bold = True
p.runs[0].font.color.rgb = RGBColor(16, 36, 58)

tf11 = s6.shapes[11].text_frame
tf11.paragraphs[0].text = "Mode 1, 2, 3 Ingestion • Risk score"
tf11.paragraphs[0].runs[0].font.size = Pt(11.0)
tf11.paragraphs[0].runs[0].font.bold = False
tf11.paragraphs[0].runs[0].font.color.rgb = RGBColor(24, 48, 71)

tf11.paragraphs[1].text = "TreeSHAP attribution • Preventive guidance"
tf11.paragraphs[1].runs[0].font.size = Pt(11.0)
tf11.paragraphs[1].runs[0].font.bold = False
tf11.paragraphs[1].runs[0].font.color.rgb = RGBColor(24, 48, 71)

# Center Module (Inside Group 25, Subshapes 2, 3) - Health Digital Twin
group25 = s6.shapes[12]
for sub_sh in group25.shapes:
    if sub_sh.name == "Rectangle 14":
        p = sub_sh.text_frame.paragraphs[0]
        p.text = "HEALTH DIGITAL TWIN"
        p.runs[0].font.size = Pt(11.5)
        p.runs[0].font.bold = True
        p.runs[0].font.color.rgb = RGBColor(16, 36, 58)
    elif sub_sh.name == "Rectangle 15":
        tf = sub_sh.text_frame
        tf.paragraphs[0].text = "What-If simulation • Sensitivity sliders"
        tf.paragraphs[0].runs[0].font.size = Pt(11.0)
        tf.paragraphs[0].runs[0].font.bold = False
        tf.paragraphs[0].runs[0].font.color.rgb = RGBColor(24, 48, 71)
        
        tf.paragraphs[1].text = "Habit modification • Real-time risk delta"
        tf.paragraphs[1].runs[0].font.size = Pt(11.0)
        tf.paragraphs[1].runs[0].font.bold = False
        tf.paragraphs[1].runs[0].font.color.rgb = RGBColor(24, 48, 71)

# Right Module (Shape 15) - High contrast dark text on light badge
p = s6.shapes[15].text_frame.paragraphs[0]
p.text = "CLINICAL & ADMIN PORTAL"
p.runs[0].font.size = Pt(11.0)
p.runs[0].font.bold = True
p.runs[0].font.color.rgb = RGBColor(16, 36, 58)

tf16 = s6.shapes[16].text_frame
tf16.paragraphs[0].text = "Bilingual controls (EN/TA) • Audit logs"
tf16.paragraphs[0].runs[0].font.size = Pt(11.0)
tf16.paragraphs[0].runs[0].font.bold = False
tf16.paragraphs[0].runs[0].font.color.rgb = RGBColor(24, 48, 71)

tf16.paragraphs[1].text = "Zero-disk PHI verification • 1-Click PDF report"
tf16.paragraphs[1].runs[0].font.size = Pt(11.0)
tf16.paragraphs[1].runs[0].font.bold = False
tf16.paragraphs[1].runs[0].font.color.rgb = RGBColor(24, 48, 71)

# ==============================================================================
# SLIDE 7: PATIENT SCREENING & ASSESSMENT MODULE
# ==============================================================================
s7 = prs.slides[6]
update_footer(s7)

# Category (Shape 1) - update to PATIENT EXPERIENCE
s7.shapes[1].text_frame.paragraphs[0].text = "PATIENT EXPERIENCE"
s7.shapes[1].text_frame.paragraphs[0].runs[0].font.size = Pt(9.75)
s7.shapes[1].text_frame.paragraphs[0].runs[0].font.bold = True
s7.shapes[1].text_frame.paragraphs[0].runs[0].font.color.rgb = RGBColor(24, 167, 161)

# Title (Shape 2)
s7.shapes[2].text_frame.paragraphs[0].text = "Patient screening & assessment module"
s7.shapes[2].text_frame.paragraphs[0].runs[0].font.size = Pt(25.5)
s7.shapes[2].text_frame.paragraphs[0].runs[0].font.bold = True
s7.shapes[2].text_frame.paragraphs[0].runs[0].font.color.rgb = RGBColor(16, 36, 58)

# Purpose (Shape 7)
s7.shapes[7].text_frame.paragraphs[0].text = "A centralized workspace for multi-modal health screening, chronic disease risk profiling, and personalized clinical guidance."
s7.shapes[7].text_frame.paragraphs[0].runs[0].font.size = Pt(12.75)
s7.shapes[7].text_frame.paragraphs[0].runs[0].font.bold = False
s7.shapes[7].text_frame.paragraphs[0].runs[0].font.color.rgb = RGBColor(97, 115, 134)

# Key Functions (Shapes 10, 12, 14, 16)
s7_funcs = [
    "Mode 1: Non-invasive lifestyle and symptom assessment",
    "Mode 2: Clinical lab biomarker screening (HbA1c, Lipids, BP)",
    "Mode 3: Medical report OCR upload & automated parsing",
    "4-Class severity tiering (Low to Critical) with score 0–100"
]
for idx, text in zip([10, 12, 14, 16], s7_funcs):
    p = s7.shapes[idx].text_frame.paragraphs[0]
    p.text = text
    p.runs[0].font.size = Pt(12.0)
    p.runs[0].font.bold = False
    p.runs[0].font.color.rgb = RGBColor(24, 48, 71)

# Workflow (Shape 18)
p = s7.shapes[18].text_frame.paragraphs[0]
p.text = "Mode Selection → Input Entry / OCR Upload → Validation → Risk Stratification"
p.runs[0].font.size = Pt(11.5)
p.runs[0].font.bold = True
p.runs[0].font.color.rgb = RGBColor(24, 48, 71)

# Application Evidence (Cards: 22/23, 26/27, 30/31, 34/35)
cards_s7 = [
    (22, 23, "Multi-Modal Form", "Lifestyle, habit & biomarker entry"),
    (26, 27, "Report OCR Upload", "Tesseract automated lab report parsing"),
    (30, 31, "Risk Dashboard", "4-Tier severity badge & multi-disease %"),
    (34, 35, "TreeSHAP Attribution", "Feature importance waterfall (exact phi_i)")
]
for t_idx, d_idx, c_title, c_desc in cards_s7:
    p_t = s7.shapes[t_idx].text_frame.paragraphs[0]
    p_t.text = c_title
    p_t.runs[0].font.size = Pt(11.0)
    p_t.runs[0].font.bold = True
    p_t.runs[0].font.color.rgb = RGBColor(16, 36, 58)
    
    p_d = s7.shapes[d_idx].text_frame.paragraphs[0]
    p_d.text = c_desc
    p_d.runs[0].font.size = Pt(9.5)
    p_d.runs[0].font.bold = False
    p_d.runs[0].font.color.rgb = RGBColor(97, 115, 134)

# ==============================================================================
# SLIDE 8: HEALTH DIGITAL TWIN MODULE
# ==============================================================================
s8 = prs.slides[7]
update_footer(s8)

# Category (Shape 1)
s8.shapes[1].text_frame.paragraphs[0].text = "DIGITAL TWIN SIMULATION"
s8.shapes[1].text_frame.paragraphs[0].runs[0].font.size = Pt(9.75)
s8.shapes[1].text_frame.paragraphs[0].runs[0].font.bold = True
s8.shapes[1].text_frame.paragraphs[0].runs[0].font.color.rgb = RGBColor(24, 167, 161)

# Title (Shape 2)
s8.shapes[2].text_frame.paragraphs[0].text = "Health Digital Twin module"
s8.shapes[2].text_frame.paragraphs[0].runs[0].font.size = Pt(25.5)
s8.shapes[2].text_frame.paragraphs[0].runs[0].font.bold = True
s8.shapes[2].text_frame.paragraphs[0].runs[0].font.color.rgb = RGBColor(16, 36, 58)

# Purpose (Shape 7)
s8.shapes[7].text_frame.paragraphs[0].text = "Interactive \"What-If\" sensitivity simulator empowering patients to simulate the clinical impact of lifestyle interventions."
s8.shapes[7].text_frame.paragraphs[0].runs[0].font.size = Pt(12.75)
s8.shapes[7].text_frame.paragraphs[0].runs[0].font.bold = False
s8.shapes[7].text_frame.paragraphs[0].runs[0].font.color.rgb = RGBColor(97, 115, 134)

# Key Functions (Shapes 10, 12, 14, 16)
s8_funcs = [
    "Interactive sensitivity sliders for body weight (±15 kg)",
    "Sleep duration (4–10 hrs) and weekly physical activity",
    "Smoking cessation modeling providing +16.5% protective gain",
    "Instantaneous recalculation of risk reduction percentage in real time"
]
for idx, text in zip([10, 12, 14, 16], s8_funcs):
    p = s8.shapes[idx].text_frame.paragraphs[0]
    p.text = text
    p.runs[0].font.size = Pt(12.0)
    p.runs[0].font.bold = False
    p.runs[0].font.color.rgb = RGBColor(24, 48, 71)

# Workflow (Shape 18)
p = s8.shapes[18].text_frame.paragraphs[0]
p.text = "Baseline Risk → Access Digital Twin → Adjust Sliders → Real-Time Delta → Action Plan"
p.runs[0].font.size = Pt(11.0)
p.runs[0].font.bold = True
p.runs[0].font.color.rgb = RGBColor(24, 48, 71)

# Application Evidence (Cards: 22/23, 26/27, 30/31, 34/35)
cards_s8 = [
    (22, 23, "What-If Sliders", "Interactive weight, sleep & exercise adjustments"),
    (26, 27, "Smoking Cessation", "Tobacco cessation toggle granting +16.5% gain"),
    (30, 31, "Risk Delta Engine", "Live before-vs-after risk score gauge & mitigation %"),
    (34, 35, "Preventive Guidance", "Personalized diet, habit modification & checkup logic")
]
for t_idx, d_idx, c_title, c_desc in cards_s8:
    p_t = s8.shapes[t_idx].text_frame.paragraphs[0]
    p_t.text = c_title
    p_t.runs[0].font.size = Pt(11.0)
    p_t.runs[0].font.bold = True
    p_t.runs[0].font.color.rgb = RGBColor(16, 36, 58)
    
    p_d = s8.shapes[d_idx].text_frame.paragraphs[0]
    p_d.text = c_desc
    p_d.runs[0].font.size = Pt(9.5)
    p_d.runs[0].font.bold = False
    p_d.runs[0].font.color.rgb = RGBColor(97, 115, 134)

# ==============================================================================
# SLIDE 9: CLINICAL ADMIN & PRIVACY MODULE
# ==============================================================================
s9 = prs.slides[8]
update_footer(s9)

# Category (Shape 1)
s9.shapes[1].text_frame.paragraphs[0].text = "CLINICAL ADMINISTRATION"
s9.shapes[1].text_frame.paragraphs[0].runs[0].font.size = Pt(9.75)
s9.shapes[1].text_frame.paragraphs[0].runs[0].font.bold = True
s9.shapes[1].text_frame.paragraphs[0].runs[0].font.color.rgb = RGBColor(24, 167, 161)

# Title (Shape 2)
s9.shapes[2].text_frame.paragraphs[0].text = "Clinical admin & privacy module"
s9.shapes[2].text_frame.paragraphs[0].runs[0].font.size = Pt(25.5)
s9.shapes[2].text_frame.paragraphs[0].runs[0].font.bold = True
s9.shapes[2].text_frame.paragraphs[0].runs[0].font.color.rgb = RGBColor(16, 36, 58)

# Purpose (Shape 7)
s9.shapes[7].text_frame.paragraphs[0].text = "Centralized clinical governance, de-identified patient record auditing, bilingual localization, and formal medical reporting."
s9.shapes[7].text_frame.paragraphs[0].runs[0].font.size = Pt(12.75)
s9.shapes[7].text_frame.paragraphs[0].runs[0].font.bold = False
s9.shapes[7].text_frame.paragraphs[0].runs[0].font.color.rgb = RGBColor(97, 115, 134)

# Key Functions (Shapes 10, 12, 14, 16)
s9_funcs = [
    "Live de-identified in-memory database record viewer",
    "Salted SHA-256 token verification and k-anonymity compliance",
    "Bilingual localization engine supporting English and Tamil",
    "1-Click official PDF medical summary generation with audit trail"
]
for idx, text in zip([10, 12, 14, 16], s9_funcs):
    p = s9.shapes[idx].text_frame.paragraphs[0]
    p.text = text
    p.runs[0].font.size = Pt(12.0)
    p.runs[0].font.bold = False
    p.runs[0].font.color.rgb = RGBColor(24, 48, 71)

# Workflow (Shape 18)
p = s9.shapes[18].text_frame.paragraphs[0]
p.text = "Clinician Login → Audit Database → Filter by Severity → Export CSV / Generate PDF"
p.runs[0].font.size = Pt(11.0)
p.runs[0].font.bold = True
p.runs[0].font.color.rgb = RGBColor(24, 48, 71)

# Application Evidence (Cards: 22/23, 26/27, 30/31, 34/35)
cards_s9 = [
    (22, 23, "De-Identified Audit", "Pseudonymized SHA-256 tokens with zero disk PHI"),
    (26, 27, "Severity Filter & Search", "Low, Moderate, High & Critical risk cohort review"),
    (30, 31, "Bilingual UI Controls", "Seamless English and Tamil language localization"),
    (34, 35, "1-Click Medical Report", "Formal clinical PDF generation for doctor consultations")
]
for t_idx, d_idx, c_title, c_desc in cards_s9:
    p_t = s9.shapes[t_idx].text_frame.paragraphs[0]
    p_t.text = c_title
    p_t.runs[0].font.size = Pt(11.0)
    p_t.runs[0].font.bold = True
    p_t.runs[0].font.color.rgb = RGBColor(16, 36, 58)
    
    p_d = s9.shapes[d_idx].text_frame.paragraphs[0]
    p_d.text = c_desc
    p_d.runs[0].font.size = Pt(9.5)
    p_d.runs[0].font.bold = False
    p_d.runs[0].font.color.rgb = RGBColor(97, 115, 134)

# ==============================================================================
# SLIDE 10: REFERENCES
# ==============================================================================
s10 = prs.slides[9]
update_footer(s10)

references_list = [
    (7, "Chen, T & Guestrin, C 2016, ‘XGBoost: A scalable tree boosting system’, Proceedings of the 22nd ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, pp. 785–794."),
    (9, "Lundberg, SM & Lee, SI 2017, ‘A unified approach to interpreting model predictions’, Advances in Neural Information Processing Systems (NeurIPS 30), pp. 4765–4774."),
    (11, "El Emam, K, Rodgers, S & Malin, B 2015, ‘Anonymising and sharing individual patient data’, BMJ, vol. 350, h1139, pp. 1–9."),
    (13, "Kamel Boulos, MN & Zhang, P 2021, ‘Digital twins: from the green deal to health systems and beyond’, International Journal of Health Geographics, vol. 20, no. 1, pp. 1–21."),
    (15, "World Health Organization 2023, ‘Noncommunicable diseases: key facts’, WHO Global Health Observatory, Geneva.")
]

for idx, ref_text in references_list:
    p = s10.shapes[idx].text_frame.paragraphs[0]
    p.text = ref_text
    p.runs[0].font.size = Pt(12.0)
    p.runs[0].font.bold = False
    p.runs[0].font.color.rgb = RGBColor(24, 48, 71)

# ==============================================================================
# SLIDE 11: CONCLUSION & THANK YOU
# ==============================================================================
s11 = prs.slides[10]

# Title (Shape 2)
p = s11.shapes[2].text_frame.paragraphs[0]
p.text = "One platform for proactive, explainable & privacy-preserving healthcare"
p.runs[0].font.size = Pt(26.0)
p.runs[0].font.bold = True
p.runs[0].font.color.rgb = RGBColor(255, 255, 255)

# Subtitle (Shape 3)
p = s11.shapes[3].text_frame.paragraphs[0]
p.text = "The platform brings multi-modal screening, explainable AI, digital twin simulation, and HIPAA privacy into a unified web application."
p.runs[0].font.size = Pt(17.0)
p.runs[0].font.bold = False
p.runs[0].font.color.rgb = RGBColor(211, 224, 234)

# 3 Columns:
# Col 1: PATIENTS (Shape 5 title, Shape 6 text)
p = s11.shapes[5].text_frame.paragraphs[0]
p.text = "PATIENTS"
p.runs[0].font.size = Pt(11.0)
p.runs[0].font.bold = True
p.runs[0].font.color.rgb = RGBColor(154, 219, 216)

p = s11.shapes[6].text_frame.paragraphs[0]
p.text = "Early non-invasive screening, transparent risk drivers, and empowering digital twin lifestyle simulations"
p.runs[0].font.size = Pt(13.0)
p.runs[0].font.bold = False
p.runs[0].font.color.rgb = RGBColor(255, 255, 255)

# Col 2: CLINICIANS (Shape 8 title, Shape 9 text)
p = s11.shapes[8].text_frame.paragraphs[0]
p.text = "CLINICIANS"
p.runs[0].font.size = Pt(11.0)
p.runs[0].font.bold = True
p.runs[0].font.color.rgb = RGBColor(154, 219, 216)

p = s11.shapes[9].text_frame.paragraphs[0]
p.text = "High-precision 99.86% predictive accuracy, exact TreeSHAP attributions, and 1-click official clinical PDF reports"
p.runs[0].font.size = Pt(13.0)
p.runs[0].font.bold = False
p.runs[0].font.color.rgb = RGBColor(255, 255, 255)

# Col 3: HEALTHCARE SYSTEMS (Shape 11 title, Shape 12 text)
p = s11.shapes[11].text_frame.paragraphs[0]
p.text = "HEALTHCARE SYSTEMS"
p.runs[0].font.size = Pt(11.0)
p.runs[0].font.bold = True
p.runs[0].font.color.rgb = RGBColor(154, 219, 216)

p = s11.shapes[12].text_frame.paragraphs[0]
p.text = "Strict zero-disk HIPAA compliance, microsecond in-memory architecture, and direct SDG-3 preventive impact"
p.runs[0].font.size = Pt(13.0)
p.runs[0].font.bold = False
p.runs[0].font.color.rgb = RGBColor(255, 255, 255)

# Thank you (Shape 13)
p = s11.shapes[13].text_frame.paragraphs[0]
p.text = "THANK YOU"
p.runs[0].font.size = Pt(21.0)
p.runs[0].font.bold = True
p.runs[0].font.color.rgb = RGBColor(244, 185, 66)

# ==============================================================================
# SAVE PRESENTATION
# ==============================================================================
os.makedirs(os.path.dirname(output_project_path), exist_ok=True)
prs.save(output_project_path)
print(f"Presentation saved to: {output_project_path}")

try:
    prs.save(output_downloads_path)
    print(f"Presentation saved to: {output_downloads_path}")
except Exception as e:
    print(f"Could not save to downloads: {e}")
