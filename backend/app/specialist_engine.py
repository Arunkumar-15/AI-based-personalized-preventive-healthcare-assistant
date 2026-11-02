"""
Clinical Specialist Triage Engine.
Selects strictly ONE single specialist doctor based on the highest disease probability
for Critical risk patients. For Low, Moderate, and High risk patients, returns None.
"""

from typing import Optional, Dict, List, Set
from backend.app.schemas import RecommendedSpecialist

def evaluate_critical_specialist(
    risk_level: str,
    continuous_score: float,
    disease_breakdown: Dict[str, float],
    sym_set: Set[str],
    fam_set: Set[str],
    norm_smoking: str,
    bmi: float,
    age: int
) -> Optional[RecommendedSpecialist]:
    """
    Evaluates whether the patient is in a Critical state, and if so,
    selects strictly ONE specialist doctor based on the highest disease probability.
    Returns None for Low, Moderate, and High risk patients.
    """
    # Rule 1: We recommend a specialist doctor ONLY for Critical patients.
    is_critical = ("Critical" in risk_level) or (continuous_score >= 75.0)
    if not is_critical:
        return None

    # Calculate disease vulnerability metrics
    cad_score = disease_breakdown.get("Cardiovascular Disease (CAD)", 0.0)
    diabetes_score = disease_breakdown.get("Type-2 Diabetes", 0.0)
    hypertension_score = disease_breakdown.get("Hypertension", 0.0)

    # Pulmonology / Respiratory assessment score
    pulmonology_score = min(
        95.0,
        max(
            5.0,
            (continuous_score * 0.40)
            + (32.0 if "Shortness of Breath" in sym_set else 0)
            + (22.0 if norm_smoking != "Non-smoker" else 0)
        )
    )

    # Neurology / Cerebrovascular assessment score
    neurology_score = min(
        95.0,
        max(
            5.0,
            (continuous_score * 0.40)
            + (28.0 if "Stroke" in fam_set else 0)
            + (18.0 if ("Dizziness" in sym_set and "Headache" in sym_set) else 0)
        )
    )

    # Compare candidates to find the highest possibility disease
    candidates = {
        "CAD": (cad_score, "Cardiovascular Disease (CAD)"),
        "DIABETES": (diabetes_score, "Type-2 Diabetes"),
        "HYPERTENSION": (hypertension_score, "Hypertension & Renal Risk"),
        "PULMONOLOGY": (pulmonology_score, "Pulmonology & Respiratory Impairment"),
        "NEUROLOGY": (neurology_score, "Neurological & Cerebrovascular Risk")
    }

    # Clinical tie-breaker: If chest pain is acute and CAD >= 65, CAD takes acute clinical priority
    if "Chest Pain" in sym_set and cad_score >= 65.0:
        top_key = "CAD"
    else:
        top_key = max(candidates.keys(), key=lambda k: candidates[k][0])

    top_score, _ = candidates[top_key]

    # Map the highest possibility disease to strictly ONE single specialist
    if top_key == "CAD":
        return RecommendedSpecialist(
            specialty_name="Cardiologist",
            specialty_name_ta="இதய நோய் நிபுணர்",
            doctor_title="Consultant Interventional Cardiologist",
            urgency="Critical / Immediate Cardiac Evaluation Needed",
            highest_disease_name="Cardiovascular Disease (CAD)",
            highest_disease_score=round(top_score, 1),
            clinical_reason=f"Your highest disease vulnerability is Cardiovascular Disease (CAD) at {round(top_score, 1)}%, driven by cardiopulmonary strain and vascular risk indicators. Immediate clinical consultation with a Cardiologist is strongly advised to prevent acute cardiac events.",
            clinical_reason_ta=f"உங்கள் அதிகபட்ச ஆபத்து இதய நோய் (CAD - {round(top_score, 1)}%) ஆகும். மார்பு வலி மற்றும் ரத்த ஓட்ட பாதிப்புகளைத் தடுக்க உடனடியாக இதய நோய் நிபுணரை (Cardiologist) அணுகவும்.",
            recommended_tests=[
                "12-Lead Electrocardiogram (ECG / EKG)",
                "2D Echocardiogram with Color Doppler",
                "Comprehensive Lipid Profile (Total, LDL, HDL, Triglycerides)",
                "Cardiac Troponin-I / High-Sensitivity CRP (hs-CRP)"
            ],
            questions_to_ask=[
                "Do my current symptoms indicate coronary artery stenosis or acute myocardial ischemia?",
                "What is my target LDL-C level, and do I need preventive cardioprotective medication?",
                "Is a treadmill stress test (TMT) or CT Coronary Angiogram indicated?"
            ],
            clinic_type="Cardiac Care Unit (CCU) / Cardiology Outpatient Clinic"
        )
    elif top_key == "DIABETES":
        return RecommendedSpecialist(
            specialty_name="Diabetologist / Endocrinologist",
            specialty_name_ta="சர்க்கரை மற்றும் நாளமில்லா சுரப்பி நிபுணர்",
            doctor_title="Consultant Diabetologist & Endocrinologist",
            urgency="Critical / Prompt Glycemic & Metabolic Review Needed",
            highest_disease_name="Type-2 Diabetes",
            highest_disease_score=round(top_score, 1),
            clinical_reason=f"Your highest disease vulnerability is Type-2 Diabetes at {round(top_score, 1)}%, indicating severe glycemic dysregulation and metabolic stress. Clinical intervention by an Endocrinologist is critical to prevent microvascular and macrovascular complications.",
            clinical_reason_ta=f"உங்கள் அதிகபட்ச ஆபத்து வகை-2 நீரிழிவு நோய் ({round(top_score, 1)}%) ஆகும். ரத்த சர்க்கரை அளவை கட்டுப்படுத்தவும் உறுப்பு பாதிப்புகளைத் தடுக்கவும் உடனடியாக சர்க்கரை நோய் நிபுணரை (Diabetologist) அணுகவும்.",
            recommended_tests=[
                "Fasting & 2-Hour Postprandial Plasma Glucose (FBS / PPBS)",
                "Glycated Hemoglobin (HbA1c) Glycemic Index Test",
                "Fasting Serum Insulin & C-Peptide Assessment",
                "Urine Routine & Microalbuminuria Screening"
            ],
            questions_to_ask=[
                "What is my individualized HbA1c target, and what pharmacological intervention is appropriate?",
                "How frequently should I self-monitor my blood glucose (SMBG) at home?",
                "What medical nutrition therapy steps must I start immediately to preserve beta-cell function?"
            ],
            clinic_type="Endocrinology & Diabetes Comprehensive Care Center"
        )
    elif top_key == "HYPERTENSION":
        # If accompanied by elevated diabetes or high BMI, Nephrology is critical
        is_renal_indicated = (diabetes_score >= 60.0) or (bmi >= 30.0)
        if is_renal_indicated:
            return RecommendedSpecialist(
                specialty_name="Nephrologist",
                specialty_name_ta="சிறுநீரக சிறப்பு மருத்துவர்",
                doctor_title="Consultant Nephrologist & Renal Specialist",
                urgency="Critical / Urgent Renal Function Assessment",
                highest_disease_name="Hypertension with Renal Vulnerability",
                highest_disease_score=round(top_score, 1),
                clinical_reason=f"Your highest disease risk is severe Hypertension ({round(top_score, 1)}%) combined with metabolic strain, putting kidney filtration at imminent risk. A Nephrologist evaluation is essential to prevent chronic kidney disease and diabetic nephropathy.",
                clinical_reason_ta=f"உயர் ரத்த அழுத்தம் மற்றும் சர்க்கரை பாதிப்பால் உங்கள் சிறுநீரக செயல்பாடு ஆபத்தில் உள்ளது ({round(top_score, 1)}%). சிறுநீரக செயலிழப்பைத் தடுக்க சிறுநீரக மருத்துவரை (Nephrologist) அணுகவும்.",
                recommended_tests=[
                    "Serum Creatinine & Estimated Glomerular Filtration Rate (eGFR)",
                    "Blood Urea Nitrogen (BUN) and Serum Electrolytes (Na+, K+)",
                    "Spot Urine Albumin-to-Creatinine Ratio (uACR)",
                    "Renal Artery Doppler Ultrasound"
                ],
                questions_to_ask=[
                    "Are my blood pressure levels causing any early renal hyperfiltration or nephron damage?",
                    "What are the best renoprotective antihypertensive options for my specific clinical profile?",
                    "What dietary sodium and protein restrictions should I adhere to?"
                ],
                clinic_type="Nephrology & Renal Care Clinic"
            )
        else:
            return RecommendedSpecialist(
                specialty_name="Hypertension Specialist / Cardiologist",
                specialty_name_ta="ரத்த அழுத்த மற்றும் இதய நிபுணர்",
                doctor_title="Consultant Physician & Hypertension Specialist",
                urgency="Critical / Immediate Blood Pressure Control Required",
                highest_disease_name="Severe Hypertension",
                highest_disease_score=round(top_score, 1),
                clinical_reason=f"Your highest disease risk is severe Hypertension at {round(top_score, 1)}%. Uncontrolled vascular pressure significantly increases the risk of stroke, aneurysm, and hypertensive heart disease. Urgent evaluation is required.",
                clinical_reason_ta=f"உங்கள் அதிகபட்ச ஆபத்து தீவிர உயர் இரத்த அழுத்தம் ({round(top_score, 1)}%) ஆகும். பக்கவாதம் மற்றும் இதய பாதிப்பைத் தடுக்க உடனடியாக ரத்த அழுத்த சிறப்பு மருத்துவரை அணுகவும்.",
                recommended_tests=[
                    "24-Hour Ambulatory Blood Pressure Monitoring (ABPM)",
                    "Fundoscopy (Hypertensive Retinopathy Eye Exam)",
                    "Serum Electrolytes (Sodium, Potassium, Chloride)",
                    "12-Lead Electrocardiogram (ECG) for Left Ventricular Hypertrophy"
                ],
                questions_to_ask=[
                    "What is my target resting blood pressure, and do I need multi-agent antihypertensive therapy?",
                    "Are there signs of secondary hypertension or target organ damage?",
                    "How should I track my blood pressure readings twice daily at home?"
                ],
                clinic_type="Hypertension & Vascular Medicine Clinic"
            )
    elif top_key == "PULMONOLOGY":
        return RecommendedSpecialist(
            specialty_name="Pulmonologist / Chest Physician",
            specialty_name_ta="நுரையீரல் மற்றும் சுவாச நோய் நிபுணர்",
            doctor_title="Consultant Pulmonologist & Respiratory Specialist",
            urgency="Critical / Respiratory Function Evaluation",
            highest_disease_name="Pulmonology & Respiratory Impairment",
            highest_disease_score=round(top_score, 1),
            clinical_reason=f"Your highest risk indicator is Respiratory and Pulmonary Impairment at {round(top_score, 1)}%, aggravated by shortness of breath and tobacco exposure. A Pulmonologist consultation is required to assess airway resistance and lung capacity.",
            clinical_reason_ta=f"உங்கள் அதிகபட்ச ஆபத்து நுரையீரல் மற்றும் சுவாசக் கோளாறு ({round(top_score, 1)}%) ஆகும். மூச்சுத் திணறல் தீவிரமடைவதைத் தடுக்க உடனடியாக நுரையீரல் நிபுணரை (Pulmonologist) அணுகவும்.",
            recommended_tests=[
                "Spirometry / Pulmonary Function Test (PFT)",
                "High-Resolution Chest Radiograph (CXR) or Low-Dose Chest CT",
                "Pulse Oximetry & Resting/Exertional Arterial Blood Gas (ABG)",
                "Carbon Monoxide (CO) Exhalation Assessment"
            ],
            questions_to_ask=[
                "Do my symptoms indicate Chronic Obstructive Pulmonary Disease (COPD) or reactive airway disease?",
                "What medical cessation therapy can protect my alveoli from further progressive injury?",
                "Are bronchodilators or pulmonary rehabilitation recommended for me?"
            ],
            clinic_type="Pulmonology & Respiratory Care Clinic"
        )
    else:  # NEUROLOGY
        return RecommendedSpecialist(
            specialty_name="Neurologist",
            specialty_name_ta="நரம்பியல் நிபுணர்",
            doctor_title="Consultant Neurologist & Stroke Specialist",
            urgency="Critical / Immediate Neurological Assessment",
            highest_disease_name="Neurological & Cerebrovascular Risk",
            highest_disease_score=round(top_score, 1),
            clinical_reason=f"Your highest vulnerability index is Cerebrovascular & Neurological Risk at {round(top_score, 1)}%, compounded by neurological symptoms and family stroke vulnerability. Immediate neurological evaluation is recommended to assess cerebral perfusion.",
            clinical_reason_ta=f"உங்கள் அதிகபட்ச ஆபத்து நரம்பியல் மற்றும் பக்கவாத பாதிப்பு ({round(top_score, 1)}%) ஆகும். மூளை ரத்த ஓட்டத்தை பரிசோதிக்க உடனடியாக நரம்பியல் நிபுணரை (Neurologist) அணுகவும்.",
            recommended_tests=[
                "Carotid Artery Doppler Ultrasound (Extracranial Doppler)",
                "Brain MRI / MR Angiography (MRA) or CT Angio",
                "Comprehensive Neurological Cranial Nerve Examination",
                "Fasting Homocysteine & Lipid Micro-panel"
            ],
            questions_to_ask=[
                "Are my headaches and dizziness transient ischemic indicators (TIA)?",
                "What is my 5-year stroke probability given my family medical history?",
                "What preventive neuroprotective interventions are recommended?"
            ],
            clinic_type="Neurology & Comprehensive Stroke Prevention Center"
        )
