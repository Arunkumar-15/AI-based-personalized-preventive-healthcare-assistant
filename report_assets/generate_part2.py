# generate_final_document.py
# Comprehensive Word Document Generator for Anna University / Sona College of Technology Project Report
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
        p_c.paragraph_format.space_before = Pt(6)
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

def generate_entire_report():
    print("Initializing Document...")
    from build_full_report import build_report
    doc = build_report()
    
    assets_dir = r'C:\Users\arunk\Projects\health-assistant\report_assets'
    user_up_dir = r'C:\Users\arunk\.gemini\antigravity\brain\87427b1b-8625-473d-acdc-fff8d0537b70\.user_uploaded'
    
    fig_4_1 = os.path.join(assets_dir, 'fig_4_1_system_architecture.png')
    fig_4_2 = os.path.join(assets_dir, 'fig_4_2_system_workflow.png')
    fig_5_1 = os.path.join(assets_dir, 'fig_5_1_confusion_matrix.png')
    fig_5_2 = os.path.join(assets_dir, 'fig_5_2_feature_importances.png')
    fig_5_3 = os.path.join(assets_dir, 'fig_5_3_model_comparison.png')
    
    img_ui_input = os.path.join(user_up_dir, 'media_1786777568161.png')
    img_ui_output = os.path.join(user_up_dir, 'media_1786777576251.png')

    # ==========================================================
    # CHAPTER 1: INTRODUCTION
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
    add_bullet_point(doc, "To construct a HIPAA Safe Harbor-compliant anonymization engine utilizing SHA-256 cryptographic pseudonymization, k-anonymity binning, and in-memory execution ensuring zero PHI storage.")
    add_bullet_point(doc, "To design an intuitive, bilingual (English and Tamil) responsive web interface featuring an administrative clinical data repository and PDF medical reporting capabilities.")

    add_styled_heading(doc, "1.5 Scope of the Project", level=2)
    add_body_paragraph(
        doc,
        "The scope of this project encompasses the design, implementation, and empirical verification of the full-stack AI healthcare assistant, spanning the React single-page frontend, the Python FastAPI backend, the XGBoost training and inference pipelines, the SHAP attribution module, and the in-memory anonymized repository. The system is designed as a preventive decision-support instrument and does not claim to replace licensed medical doctors or deliver definitive surgical/pharmacological diagnoses. Clinical deployment must always preserve human medical oversight."
    )

    # ==========================================================
    # CHAPTER 2: LITERATURE REVIEW
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
    add_body_paragraph(
        doc,
        "A rigorous synthesis of the reviewed literature reveals significant application-level research gaps:"
    )
    add_bullet_point(doc, "Multi-Modal Disconnection: Existing platforms either process lifestyle questionnaires OR blood test biomarkers OR medical documents, lacking a unified multi-modal screening architecture capable of transitioning seamlessly across screening tiers [7], [20].")
    add_bullet_point(doc, "The Explanatory Deficit: High-performing predictive models frequently lack native, mathematically sound explainability, preventing users from understanding the clinical rationale behind their assigned risk level [2], [8], [17].")
    add_bullet_point(doc, "Static Diagnostics vs. Proactive Simulation: Current platforms stop at diagnostic classification without offering an interactive 'What-If' digital twin simulator that models real-time risk reduction from personalized lifestyle interventions [5], [15].")
    add_bullet_point(doc, "Data Persistence and Privacy Non-Compliance: Standard healthcare applications persist identifiable patient data on physical hard drives, violating HIPAA Safe Harbor mandates regarding data minimization and ephemeral in-memory execution [3], [10].")

    add_styled_heading(doc, "2.5 Summary", level=2)
    add_body_paragraph(
        doc,
        "The literature establishes that gradient boosting algorithms, particularly XGBoost, represent the gold standard for clinical tabular data analysis. Furthermore, combining TreeSHAP interpretability, digital twin sensitivity simulation, multi-modal ingestion, and zero-disk persistent anonymization directly addresses the structural limitations of existing systems, providing the foundation for the proposed AI-Based Personalized Preventive Healthcare Assistant."
    )

    # Save progress
    doc.save(os.path.join(r'C:\Users\arunk\Projects\health-assistant', 'AI_Preventive_Healthcare_Assistant_Project_Report.docx'))
    print("Chapters 1 & 2 generated.")
    return doc

if __name__ == '__main__':
    generate_entire_report()
