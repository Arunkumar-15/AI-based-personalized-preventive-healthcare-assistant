# Complete script to generate the project report in Word (.docx) format
import os
import docx
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import nsdecls, qn

from docx_helpers import (
    set_cell_margins, set_cell_background,
    add_styled_heading, add_body_paragraph, add_bullet_point
)

def build_report():
    doc = Document()
    
    # Configure A4 Margins: Left 1.25", Right 1.0", Top 1.0", Bottom 1.0"
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
        p0.add_run().add_picture(anna_logo, width=Inches(1.2))
        
        c1 = t_logo.cell(0, 1)
        p1 = c1.paragraphs[0]
        p1.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        p1.add_run().add_picture(sona_logo, width=Inches(2.2))
        
        set_cell_margins(c0, 0, 0, 0, 0)
        set_cell_margins(c1, 0, 0, 0, 0)
    
    p_t = doc.add_paragraph()
    p_t.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_t.paragraph_format.space_before = Pt(36)
    p_t.paragraph_format.space_after = Pt(12)
    p_t.paragraph_format.line_spacing = 1.3
    r = p_t.add_run("AI-BASED PERSONALIZED PREVENTIVE HEALTHCARE ASSISTANT")
    r.font.name = 'Times New Roman'
    r.font.size = Pt(16)
    r.font.bold = True
    
    p_sub = doc.add_paragraph()
    p_sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_sub.paragraph_format.space_after = Pt(24)
    r = p_sub.add_run("A Mini Project Report\nU23IT705 – MINI PROJECT")
    r.font.name = 'Times New Roman'
    r.font.size = Pt(13)
    r.font.italic = True
    
    p_subm = doc.add_paragraph()
    p_subm.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_subm.paragraph_format.space_after = Pt(12)
    r = p_subm.add_run("Submitted by")
    r.font.name = 'Times New Roman'
    r.font.size = Pt(13)
    r.font.bold = True
    
    # Students Table
    t_stud = doc.add_table(rows=3, cols=2)
    t_stud.alignment = WD_TABLE_ALIGNMENT.CENTER
    t_stud.autofit = False
    t_stud.columns[0].width = Inches(3.2)
    t_stud.columns[1].width = Inches(2.6)
    
    students = [
        ("DEEPAK PRIYAN M", "(61782323106022)"),
        ("ARUNKUMAR N", "(61782323106701)"),
        ("BABY SHALINI K", "(61782323106014)")
    ]
    for idx, (name, reg) in enumerate(students):
        c_n = t_stud.cell(idx, 0)
        c_r = t_stud.cell(idx, 1)
        
        p_n = c_n.paragraphs[0]
        p_n.alignment = WD_ALIGN_PARAGRAPH.LEFT
        rn = p_n.add_run(name)
        rn.font.name = 'Times New Roman'
        rn.font.size = Pt(13)
        rn.font.bold = True
        
        p_r = c_r.paragraphs[0]
        p_r.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        rr = p_r.add_run(reg)
        rr.font.name = 'Times New Roman'
        rr.font.size = Pt(13)
        rr.font.bold = True
        
        set_cell_margins(c_n, 50, 50, 50, 50)
        set_cell_margins(c_r, 50, 50, 50, 50)
        
    p_deg = doc.add_paragraph()
    p_deg.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_deg.paragraph_format.space_before = Pt(36)
    p_deg.paragraph_format.space_after = Pt(6)
    p_deg.paragraph_format.line_spacing = 1.3
    r = p_deg.add_run("in partial fulfillment for the award of the degree\nof\nBACHELOR OF TECHNOLOGY\nin\nINFORMATION TECHNOLOGY")
    r.font.name = 'Times New Roman'
    r.font.size = Pt(13)
    r.font.bold = True
    
    p_col = doc.add_paragraph()
    p_col.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_col.paragraph_format.space_before = Pt(36)
    p_col.paragraph_format.line_spacing = 1.3
    r = p_col.add_run("SONA COLLEGE OF TECHNOLOGY (AUTONOMOUS), SALEM – 636005\nANNA UNIVERSITY: CHENNAI 600 025\nOCTOBER 2026")
    r.font.name = 'Times New Roman'
    r.font.size = Pt(13)
    r.font.bold = True

    # ==========================================================
    # 2. BONAFIDE CERTIFICATE
    # ==========================================================
    doc.add_page_break()
    
    p_bc_head = doc.add_paragraph()
    p_bc_head.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_bc_head.paragraph_format.line_spacing = 1.3
    p_bc_head.paragraph_format.space_after = Pt(16)
    r = p_bc_head.add_run("SONA COLLEGE OF TECHNOLOGY (AUTONOMOUS)\nANNA UNIVERSITY: CHENNAI – 600 025")
    r.font.name = 'Times New Roman'
    r.font.size = Pt(14)
    r.font.bold = True
    
    p_bc_title = doc.add_paragraph()
    p_bc_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_bc_title.paragraph_format.space_after = Pt(24)
    r = p_bc_title.add_run("BONAFIDE CERTIFICATE")
    r.font.name = 'Times New Roman'
    r.font.size = Pt(15)
    r.font.bold = True
    
    add_body_paragraph(
        doc,
        'Certified that this Project titled "AI-BASED PERSONALIZED PREVENTIVE HEALTHCARE ASSISTANT" is the bonafide work of "DEEPAK PRIYAN M (61782323106022), ARUNKUMAR N (61782323106701), BABY SHALINI K (61782323106014)" who carried out the project work U23IT705 - MINI PROJECT under my supervision.',
        space_after=36, line_spacing=2.0
    )
    
    t_sign = doc.add_table(rows=1, cols=2)
    t_sign.alignment = WD_TABLE_ALIGNMENT.CENTER
    t_sign.autofit = False
    t_sign.columns[0].width = Inches(3.2)
    t_sign.columns[1].width = Inches(3.0)
    
    cs0 = t_sign.cell(0, 0)
    cs1 = t_sign.cell(0, 1)
    
    p_s0 = cs0.paragraphs[0]
    p_s0.paragraph_format.line_spacing = 1.3
    r = p_s0.add_run("Signature of the Supervisor\n\n\n\nDr. P. Shanmugaraja\nSUPERVISOR\nAssociate Professor\nDepartment of Information Technology\nSona College of Technology,\nSalem – 636005")
    r.font.name = 'Times New Roman'
    r.font.size = Pt(13)
    
    p_s1 = cs1.paragraphs[0]
    p_s1.paragraph_format.line_spacing = 1.3
    r = p_s1.add_run("Head of the Department\n\n\n\nDr. J. Akilandeswari, M.E., Ph.D.\nHEAD OF THE DEPARTMENT\nProfessor\nDepartment of Information Technology\nSona College of Technology,\nSalem – 636005")
    r.font.name = 'Times New Roman'
    r.font.size = Pt(13)
    
    set_cell_margins(cs0, 50, 50, 50, 50)
    set_cell_margins(cs1, 50, 50, 50, 50)
    
    p_viva = doc.add_paragraph()
    p_viva.paragraph_format.space_before = Pt(48)
    p_viva.paragraph_format.space_after = Pt(36)
    r = p_viva.add_run("Submitted for the Mini Project Viva-Voce Examination held on ____________________")
    r.font.name = 'Times New Roman'
    r.font.size = Pt(13)
    
    t_ex = doc.add_table(rows=1, cols=2)
    t_ex.alignment = WD_TABLE_ALIGNMENT.CENTER
    t_ex.autofit = False
    t_ex.columns[0].width = Inches(3.2)
    t_ex.columns[1].width = Inches(3.0)
    
    ce0 = t_ex.cell(0, 0)
    ce1 = t_ex.cell(0, 1)
    
    p_e0 = ce0.paragraphs[0]
    r = p_e0.add_run("INTERNAL EXAMINER")
    r.font.name = 'Times New Roman'
    r.font.size = Pt(13)
    r.font.bold = True
    
    p_e1 = ce1.paragraphs[0]
    p_e1.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    r = p_e1.add_run("EXTERNAL EXAMINER")
    r.font.name = 'Times New Roman'
    r.font.size = Pt(13)
    r.font.bold = True

    # ==========================================================
    # 3. DECLARATION FORM
    # ==========================================================
    doc.add_page_break()
    
    p_dec_h = doc.add_paragraph()
    p_dec_h.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_dec_h.paragraph_format.line_spacing = 1.3
    p_dec_h.paragraph_format.space_after = Pt(14)
    r = p_dec_h.add_run("Sona College of Technology\nDepartment of Information Technology\nU23IT705 - MINIPROJECT - DECLARATION FORM")
    r.font.name = 'Times New Roman'
    r.font.size = Pt(14)
    r.font.bold = True
    
    p_dt = doc.add_paragraph()
    p_dt.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_dt.paragraph_format.space_after = Pt(18)
    r = p_dt.add_run("Declaration by the Students")
    r.font.name = 'Times New Roman'
    r.font.size = Pt(14)
    r.font.bold = True
    
    add_body_paragraph(
        doc,
        'We hereby declare that the project titled "AI-BASED PERSONALIZED PREVENTIVE HEALTHCARE ASSISTANT" is an original work carried out by us under the guidance of Dr. P. Shanmugaraja, Associate Professor, Department of Information Technology, Sona College of Technology. This project has not been submitted elsewhere for the award of any degree or diploma.',
        space_after=14, line_spacing=1.5
    )
    
    add_body_paragraph(
        doc,
        'We also affirm that all the data, clinical models, and information used in this project are genuine and properly acknowledged. This project work is carried out with direct reference to the United Nations Sustainable Development Goals: Goal 3 – Good Health and Well-Being, and Goal 9 – Industry, Innovation, and Infrastructure.',
        space_after=24, line_spacing=1.5
    )
    
    # Students Signature Table
    t_dstud = doc.add_table(rows=4, cols=4)
    t_dstud.alignment = WD_TABLE_ALIGNMENT.CENTER
    t_dstud.autofit = False
    
    col_w = [Inches(0.6), Inches(1.8), Inches(2.2), Inches(1.6)]
    headers = ["S.No", "Register Number", "Name", "Signature"]
    
    for c_idx, h_text in enumerate(headers):
        cell = t_dstud.cell(0, c_idx)
        cell.width = col_w[c_idx]
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = p.add_run(h_text)
        r.font.name = 'Times New Roman'
        r.font.size = Pt(12)
        r.font.bold = True
        set_cell_background(cell, "F1F5F9")
        set_cell_margins(cell, 80, 80, 80, 80)
        
    s_rows = [
        ("1.", "61782323106022", "DEEPAK PRIYAN M", ""),
        ("2.", "61782323106701", "ARUNKUMAR N", ""),
        ("3.", "61782323106014", "BABY SHALINI K", "")
    ]
    for r_idx, row_data in enumerate(s_rows):
        for c_idx, val in enumerate(row_data):
            cell = t_dstud.cell(r_idx + 1, c_idx)
            cell.width = col_w[c_idx]
            p = cell.paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER if c_idx in [0, 1] else WD_ALIGN_PARAGRAPH.LEFT
            r = p.add_run(val)
            r.font.name = 'Times New Roman'
            r.font.size = Pt(12)
            r.font.bold = (c_idx == 2)
            set_cell_margins(cell, 80, 80, 80, 80)
            
    p_dp = doc.add_paragraph()
    p_dp.paragraph_format.space_before = Pt(36)
    r = p_dp.add_run("Date: ____________________\nPlace: Sona College of Technology, Salem")
    r.font.name = 'Times New Roman'
    r.font.size = Pt(13)

    # ==========================================================
    # 4. ACKNOWLEDGMENT
    # ==========================================================
    doc.add_page_break()
    add_styled_heading(doc, "ACKNOWLEDGEMENT", level=1, align=WD_ALIGN_PARAGRAPH.CENTER)
    
    add_body_paragraph(
        doc,
        "First and foremost, we thank the Almighty for showing us inner peace, strength, and divine wisdom in bringing this project to a fruitful completion. We express our deep and heartfelt gratitude to our beloved parents for their unconditional love, constant sacrifices, moral support, and endless encouragement throughout our education.",
        space_after=12, line_spacing=1.5
    )
    
    add_body_paragraph(
        doc,
        "We express our sincere thanks to our esteemed Chairman, Sri. C. Valliappa, Vice Chairmen Sri. Chocko Valliappa and Sri. Thyagu Valliappa, and our respected Principal, Dr. S. R. R. Senthilkumar, for their visionary leadership and for providing state-of-the-art infrastructural and laboratory facilities to carry out this research successfully.",
        space_after=12, line_spacing=1.5
    )
    
    add_body_paragraph(
        doc,
        "We are immensely grateful to our respected Head of the Department of Information Technology, Dr. J. Akilandeswari, M.E., Ph.D., for her continuous encouragement, academic support, and constructive feedback throughout the course of this work.",
        space_after=12, line_spacing=1.5
    )
    
    add_body_paragraph(
        doc,
        "We express our deepest and most heartfelt thanks to our Project Supervisor and Coordinator, Dr. P. Shanmugaraja, Associate Professor, Department of Information Technology, for his extraordinary guidance, valuable insights, constant technical support, and fruit-bearing discussions that steered our work in the right direction.",
        space_after=12, line_spacing=1.5
    )
    
    add_body_paragraph(
        doc,
        "We also extend our warm gratitude to all our department faculty members, technical staff, and peer friends who assisted us directly and indirectly during the development, testing, and documentation stages of this project.",
        space_after=28, line_spacing=1.5
    )
    
    p_sig = doc.add_paragraph()
    p_sig.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    p_sig.paragraph_format.line_spacing = 1.3
    r = p_sig.add_run("DEEPAK PRIYAN M (61782323106022)\nARUNKUMAR N (61782323106701)\nBABY SHALINI K (61782323106014)")
    r.font.name = 'Times New Roman'
    r.font.size = Pt(13)
    r.font.bold = True

    # ==========================================================
    # 5. ABSTRACT
    # ==========================================================
    doc.add_page_break()
    add_styled_heading(doc, "ABSTRACT", level=1, align=WD_ALIGN_PARAGRAPH.CENTER)
    
    add_body_paragraph(
        doc,
        "Chronic lifestyle disorders such as cardiovascular disease, hypertension, and type-2 diabetes mellitus are responsible for over 70% of non-communicable fatalities globally. Traditional diagnostic frameworks are overwhelmingly reactive, identifying pathologies only after severe symptomatic progression or irreversible physiological organ damage has occurred. Furthermore, existing clinical risk calculators frequently operate as opaque black boxes, lack interpretability, demand invasive and costly diagnostic procedures, and raise substantial patient privacy concerns by persisting identifiable protected health information (PHI) across centralized data stores.",
        space_after=12, line_spacing=2.0
    )
    add_body_paragraph(
        doc,
        "To overcome these critical healthcare challenges, this project introduces the AI-Based Personalized Preventive Healthcare Assistant, an explainable, multi-modal, and privacy-preserving clinical decision-support ecosystem. The platform ingests heterogeneous health inputs across three operational screening tiers: Mode 1 (non-invasive demographic, lifestyle, and symptomatic assessment), Mode 2 (clinical laboratory biomarker screening including systolic/diastolic blood pressure, fasting blood glucose, HbA1c, and lipid profiles), and Mode 3 (automated document OCR extraction of unstructured clinical reports). Risk stratification is orchestrated using an Extreme Gradient Boosting (XGBoost) classifier trained on 3,500 clinically calibrated patient samples across 21 multi-system features. Experimental evaluation demonstrates superior predictive efficacy, achieving an overall classification accuracy of 99.86% (699/700 correct predictions on held-out test data) and a macro F1-score of 99.79%, significantly outperforming conventional Random Forest, Support Vector Machine, and Logistic Regression baselines.",
        space_after=12, line_spacing=2.0
    )
    add_body_paragraph(
        doc,
        "To resolve the healthcare black-box dilemma, the system embeds game-theoretic TreeSHAP (SHapley Additive exPlanations) attribution, quantifying exact mathematical Shapley contributions (phi_i) to rank individual clinical drivers transparently. For proactive patient empowerment, the architecture incorporates an interactive Personal Health Digital Twin ('What-If' Lifestyle Simulator), enabling real-time sensitivity analysis to simulate how weight loss, smoking cessation, and sleep optimization directly decrease health risk before physical implementation. Finally, patient privacy is strictly enforced under HIPAA Safe Harbor regulations via cryptographic SHA-256 pseudonymization, k-anonymity quasi-identifier binning, and an in-memory repository ensuring zero persistent PHI on disk. The system provides an end-to-end, bilingual (English and Tamil) clinical decision support platform advancing early disease prevention.",
        space_after=16, line_spacing=2.0
    )

    # ==========================================================
    # 6. TABLE OF CONTENTS
    # ==========================================================
    doc.add_page_break()
    add_styled_heading(doc, "TABLE OF CONTENTS", level=1, align=WD_ALIGN_PARAGRAPH.CENTER)
    
    t_toc = doc.add_table(rows=1, cols=2)
    t_toc.alignment = WD_TABLE_ALIGNMENT.CENTER
    t_toc.autofit = False
    t_toc.columns[0].width = Inches(5.2)
    t_toc.columns[1].width = Inches(1.0)
    
    h_c0 = t_toc.cell(0, 0)
    h_c1 = t_toc.cell(0, 1)
    h_c0.paragraphs[0].add_run("TITLE").font.bold = True
    h_c1.paragraphs[0].add_run("PAGE NO").font.bold = True
    h_c1.paragraphs[0].alignment = WD_ALIGN_PARAGRAPH.RIGHT
    set_cell_background(h_c0, "F1F5F9")
    set_cell_background(h_c1, "F1F5F9")
    
    toc_items = [
        ("ABSTRACT", "v"),
        ("LIST OF FIGURES", "viii"),
        ("LIST OF TABLES", "ix"),
        ("LIST OF ABBREVIATIONS", "x"),
        ("1. INTRODUCTION", "1"),
        ("   1.1 Background of the Project", "1"),
        ("   1.2 Problem Statement", "2"),
        ("   1.3 Motivation", "3"),
        ("   1.4 Objectives", "4"),
        ("   1.5 Scope of the Project", "5"),
        ("2. LITERATURE REVIEW", "6"),
        ("   2.1 Introduction", "6"),
        ("   2.2 Review of Related Studies", "6"),
        ("   2.3 Techniques and Technologies Used in Existing Systems", "12"),
        ("   2.4 Research Gap", "13"),
        ("   2.5 Summary", "14"),
        ("3. CHAPTER 1 – NEED FOR PROPOSED TECHNIQUE", "15"),
        ("   3.1 Existing Techniques", "15"),
        ("   3.2 Limitations of Existing Techniques", "16"),
        ("   3.3 Proposed Technique", "17"),
        ("   3.4 Objectives of the Proposed Technique", "18"),
        ("   3.5 Advantages of the Proposed Technique", "19"),
        ("   3.6 Main User and System Interaction", "20"),
        ("4. CHAPTER 2 – DESIGN OF PROPOSED SYSTEM AND ITS IMPLEMENTATION", "21"),
        ("   4.1 Introduction", "21"),
        ("   4.2 System Requirements", "21"),
        ("      4.2.1 Hardware Requirements", "21"),
        ("      4.2.2 Software Requirements", "22"),
        ("   4.3 System Architecture", "23"),
        ("   4.4 System Components / Modules", "25"),
        ("   4.5 Proposed Methodology", "28"),
        ("   4.6 System Workflow", "29"),
        ("   4.7 Algorithms / Techniques Used", "31"),
        ("   4.8 Dataset / Data Collection", "33"),
        ("   4.9 Data Preprocessing", "34"),
        ("   4.10 Model / System Development", "35"),
        ("   4.11 System Design Diagrams", "36"),
        ("   4.12 Implementation", "37"),
        ("   4.13 Coding / Program Implementation", "38"),
        ("   4.14 User Interface / Application Screens", "42"),
        ("   4.15 Summary", "44"),
        ("5. CHAPTER 3 – RESULTS AND DISCUSSION", "45"),
        ("   5.1 Introduction", "45"),
        ("   5.2 Experimental Setup", "45"),
        ("   5.3 Evaluation Metrics", "46"),
        ("   5.4 Experimental Results", "47"),
        ("   5.5 Comparison with Existing Techniques", "50"),
        ("   5.6 Discussion of Results", "51"),
        ("   5.7 Summary", "52"),
        ("6. CHAPTER 4 – CONCLUSION AND FUTURE SCOPE", "53"),
        ("   6.1 Summary of the Project", "53"),
        ("   6.2 Conclusion", "54"),
        ("   6.3 Future Scope", "55"),
        ("SDG GOALS", "56"),
        ("PUBLICATIONS (IF ANY)", "58"),
        ("REFERENCES", "59"),
        ("APPENDICES", "63")
    ]
    
    for title, pg in toc_items:
        row = t_toc.add_row()
        c0 = row.cells[0]
        c1 = row.cells[1]
        
        p0 = c0.paragraphs[0]
        r0 = p0.add_run(title)
        r0.font.name = 'Times New Roman'
        r0.font.size = Pt(12)
        if title.startswith("1.") or title.startswith("2.") or title.startswith("3.") or title.startswith("4.") or title.startswith("5.") or title.startswith("6.") or "ABSTRACT" in title or "REFERENCES" in title or "SDG" in title or "APPENDICES" in title:
            r0.font.bold = True
            
        p1 = c1.paragraphs[0]
        p1.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        r1 = p1.add_run(pg)
        r1.font.name = 'Times New Roman'
        r1.font.size = Pt(12)
        set_cell_margins(c0, 40, 40, 40, 40)
        set_cell_margins(c1, 40, 40, 40, 40)

    # ==========================================================
    # 7. LIST OF FIGURES
    # ==========================================================
    doc.add_page_break()
    add_styled_heading(doc, "LIST OF FIGURES", level=1, align=WD_ALIGN_PARAGRAPH.CENTER)
    
    t_lof = doc.add_table(rows=1, cols=3)
    t_lof.alignment = WD_TABLE_ALIGNMENT.CENTER
    t_lof.autofit = False
    t_lof.columns[0].width = Inches(1.2)
    t_lof.columns[1].width = Inches(4.0)
    t_lof.columns[2].width = Inches(1.0)
    
    for c_i, h_txt in enumerate(["Figure No", "TITLE", "PAGE NO"]):
        c = t_lof.cell(0, c_i)
        p = c.paragraphs[0]
        if c_i == 2: p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        r = p.add_run(h_txt)
        r.font.bold = True
        set_cell_background(c, "F1F5F9")
        
    figures = [
        ("4.1", "High-Level Architecture of the AI-Based Personalized Preventive Healthcare Assistant", "24"),
        ("4.2", "End-to-End Diagnostic Assessment and Simulation Workflow", "30"),
        ("4.3", "Feature Extraction, Encoding, and SHAP Explainability Pipeline", "36"),
        ("4.4", "Project Directory Structure and Repository Modular Organization", "39"),
        ("4.5", "Multi-Modal Health Screening and Assessment Interface", "43"),
        ("4.6", "Diagnostic Output Dashboard with Digital Twin Simulator", "44"),
        ("5.1", "Confusion Matrix of XGBoost 4-Class Healthcare Classifier (99.86% Accuracy)", "48"),
        ("5.2", "Top 10 Clinical Risk Feature Importances Identified by XGBoost", "49"),
        ("5.3", "Comparative Evaluation Across Machine Learning Algorithms", "50")
    ]
    for num, title, pg in figures:
        row = t_lof.add_row()
        row.cells[0].paragraphs[0].add_run(num)
        row.cells[1].paragraphs[0].add_run(title)
        p = row.cells[2].paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        p.add_run(pg)
        for cell in row.cells:
            set_cell_margins(cell, 40, 40, 40, 40)

    # ==========================================================
    # 8. LIST OF TABLES
    # ==========================================================
    doc.add_page_break()
    add_styled_heading(doc, "LIST OF TABLES", level=1, align=WD_ALIGN_PARAGRAPH.CENTER)
    
    t_lot = doc.add_table(rows=1, cols=3)
    t_lot.alignment = WD_TABLE_ALIGNMENT.CENTER
    t_lot.autofit = False
    t_lot.columns[0].width = Inches(1.2)
    t_lot.columns[1].width = Inches(4.0)
    t_lot.columns[2].width = Inches(1.0)
    
    for c_i, h_txt in enumerate(["Table No", "TITLE", "PAGE NO"]):
        c = t_lot.cell(0, c_i)
        p = c.paragraphs[0]
        if c_i == 2: p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        r = p.add_run(h_txt)
        r.font.bold = True
        set_cell_background(c, "F1F5F9")
        
    tables = [
        ("4.1", "System Hardware and Software Technical Specifications", "22"),
        ("4.2", "Core System Modules and Architectural Responsibilities", "26"),
        ("4.3", "Healthcare Dataset Attributes and Feature Encoding Matrix", "33"),
        ("4.4", "Application Web Screens Identified in the System Repository", "42"),
        ("5.1", "Classification Performance Metrics for Evaluated Machine Learning Models", "47"),
        ("5.2", "Detailed Per-Class Classification Report for Proposed XGBoost Model", "48"),
        ("5.3", "Benchmarking Proposed System Against Existing Literature Approaches", "51")
    ]
    for num, title, pg in tables:
        row = t_lot.add_row()
        row.cells[0].paragraphs[0].add_run(num)
        row.cells[1].paragraphs[0].add_run(title)
        p = row.cells[2].paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
        p.add_run(pg)
        for cell in row.cells:
            set_cell_margins(cell, 40, 40, 40, 40)

    # ==========================================================
    # 9. LIST OF ABBREVIATIONS
    # ==========================================================
    doc.add_page_break()
    add_styled_heading(doc, "LIST OF ABBREVIATIONS", level=1, align=WD_ALIGN_PARAGRAPH.CENTER)
    
    t_abbr = doc.add_table(rows=1, cols=2)
    t_abbr.alignment = WD_TABLE_ALIGNMENT.CENTER
    t_abbr.autofit = False
    t_abbr.columns[0].width = Inches(2.0)
    t_abbr.columns[1].width = Inches(4.2)
    
    c0 = t_abbr.cell(0, 0)
    c1 = t_abbr.cell(0, 1)
    c0.paragraphs[0].add_run("Abbreviation").font.bold = True
    c1.paragraphs[0].add_run("Expansion").font.bold = True
    set_cell_background(c0, "F1F5F9")
    set_cell_background(c1, "F1F5F9")
    
    abbreviations = [
        ("AI", "Artificial Intelligence"),
        ("API", "Application Programming Interface"),
        ("ASGI", "Asynchronous Server Gateway Interface"),
        ("BMI", "Body Mass Index"),
        ("BP", "Blood Pressure (Systolic / Diastolic)"),
        ("CAD", "Coronary Artery Disease / Cardiovascular Disease"),
        ("CORS", "Cross-Origin Resource Sharing"),
        ("CSV", "Comma-Separated Values"),
        ("DFD", "Data Flow Diagram"),
        ("F1", "Harmonic Mean of Precision and Recall"),
        ("HIPAA", "Health Insurance Portability and Accountability Act"),
        ("HTTP", "Hypertext Transfer Protocol"),
        ("IMDB", "In-Memory Database"),
        ("JSON", "JavaScript Object Notation"),
        ("ML", "Machine Learning"),
        ("NCD", "Non-Communicable Disease"),
        ("OCR", "Optical Character Recognition"),
        ("PHI", "Protected Health Information"),
        ("RAM", "Random Access Memory"),
        ("REST", "Representational State Transfer"),
        ("ROC-AUC", "Receiver Operating Characteristic - Area Under Curve"),
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
            set_cell_margins(cell, 30, 30, 30, 30)

    # Save initial milestone
    doc.save(os.path.join(r'C:\Users\arunk\Projects\health-assistant', 'AI_Preventive_Healthcare_Assistant_Project_Report.docx'))
    print("Preliminaries generated successfully.")
    return doc

if __name__ == '__main__':
    build_report()
