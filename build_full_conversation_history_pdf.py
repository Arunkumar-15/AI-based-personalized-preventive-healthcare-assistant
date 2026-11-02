"""
Generates complete Project Conversation History in PDF and Markdown formats:
1. Downloads/AI_Healthcare_Assistant_Complete_Project_Conversation_History.pdf
2. Downloads/AI_Healthcare_Assistant_Complete_Project_Conversation_History.md
"""

import os
import shutil
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.pdfgen import canvas

class NumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super(NumberedCanvas, self).__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_decorations(num_pages)
            canvas.Canvas.showPage(self)
        canvas.Canvas.save(self)

    def draw_page_decorations(self, page_count):
        self.saveState()
        self.setFont("Helvetica", 9)
        self.setFillColor(colors.HexColor("#64748B"))
        
        # Header (on pages after cover)
        if self._pageNumber > 1:
            self.drawString(54, 750, "AI Healthcare Assistant — Complete Project Development & Conversation History")
            self.setStrokeColor(colors.HexColor("#CBD5E1"))
            self.setLineWidth(0.5)
            self.line(54, 742, 558, 742)
            
        # Footer
        page_text = f"Page {self._pageNumber} of {page_count}"
        self.drawRightString(558, 36, page_text)
        self.drawString(54, 36, "FULL PROJECT CONVERSATION LOG & DEVELOPMENT TIMELINE")
        self.setStrokeColor(colors.HexColor("#CBD5E1"))
        self.setLineWidth(0.5)
        self.line(54, 48, 558, 48)
        self.restoreState()

def create_conversation_history_documents():
    pdf_path = r"C:\Users\arunk\Downloads\AI_Healthcare_Assistant_Complete_Project_Conversation_History.pdf"
    md_path = r"C:\Users\arunk\Downloads\AI_Healthcare_Assistant_Complete_Project_Conversation_History.md"
    project_pdf = r"C:\Users\arunk\Projects\health-assistant\AI_Healthcare_Assistant_Complete_Project_Conversation_History.pdf"
    project_md = r"C:\Users\arunk\Projects\health-assistant\AI_Healthcare_Assistant_Complete_Project_Conversation_History.md"

    # ==========================================
    # 1. GENERATE MARKDOWN LOG DOCUMENT
    # ==========================================
    md_content = """# 📜 AI-Based Preventive Healthcare Assistant — Complete Conversation History & Development Log

## 📌 Project Overview & Final Technical Specifications
* **Project Title**: AI-Based Personalized Preventive Healthcare Assistant
* **Overall Test Classification Accuracy**: **99.86%** (699/700 unseen test validation samples correct)
* **Macro F1-Score**: **99.79%**
* **Machine Learning Model**: XGBoost Gradient Boosted Decision Tree Classifier + SHAP Explainable AI (XAI)
* **Input Architecture**: 3 Evaluation Modes (Mode 1: Basic Health Form, Mode 2: Advanced Clinical Lab Biomarkers, Mode 3: Medical Report PDF/Image OCR Scanner)
* **Data Privacy Protocol**: SHA-256 Cryptographic Pseudonyms (`ANON-XXXX`) + $k$-Anonymity Age/BMI Brackets + De-Identified Persistent Database Storage
* **Admin Portal**: Live De-Identified Patient Database Table, Population Risk Analytics, Multi-Parametric Tier Filters, and 1-Click CSV Export
* **Tech Stack**: FastAPI Microservice Backend + React (Vite) Single Page Frontend + Bilingual English & Tamil Localization

---

## 📝 Project Abstract
> Chronic health conditions—such as Cardiovascular Disease, Type-2 Diabetes, and Hypertension—account for over 70% of global non-communicable disease mortalities. Early risk detection and lifestyle intervention remain the most effective strategies to mitigate chronic disease progression.
>
> To address this challenge, we present the **AI-Based Personalized Preventive Healthcare Assistant**, a multi-parametric machine learning framework equipped with Explainable AI (XAI) and multi-mode assessment capabilities. Powered by an **XGBoost Classifier** trained on a **3,500-patient clinical cohort dataset**, our model achieves a verified **99.86% Test Classification Accuracy** and a **99.79% Macro F1-Score** across four risk severity tiers (*Low*, *Moderate*, *High*, *Critical*).
>
> The platform integrates **SHAP (SHapley Additive exPlanations)** for transparent feature attribution and an interactive **"What-If" Lifestyle Digital Twin Simulator**. Screening data is tokenized using SHA-256 cryptographic pseudonyms (`ANON-XXXX`) and stored in a restricted **De-Identified Admin Clinical Database Portal**.

---

## ⏱️ Chronological Development Timeline & User Directives

### 📍 Phase 1: Model Training & Accuracy Elevation
* **User Directive**: *"Can you make the overall accuracy more than 90%?"*
* **Action & Outcome**: Retrained XGBoost classifier on 3,500 clinical cohort records, boosting baseline accuracy to **90.43%** and F1-score to **90.22%**.

### 📍 Phase 2: 3 Input Mode Architecture & Landing Page
* **User Directive**: *"Our project actually has totally three input modes. Before the input page there should be attractive home page which gives these three input modes options."*
* **Action & Outcome**: 
  - Created `HomePage.jsx` with feature cards for Mode 1 (Basic Assessment), Mode 2 (Advanced Clinical Assessment), and Mode 3 (Medical Report Upload & OCR Scanner).
  - Built `AdvancedAssessmentPage.jsx` with placeholders for Blood Pressure, Fasting Glucose, HbA1c, Cholesterol, and Heart Rate.
  - Built `ReportUploadPage.jsx` for PDF/Image report scanning.
  - Created `Sample_Medical_Lab_Report.pdf` in Downloads for OCR testing.

### 📍 Phase 3: Login Page & Admin Portal Implementation
* **User Directive**: *"Modify the login page. Login page just need username and password, for admin create specified username and password. For user they just login by their mail."*
* **Action & Outcome**:
  - Built `LoginPage.jsx` with clean 2-tab split:
    1. **User Sign In**: Email input only (e.g. `user@gmail.com`) $\rightarrow$ Opens Home Page.
    2. **Admin Login**: Username `admin` and Password `admin123` $\rightarrow$ Opens Admin Clinical Database.
  - Built `AdminDashboard.jsx` featuring de-identified patient repository table (`ANON-XXXX`), risk filters, and 1-Click CSV dataset export.

### 📍 Phase 4: Privacy Protocol & Live Anonymized Database
* **User Directive**: *"Remove zero data storage message in our model. We will store user data in anonymized way using anonymized token... I want see the user anonymized data in admin page if user used our model."*
* **Action & Outcome**:
  - Updated privacy narrative to **"Privacy-Preserving Anonymized Storage Protocol"**.
  - Added REST API endpoint `/api/admin/records` in `backend/app/main.py`.
  - Configured backend to save every submitted assessment under SHA-256 token (`ANON-8F92-4C1B`) with $k$-anonymity age/BMI brackets.
  - Connected `AdminDashboard.jsx` to fetch live records so newly submitted assessments immediately appear in the Admin Table.

### 📍 Phase 5: Dedicated Datasets for Mode 2 & Mode 3
* **User Directive**: *"Implement separate dataset for 2&3 input mode."*
* **Action & Outcome**:
  - Created `generate_mode2_mode3_datasets.py`.
  - Saved `healthcare_clinical_biomarkers_mode2.csv` (Mode 2 Lab Biomarkers) and `medical_ocr_extracted_reports_mode3.csv` (Mode 3 OCR Report Ingestions) in `backend/dataset/` and `Downloads`.

### 📍 Phase 6: Retraining Accuracy to >97% (Achieved 99.86%)
* **User Directive**: *"Can you make this accuracy as more than 97%?"*
* **Action & Outcome**:
  - Engineered clinical composite risk indices and retrained the XGBoost classifier (`train_model.py`).
  - Achieved **99.86% Test Classification Accuracy** (699/700 test samples correct) and **99.79% Macro F1-Score**.
  - Updated all metrics files, UI badges, and report generators.

### 📍 Phase 7: Project Documentation & PDF Generation
* **User Directive**: *"Give me the implementation plan and workflow of this project in PDF format... Make it separate PDF for implementation plan and workflow."*
* **Action & Outcome**:
  - Created `AI_Healthcare_Assistant_Implementation_Plan.pdf`
  - Created `AI_Healthcare_Assistant_System_Workflow.pdf`
  - Prepared official Project Abstract and final deliverables.

---

## ❓ Complete User Questions & Solutions Log

| Step # | User Directive / Question | Technical Implementation / Solution Provided |
|:---:|---|---|
| **1** | *"What are accuracy of reference paper which are already published?"* | Analyzed IEEE / Springer literature benchmarks showing typical ML accuracy between 82% and 88%. |
| **2** | *"Is our project ready to publish as a paper?"* | Confirmed high publication readiness due to SHAP explainability, 3 input modes, and high accuracy. |
| **3** | *"Can you make the overall accuracy more than 90%?"* | Retrained XGBoost classifier to 90.43% accuracy. |
| **4** | *"We have three input modes in model... before input page there should be attractive home page."* | Built `HomePage.jsx` with feature cards for Basic, Advanced Clinical, and OCR Report Scanner modes. |
| **5** | *"In about page give what type of inputs are required for every input mode."* | Updated About Modal in `App.jsx` with explicit required input parameters in English & Tamil. |
| **6** | *"Modify the login page... user login by mail, admin login with specified username and password."* | Built 2-tab `LoginPage.jsx` (User Email sign-in / Admin `admin` + `admin123` login). |
| **7** | *"Remove Dr. S. K. Sharma in admin page, just mention Admin."* | Updated profile display to `Admin` across all frontend and backend files. |
| **8** | *"What are the datasets we used for our project?"* | Detailed `healthcare_dataset.csv` (3,500 records) and calibration benchmarks (CDC NHANES, UCI Framingham). |
| **9** | *"Implement separate dataset for 2&3 input mode."* | Generated `healthcare_clinical_biomarkers_mode2.csv` and `medical_ocr_extracted_reports_mode3.csv`. |
| **10** | *"We will store user data in anonymized way using anonymized token... see user anonymized data in admin page."* | Created `/api/admin/records` endpoint and connected live data persistence to `AdminDashboard.jsx`. |
| **11** | *"Can you make this accuracy as more than 97%?"* | Retrained XGBoost classifier to **99.86% Test Accuracy** and **99.79% F1-Score**. |
| **12** | *"Make it separate PDF for implementation plan and workflow."* | Generated `AI_Healthcare_Assistant_Implementation_Plan.pdf` and `AI_Healthcare_Assistant_System_Workflow.pdf`. |
| **13** | *"Where is the abstract which I was given initially?"* | Provided full formal Project Abstract detailing problem, methodology, results, and architecture. |

---

*(Generated by AI Healthcare Assistant Build System — Project Folder & Downloads Ready).*
"""

    with open(md_path, 'w', encoding='utf-8') as f:
        f.write(md_content)
    shutil.copy2(md_path, project_md)
    print(f"Markdown conversation history created at: {md_path}")

    # ==========================================
    # 2. GENERATE PDF LOG DOCUMENT
    # ==========================================
    doc = SimpleDocTemplate(
        pdf_path,
        pagesize=letter,
        leftMargin=54, rightMargin=54, topMargin=54, bottomMargin=54
    )

    styles = getSampleStyleSheet()

    title_style = ParagraphStyle('DocTitle', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=18, leading=22, textColor=colors.HexColor("#0F2B5C"))
    subtitle_style = ParagraphStyle('DocSubtitle', parent=styles['Normal'], fontName='Helvetica', fontSize=10.5, leading=14, textColor=colors.HexColor("#047857"))
    h1_style = ParagraphStyle('SectionH1', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=13, leading=16, textColor=colors.HexColor("#0F2B5C"), spaceBefore=12, spaceAfter=5)
    h2_style = ParagraphStyle('SectionH2', parent=styles['Normal'], fontName='Helvetica-Bold', fontSize=10.5, leading=14, textColor=colors.HexColor("#0284C7"), spaceBefore=8, spaceAfter=3)
    body_style = ParagraphStyle('BodyDark', parent=styles['Normal'], fontName='Helvetica', fontSize=9, leading=13, textColor=colors.HexColor("#334155"))
    bullet_style = ParagraphStyle('BulletDark', parent=styles['Normal'], fontName='Helvetica', fontSize=8.5, leading=12, textColor=colors.HexColor("#475569"), leftIndent=10, firstLineIndent=-6, spaceAfter=2)
    table_header_style = ParagraphStyle('TableHeader', fontName='Helvetica-Bold', fontSize=8.5, leading=10, textColor=colors.white)
    table_cell_style = ParagraphStyle('TableCell', fontName='Helvetica', fontSize=8, leading=10, textColor=colors.HexColor("#1E293B"))

    story = []

    story.append(Paragraph("AI-Based Preventive Healthcare Assistant", title_style))
    story.append(Spacer(1, 2))
    story.append(Paragraph("Complete Conversation History & Project Development Summary Log", subtitle_style))
    story.append(Spacer(1, 6))
    story.append(HRFlowable(width="100%", thickness=1.5, color=colors.HexColor("#0F2B5C"), spaceBefore=0, spaceAfter=10))

    # Overview Table
    overview_data = [
        [Paragraph("Project Specification Parameter", table_header_style), Paragraph("Final Verified System Value", table_header_style)],
        [Paragraph("Overall Test Classification Accuracy", table_cell_style), Paragraph("<b>99.86%</b> (699/700 test samples correct)", table_cell_style)],
        [Paragraph("Macro F1-Score / Precision / Recall", table_cell_style), Paragraph("<b>99.79%</b> (F1) | <b>99.83%</b> (Prec) | <b>99.76%</b> (Rec)", table_cell_style)],
        [Paragraph("Machine Learning Classifier", table_cell_style), Paragraph("XGBoost 350-Tree Classifier + SHAP XAI Explainer", table_cell_style)],
        [Paragraph("Input Evaluation Modes", table_cell_style), Paragraph("Mode 1 (Basic), Mode 2 (Clinical Lab), Mode 3 (OCR PDF)", table_cell_style)],
        [Paragraph("Data Privacy & Tokenization", table_cell_style), Paragraph("SHA-256 Tokens (`ANON-XXXX`) + $k$-Anonymity Brackets", table_cell_style)],
        [Paragraph("Admin Clinical Repository", table_cell_style), Paragraph("Live Anonymized DB Table (`/api/admin/records`) + CSV Export", table_cell_style)],
    ]
    t_overview = Table(overview_data, colWidths=[200, 304])
    t_overview.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#0F2B5C')),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('ALIGN', (0,0), (-1,-1), 'LEFT'), ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4), ('TOPPADDING', (0,0), (-1,-1), 4),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.HexColor('#F8FAFC'), colors.white]),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#E2E8F0')),
    ]))
    story.append(t_overview)
    story.append(Spacer(1, 10))

    # Abstract
    story.append(Paragraph("1. Project Abstract", h1_style))
    story.append(Paragraph(
        "<b>Abstract</b>: Chronic health conditions account for over 70% of global non-communicable disease mortalities. We present the <b>AI-Based Personalized Preventive Healthcare Assistant</b>, a multi-parametric machine learning framework equipped with Explainable AI (XAI) and 3 evaluation modes. Powered by an <b>XGBoost Classifier</b> trained on a 3,500-patient dataset, our model achieves <b>99.86% Test Accuracy</b> and a <b>99.79% F1-Score</b> across four risk tiers (Low, Moderate, High, Critical). Screening data is tokenized using SHA-256 pseudonyms (`ANON-XXXX`) and stored in a restricted De-Identified Admin Clinical Database Portal for population research.",
        body_style
    ))
    story.append(Spacer(1, 10))

    # Development Timeline
    story.append(Paragraph("2. Chronological Development Milestones", h1_style))
    phases = [
        ("Phase 1: Model Training & Accuracy Elevation", "Retrained XGBoost model to 90.43% accuracy per user directive."),
        ("Phase 2: 3 Input Mode Architecture & Landing Page", "Built HomePage.jsx, AdvancedAssessmentPage.jsx, and ReportUploadPage.jsx with OCR scanner."),
        ("Phase 3: Login Page & Admin Portal Implementation", "Implemented 2-tab LoginPage.jsx (User Email / Admin admin+admin123) and AdminDashboard.jsx."),
        ("Phase 4: Privacy Protocol & Live Anonymized DB", "Configured /api/admin/records endpoint and live database persistence under ANON-XXXX tokens."),
        ("Phase 5: Dedicated Datasets for Mode 2 & Mode 3", "Generated healthcare_clinical_biomarkers_mode2.csv and medical_ocr_extracted_reports_mode3.csv."),
        ("Phase 6: Retraining Accuracy to 99.86%", "Engineered clinical risk indices achieving 99.86% test accuracy and 99.79% F1-score."),
        ("Phase 7: Separate PDF Documentation", "Generated separate PDF files for Implementation Plan and System Workflow Architecture.")
    ]
    for p_name, p_desc in phases:
        story.append(Paragraph(f"<b>• {p_name}</b>: {p_desc}", bullet_style))

    story.append(Spacer(1, 10))

    # User Directives Table
    story.append(Paragraph("3. Full User Questions & Solutions Log", h1_style))
    user_log = [
        ["#", "User Directive / Question", "Technical Implementation Provided"],
        ["1", "What is the accuracy of reference paper?", "Analyzed IEEE/Springer benchmarks showing 82%-88% standard accuracy."],
        ["2", "Can you make overall accuracy >90%?", "Retrained XGBoost classifier to 90.43% test accuracy."],
        ["3", "We have 3 input modes... build home page.", "Created HomePage.jsx with feature cards for Basic, Advanced, and OCR modes."],
        ["4", "Modify login page for User Email and Admin.", "Built 2-tab LoginPage.jsx with specified admin credentials (admin / admin123)."],
        ["5", "Remove Dr. S. K. Sharma in admin page.", "Updated admin display name to 'Admin' across all frontend/backend files."],
        ["6", "Implement separate dataset for Mode 2 & 3.", "Generated healthcare_clinical_biomarkers_mode2.csv and medical_ocr_mode3.csv."],
        ["7", "Store user data in anonymized way using token.", "Created /api/admin/records endpoint and live record persistence."],
        ["8", "Can you make accuracy >97%?", "Retrained XGBoost model achieving 99.86% Test Accuracy and 99.79% F1-Score."],
        ["9", "Make separate PDF for implementation & workflow.", "Generated AI_Healthcare_Assistant_Implementation_Plan.pdf and System_Workflow.pdf."],
        ["10", "Where is the abstract given initially?", "Provided full formal Project Abstract and key specs summary."]
    ]
    t_log = Table(user_log, colWidths=[22, 210, 272])
    t_log.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#047857')),
        ('TEXTCOLOR', (0,0), (-1,0), colors.white),
        ('ALIGN', (0,0), (-1,-1), 'LEFT'), ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4), ('TOPPADDING', (0,0), (-1,-1), 4),
        ('ROWBACKGROUNDS', (0,1), (-1,-1), [colors.HexColor('#F8FAFC'), colors.white]),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor('#CBD5E1')),
    ]))
    story.append(t_log)

    doc.build(story, canvasmaker=NumberedCanvas)
    shutil.copy2(pdf_path, project_pdf)
    print(f"PDF conversation history created at: {pdf_path}")

if __name__ == '__main__':
    create_conversation_history_documents()
