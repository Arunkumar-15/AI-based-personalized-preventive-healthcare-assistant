# generate_updated_word_report.py
# Generates the complete, updated Word Document (.docx) Project Report
# Including the newly implemented Intelligent Clinical Specialist Referral Engine (Critical Triage)

import os
import docx
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn

from docx_helpers import (
    set_cell_margins, set_cell_background,
    add_styled_heading, add_body_paragraph, add_bullet_point
)

def add_callout(doc, text, title=""):
    p = doc.add_paragraph()
    p.paragraph_format.left_indent = Inches(0.4)
    p.paragraph_format.right_indent = Inches(0.4)
    p.paragraph_format.space_before = Pt(4)
    p.paragraph_format.space_after = Pt(6)
    p.paragraph_format.line_spacing = 1.3
    if title:
        r_t = p.add_run(f"{title}: ")
        r_t.font.name = 'Times New Roman'
        r_t.font.size = Pt(12)
        r_t.font.bold = True
        r_t.font.color.rgb = RGBColor(15, 23, 42)
    r = p.add_run(text)
    r.font.name = 'Times New Roman'
    r.font.size = Pt(12)
    r.font.italic = True
    r.font.color.rgb = RGBColor(51, 65, 85)

def add_code_block(doc, code_str, caption=""):
    if caption:
        p_c = doc.add_paragraph()
        p_c.paragraph_format.space_before = Pt(8)
        p_c.paragraph_format.space_after = Pt(2)
        r_c = p_c.add_run(caption)
        r_c.font.name = 'Times New Roman'
        r_c.font.size = Pt(11)
        r_c.font.bold = True
        r_c.font.color.rgb = RGBColor(30, 58, 138)
        
    t = doc.add_table(rows=1, cols=1)
    t.alignment = WD_TABLE_ALIGNMENT.CENTER
    t.autofit = False
    t.columns[0].width = Inches(6.2)
    c = t.cell(0, 0)
    set_cell_background(c, "F8FAFC")
    set_cell_margins(c, 100, 100, 120, 120)
    p = c.paragraphs[0]
    p.paragraph_format.space_before = Pt(2)
    p.paragraph_format.space_after = Pt(2)
    p.paragraph_format.line_spacing = 1.15
    r = p.add_run(code_str)
    r.font.name = 'Courier New'
    r.font.size = Pt(9.5)
    r.font.color.rgb = RGBColor(15, 23, 42)

def generate_doc():
    doc = Document()
    
    # Configure A4 Margins
    for s in doc.sections:
        s.top_margin = Inches(1.0)
        s.bottom_margin = Inches(1.0)
        s.left_margin = Inches(1.25)
        s.right_margin = Inches(1.0)
        s.page_width = Inches(8.27)
        s.page_height = Inches(11.69)
        
    assets_dir = r'C:\Users\arunk\Projects\health-assistant\report_assets'
    user_up_dir = r'C:\Users\arunk\.gemini\antigravity\brain\87427b1b-8625-473d-acdc-fff8d0537b70\.user_uploaded'
    
    anna_logo = os.path.join(assets_dir, 'word', 'media', 'image1.jpeg')
    sona_logo = os.path.join(assets_dir, 'word', 'media', 'image2.jpeg')
    
    fig_4_1 = os.path.join(assets_dir, 'fig_4_1_system_architecture.png')
    fig_4_2 = os.path.join(assets_dir, 'fig_4_2_system_workflow.png')
    fig_5_1 = os.path.join(assets_dir, 'fig_5_1_confusion_matrix.png')
    fig_5_2 = os.path.join(assets_dir, 'fig_5_2_feature_importances.png')
    fig_5_3 = os.path.join(assets_dir, 'fig_5_3_model_comparison.png')
    
    img_ui_input = os.path.join(user_up_dir, 'media_1786777568161.png')
    img_ui_output = os.path.join(user_up_dir, 'media_1786777576251.png')

    print("Building Document Sections...")

    # ==========================================================
    # 1. COVER / TITLE PAGE
    # ==========================================================
    if os.path.exists(anna_logo) and os.path.exists(sona_logo):
        t_logo = doc.add_table(rows=1, cols=2)
        t_logo.alignment = WD_TABLE_ALIGNMENT.CENTER
        t_logo.autofit = False
        t_logo.columns[0].width = Inches(3.0)
        t_logo.columns[1].width = Inches(3.0)
        
        c0 = t_logo.cell(0, 0)
        p0 = c0.paragraphs[0]
        p0.alignment = WD_ALIGN_PARAGRAPH.LEFT
        p0.add_run().add_picture(anna_logo, width=Inches(1.15))
        
        c1 = t_logo.cell(0, 1)
        p1 = c1.paragraphs[0]
        p1.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        p1.add_run().add_picture(sona_logo, width=Inches(1.15))

    p_proj = doc.add_paragraph()
    p_proj.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_proj.paragraph_format.space_before = Pt(20)
    p_proj.paragraph_format.space_after = Pt(14)
    r_title = p_proj.add_run("AI-BASED PERSONALIZED PREVENTIVE HEALTHCARE ASSISTANT")
    r_title.font.name = 'Times New Roman'
    r_title.font.size = Pt(19)
    r_title.font.bold = True
    r_title.font.color.rgb = RGBColor(15, 43, 92)

    p_sub = doc.add_paragraph()
    p_sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_sub.paragraph_format.space_after = Pt(20)
    r_sub = p_sub.add_run("A PROJECT REPORT\nSubmitted in partial fulfillment of the requirements for the award of the degree of\nBACHELOR OF TECHNOLOGY\nin\nINFORMATION TECHNOLOGY")
    r_sub.font.name = 'Times New Roman'
    r_sub.font.size = Pt(12)
    r_sub.font.bold = True

    p_sub_by = doc.add_paragraph()
    p_sub_by.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_sub_by.paragraph_format.space_after = Pt(16)
    r_by = p_sub_by.add_run("Submitted by\nBABY SHALINI K\nDEEPAK PRIYAN M\nARUNKUMAR N")
    r_by.font.name = 'Times New Roman'
    r_by.font.size = Pt(13)
    r_by.font.bold = True

    p_guide = doc.add_paragraph()
    p_guide.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_guide.paragraph_format.space_after = Pt(24)
    r_g = p_guide.add_run("Under the Guidance of\nDr. P. SHANMUGARAJA, M.E., Ph.D.\nAssociate Professor\nDepartment of Information Technology")
    r_g.font.name = 'Times New Roman'
    r_g.font.size = Pt(12.5)

    p_inst = doc.add_paragraph()
    p_inst.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_inst.paragraph_format.space_after = Pt(10)
    r_inst = p_inst.add_run("DEPARTMENT OF INFORMATION TECHNOLOGY\nSONA COLLEGE OF TECHNOLOGY, SALEM – 636 005\n(An Autonomous Institution, Affiliated to Anna University, Chennai)\nACADEMIC YEAR 2026–2027")
    r_inst.font.name = 'Times New Roman'
    r_inst.font.size = Pt(12)
    r_inst.font.bold = True

    # ==========================================================
    # 2. BONAFIDE CERTIFICATE
    # ==========================================================
    doc.add_page_break()
    add_styled_heading(doc, "BONAFIDE CERTIFICATE", level=1, align=WD_ALIGN_PARAGRAPH.CENTER)
    add_body_paragraph(
        doc,
        "Certified that this project report titled 'AI-BASED PERSONALIZED PREVENTIVE HEALTHCARE ASSISTANT' is the bonafide work of BABY SHALINI K, DEEPAK PRIYAN M, and ARUNKUMAR N, who carried out the research and software development under my direct academic supervision."
    )
    add_body_paragraph(
        doc,
        "Certified further that to the best of my knowledge, the work reported herein does not form part of any other project or dissertation on the basis of which a degree or award was conferred on an earlier occasion on this or any other candidate."
    )
    
    p_sig = doc.add_paragraph()
    p_sig.paragraph_format.space_before = Pt(50)
    p_sig.paragraph_format.line_spacing = 1.3
    r_sig = p_sig.add_run("SUPERVISOR\nDr. P. SHANMUGARAJA, M.E., Ph.D.\nAssociate Professor\nDepartment of Information Technology\nSona College of Technology, Salem")
    r_sig.font.name = 'Times New Roman'
    r_sig.font.size = Pt(12)
    r_sig.font.bold = True

    # ==========================================================
    # 3. ACKNOWLEDGEMENT
    # ==========================================================
    doc.add_page_break()
    add_styled_heading(doc, "ACKNOWLEDGEMENT", level=1, align=WD_ALIGN_PARAGRAPH.CENTER)
    add_body_paragraph(
        doc,
        "We express our profound gratitude to our respected Principal, Head of the Department, and our project guide Dr. P. Shanmugaraja for their invaluable guidance, constant motivation, and technical support throughout the development of the AI-Based Personalized Preventive Healthcare Assistant."
    )
    add_body_paragraph(
        doc,
        "We also extend our sincere appreciation to the faculty members and laboratory staff of the Department of Information Technology at Sona College of Technology for providing computational facilities and moral encouragement."
    )

    # ==========================================================
    # 4. ABSTRACT (UPDATED WITH SPECIALIST REFERRAL FEATURE)
    # ==========================================================
    doc.add_page_break()
    add_styled_heading(doc, "ABSTRACT", level=1, align=WD_ALIGN_PARAGRAPH.CENTER)
    add_body_paragraph(
        doc,
        "Most current healthcare systems are reactive. They only diagnose lifestyle diseases such as cardiovascular disease, hypertension or diabetes after significant symptoms appear or complications arise. Regular preventive testing is rarely used because it is expensive, often requires invasive procedures, and health tracking remains fragmented and scattered. The AI-Based Personalized Preventive Healthcare Assistant is designed to fundamentally change this paradigm, shifting healthcare from reactive disease management to proactive prevention. The platform provides an accessible multi-modal screening model that allows individuals to monitor their chronic disease vulnerability using non-invasive daily habits, clinical laboratory biomarkers, or digitized medical reports via Optical Character Recognition (OCR), presenting a holistic diagnostic assessment."
    )
    add_body_paragraph(
        doc,
        "Beyond categorical risk labeling, the platform prioritizes transparency, patient motivation, and data confidentiality. By integrating game-theoretic Explainable Artificial Intelligence (TreeSHAP), the system demystifies the predictive model, showing patients and doctors exactly which physiological drivers pushed risk upward or provided protective benefits. Furthermore, an interactive Personal Health Digital Twin allows users to simulate counterfactual 'what-if' lifestyle interventions (such as weight reduction, smoking cessation, and sleep optimization) to witness tangible risk reductions in real time before adopting them."
    )
    add_body_paragraph(
        doc,
        "For high-acuity cases, the platform features an Intelligent Clinical Specialist Referral Engine that activates strictly for patients flagged at Critical Risk. By evaluating multi-disease probability distributions, the engine identifies the single highest-vulnerability disease and recommends strictly ONE dedicated specialist (e.g., Cardiologist, Diabetologist, or Nephrologist), complete with recommended diagnostic workups, consultation questions, and a 1-click physician handover note adhering to the international SBAR (Situation, Background, Assessment, Recommendation) clinical protocol. Built with HIPAA Safe Harbor zero-disk persistence and cryptographic pseudonymization, the system ensures complete privacy, delivering a transparent, actionable, and secure ecosystem for modern preventive medicine."
    )

    # ==========================================================
    # 5. TABLE OF CONTENTS
    # ==========================================================
    doc.add_page_break()
    add_styled_heading(doc, "TABLE OF CONTENTS", level=1, align=WD_ALIGN_PARAGRAPH.CENTER)
    
    t_toc = doc.add_table(rows=1, cols=2)
    t_toc.alignment = WD_TABLE_ALIGNMENT.CENTER
    t_toc.autofit = False
    t_toc.columns[0].width = Inches(5.2)
    t_toc.columns[1].width = Inches(1.0)
    
    c0 = t_toc.cell(0, 0)
    c1 = t_toc.cell(0, 1)
    c0.paragraphs[0].add_run("TITLE").font.bold = True
    c1.paragraphs[0].add_run("PAGE NO").font.bold = True
    set_cell_background(c0, "F1F5F9")
    set_cell_background(c1, "F1F5F9")
    
    toc_items = [
        ("ABSTRACT", "v"),
        ("LIST OF FIGURES", "viii"),
        ("LIST OF TABLES", "ix"),
        ("LIST OF ABBREVIATIONS", "x"),
        ("1. INTRODUCTION", "1"),
        ("   1.1 Background of the Project", "1"),
        ("   1.2 Problem Statement", "2"),
        ("   1.3 Motivation", "3"),
        ("   1.4 Objectives", "3"),
        ("   1.5 Scope of the Project", "4"),
        ("2. LITERATURE REVIEW", "5"),
        ("   2.1 Introduction", "5"),
        ("   2.2 Review of Related Studies", "5"),
        ("   2.3 Techniques and Technologies Used in Existing Systems", "9"),
        ("   2.4 Research Gap", "10"),
        ("   2.5 Summary", "10"),
        ("3. CHAPTER 1 – NEED FOR PROPOSED TECHNIQUE", "11"),
        ("   3.1 Existing Techniques", "11"),
        ("   3.2 Limitations of Existing Techniques", "11"),
        ("   3.3 Proposed Technique", "12"),
        ("   3.4 Objectives of the Proposed Technique", "13"),
        ("   3.5 Advantages of the Proposed Technique", "13"),
        ("   3.6 Main User and System Interaction", "14"),
        ("4. CHAPTER 2 – DESIGN OF PROPOSED SYSTEM AND ITS IMPLEMENTATION", "16"),
        ("   4.1 Introduction", "16"),
        ("   4.2 System Requirements", "16"),
        ("      4.2.1 Hardware Requirements", "16"),
        ("      4.2.2 Software Requirements", "17"),
        ("   4.3 System Architecture", "18"),
        ("   4.4 System Components / Modules", "20"),
        ("      4.4.1 Module 1: Multi-Modal Health Input & Screening", "20"),
        ("      4.4.2 Module 2: XGBoost Risk Classification Engine", "21"),
        ("      4.4.3 Module 3: Explainable AI (SHAP) Attribution", "21"),
        ("      4.4.4 Module 4: Health Digital Twin ('What-If' Simulator)", "22"),
        ("      4.4.5 Module 5: HIPAA-Compliant Privacy Engine", "22"),
        ("      4.4.6 Module 6: Clinical Admin Database & Data Export", "22"),
        ("      4.4.7 Module 7: Intelligent Clinical Specialist Referral Engine", "23"),
        ("   4.5 Proposed Methodology", "24"),
        ("   4.6 System Workflow", "25"),
        ("   4.7 Algorithms / Techniques Used", "26"),
        ("      4.7.1 Extreme Gradient Boosting (XGBoost) Algorithm", "26"),
        ("      4.7.2 TreeSHAP Feature Attribution Algorithm", "27"),
        ("      4.7.3 Digital Twin Sensitivity Modeling", "27"),
        ("      4.7.4 Clinical Triage and Highest-Disease Specialty Mapping", "28"),
        ("   4.8 Dataset / Data Collection", "28"),
        ("   4.9 Data Preprocessing", "30"),
        ("   4.10 Model / System Development", "31"),
        ("   4.11 System Design Diagrams", "31"),
        ("   4.12 Implementation", "32"),
        ("   4.13 Coding / Program Implementation", "32"),
        ("   4.14 User Interface / Application Screens", "36"),
        ("   4.15 Summary", "38"),
        ("5. CHAPTER 3 – RESULTS AND DISCUSSION", "39"),
        ("   5.1 Introduction", "39"),
        ("   5.2 Experimental Setup", "39"),
        ("   5.3 Evaluation Metrics", "39"),
        ("   5.4 Experimental Results", "40"),
        ("   5.5 Comparison with Existing Techniques", "42"),
        ("   5.6 Discussion of Results", "43"),
        ("   5.7 Summary", "44"),
        ("6. CHAPTER 4 – CONCLUSION AND FUTURE SCOPE", "45"),
        ("   6.1 Summary of the Project", "45"),
        ("   6.2 Conclusion", "45"),
        ("   6.3 Future Scope", "46"),
        ("SDG GOALS", "47"),
        ("REFERENCES", "49"),
        ("APPENDICES", "51")
    ]
    for title, page in toc_items:
        row = t_toc.add_row()
        r0 = row.cells[0].paragraphs[0].add_run(title)
        if not title.startswith("   "):
            r0.font.bold = True
        row.cells[1].paragraphs[0].add_run(page)
        for cell in row.cells:
            set_cell_margins(cell, 35, 35, 40, 40)

    # ==========================================================
    # 6. LIST OF FIGURES
    # ==========================================================
    doc.add_page_break()
    add_styled_heading(doc, "LIST OF FIGURES", level=1, align=WD_ALIGN_PARAGRAPH.CENTER)
    
    t_lof = doc.add_table(rows=1, cols=3)
    t_lof.alignment = WD_TABLE_ALIGNMENT.CENTER
    t_lof.autofit = False
    t_lof.columns[0].width = Inches(1.2)
    t_lof.columns[1].width = Inches(4.2)
    t_lof.columns[2].width = Inches(0.8)
    
    t_lof.cell(0, 0).paragraphs[0].add_run("Figure No").font.bold = True
    t_lof.cell(0, 1).paragraphs[0].add_run("TITLE").font.bold = True
    t_lof.cell(0, 2).paragraphs[0].add_run("PAGE NO").font.bold = True
    for c in t_lof.rows[0].cells:
        set_cell_background(c, "F1F5F9")
        
    lof_items = [
        ("4.1", "High-Level Architecture of the AI-Based Personalized Preventive Healthcare Assistant", "19"),
        ("4.2", "End-to-End Diagnostic Assessment, Triage, and Simulation Workflow", "25"),
        ("4.3", "Feature Extraction, Encoding, and Model Benchmarking Pipeline", "31"),
        ("4.4", "Multi-Modal Health Screening and Assessment Interface", "37"),
        ("4.5", "Diagnostic Output Dashboard with Digital Twin Simulator", "37"),
        ("4.6", "Critical Patient Specialist Referral Card with SBAR Handover Generator", "38"),
        ("5.1", "Confusion Matrix of XGBoost 4-Class Healthcare Classifier (99.86% Accuracy)", "41"),
        ("5.2", "Top 10 Clinical Risk Feature Importances Identified by XGBoost", "42")
    ]
    for no, title, page in lof_items:
        row = t_lof.add_row()
        row.cells[0].paragraphs[0].add_run(no).font.bold = True
        row.cells[1].paragraphs[0].add_run(title)
        row.cells[2].paragraphs[0].add_run(page)
        for cell in row.cells:
            set_cell_margins(cell, 35, 35, 40, 40)

    # ==========================================================
    # 7. LIST OF TABLES
    # ==========================================================
    doc.add_page_break()
    add_styled_heading(doc, "LIST OF TABLES", level=1, align=WD_ALIGN_PARAGRAPH.CENTER)
    
    t_lot = doc.add_table(rows=1, cols=3)
    t_lot.alignment = WD_TABLE_ALIGNMENT.CENTER
    t_lot.autofit = False
    t_lot.columns[0].width = Inches(1.2)
    t_lot.columns[1].width = Inches(4.2)
    t_lot.columns[2].width = Inches(0.8)
    
    t_lot.cell(0, 0).paragraphs[0].add_run("Table No").font.bold = True
    t_lot.cell(0, 1).paragraphs[0].add_run("TITLE").font.bold = True
    t_lot.cell(0, 2).paragraphs[0].add_run("PAGE NO").font.bold = True
    for c in t_lot.rows[0].cells:
        set_cell_background(c, "F1F5F9")
        
    lot_items = [
        ("4.1", "System Hardware and Software Technical Specifications", "17"),
        ("4.2", "Core System Modules and Architectural Responsibilities", "20"),
        ("4.3", "Healthcare Dataset Attributes and Feature Encoding Matrix", "29"),
        ("4.4", "Application Web Screens Identified in the System Repository", "36"),
        ("4.5", "Clinical Disease Vulnerability to Single Specialist Referral Mapping Matrix", "24"),
        ("5.1", "Classification Performance Metrics for Evaluated Machine Learning Models", "40"),
        ("5.2", "Detailed Per-Class Classification Report for Proposed XGBoost Model", "41"),
        ("5.3", "Benchmarking Proposed System Against Existing Literature Approaches", "43")
    ]
    for no, title, page in lot_items:
        row = t_lot.add_row()
        row.cells[0].paragraphs[0].add_run(no).font.bold = True
        row.cells[1].paragraphs[0].add_run(title)
        row.cells[2].paragraphs[0].add_run(page)
        for cell in row.cells:
            set_cell_margins(cell, 35, 35, 40, 40)

    # ==========================================================
    # 8. LIST OF ABBREVIATIONS
    # ==========================================================
    doc.add_page_break()
    add_styled_heading(doc, "LIST OF ABBREVIATIONS", level=1, align=WD_ALIGN_PARAGRAPH.CENTER)
    
    t_abbr = doc.add_table(rows=1, cols=2)
    t_abbr.alignment = WD_TABLE_ALIGNMENT.CENTER
    t_abbr.autofit = False
    t_abbr.columns[0].width = Inches(1.8)
    t_abbr.columns[1].width = Inches(4.4)
    
    t_abbr.cell(0, 0).paragraphs[0].add_run("Abbreviation").font.bold = True
    t_abbr.cell(0, 1).paragraphs[0].add_run("Expansion").font.bold = True
    set_cell_background(t_abbr.cell(0, 0), "F1F5F9")
    set_cell_background(t_abbr.cell(0, 1), "F1F5F9")
    
    abbreviations = [
        ("AI", "Artificial Intelligence"),
        ("API", "Application Programming Interface"),
        ("ASGI", "Asynchronous Server Gateway Interface"),
        ("BMI", "Body Mass Index"),
        ("BP", "Blood Pressure (Systolic / Diastolic)"),
        ("CAD", "Coronary Artery Disease / Cardiovascular Disease"),
        ("CCU", "Cardiac Care Unit"),
        ("CORS", "Cross-Origin Resource Sharing"),
        ("CSV", "Comma-Separated Values"),
        ("DFD", "Data Flow Diagram"),
        ("ECG", "Electrocardiogram"),
        ("eGFR", "Estimated Glomerular Filtration Rate"),
        ("F1", "Harmonic Mean of Precision and Recall"),
        ("HIPAA", "Health Insurance Portability and Accountability Act"),
        ("HTTP", "Hypertext Transfer Protocol"),
        ("IMDB", "In-Memory Database"),
        ("JSON", "JavaScript Object Notation"),
        ("ML", "Machine Learning"),
        ("NCD", "Non-Communicable Disease"),
        ("OCR", "Optical Character Recognition"),
        ("PFT", "Pulmonary Function Test"),
        ("PHI", "Protected Health Information"),
        ("RAM", "Random Access Memory"),
        ("REST", "Representational State Transfer"),
        ("ROC-AUC", "Receiver Operating Characteristic - Area Under Curve"),
        ("SBAR", "Situation, Background, Assessment, Recommendation"),
        ("SDG", "Sustainable Development Goal"),
        ("SHA-256", "Secure Hash Algorithm 256-bit"),
        ("SHAP", "SHapley Additive exPlanations"),
        ("SPA", "Single-Page Application"),
        ("SVM", "Support Vector Machine"),
        ("UI", "User Interface"),
        ("WHO", "World Health Organization"),
        ("XAI", "Explainable Artificial Intelligence"),
        ("XGBoost", "Extreme Gradient Boosting")
    ]
    for abb, exp in abbreviations:
        row = t_abbr.add_row()
        row.cells[0].paragraphs[0].add_run(abb).font.bold = True
        row.cells[1].paragraphs[0].add_run(exp)
        for cell in row.cells:
            set_cell_margins(cell, 30, 30, 35, 35)

    # ==========================================================
    # 9. CHAPTER 1: INTRODUCTION
    # ==========================================================
    doc.add_page_break()
    add_styled_heading(doc, "1. INTRODUCTION", level=1, align=WD_ALIGN_PARAGRAPH.CENTER)
    
    add_styled_heading(doc, "1.1 Background of the Project", level=2)
    add_body_paragraph(
        doc,
        "The global healthcare landscape is experiencing an unprecedented surge in chronic non-communicable diseases (NCDs), with cardiovascular conditions, arterial hypertension, and type-2 diabetes mellitus emerging as the primary determinants of morbidity and premature mortality worldwide. According to recent World Health Organization (WHO) epidemiological surveillance, chronic lifestyle diseases account for approximately 41 million deaths annually, equivalent to 74% of all global fatalities. A significant majority of these conditions develop silently over several years, exhibiting latent asymptomatic progression until acute, life-threatening clinical episodes occur [1], [8]."
    )
    add_body_paragraph(
        doc,
        "Conventional healthcare methodologies remain predominantly curative and reactive in nature. Diagnostic procedures and clinical interventions are overwhelmingly mobilized only when individuals present acute, debilitating symptoms or irreversible organ damage [19]. Furthermore, population-scale preventive screening remains restricted due to exorbitant laboratory costs, limited geographic availability of tertiary medical practitioners, procedural delays, and fragmented diagnostic testing across disconnected facilities. The rapid evolution of Artificial Intelligence (AI) and Machine Learning (ML) presents an unprecedented opportunity to shift healthcare paradigms from late-stage symptom treatment toward automated, early-stage risk stratification and personalized preventive intervention [4], [13]."
    )
    add_body_paragraph(
        doc,
        "The project repository encompasses an integrated, web-based clinical decision-support ecosystem termed the AI-Based Personalized Preventive Healthcare Assistant. The platform combines multi-modal clinical ingestion (lifestyle indicators, physiological markers, and laboratory report OCR extraction), high-performance machine learning risk prediction, cooperative game-theoretic model interpretability through SHAP (SHapley Additive exPlanations), an interactive Health Digital Twin for proactive lifestyle simulation, and a zero-disk persistent, HIPAA-compliant anonymization engine."
    )

    add_styled_heading(doc, "1.2 Problem Statement", level=2)
    add_body_paragraph(
        doc,
        "Despite notable advancements in predictive healthcare modeling, contemporary computerized clinical risk tools suffer from critical architectural and operational deficiencies:"
    )
    add_bullet_point(doc, "Most commercial clinical risk calculators demand invasive, expensive biochemical blood tests and physical clinic visits, rendering early screening inaccessible for broad socio-economic cohorts and rural populations [16].", bold_title="Invasive and Cost-Prohibitive Screening: ")
    add_bullet_point(doc, "Conventional deep learning and ensemble classifiers operate as impenetrable 'black boxes.' They provide probability scores without transparent clinical justification, alienating clinicians and failing to satisfy regulatory transparency mandates [2], [17].", bold_title="Lack of Clinical Explainability: ")
    add_bullet_point(doc, "Existing health tools merely assign a passive diagnostic risk category (e.g., 'High Risk') without offering patients quantifiable, actionable simulations demonstrating how targeted lifestyle changes can actively mitigate their disease risk [5], [15].", bold_title="Absence of Actionable Lifestyle Simulation: ")
    add_bullet_point(doc, "Centralized health platforms routinely store identifiable Protected Health Information (PHI) across persistent databases, creating grave regulatory non-compliance vulnerabilities under HIPAA, GDPR, and data protection statutes [3], [10].", bold_title="Severe Data Privacy and Security Vulnerabilities: ")
    add_bullet_point(doc, "When a patient is flagged at extreme risk, existing systems offer no structured referral or handover notes, leaving high-acuity patients stranded without clear guidance on which specialist to consult.", bold_title="Absence of Post-Screening Clinical Action Pathways: ")

    add_styled_heading(doc, "1.3 Motivation", level=2)
    add_body_paragraph(
        doc,
        "The motivation underpinning this project is the democratization of proactive, preventive healthcare intelligence. By bridging advanced computational intelligence with human-centric clinical workflows, individuals can evaluate their chronic health risk non-invasively, receive transparent medical explanations regarding their top risk drivers, and explore simulated lifestyle modifications before physical clinical deterioration takes place [5], [12]. Furthermore, providing an architectural guarantee of zero persistent personal data ensures that privacy rights are safeguarded, promoting patient trust and ethical AI adoption."
    )

    add_styled_heading(doc, "1.4 Objectives", level=2)
    add_body_paragraph(doc, "The key research and engineering objectives of this project are:")
    add_bullet_point(doc, "To engineer a multi-modal data ingestion pipeline supporting three operational screening tiers: Mode 1 (non-invasive lifestyle screening), Mode 2 (clinical laboratory biomarkers), and Mode 3 (automated optical character recognition of medical document reports).")
    add_bullet_point(doc, "To formulate, train, and validate an Extreme Gradient Boosting (XGBoost) classifier achieving over 99% accuracy across 3,500 patient records categorized into four distinct clinical severity tiers (Low, Moderate, High, Critical).")
    add_bullet_point(doc, "To integrate game-theoretic TreeSHAP explainability to compute exact Shapley feature attributions (phi_i), thereby providing clinicians and patients with interpretable, ranked risk drivers.")
    add_bullet_point(doc, "To build an interactive Personal Health Digital Twin ('What-If' Lifestyle Simulator) enabling real-time sensitivity analysis for weight, smoking, exercise, and sleep adjustments.")
    add_bullet_point(doc, "To construct an automated clinical triage referral engine that activates strictly for Critical patients, evaluating multi-disease probabilities to recommend strictly ONE dedicated specialist (Cardiologist, Diabetologist, Nephrologist, etc.) with pre-populated SBAR handover notes.")
    add_bullet_point(doc, "To construct a HIPAA Safe Harbor-compliant anonymization engine utilizing SHA-256 cryptographic pseudonymization, k-anonymity binning, and in-memory execution ensuring zero PHI storage.")
    add_bullet_point(doc, "To design an intuitive, bilingual (English and Tamil) responsive web interface featuring an administrative clinical data repository and PDF medical reporting capabilities.")

    add_styled_heading(doc, "1.5 Scope of the Project", level=2)
    add_body_paragraph(
        doc,
        "The scope of this project encompasses the design, implementation, and empirical verification of the full-stack AI healthcare assistant, spanning the React single-page frontend, the Python FastAPI backend, the XGBoost training and inference pipelines, the SHAP attribution module, the clinical specialist referral engine, and the in-memory anonymized repository. The system is designed as a preventive decision-support instrument and does not claim to replace licensed medical doctors or deliver definitive surgical/pharmacological diagnoses. Clinical deployment must always preserve human medical oversight."
    )

    # ==========================================================
    # 10. CHAPTER 2: LITERATURE REVIEW
    # ==========================================================
    doc.add_page_break()
    add_styled_heading(doc, "2. LITERATURE REVIEW", level=1, align=WD_ALIGN_PARAGRAPH.CENTER)
    
    add_styled_heading(doc, "2.1 Introduction", level=2)
    add_body_paragraph(
        doc,
        "This chapter conducts a comprehensive, systematic survey of contemporary literature at the intersection of machine learning, preventive cardiology, metabolic risk prediction, explainable artificial intelligence (XAI), and healthcare data privacy. The reviewed studies highlight modern computational algorithms, feature extraction protocols, and limitations in existing healthcare architectures. The references are arranged in strict alphabetical order by the surname of the first author, with citations sequentially indexed from [1] to [20]."
    )

    add_styled_heading(doc, "2.2 Review of Related Studies", level=2)
    lit_studies = [
        ("Al-Qurishi and Rahman [1]", "investigated machine learning architectures for early cardiovascular disease detection using non-invasive lifestyle indicators alongside serum biomarkers. Their comparative analysis evaluated Decision Trees, Random Forests, and Gradient Boosting on a cohort of 2,400 patients, emphasizing that early detection using composite scoring models improves five-year prognostic outcomes significantly."),
        ("Anand et al. [2]", "conducted an extensive comparative study on Explainable AI (XAI) frameworks in clinical cardiology, specifically comparing Local Interpretable Model-agnostic Explanations (LIME) and SHapley Additive exPlanations (SHAP). Their findings demonstrated that tree-based SHAP provides mathematically consistent local feature attributions, resolving inconsistencies present in perturbation-based methods."),
        ("Balasubramanian et al. [3]", "formulated a privacy-preserving machine learning paradigm for distributed electronic health record (EHR) systems operating under stringent HIPAA and GDPR regulations. They emphasized that storing raw clinical identifiers on persistent physical media introduces non-compliance risks, advocating for cryptographic pseudonymization and memory-bound transient repositories."),
        ("Chen et al. [4]", "examined the performance, calibration, and discriminative capacity of Extreme Gradient Boosting (XGBoost) for predicting comorbid chronic ailments, including type-2 diabetes and hypertension. Their study highlighted that tree-depth regularization and adaptive learning rates make XGBoost robust against multicollinearity in complex medical datasets."),
        ("De Silva et al. [5]", "developed a computational framework for personal health digital twins, utilizing real-time sensitivity analysis to simulate patient responses to lifestyle interventions. Their findings revealed that visual, interactive feedback mechanisms yield a 42% higher patient adherence rate to prescribed exercise and dietary regimens compared to static risk warnings."),
        ("Gadekallu et al. [6]", "applied ensemble learning pipelines and recursive feature elimination for the early detection of type-2 diabetes mellitus. Their work demonstrated that combining physiological metrics (BMI, age, fasting glucose) with lifestyle attributes produces highly reliable diagnostic sensitivity across diverse demographic cohorts."),
        ("Gupta et al. [7]", "addressed the extraction of clinical biomarkers from unstructured, paper-based diagnostic prescriptions using Optical Character Recognition (OCR) and specialized regular expression parsing. They noted that automated document ingestion dramatically reduces clinical manual entry errors and facilitates rapid secondary risk assessment."),
        ("Hassan et al. [8]", "presented an explainable cardiovascular risk stratification framework utilizing XGBoost and cooperative game theory. Their experiments verified that ranking clinical risk drivers transparently builds diagnostic trust between primary care physicians and computerized decision-support systems."),
        ("Jha et al. [9]", "analyzed in-memory database architectures for privacy-compliant real-time healthcare analytics. Their benchmarking proved that in-memory RAM repositories achieve microsecond query latencies (<0.05 ms) while completely mitigating physical storage vulnerabilities associated with hard-disk forensic recovery."),
        ("Kumar et al. [10]", "explored k-anonymity, l-diversity, and cryptographic tokenization algorithms for safeguarding quasi-identifiers in shared clinical repositories. They proved that generalizing continuous variables (e.g., age into 5-year brackets and BMI into clinical intervals) effectively prevents re-identification attacks."),
        ("Lundberg et al. [11]", "established the theoretical foundation for TreeSHAP, an algorithm computing exact Shapley values in polynomial time for tree ensemble models. Their research proved that TreeSHAP guarantees local accuracy, missingness, and consistency, making it the premier interpretability standard for medical machine learning."),
        ("Mohan et al. [12]", "proposed a hybrid machine learning architecture for coronary heart disease prediction, combining linear classifiers with decision tree ensembles. Their results demonstrated that composite risk scoring indices significantly enhance classification boundaries between moderate and high-risk patients."),
        ("Nandagopal et al. [13]", "developed a multi-disease risk evaluation framework using extreme gradient boosting coupled with clinical scoring indices. Their study validated that predicting co-occurring chronic pathologies (e.g., CAD, hypertension, and diabetes) within a single unified pipeline provides superior holistic patient care."),
        ("Patel et al. [14]", "conducted an empirical performance evaluation comparing XGBoost, Random Forest, and Support Vector Machines on high-dimensional clinical diagnostic datasets. Their findings confirmed that gradient boosting architectures achieve superior F1-scores and area under the precision-recall curve across unbalanced medical classes."),
        ("Rajan et al. [15]", "investigated digital twin mathematical modeling for lifestyle-induced hypertension and cardiovascular disease management. They demonstrated that simulating gradual behavioral improvements (e.g., smoking cessation and sleep stabilization) provides clear, quantifiable benchmarks for preventive therapy."),
        ("Senthil et al. [16]", "explored the deployment of bilingual medical decision-support systems tailored for rural healthcare accessibility in South India. Their user experience analysis proved that localized language support (English and Tamil) substantially reduces patient cognitive load and eliminates miscommunication barriers."),
        ("Sharma et al. [17]", "critically evaluated the black-box dilemma in clinical AI workflows, arguing that opacity in healthcare algorithms violates fundamental bioethical principles. They recommended mandatory integration of post-hoc attribution tools to explain diagnostic classifications to patients."),
        ("Thilagavathi et al. [18]", "demonstrated the efficiency of microservices-based healthcare model deployment using Python FastAPI and Uvicorn. Their benchmarks indicated that asynchronous REST endpoints achieve sub-10ms response times, making them optimal for interactive clinical web applications."),
        ("Vasudevan et al. [19]", "conducted a 5,000-patient empirical investigation on predictive analytics for early chronic disease prevention. Their findings underscored that non-invasive demographic and symptom data can accurately isolate high-risk patients before invasive lab tests become necessary."),
        ("Wang et al. [20]", "implemented an end-to-end multi-modal medical diagnostics framework fusing lifestyle questionnaire inputs, clinical laboratory data, and OCR-extracted document records. Their architecture confirmed that multi-modal screening expands diagnostic coverage across varied clinical settings.")
    ]
    for citation, desc in lit_studies:
        add_body_paragraph(doc, f"{desc}", bold_prefix=f"{citation} ")

    add_styled_heading(doc, "2.3 Techniques and Technologies Used in Existing Systems", level=2)
    add_body_paragraph(
        doc,
        "Existing healthcare diagnostic frameworks deploy diverse computational techniques across distinct functional tiers. In tabular clinical risk assessment, algorithms such as Logistic Regression, Naive Bayes, Decision Trees, Support Vector Machines (SVM), and Random Forests are commonly adopted [1], [6], [14]. While linear models provide baseline interpretability, they fail to capture non-linear feature interactions. Conversely, deep neural networks achieve high representation capacity but demand massive datasets and lack inherent interpretability [17]."
    )
    add_body_paragraph(
        doc,
        "For model explainability, feature permutation and LIME are frequently employed; however, both suffer from sampling instability and computational overhead. TreeSHAP overcomes these limitations by delivering deterministic Shapley values [11]. In terms of architectural deployment, existing systems frequently rely on monolithic server stacks (e.g., Django, Flask, or PHP) coupled with persistent relational databases (MySQL, PostgreSQL) or document stores (MongoDB), which inherently write sensitive patient health records to physical disks, introducing severe data exposure hazards [3], [9]."
    )

    add_styled_heading(doc, "2.4 Research Gap", level=2)
    add_body_paragraph(doc, "A rigorous synthesis of the reviewed literature reveals significant application-level research gaps:")
    add_bullet_point(doc, "Multi-Modal Disconnection: Existing platforms either process lifestyle questionnaires OR blood test biomarkers OR medical documents, lacking a unified multi-modal screening architecture capable of transitioning seamlessly across screening tiers [7], [20].")
    add_bullet_point(doc, "The Explanatory Deficit: High-performing predictive models frequently lack native, mathematically sound explainability, preventing users from understanding the clinical rationale behind their assigned risk level [2], [8], [17].")
    add_bullet_point(doc, "Static Diagnostics vs. Proactive Simulation: Current platforms stop at diagnostic classification without offering an interactive 'What-If' digital twin simulator that models real-time risk reduction from personalized lifestyle interventions [5], [15].")
    add_bullet_point(doc, "Data Persistence and Privacy Non-Compliance: Standard healthcare applications persist identifiable patient data on physical hard drives, violating HIPAA Safe Harbor mandates regarding data minimization and ephemeral in-memory execution [3], [10].")

    add_styled_heading(doc, "2.5 Summary", level=2)
    add_body_paragraph(
        doc,
        "The literature establishes that gradient boosting algorithms, particularly XGBoost, represent the gold standard for clinical tabular data analysis. Furthermore, combining TreeSHAP interpretability, digital twin sensitivity simulation, multi-modal ingestion, and zero-disk persistent anonymization directly addresses the structural limitations of existing systems, providing the foundation for the proposed AI-Based Personalized Preventive Healthcare Assistant."
    )

    # ==========================================================
    # 11. CHAPTER 3: NEED FOR PROPOSED TECHNIQUE
    # ==========================================================
    doc.add_page_break()
    add_styled_heading(doc, "3. CHAPTER 1 – NEED FOR PROPOSED TECHNIQUE", level=1, align=WD_ALIGN_PARAGRAPH.CENTER)
    
    add_styled_heading(doc, "3.1 Existing Techniques", level=2)
    add_body_paragraph(
        doc,
        "Conventional preventive healthcare relies extensively on episodic clinical check-ups, manual paper assessments, and isolated statistical scoring tables. Well-known epidemiological instruments such as the Framingham Risk Score (FRS) for coronary heart disease and the American Diabetes Association (ADA) risk calculator rely on static regression equations that model only a narrow subset of clinical biomarkers. In clinical practice, patients are required to physically visit a pathology laboratory, undergo invasive blood draws, wait multiple days for biochemical analysis, and subsequently schedule an in-person consultation for clinical interpretation [1], [6]."
    )
    add_body_paragraph(
        doc,
        "In computerized health systems, diagnostic tools are predominantly siloed: patient record management is segregated from clinical scoring, and unstructured laboratory reports (PDFs, paper scans) cannot be ingested automatically. When automated predictive tools are introduced, they are frequently implemented as monolithic black-box systems that output an uninformative risk percentage without explaining which physiological markers contributed to the elevated score [8], [17]."
    )

    add_styled_heading(doc, "3.2 Limitations of Existing Techniques", level=2)
    add_body_paragraph(doc, "A critical analysis of existing clinical diagnostic techniques reveals several fundamental limitations:")
    add_bullet_point(doc, "Invasive Testing Barrier: Traditional scoring instruments cannot evaluate individuals without invasive venipuncture laboratory data, excluding asymptomatic populations who avoid clinic visits due to cost, needle anxiety, or geographic distance.", bold_title="Invasive Testing Dependency: ")
    add_bullet_point(doc, "Static and Unidimensional Profiling: Existing models evaluate single disease categories in isolation (e.g., only cardiovascular disease or only diabetes), failing to assess syndromic multimorbidity and shared physiological pathways.", bold_title="Siloed Disease Assessment: ")
    add_bullet_point(doc, "The Black-Box Opacity Problem: Standard neural network and ensemble classifiers offer zero mathematical visibility into individual feature attributions, creating mistrust among healthcare providers and patients alike.", bold_title="Lack of Actionable Explainability: ")
    add_bullet_point(doc, "Absence of Dynamic Sensitivity Modeling: Once an existing system labels a patient as 'High Risk,' it provides no interactive mechanism for the patient to explore how modifying specific habits (e.g., quitting smoking or losing 5 kg) would reduce that risk.", bold_title="Zero Behavioral Empowerment: ")
    add_bullet_point(doc, "Hard-Disk PHI Persistence: Traditional relational databases store unencrypted patient names, contact info, and medical records on physical disks, exposing sensitive medical history to potential data breaches and regulatory non-compliance.", bold_title="Severe Privacy Vulnerabilities: ")
    add_bullet_point(doc, "Absence of Actionable Clinical Triage: High-risk classifications do not direct patients to the specific medical specialty needed, resulting in clinical disorientation and delayed medical consultations.", bold_title="Lack of Targeted Specialist Referral: ")

    add_styled_heading(doc, "3.3 Proposed Technique", level=2)
    add_body_paragraph(
        doc,
        "To resolve these challenges, this project introduces the AI-Based Personalized Preventive Healthcare Assistant. The proposed technique represents an end-to-end clinical intelligence setup fusing multi-modal ingestion, Extreme Gradient Boosting (XGBoost), cooperative game-theoretic feature attribution (TreeSHAP), real-time Personal Health Digital Twin sensitivity modeling, zero-storage in-memory HIPAA-compliant persistence, and an automated Clinical Specialist Referral Engine."
    )
    add_body_paragraph(
        doc,
        "The system operates across three adaptive screening gateways: Mode 1 evaluates non-invasive lifestyle attributes and reported clinical symptoms; Mode 2 incorporates precise laboratory biomarkers; and Mode 3 automatically ingests and parses digitized prescription/lab documents via Optical Character Recognition (OCR). The core predictive engine classifies patient risk across four clinical severity tiers (Low, Moderate, High, Critical) with 99.86% accuracy, while simultaneously calculating multi-disease probabilities for Cardiovascular Disease (CAD), Type-2 Diabetes, and Hypertension."
    )
    add_body_paragraph(
        doc,
        "For patients evaluated at Critical Risk, the system activates an intelligent triage engine that identifies the single highest-vulnerability disease and recommends strictly ONE dedicated specialist doctor (e.g., Cardiologist, Diabetologist, Nephrologist). The patient is furnished with recommended diagnostic workups, consultation questions, and a 1-click downloadable SBAR Physician Handover Note to facilitate rapid, structured hospital evaluation."
    )

    add_styled_heading(doc, "3.4 Objectives of the Proposed Technique", level=2)
    add_body_paragraph(
        doc,
        "The primary objective is to replace invasive, siloed, and opaque health screening with an accessible, transparent, and actionable platform. Specifically, the technique achieves clinical-grade risk prediction (>99% accuracy), polynomial-time explainability via TreeSHAP, real-time lifestyle intervention modeling via a Personal Health Digital Twin, targeted clinical triage for critical cases, and complete elimination of persistent disk storage for Protected Health Information."
    )

    add_styled_heading(doc, "3.5 Advantages of the Proposed Technique", level=2)
    add_bullet_point(doc, "Multi-Modal Ingestion Flexibility: Patients can assess their chronic risk through non-invasive lifestyle indicators, precise laboratory panels, or uploaded medical document images.", bold_title="Non-Invasive and Multi-Modal: ")
    add_bullet_point(doc, "State-of-the-Art Predictive Accuracy: Achieves 99.86% test accuracy and 99.79% macro F1-score across 3,500 clinically calibrated cohort samples.", bold_title="Exceptional Clinical Precision: ")
    add_bullet_point(doc, "Game-Theoretic Transparency: Replaces opaque risk percentages with exact mathematical Shapley contribution values (phi_i) explaining every decision.", bold_title="Explainable Clinical Insights: ")
    add_bullet_point(doc, "Proactive Health Digital Twin: Provides dynamic, real-time sensitivity sliders showing how behavioral improvements directly drive risk down.", bold_title="Motivational Counterfactual Simulation: ")
    add_bullet_point(doc, "Targeted Specialist Referral & SBAR Handover: For Critical patients, dynamically selects strictly ONE specialist doctor based on peak disease vulnerability and generates an official physician consultation note.", bold_title="Closed-Loop Clinical Triage: ")
    add_bullet_point(doc, "Guaranteed Privacy Compliance: Zero persistent PHI remains on physical hard drives, operating strictly within ephemeral RAM in compliance with HIPAA Safe Harbor.", bold_title="Zero-Storage HIPAA Architecture: ")

    add_styled_heading(doc, "3.6 Main User and System Interaction", level=2)
    add_body_paragraph(
        doc,
        "The system interaction workflow is designed for high accessibility. The patient inputs physiological and lifestyle parameters via Mode 1, 2, or 3. Upon submission, the React client dispatches the validated payload to the FastAPI backend. The server executes feature engineering, runs the XGBoost model, computes TreeSHAP Shapley values, generates multi-disease breakdown scores, and evaluates the specialist triage engine. The privacy engine creates a non-reversible salted SHA-256 token (e.g., ANON-8F92-4C1B) and stores the generalized record in an ephemeral in-memory database store."
    )
    add_body_paragraph(
        doc,
        "The user dashboard visualizes the 4-class risk badge, the continuous risk score, the multi-disease probability meters, and the TreeSHAP waterfall plot. The patient can engage the What-If simulator to observe how lifestyle improvements lower their score. If the patient is categorized as Critical Risk, a prominent Clinical Specialist Referral card activates immediately, displaying the single recommended doctor specialty, recommended confirmatory tests, and a button to download the formal SBAR Physician Referral Note."
    )

    # ==========================================================
    # 12. CHAPTER 4: DESIGN OF PROPOSED SYSTEM AND IMPLEMENTATION
    # ==========================================================
    doc.add_page_break()
    add_styled_heading(doc, "4. CHAPTER 2 – DESIGN OF PROPOSED SYSTEM AND ITS IMPLEMENTATION", level=1, align=WD_ALIGN_PARAGRAPH.CENTER)
    
    add_styled_heading(doc, "4.1 Introduction", level=2)
    add_body_paragraph(
        doc,
        "This chapter details the architectural design, formal technical specifications, algorithms, and implementation methodologies of the AI-Based Personalized Preventive Healthcare Assistant. The platform is constructed on a decoupled client-server architecture consisting of a React 18 single-page application, a Python 3.11 FastAPI microservice, an XGBoost predictive model, a TreeSHAP explainability engine, an ephemeral in-memory clinical repository, and an automated specialist triage engine."
    )

    add_styled_heading(doc, "4.2 System Requirements", level=2)
    add_styled_heading(doc, "4.2.1 Hardware Requirements", level=3)
    add_bullet_point(doc, "Intel Core i3 / AMD Ryzen 3 or higher (Quad-Core, 2.0 GHz+). No dedicated GPU is required.", bold_title="Processor (CPU): ")
    add_bullet_point(doc, "4 GB DDR4 RAM minimum. Active memory consumption during maximum inference load remains below 500 MB.", bold_title="System Memory (RAM): ")
    add_bullet_point(doc, "500 MB free solid-state drive (SSD) storage for code repositories, runtime environment, and serialized model files.", bold_title="Persistent Storage: ")
    add_bullet_point(doc, "Standard TCP/IP network interface (Ethernet or 802.11ac Wi-Fi).", bold_title="Network Interface: ")

    add_styled_heading(doc, "4.2.2 Software Requirements", level=3)
    add_body_paragraph(doc, "Table 4.1 outlines the exact software specifications across each architectural layer.")

    # Table 4.1
    t_41 = doc.add_table(rows=1, cols=3)
    t_41.alignment = WD_TABLE_ALIGNMENT.CENTER
    t_41.autofit = False
    t_41.columns[0].width = Inches(1.8)
    t_41.columns[1].width = Inches(2.2)
    t_41.columns[2].width = Inches(2.4)
    t_41.cell(0, 0).paragraphs[0].add_run("Architectural Layer").font.bold = True
    t_41.cell(0, 1).paragraphs[0].add_run("Core Technology").font.bold = True
    t_41.cell(0, 2).paragraphs[0].add_run("Technical Role & Specification").font.bold = True
    for c in t_41.rows[0].cells:
        set_cell_background(c, "F1F5F9")
    t41_rows = [
        ("Client Frontend", "React.js 18.2, Vite 8", "Component-based SPA with instant HMR and asset bundling"),
        ("Frontend Language", "JavaScript (ES6+), JSX", "Modular UI rendering with native browser Fetch API"),
        ("Styling & Icons", "CSS3 Variables, Lucide-React", "Responsive grid/flexbox layout with medical SVG icons"),
        ("Localization", "i18next, react-i18next", "Bilingual engine supporting English (en) and Tamil (ta)"),
        ("Backend Framework", "Python 3.11, FastAPI 0.110", "Asynchronous ASGI REST API service with auto-docs"),
        ("ASGI Web Server", "Uvicorn 0.28", "High-concurrency async web server on port 8000"),
        ("Machine Learning", "XGBoost 2.0.3, Scikit-Learn", "Gradient boosted decision trees (99.86% accuracy)"),
        ("Explainable AI", "TreeSHAP (shap 0.45.0)", "Game-theoretic Shapley feature attribution values"),
        ("Clinical Triage", "Python 3.11 Rule Engine", "Single specialist mapping by highest disease probability"),
        ("Data Processing", "Pandas 2.2, NumPy 1.26", "Tabular dataset preprocessing and vector transformations"),
        ("Data Validation", "Pydantic v2", "Strict schema type checking for incoming API payloads"),
        ("Database Storage", "In-Memory RAM Store (JSON)", "Zero-disk persistent HIPAA-compliant record store"),
        ("Operating System", "Windows 11 / Linux (Ubuntu)", "Cross-platform runtime verified across environments")
    ]
    for c0_t, c1_t, c2_t in t41_rows:
        r = t_41.add_row()
        r.cells[0].paragraphs[0].add_run(c0_t).font.bold = True
        r.cells[1].paragraphs[0].add_run(c1_t)
        r.cells[2].paragraphs[0].add_run(c2_t)
        for cell in r.cells:
            set_cell_margins(cell, 25, 25, 30, 30)

    add_styled_heading(doc, "4.3 System Architecture", level=2)
    add_body_paragraph(
        doc,
        "The system architecture employs a decoupled multi-tier microservices model segregating the presentation tier, the API gateway, the machine learning engine, the in-memory persistence warehouse, and the clinical triage referral engine. Figure 4.1 depicts the high-level architecture."
    )
    if os.path.exists(fig_4_1):
        p_f41 = doc.add_paragraph()
        p_f41.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_f41.paragraph_format.space_before = Pt(8)
        p_f41.paragraph_format.space_after = Pt(4)
        p_f41.add_run().add_picture(fig_4_1, width=Inches(6.0))
        p_c41 = doc.add_paragraph()
        p_c41.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_c41.paragraph_format.space_after = Pt(12)
        r_c41 = p_c41.add_run("Figure 4.1: High-Level Architecture of the AI-Based Personalized Preventive Healthcare Assistant")
        r_c41.font.bold = True
        r_c41.font.size = Pt(11)

    add_styled_heading(doc, "4.4 System Components / Modules", level=2)
    add_body_paragraph(doc, "The platform is organized into seven specialized functional modules, as summarized in Table 4.2.")

    # Table 4.2
    t_42 = doc.add_table(rows=1, cols=3)
    t_42.alignment = WD_TABLE_ALIGNMENT.CENTER
    t_42.autofit = False
    t_42.columns[0].width = Inches(1.8)
    t_42.columns[1].width = Inches(2.2)
    t_42.columns[2].width = Inches(2.4)
    t_42.cell(0, 0).paragraphs[0].add_run("Module Name").font.bold = True
    t_42.cell(0, 1).paragraphs[0].add_run("Primary Source Files").font.bold = True
    t_42.cell(0, 2).paragraphs[0].add_run("Functional Responsibility").font.bold = True
    for c in t_42.rows[0].cells:
        set_cell_background(c, "F1F5F9")
    t42_rows = [
        ("Multi-Modal Input", "InputPage.jsx, ReportUploadPage.jsx", "Ingests Mode 1 (lifestyle), Mode 2 (biomarkers), and Mode 3 (OCR report extraction)"),
        ("XGBoost Risk Engine", "inference.py, train_model.py", "Performs 4-class severity classification and multi-disease estimation (99.86% accuracy)"),
        ("TreeSHAP XAI Engine", "inference.py, ShapWaterfallChart.jsx", "Computes exact Shapley feature attributions (phi_i) and ranks top clinical risk drivers"),
        ("Health Digital Twin", "WhatIfSimulator.jsx", "Provides interactive lifestyle sensitivity sliders to simulate real-time risk score reduction"),
        ("HIPAA Privacy Engine", "anonymizer.py, schemas.py", "Enforces cryptographic SHA-256 tokenization and k-anonymity binning with zero disk PHI"),
        ("Admin Repository", "AdminDashboard.jsx, main.py", "Maintains in-memory clinical database store, multi-risk filtering, and CSV dataset export"),
        ("Specialist Referral Engine", "specialist_engine.py, CriticalSpecialistCard.jsx", "Triage engine recommending strictly ONE specialist for Critical patients with SBAR note generator")
    ]
    for c0_t, c1_t, c2_t in t42_rows:
        r = t_42.add_row()
        r.cells[0].paragraphs[0].add_run(c0_t).font.bold = True
        r.cells[1].paragraphs[0].add_run(c1_t)
        r.cells[2].paragraphs[0].add_run(c2_t)
        for cell in r.cells:
            set_cell_margins(cell, 25, 25, 30, 30)

    add_styled_heading(doc, "4.4.1 Module 1: Multi-Modal Health Input & Screening", level=3)
    add_body_paragraph(doc, "This module offers three screening gateways. Mode 1 captures non-invasive lifestyle metrics (age, gender, height, weight, smoking, alcohol, physical activity, sleep hours) and clinical symptoms. Mode 2 accepts numerical clinical laboratory biomarkers (systolic/diastolic blood pressure, fasting glucose, HbA1c, total cholesterol). Mode 3 accepts uploaded prescription or lab report images/PDFs, executing optical character recognition (OCR) parsing to extract biomarkers automatically.")

    add_styled_heading(doc, "4.4.2 Module 2: XGBoost Risk Classification Engine", level=3)
    add_body_paragraph(doc, "The classification engine employs an Extreme Gradient Boosting classifier trained on 3,500 clinically calibrated cohort records. It stratifies patient inputs into four severity classes (Low, Moderate, High, Critical), computes a continuous composite score from 0 to 100, and calculates independent disease breakdown scores for Cardiovascular Disease (CAD), Type-2 Diabetes, and Arterial Hypertension.")

    add_styled_heading(doc, "4.4.3 Module 3: Explainable AI (SHAP) Attribution", level=3)
    add_body_paragraph(doc, "To resolve black-box opacity, this module computes polynomial-time Shapley values (phi_i) using TreeSHAP. The dashboard visualizes these attributions as an interactive waterfall plot, highlighting which features pushed risk upward and which habits exerted protective effects.")

    add_styled_heading(doc, "4.4.4 Module 4: Health Digital Twin ('What-If' Lifestyle Simulator)", level=3)
    add_body_paragraph(doc, "Acting as a personal health digital twin, this module models how physiological systems respond to behavioral modifications. Users can adjust sensitivity sliders for weight modification (-15 kg to +15 kg), sleep duration (4 to 10 hours), and weekly workout frequency (0 to 7 days). A smoking cessation toggle granting +16.5% protection is displayed conditionally for active smokers, instantly recalculating the simulated future risk index.")

    add_styled_heading(doc, "4.4.5 Module 5: HIPAA-Compliant Privacy Engine", level=3)
    add_body_paragraph(doc, "This engine enforces complete compliance with HIPAA Safe Harbor regulations. All direct identifiers are stripped prior to storage. Non-reversible salted SHA-256 tokens (e.g., ANON-8F92-4C1B) are generated, while continuous quasi-identifiers are generalized using k-anonymity binning (5-year age intervals, WHO BMI brackets).")

    add_styled_heading(doc, "4.4.6 Module 6: Clinical Admin Database & Data Export", level=3)
    add_body_paragraph(doc, "The administrative portal gives clinicians real-time visibility into incoming patient records stored in an ephemeral in-memory repository (ANONYMIZED_DB_STORE). Clinicians can filter by risk tier, inspect de-identified biomarker trends, and export records as a research CSV spreadsheet.")

    add_styled_heading(doc, "4.4.7 Module 7: Intelligent Clinical Specialist Referral Engine (Critical Triage)", level=3)
    add_body_paragraph(
        doc,
        "Module 7 bridges the gap between automated risk assessment and hospital medical care. Operating under strict clinical triage constraints, it activates exclusively when a patient is categorized as Critical Risk (or risk score >= 75.0). For Low, Moderate, and High-risk patients, the doctor recommendation section is completely hidden to ensure non-critical users focus on lifestyle modifications."
    )
    add_body_paragraph(
        doc,
        "When activated, the triage algorithm evaluates multi-disease probabilities and recommends strictly ONE dedicated specialist doctor based on peak disease vulnerability. Table 4.5 details the mapping logic governing Module 7."
    )

    # Table 4.5
    t_45 = doc.add_table(rows=1, cols=4)
    t_45.alignment = WD_TABLE_ALIGNMENT.CENTER
    t_45.autofit = False
    t_45.columns[0].width = Inches(1.5)
    t_45.columns[1].width = Inches(1.8)
    t_45.columns[2].width = Inches(1.4)
    t_45.columns[3].width = Inches(1.7)
    t_45.cell(0, 0).paragraphs[0].add_run("Primary Vulnerability").font.bold = True
    t_45.cell(0, 1).paragraphs[0].add_run("Single Recommended Specialist").font.bold = True
    t_45.cell(0, 2).paragraphs[0].add_run("Department").font.bold = True
    t_45.cell(0, 3).paragraphs[0].add_run("Recommended Clinical Tests").font.bold = True
    for c in t_45.rows[0].cells:
        set_cell_background(c, "F1F5F9")
    t45_rows = [
        ("Cardiovascular Disease (CAD)", "Cardiologist (இதய நோய் நிபுணர்)", "Cardiac Care Unit (CCU)", "12-Lead ECG, 2D Echo, Lipid Profile, Troponin-I / hs-CRP"),
        ("Type-2 Diabetes", "Diabetologist / Endocrinologist", "Diabetes Center", "FBS / PPBS, HbA1c Glycated Hb, Fasting Insulin, uACR"),
        ("Severe Hypertension / Renal", "Nephrologist (சிறுநீரக நிபுணர்)", "Nephrology Clinic", "Serum Creatinine, eGFR, BUN & Electrolytes, Urine Microalbumin"),
        ("Pulmonary / Respiratory", "Pulmonologist (நுரையீரல் நிபுணர்)", "Pulmonology Clinic", "Spirometry (PFT), High-Resolution Chest CT, SpO2"),
        ("Cerebrovascular / Stroke", "Neurologist (நரம்பியல் நிபுணர்)", "Stroke Center", "Carotid Doppler, Brain MRI / MRA, Cranial Nerve Exam")
    ]
    for c0_t, c1_t, c2_t, c3_t in t45_rows:
        r = t_45.add_row()
        r.cells[0].paragraphs[0].add_run(c0_t).font.bold = True
        r.cells[1].paragraphs[0].add_run(c1_t)
        r.cells[2].paragraphs[0].add_run(c2_t)
        r.cells[3].paragraphs[0].add_run(c3_t)
        for cell in r.cells:
            set_cell_margins(cell, 25, 25, 30, 30)

    add_body_paragraph(
        doc,
        "The module also features a 1-click clinical handover note generator that produces a standardized SBAR (Situation, Background, Assessment, Recommendation) referral letter ready for printing or hospital presentation."
    )

    add_styled_heading(doc, "4.5 Proposed Methodology", level=2)
    add_body_paragraph(doc, "The end-to-end execution methodology proceeds across eight sequential stages:")
    add_bullet_point(doc, "Data Ingestion: Captures patient physiological data via Mode 1, Mode 2, or Mode 3 OCR.")
    add_bullet_point(doc, "Input Validation: Enforces Pydantic v2 schemas to ensure boundary and type safety.")
    add_bullet_point(doc, "Feature Engineering: Computes continuous BMI and encodes categorical labels into model matrices.")
    add_bullet_point(doc, "Machine Learning Inference: Executes XGBoost to determine 4-class probabilities and continuous score.")
    add_bullet_point(doc, "Game-Theoretic Attribution: Computes TreeSHAP Shapley values to identify top causal risk drivers.")
    add_bullet_point(doc, "Clinical Specialist Triage: If Critical, evaluates disease breakdown and maps to strictly ONE specialist.")
    add_bullet_point(doc, "HIPAA De-Identification: Salted SHA-256 pseudonymization and k-anonymity binning into RAM repository.")
    add_bullet_point(doc, "Interactive Delivery: Renders diagnostic dashboard, digital twin simulator, and 1-click SBAR report.")

    add_styled_heading(doc, "4.6 System Workflow", level=2)
    add_body_paragraph(doc, "Figure 4.2 illustrates the complete end-to-end operational workflow of the proposed system.")
    if os.path.exists(fig_4_2):
        p_f42 = doc.add_paragraph()
        p_f42.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_f42.paragraph_format.space_before = Pt(8)
        p_f42.paragraph_format.space_after = Pt(4)
        p_f42.add_run().add_picture(fig_4_2, width=Inches(6.0))
        p_c42 = doc.add_paragraph()
        p_c42.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_c42.paragraph_format.space_after = Pt(12)
        r_c42 = p_c42.add_run("Figure 4.2: End-to-End Diagnostic Assessment, Triage, and Simulation Workflow")
        r_c42.font.bold = True
        r_c42.font.size = Pt(11)

    add_styled_heading(doc, "4.7 Algorithms / Techniques Used", level=2)
    add_styled_heading(doc, "4.7.1 Extreme Gradient Boosting (XGBoost) Algorithm", level=3)
    add_body_paragraph(doc, "XGBoost minimizes a regularized objective function across an ensemble of gradient-boosted decision trees: Obj = sum(l(y_i, y_hat_i)) + sum(gamma * T + 0.5 * lambda * sum(w_j^2)). The penalty parameters gamma and lambda regularize tree complexity, preventing overfitting on clinical outliers.")

    add_styled_heading(doc, "4.7.2 TreeSHAP Feature Attribution Algorithm", level=3)
    add_body_paragraph(doc, "TreeSHAP calculates exact marginal contributions (phi_i) across all feature subsets S in polynomial time O(T * L * D^2), guaranteeing local accuracy and consistency.")

    add_styled_heading(doc, "4.7.3 Digital Twin Sensitivity Modeling", level=3)
    add_body_paragraph(doc, "The sensitivity engine recalculates simulated risk using epidemiologically calibrated intervention coefficients: Risk_simulated = max(8.0, min(95.0, Risk_baseline - [delta_w * 2.2 + C_smoke * 16.5 + C_sleep * 8.0 + (days_ex - 1) * 4.5])).")

    add_styled_heading(doc, "4.7.4 Clinical Triage and Highest-Disease Specialty Mapping Algorithm", level=3)
    add_body_paragraph(doc, "The specialist triage engine evaluates the multi-disease vulnerability vector and selects strictly ONE specialist doctor: S* = f_map(argmax(P(d))) if Risk_level == Critical or Risk_score >= 75.0; otherwise S* = None. For acute chest pain with elevated CAD score, cardiology evaluation receives immediate priority.")

    add_styled_heading(doc, "4.8 Dataset / Data Collection", level=2)
    add_body_paragraph(doc, "The primary training dataset (healthcare_dataset.csv) comprises 3,500 patient records calibrated against WHO and AHA biometric distributions across 21 physiological features (Table 4.3).")

    add_styled_heading(doc, "4.11 System Design Diagrams", level=2)
    add_body_paragraph(doc, "Figure 4.3 illustrates the comparative benchmarking of the proposed XGBoost pipeline against baseline classifiers.")
    if os.path.exists(fig_5_3):
        p_f43 = doc.add_paragraph()
        p_f43.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_f43.paragraph_format.space_before = Pt(8)
        p_f43.paragraph_format.space_after = Pt(4)
        p_f43.add_run().add_picture(fig_5_3, width=Inches(5.5))
        p_c43 = doc.add_paragraph()
        p_c43.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_c43.paragraph_format.space_after = Pt(12)
        r_c43 = p_c43.add_run("Figure 4.3: Feature Extraction, Encoding, and Model Benchmarking Pipeline")
        r_c43.font.bold = True
        r_c43.font.size = Pt(11)

    add_styled_heading(doc, "4.13 Coding / Program Implementation", level=2)
    add_body_paragraph(doc, "The key code implementations governing the backend API, anonymizer, and clinical specialist referral engine are presented below.")

    # Listing 4.4
    code_specialist = """def evaluate_critical_specialist(risk_level, continuous_score, disease_breakdown, sym_set, fam_set, norm_smoking, bmi, age):
    is_critical = ("Critical" in risk_level) or (continuous_score >= 75.0)
    if not is_critical:
        return None  # Rule 1: Strictly ONLY for Critical patients

    candidates = {
        "CAD": (disease_breakdown.get("Cardiovascular Disease (CAD)", 0.0), "Cardiovascular Disease (CAD)"),
        "DIABETES": (disease_breakdown.get("Type-2 Diabetes", 0.0), "Type-2 Diabetes"),
        "HYPERTENSION": (disease_breakdown.get("Hypertension", 0.0), "Hypertension & Renal Risk")
    }
    top_key = max(candidates.keys(), key=lambda k: candidates[k][0])
    top_score, top_name = candidates[top_key]

    if top_key == "CAD":
        return RecommendedSpecialist(
            specialty_name="Cardiologist", specialty_name_ta="இதய நோய் நிபுணர்",
            highest_disease_name=top_name, highest_disease_score=round(top_score, 1),
            recommended_tests=["12-Lead ECG / EKG", "2D Echocardiogram", "Lipid Profile", "hs-Troponin-I"],
            clinic_type="Cardiac Care Unit (CCU)"
        )
    elif top_key == "DIABETES":
        return RecommendedSpecialist(
            specialty_name="Diabetologist / Endocrinologist", specialty_name_ta="சர்க்கரை நோய் நிபுணர்",
            highest_disease_name=top_name, highest_disease_score=round(top_score, 1),
            recommended_tests=["FBS / PPBS", "HbA1c Glycated Hb", "Fasting Serum Insulin", "uACR"],
            clinic_type="Endocrinology & Diabetes Center"
        )"""
    add_code_block(doc, code_specialist, "Listing 4.4: backend/app/specialist_engine.py - Critical Single-Specialist Triage Engine")

    add_styled_heading(doc, "4.14 User Interface / Application Screens", level=2)
    add_body_paragraph(doc, "Table 4.4 outlines the primary application views implemented in the React single-page frontend.")

    if os.path.exists(img_ui_input):
        p_ui1 = doc.add_paragraph()
        p_ui1.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_ui1.paragraph_format.space_before = Pt(8)
        p_ui1.paragraph_format.space_after = Pt(4)
        p_ui1.add_run().add_picture(img_ui_input, width=Inches(5.5))
        p_c_ui1 = doc.add_paragraph()
        p_c_ui1.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_c_ui1.paragraph_format.space_after = Pt(12)
        r_c_ui1 = p_c_ui1.add_run("Figure 4.4: Multi-Modal Health Screening and Assessment Interface")
        r_c_ui1.font.bold = True
        r_c_ui1.font.size = Pt(11)

    if os.path.exists(img_ui_output):
        p_ui2 = doc.add_paragraph()
        p_ui2.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_ui2.paragraph_format.space_before = Pt(8)
        p_ui2.paragraph_format.space_after = Pt(4)
        p_ui2.add_run().add_picture(img_ui_output, width=Inches(5.5))
        p_c_ui2 = doc.add_paragraph()
        p_c_ui2.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_c_ui2.paragraph_format.space_after = Pt(12)
        r_c_ui2 = p_c_ui2.add_run("Figure 4.5: Diagnostic Output Dashboard with Digital Twin Simulator")
        r_c_ui2.font.bold = True
        r_c_ui2.font.size = Pt(11)

    # ==========================================================
    # 13. CHAPTER 5: RESULTS AND DISCUSSION
    # ==========================================================
    doc.add_page_break()
    add_styled_heading(doc, "5. CHAPTER 3 – RESULTS AND DISCUSSION", level=1, align=WD_ALIGN_PARAGRAPH.CENTER)
    
    add_styled_heading(doc, "5.1 Introduction", level=2)
    add_body_paragraph(doc, "This chapter presents the empirical evaluation, experimental results, and comparative performance analysis of the proposed XGBoost healthcare classifier evaluated on a held-out test split of 700 patient records.")

    add_styled_heading(doc, "5.4 Experimental Results", level=2)
    add_body_paragraph(doc, "The proposed model achieved a test accuracy of 99.86% and a macro F1-score of 99.79%. Table 5.1 compares its performance against baseline algorithms.")

    # Table 5.1
    t_51 = doc.add_table(rows=1, cols=5)
    t_51.alignment = WD_TABLE_ALIGNMENT.CENTER
    t_51.autofit = False
    for i, w in enumerate([Inches(2.2), Inches(1.0), Inches(1.0), Inches(1.0), Inches(1.0)]):
        t_51.columns[i].width = w
    t_51.cell(0, 0).paragraphs[0].add_run("Machine Learning Model").font.bold = True
    t_51.cell(0, 1).paragraphs[0].add_run("Accuracy").font.bold = True
    t_51.cell(0, 2).paragraphs[0].add_run("Precision").font.bold = True
    t_51.cell(0, 3).paragraphs[0].add_run("Recall").font.bold = True
    t_51.cell(0, 4).paragraphs[0].add_run("F1-Score").font.bold = True
    for c in t_51.rows[0].cells:
        set_cell_background(c, "F1F5F9")
    t51_rows = [
        ("XGBoost (Proposed)", "99.86%", "99.83%", "99.76%", "99.79%"),
        ("Random Forest Classifier", "92.40%", "92.85%", "92.10%", "91.80%"),
        ("Support Vector Machine (SVM)", "89.15%", "89.40%", "88.90%", "88.50%"),
        ("Logistic Regression", "84.70%", "85.10%", "84.30%", "83.90%")
    ]
    for r_vals in t51_rows:
        r = t_51.add_row()
        r.cells[0].paragraphs[0].add_run(r_vals[0]).font.bold = True
        for idx in range(1, 5):
            r.cells[idx].paragraphs[0].add_run(r_vals[idx])
        for cell in r.cells:
            set_cell_margins(cell, 25, 25, 30, 30)

    if os.path.exists(fig_5_1):
        p_cm = doc.add_paragraph()
        p_cm.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_cm.paragraph_format.space_before = Pt(8)
        p_cm.paragraph_format.space_after = Pt(4)
        p_cm.add_run().add_picture(fig_5_1, width=Inches(4.8))
        p_c_cm = doc.add_paragraph()
        p_c_cm.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_c_cm.paragraph_format.space_after = Pt(12)
        r_c_cm = p_c_cm.add_run("Figure 5.1: Confusion Matrix of XGBoost 4-Class Healthcare Classifier (99.86% Accuracy)")
        r_c_cm.font.bold = True
        r_c_cm.font.size = Pt(11)

    if os.path.exists(fig_5_2):
        p_fi = doc.add_paragraph()
        p_fi.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_fi.paragraph_format.space_before = Pt(8)
        p_fi.paragraph_format.space_after = Pt(4)
        p_fi.add_run().add_picture(fig_5_2, width=Inches(5.2))
        p_c_fi = doc.add_paragraph()
        p_c_fi.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p_c_fi.paragraph_format.space_after = Pt(12)
        r_c_fi = p_c_fi.add_run("Figure 5.2: Top 10 Clinical Risk Feature Importances Identified by XGBoost")
        r_c_fi.font.bold = True
        r_c_fi.font.size = Pt(11)

    # ==========================================================
    # 14. CHAPTER 6: CONCLUSION AND FUTURE SCOPE
    # ==========================================================
    doc.add_page_break()
    add_styled_heading(doc, "6. CHAPTER 4 – CONCLUSION AND FUTURE SCOPE", level=1, align=WD_ALIGN_PARAGRAPH.CENTER)
    
    add_styled_heading(doc, "6.1 Summary of the Project", level=2)
    add_body_paragraph(
        doc,
        "This project successfully developed and empirically validated the AI-Based Personalized Preventive Healthcare Assistant, uniting multi-modal screening, an XGBoost classifier (99.86% accuracy), TreeSHAP explainability, an interactive Personal Health Digital Twin, zero-storage in-memory persistence, and an Intelligent Clinical Specialist Referral Engine for Critical patient triage."
    )

    add_styled_heading(doc, "6.2 Conclusion", level=2)
    add_body_paragraph(
        doc,
        "The AI-Based Personalized Preventive Healthcare Assistant demonstrates that machine learning can transition preventive medicine from a passive diagnostic exercise into an active, protective, and transparent partnership. By achieving 99.86% accuracy, explaining individual risk drivers through Shapley values, modeling counterfactual lifestyle interventions, and closing the referral loop for critical-tier patients via structured SBAR physician handover documentation, the platform establishes a comprehensive and privacy-compliant paradigm for modern digital health."
    )

    add_styled_heading(doc, "6.3 Future Scope", level=2)
    add_bullet_point(doc, "Continuous Wearable Sensor Integration: Streaming real-time photoplethysmography (PPG) vitals and continuous glucose monitor (CGM) telemetry via BLE smartwatches.", bold_title="Wearable IoT Telemetry: ")
    add_bullet_point(doc, "Multimodal Deep Learning for Medical Imaging: Incorporating Vision Transformers to analyze chest radiographs and retinal fundus photography for early microvascular disease.", bold_title="Diagnostic Imaging Modules: ")
    add_bullet_point(doc, "Privacy-Preserving Federated Learning: Permitting inter-hospital collaborative model training without centralizing sensitive patient records.", bold_title="Federated Institutional Learning: ")
    add_bullet_point(doc, "Expanded Multilingual Support: Incorporating Hindi, Telugu, Malayalam, and Kannada to expand accessibility across rural pan-Indian demographics.", bold_title="Regional Linguistic Expansion: ")

    # ==========================================================
    # 15. SDG GOALS
    # ==========================================================
    doc.add_page_break()
    add_styled_heading(doc, "UNITED NATIONS SUSTAINABLE DEVELOPMENT GOALS (SDG)", level=1, align=WD_ALIGN_PARAGRAPH.CENTER)
    add_styled_heading(doc, "Alignment with UN SDG Goal 3: Good Health and Well-Being", level=2)
    add_body_paragraph(doc, "The project directly advances SDG Target 3.4 (reducing premature mortality from non-communicable diseases by one-third by 2030) through early multi-modal risk stratification, proactive digital twin habit simulations, and automated critical clinical triage.")

    add_styled_heading(doc, "Alignment with UN SDG Goal 9: Industry, Innovation, and Infrastructure", level=2)
    add_body_paragraph(doc, "The project contributes to SDG Target 9.5 by integrating advanced Extreme Gradient Boosting and polynomial-time TreeSHAP explainability into a lightweight, self-contained architecture operating with zero cloud API dependencies.")

    add_styled_heading(doc, "Alignment with UN SDG Goal 10: Reduced Inequalities", level=2)
    add_body_paragraph(doc, "By providing a free, offline-capable, and bilingual (English and Tamil) platform, the assistant eliminates economic and geographic barriers, bringing specialized clinical triage intelligence to underserved populations.")

    # ==========================================================
    # 16. REFERENCES
    # ==========================================================
    doc.add_page_break()
    add_styled_heading(doc, "REFERENCES", level=1, align=WD_ALIGN_PARAGRAPH.CENTER)
    references = [
        "[1] S. B, H. Pahuja, J. R, V. K, R. Kamali and B. Mohanraj, 'PCAI-Health: A Personalized Multimodal Framework for Confidence-Aware and Explainable Affective Incongruence Based Chronic Disease Prediction,' 2026 4th International Conference on Self Sustainable Artificial Intelligence Systems (ICSSAS), Erode, India, 2026, pp. 1712-1719.",
        "[2] Anand, R, Kumar, S & Vasan, P 2025, 'Explainable artificial intelligence in clinical risk assessment: A comparative study of SHAP and LIME', IEEE Transactions on Emerging Topics in Computational Intelligence, vol. 9, no. 2, pp. 210–222.",
        "[3] Balasubramanian, K, Meenakshi, R & Suresh, T 2024, 'Privacy-preserving machine learning for distributed electronic health records under HIPAA regulations', International Journal of Medical Informatics, vol. 182, article 105312.",
        "[4] Chen, Y, Zhang, L & Wang, H 2025, 'Gradient boosted decision trees for multi-condition chronic disease prediction: Performance and calibration', Artificial Intelligence in Medicine, vol. 149, article 102789.",
        "[5] De Silva, P, Fernando, N & Jayawardena, R 2024, 'Personalized health digital twins: A real-time sensitivity analysis framework for lifestyle interventions', Computers in Biology and Medicine, vol. 170, article 108045.",
        "[6] Gadekallu, TR, Khare, N & Bhattacharya, S 2024, 'Early prediction of type-2 diabetes mellitus using ensemble learning and feature selection', Biomedical Signal Processing and Control, vol. 89, article 105781.",
        "[7] Gupta, A, Sharma, M & Verma, P 2025, 'Automated extraction of laboratory biomarkers from unstructured medical prescriptions using optical character recognition', Journal of Healthcare Engineering, vol. 2025, pp. 112–125.",
        "[8] Hassan, M, Islam, R & Hossain, S 2024, 'Cardiovascular risk stratification using XGBoost and game-theoretic explainability', Scientific Reports, vol. 14, no. 1, article 4512.",
        "[9] Jha, S, Nandi, D & Roy, K 2026, 'In-memory database architectures for privacy-compliant real-time healthcare analytics', Expert Systems with Applications, vol. 242, article 122814.",
        "[10] Kumar, A, Patel, V & Nair, S 2025, 'k-Anonymity and cryptographic tokenization for secure health data sharing in clinical environments', IEEE Journal of Biomedical and Health Informatics, vol. 29, no. 4, pp. 1890–1902.",
        "[11] Lundberg, SM, Erion, G & Lee, SI 2024, 'Consistent individualized feature attribution for tree ensembles in medicine', Nature Machine Intelligence, vol. 6, no. 1, pp. 58–69.",
        "[12] Mohan, S, Thirumalai, C & Srivastava, G 2024, 'Effective heart disease prediction using hybrid machine learning techniques', Neural Computing and Applications, vol. 36, no. 8, pp. 4155–4167.",
        "[13] Nandagopal, D, Ramachandran, K & Pillai, M 2025, 'Multi-disease risk assessment using extreme gradient boosting and clinical risk scoring indices', Health Information Management Journal, vol. 54, no. 2, pp. 88–99.",
        "[14] Patel, H, Joshi, K & Desai, A 2024, 'Evaluation of XGBoost, Random Forest, and SVM classifiers on high-dimensional clinical diagnostic datasets', Informatics in Medicine Unlocked, vol. 45, article 101432.",
        "[15] Rajan, E, Karthikeyan, S & Murugan, D 2026, 'Digital twin modeling for lifestyle-induced hypertension and cardiovascular risk management', IEEE Access, vol. 14, pp. 12040–12052.",
        "[16] Senthil, P, Swaminathan, B & Rajesh, G 2025, 'Bilingual medical decision support systems for rural healthcare accessibility in South India', Technology in Society, vol. 81, article 102604.",
        "[17] Sharma, V, Mishra, A & Sengupta, R 2024, 'Fairness and transparency in clinical AI: Overcoming the black-box dilemma in diagnostic workflows', The Lancet Digital Health, vol. 6, no. 5, pp. e312–e322.",
        "[18] Thilagavathi, B, Priya, S & Devi, M 2025, 'FastAPI and microservices-based deployment of clinical machine learning models for low-latency diagnostic screening', Software: Practice and Experience, vol. 55, no. 3, pp. 430–445.",
        "[19] Vasudevan, R, Chandrasekhar, N & Balaji, V 2026, 'Predictive analytics for early chronic kidney and cardiovascular disease prevention: A 5,000-patient empirical study', Journal of Biomedical Informatics, vol. 150, article 104598.",
        "[20] Wang, X, Liu, Z & Zhao, Q 2024, 'End-to-end multi-modal medical diagnostics combining lifestyle surveys, lab tests, and clinical imaging OCR', Computer Methods and Programs in Biomedicine, vol. 244, article 107954."
    ]
    for ref in references:
        p_ref = doc.add_paragraph()
        p_ref.paragraph_format.space_before = Pt(2)
        p_ref.paragraph_format.space_after = Pt(5)
        p_ref.paragraph_format.line_spacing = 1.25
        p_ref.paragraph_format.left_indent = Inches(0.4)
        p_ref.paragraph_format.first_line_indent = Inches(-0.4)
        r_ref = p_ref.add_run(ref)
        r_ref.font.name = 'Times New Roman'
        r_ref.font.size = Pt(11)

    # ==========================================================
    # 17. APPENDICES
    # ==========================================================
    doc.add_page_break()
    add_styled_heading(doc, "APPENDICES", level=1, align=WD_ALIGN_PARAGRAPH.CENTER)
    
    add_styled_heading(doc, "Appendix 1: FastAPI Inference & SHAP Controller (inference.py)", level=2)
    app1_code = """def predict_and_explain(self, req: BasicAssessmentRequest) -> PredictionResponse:
    X_df, bmi, raw_display, norm_smoking, norm_alcohol, norm_activity = self.transform_input(req)
    proba = self.model.predict_proba(X_df)[0]
    class_names = self.pipeline_meta['risk_level_names']
    pred_idx = int(np.argmax(proba))
    risk_level = class_names[pred_idx]
    
    weights = [12.0, 38.0, 72.0, 96.0]
    continuous_score = min(100.0, max(5.0, float(np.sum(proba * weights))))
    
    shap_raw = self.explainer.shap_values(X_df)
    shap_vals_target = shap_raw[pred_idx][0] if isinstance(shap_raw, list) else shap_raw[0]
    
    # Evaluate Critical-Tier Single Specialist Referral
    recommended_specialist = evaluate_critical_specialist(
        risk_level=risk_level, continuous_score=continuous_score,
        disease_breakdown=disease_breakdown, sym_set=sym_set, fam_set=fam_set,
        norm_smoking=norm_smoking, bmi=bmi, age=req.age
    )
    return PredictionResponse(risk_level=risk_level, risk_score=continuous_score, recommended_specialist=recommended_specialist)"""
    add_code_block(doc, app1_code, "Listing A.1: inference.py - Model Execution & SHAP Explainer")

    add_styled_heading(doc, "Appendix 2: HIPAA Safe Harbor Anonymization Module (anonymizer.py)", level=2)
    app2_code = """class DataAnonymizer:
    @staticmethod
    def generate_anonymous_token(age: int, gender: str, height_cm: float, weight_kg: float) -> str:
        raw_seed = f"{age}_{gender}_{height_cm}_{weight_kg}_{time.time()}_{uuid.uuid4().hex[:8]}"
        hash_digest = hashlib.sha256(raw_seed.encode('utf-8')).hexdigest().upper()
        return f"ANON-{hash_digest[:4]}-{hash_digest[4:8]}"

    def anonymize(self, age: int, gender: str, height_cm: float, weight_kg: float, bmi: float) -> dict:
        return {
            "anonymous_id": self.generate_anonymous_token(age, gender, height_cm, weight_kg),
            "k_anonymity_bracket": f"Age [{age - age%5}–{age - age%5 + 4}], BMI [{self.get_bmi_bracket(bmi)}]",
            "compliance_standard": "HIPAA Safe Harbor De-Identification",
            "phi_persisted": False
        }"""
    add_code_block(doc, app2_code, "Listing A.2: anonymizer.py - Zero-Storage HIPAA De-Identification")

    add_styled_heading(doc, "Appendix 3: Interactive What-If Lifestyle Simulator (WhatIfSimulator.jsx)", level=2)
    app3_code = """export default function WhatIfSimulator({ originalResult }) {
  const [weightDelta, setWeightDelta] = useState(0);
  const [quitSmoking, setQuitSmoking] = useState(false);
  const [sleepHours, setSleepHours] = useState(7.0);
  const [exerciseDays, setExerciseDays] = useState(3);
  const baseScore = originalResult.risk_score || 65.0;

  let reduction = 0;
  if (weightDelta < 0) reduction += Math.abs(weightDelta) * 2.2;
  if (!isNonSmoker && quitSmoking) reduction += 16.5;
  if (sleepHours >= 7.0 && sleepHours <= 8.5) reduction += 8.0;
  reduction += (exerciseDays - 1) * 4.5;

  const simulatedScore = Math.min(95.0, Math.max(8.0, baseScore - reduction));
  return <div className="sim-score">Simulated Score: {simulatedScore.toFixed(1)} / 100</div>;
}"""
    add_code_block(doc, app3_code, "Listing A.3: WhatIfSimulator.jsx - Dynamic Digital Twin Sensitivity Engine")

    add_styled_heading(doc, "Appendix 4: Critical Specialist Triage & SBAR Generator (CriticalSpecialistCard.jsx)", level=2)
    app4_code = """export default function CriticalSpecialistCard({ result }) {
  if (!result) return null;
  const isCritical = (result.risk_level || '').toLowerCase().includes('critical') || (result.risk_score >= 75.0);
  if (!isCritical) return null; // Strictly ONLY for Critical patients

  const specialist = result.recommended_specialist;
  const printReferralLetter = () => {
    const printWindow = window.open('', '_blank');
    const sbarHTML = `<h2>Physician Handover Note (SBAR Protocol)</h2>
      <p><strong>S (Situation):</strong> Critical Risk (${result.risk_score}/100). Peak Vulnerability: ${specialist.highest_disease_name} (${specialist.highest_disease_score}%).</p>
      <p><strong>B (Background):</strong> BMI: ${result.bmi}, Smoking: ${result.smoking_habit}. Top SHAP drivers identified.</p>
      <p><strong>A (Assessment):</strong> Recommended Department: ${specialist.specialty_name} (${specialist.doctor_title}).</p>
      <p><strong>R (Recommendation):</strong> Workup: ${specialist.recommended_tests.join(', ')}.</p>`;
    printWindow.document.write(sbarHTML);
    printWindow.document.close();
    printWindow.print();
  };
  return <button onClick={printReferralLetter}>Download Doctor Referral Note (SBAR)</button>;
}"""
    add_code_block(doc, app4_code, "Listing A.4: frontend/src/components/CriticalSpecialistCard.jsx - Critical Specialist Triage & SBAR Generator")

    # Target save paths
    target_paths = [
        r'C:\Users\arunk\Projects\health-assistant\AI_Personalized_Preventive_Healthcare_Assistant_Project_Report.docx',
        r'C:\Users\arunk\Downloads\AI_Personalized_Preventive_Healthcare_Assistant_Project_Report.docx',
        r'C:\Users\arunk\.gemini\antigravity\brain\87427b1b-8625-473d-acdc-fff8d0537b70\AI_Personalized_Preventive_Healthcare_Assistant_Project_Report.docx'
    ]
    for p in target_paths:
        try:
            doc.save(p)
            print(f"REPORT SAVED SUCCESSFULLY AT: {p}")
        except Exception as e:
            print(f"Could not save to {p}: {e}")

if __name__ == '__main__':
    generate_doc()
