"""
Generates 2 dedicated separate CSV datasets for Mode 2 (Advanced Clinical Lab Biomarkers)
and Mode 3 (Medical Report Upload & OCR Ingestion).
"""

import os
import shutil
import numpy as np
import pandas as pd

def generate_mode_datasets():
    np.random.seed(42)
    n_samples = 3500

    # ==========================================
    # DATASET 2: MODE 2 CLINICAL LAB BIOMARKERS
    # ==========================================
    ages = np.random.randint(18, 85, size=n_samples)
    genders = np.random.choice(['Male', 'Female', 'Other'], size=n_samples, p=[0.51, 0.47, 0.02])
    heights = np.where(genders == 'Male', np.random.normal(172, 7, n_samples), np.random.normal(160, 6, n_samples)).round(1)
    weights = np.where(genders == 'Male', np.random.normal(78, 14, n_samples), np.random.normal(66, 12, n_samples)).round(1)
    bmis = (weights / ((heights / 100) ** 2)).round(1)

    # Clinical Biomarkers
    systolic_bp = np.random.normal(122, 16, n_samples).round(0).astype(int)
    diastolic_bp = (systolic_bp * 0.65 + np.random.normal(5, 4, n_samples)).round(0).astype(int)
    fasting_glucose = np.random.normal(105, 25, n_samples).round(1)
    hba1c = (fasting_glucose * 0.04 + np.random.normal(1.2, 0.4, n_samples)).round(1)
    total_cholesterol = np.random.normal(195, 35, n_samples).round(1)
    hdl = np.random.normal(48, 10, n_samples).round(1)
    ldl = (total_cholesterol - hdl - 20).round(1)
    triglycerides = np.random.normal(145, 40, n_samples).round(1)
    resting_hr = np.random.normal(74, 9, n_samples).round(0).astype(int)

    # Lifestyle & Symptoms
    smk = np.random.choice(['Non-smoker', 'Former Smoker', 'Occasional Smoker', 'Regular Smoker'], size=n_samples, p=[0.55, 0.20, 0.10, 0.15])
    alc = np.random.choice(['None', 'Occasional', 'Moderate', 'Frequent'], size=n_samples, p=[0.45, 0.30, 0.15, 0.10])
    phy = np.random.choice(['Sedentary', 'Light', 'Moderate', 'Active'], size=n_samples, p=[0.30, 0.35, 0.25, 0.10])
    slp = np.random.normal(6.8, 1.1, n_samples).round(1)
    fam = np.random.choice(['None', 'Heart Disease', 'Diabetes', 'Hypertension', 'Stroke'], size=n_samples, p=[0.40, 0.20, 0.20, 0.10, 0.10])

    # Calculate Multi-Disease Risk Percentages
    cad_risk = np.clip((ages * 0.4) + (systolic_bp * 0.25) + (total_cholesterol * 0.15) - 25, 5.0, 95.0).round(1)
    diabetes_risk = np.clip((fasting_glucose * 0.4) + (hba1c * 5.0) + (bmis * 0.8) - 30, 5.0, 95.0).round(1)
    hypertension_risk = np.clip((systolic_bp * 0.5) + (diastolic_bp * 0.3) - 35, 5.0, 95.0).round(1)
    overall_score = np.clip((cad_risk * 0.4 + diabetes_risk * 0.35 + hypertension_risk * 0.25), 8.0, 98.0).round(1)

    risk_levels = []
    for s in overall_score:
        if s < 35: risk_levels.append('Low')
        elif s < 65: risk_levels.append('Moderate')
        elif s < 85: risk_levels.append('High')
        else: risk_levels.append('Critical')

    df_mode2 = pd.DataFrame({
        'patient_id': [f'PAT-{1000+i}' for i in range(n_samples)],
        'age': ages,
        'gender': genders,
        'height_cm': heights,
        'weight_kg': weights,
        'bmi': bmis,
        'systolic_bp': systolic_bp,
        'diastolic_bp': diastolic_bp,
        'fasting_glucose': fasting_glucose,
        'hba1c': hba1c,
        'total_cholesterol': total_cholesterol,
        'hdl_cholesterol': hdl,
        'ldl_cholesterol': ldl,
        'triglycerides': triglycerides,
        'resting_heart_rate': resting_hr,
        'smoking_habit': smk,
        'alcohol_consumption': alc,
        'physical_activity': phy,
        'sleep_hours': slp,
        'family_history': fam,
        'cad_risk_pct': cad_risk,
        'diabetes_risk_pct': diabetes_risk,
        'hypertension_risk_pct': hypertension_risk,
        'overall_risk_score': overall_score,
        'risk_level': risk_levels
    })

    # ==========================================
    # DATASET 3: MODE 3 OCR REPORT EXTRACTIONS
    # ==========================================
    file_formats = np.random.choice(['PDF_Report', 'PNG_Scan', 'JPG_Scan'], size=n_samples, p=[0.60, 0.25, 0.15])
    confidence_scores = np.random.normal(98.2, 1.2, n_samples).clip(92.0, 99.9).round(1)
    dates = [f"2026-08-{(i%28)+1:02d}" for i in range(n_samples)]

    df_mode3 = pd.DataFrame({
        'document_id': [f'DOC-{8000+i}' for i in range(n_samples)],
        'file_format': file_formats,
        'file_name': [f'Lab_Report_{100+i}.pdf' if file_formats[i] == 'PDF_Report' else f'Pathology_Scan_{100+i}.png' for i in range(n_samples)],
        'extracted_date': dates,
        'ocr_engine_version': 'Tesseract-Vision-v4.2',
        'ocr_confidence_score': confidence_scores,
        'extracted_systolic_bp': systolic_bp,
        'extracted_diastolic_bp': diastolic_bp,
        'extracted_fasting_glucose': fasting_glucose,
        'extracted_hba1c': hba1c,
        'extracted_total_cholesterol': total_cholesterol,
        'extracted_heart_rate': resting_hr,
        'ocr_validation_status': 'VERIFIED_PARSED',
        'processed_risk_level': risk_levels
    })

    # Save Paths
    project_dataset_dir = r"C:\Users\arunk\Projects\health-assistant\backend\dataset"
    downloads_dir = r"C:\Users\arunk\Downloads"

    csv_mode2_proj = os.path.join(project_dataset_dir, "healthcare_clinical_biomarkers_mode2.csv")
    csv_mode2_down = os.path.join(downloads_dir, "healthcare_clinical_biomarkers_mode2.csv")

    csv_mode3_proj = os.path.join(project_dataset_dir, "medical_ocr_extracted_reports_mode3.csv")
    csv_mode3_down = os.path.join(downloads_dir, "medical_ocr_extracted_reports_mode3.csv")

    df_mode2.to_csv(csv_mode2_proj, index=False)
    shutil.copy2(csv_mode2_proj, csv_mode2_down)

    df_mode3.to_csv(csv_mode3_proj, index=False)
    shutil.copy2(csv_mode3_proj, csv_mode3_down)

    print(f"Mode 2 Clinical Dataset generated successfully: {csv_mode2_proj} ({len(df_mode2)} records)")
    print(f"Mode 3 OCR Report Dataset generated successfully: {csv_mode3_proj} ({len(df_mode3)} records)")

if __name__ == '__main__':
    generate_mode_datasets()
