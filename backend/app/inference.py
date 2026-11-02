"""
Real-Time Inference Engine: Preprocessing, XGBoost Prediction, and SHAP Explainability.
"""

import os
import json
import joblib
import numpy as np
import pandas as pd
from datetime import datetime
from typing import Dict, List, Tuple
import shap

from backend.app.schemas import (
    BasicAssessmentRequest, PredictionResponse, SHAPFactor, PrivacyMetadata, RecommendedSpecialist
)
from backend.app.guidance_engine import (
    generate_preventive_guidance, get_bmi_category, DISCLAIMER_TEXT
)
from backend.app.anonymizer import anonymizer
from backend.app.specialist_engine import evaluate_critical_specialist

FEATURE_DISPLAY_NAMES = {
    'age': 'Age',
    'height_cm': 'Height',
    'weight_kg': 'Weight',
    'bmi': 'Body Mass Index (BMI)',
    'sleep_hours': 'Sleep Duration',
    'gender_enc': 'Gender',
    'smoking_enc': 'Smoking Habit',
    'alcohol_enc': 'Alcohol Consumption',
    'physical_enc': 'Physical Activity Level',
    'fam_hypertension': 'Family History: Hypertension',
    'fam_diabetes': 'Family History: Diabetes',
    'fam_heart_disease': 'Family History: Heart Disease',
    'fam_stroke': 'Family History: Stroke',
    'fam_cancer': 'Family History: Cancer',
    'symptom_fatigue': 'Symptom: Fatigue',
    'symptom_chest_pain': 'Symptom: Chest Pain',
    'symptom_excessive_thirst': 'Symptom: Excessive Thirst',
    'symptom_frequent_urination': 'Symptom: Frequent Urination',
    'symptom_shortness_of_breath': 'Symptom: Shortness of Breath',
    'symptom_dizziness': 'Symptom: Dizziness',
    'symptom_headache': 'Symptom: Headache',
    'symptom_other': 'Symptom: Other Reported Symptoms'
}

class HealthcarePredictor:
    def __init__(self):
        self.model = None
        self.explainer = None
        self.pipeline_meta = None
        self.metrics = None
        self._load_resources()
        
    def _load_resources(self):
        backend_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        model_path = os.path.join(backend_dir, 'ml', 'model_pipeline.joblib')
        metrics_path = os.path.join(backend_dir, 'ml', 'metrics.json')
        
        # If model doesn't exist yet, train it on the fly
        if not os.path.exists(model_path):
            from backend.ml.train_model import train_and_evaluate
            train_and_evaluate()
            
        self.pipeline_meta = joblib.load(model_path)
        self.model = self.pipeline_meta['model']
        self.explainer = shap.TreeExplainer(self.model)
        
        if os.path.exists(metrics_path):
            with open(metrics_path, 'r', encoding='utf-8') as f:
                self.metrics = json.load(f)
                
    def get_metrics(self) -> Dict:
        return self.metrics or {}
        
    def transform_input(self, req: BasicAssessmentRequest) -> Tuple[pd.DataFrame, float, Dict, str, str, str]:
        bmi = round(req.weight_kg / ((req.height_cm / 100) ** 2), 1)
        
        # Normalize Smoking (supports Yes/No or full string)
        smk_raw = str(req.smoking_habit).strip()
        if smk_raw.lower() in ['yes', 'true', '1']:
            normalized_smoking = 'Regular Smoker'
        elif smk_raw.lower() in ['no', 'false', '0']:
            normalized_smoking = 'Non-smoker'
        else:
            normalized_smoking = req.smoking_habit if req.smoking_habit in self.pipeline_meta['smoking_map'] else 'Non-smoker'
            
        # Normalize Alcohol (supports Yes/No or full string)
        alc_raw = str(req.alcohol_consumption).strip()
        if alc_raw.lower() in ['yes', 'true', '1']:
            normalized_alcohol = 'Moderate'
        elif alc_raw.lower() in ['no', 'false', '0']:
            normalized_alcohol = 'None'
        else:
            normalized_alcohol = req.alcohol_consumption if req.alcohol_consumption in self.pipeline_meta['alcohol_map'] else 'None'
            
        # Normalize Physical Activity
        act_raw = str(req.physical_activity).strip()
        if act_raw in self.pipeline_meta['physical_map']:
            normalized_activity = act_raw
        elif 'sedentary' in act_raw.lower():
            normalized_activity = 'Sedentary'
        elif 'light' in act_raw.lower():
            normalized_activity = 'Light'
        elif 'active' in act_raw.lower():
            normalized_activity = 'Active'
        else:
            normalized_activity = 'Moderate'
            
        # Encoding maps from pipeline meta
        gender_enc = self.pipeline_meta['gender_map'].get(req.gender, 0)
        smoking_enc = self.pipeline_meta['smoking_map'].get(normalized_smoking, 0)
        alcohol_enc = self.pipeline_meta['alcohol_map'].get(normalized_alcohol, 0)
        physical_enc = self.pipeline_meta['physical_map'].get(normalized_activity, 0)
        
        fam_set = set(req.family_history)
        sym_set = set(req.symptoms)
        has_other_sym = 1 if (req.other_symptom and req.other_symptom.strip()) or ('Other' in sym_set) else 0
        has_other_fam = 1 if 'Other' in fam_set else 0
        
        row_dict = {
            'age': float(req.age),
            'height_cm': float(req.height_cm),
            'weight_kg': float(req.weight_kg),
            'bmi': float(bmi),
            'sleep_hours': float(req.sleep_hours),
            'gender_enc': int(gender_enc),
            'smoking_enc': int(smoking_enc),
            'alcohol_enc': int(alcohol_enc),
            'physical_enc': int(physical_enc),
            'fam_hypertension': 1 if 'Hypertension' in fam_set else 0,
            'fam_diabetes': 1 if 'Diabetes' in fam_set else 0,
            'fam_heart_disease': 1 if 'Heart Disease' in fam_set else 0,
            'fam_stroke': 1 if 'Stroke' in fam_set else 0,
            'fam_cancer': 1 if 'Cancer' in fam_set or has_other_fam else 0,
            'symptom_fatigue': 1 if 'Fatigue' in sym_set else 0,
            'symptom_chest_pain': 1 if 'Chest Pain' in sym_set else 0,
            'symptom_excessive_thirst': 1 if 'Excessive Thirst' in sym_set else 0,
            'symptom_frequent_urination': 1 if 'Frequent Urination' in sym_set else 0,
            'symptom_shortness_of_breath': 1 if 'Shortness of Breath' in sym_set else 0,
            'symptom_dizziness': 1 if 'Dizziness' in sym_set else 0,
            'symptom_headache': 1 if 'Headache' in sym_set else 0,
            'symptom_other': int(has_other_sym)
        }

        # Ensure column order matches training feature names
        feature_names = self.pipeline_meta['feature_names']
        
        if 'risk_score' in feature_names:
            score = (req.age - 20) * 0.65
            if bmi > 25: score += (bmi - 25) * 2.6
            if bmi > 30: score += (bmi - 30) * 2.2
            smk_map = {'Non-smoker': 0, 'Former Smoker': 7, 'Occasional Smoker': 14, 'Regular Smoker': 28}
            score += smk_map.get(normalized_smoking, 0)
            alc_map = {'None': 0, 'Occasional': 4, 'Moderate': 10, 'Frequent': 20}
            score += alc_map.get(normalized_alcohol, 0)
            phy_map = {'Sedentary': 18, 'Light': 8, 'Moderate': -7, 'Active': -18}
            score += phy_map.get(normalized_activity, 0)
            if req.sleep_hours < 6.0: score += (6.0 - req.sleep_hours) * 6.5
            elif req.sleep_hours > 8.5: score += (req.sleep_hours - 8.5) * 4.5
            else: score -= 6.0
            if 'Heart Disease' in fam_set: score += 18
            if 'Diabetes' in fam_set: score += 14
            if 'Hypertension' in fam_set: score += 12
            if 'Stroke' in fam_set: score += 15
            score += (28.0 if 'Chest Pain' in sym_set else 0)
            score += (20.0 if 'Shortness of Breath' in sym_set else 0)
            score += (18.0 if 'Excessive Thirst' in sym_set else 0)
            score += (15.0 if 'Frequent Urination' in sym_set else 0)
            score += (9.0 if 'Fatigue' in sym_set else 0)
            score += (10.0 if 'Dizziness' in sym_set else 0)
            score += (8.0 if 'Headache' in sym_set else 0)
            score += (5.0 if has_other_sym else 0)
            row_dict['risk_score'] = max(0.0, score)
            
        df_row = pd.DataFrame([row_dict])[feature_names]
        
        raw_values_display = {
            'age': f"{req.age} yrs",
            'height_cm': f"{req.height_cm} cm",
            'weight_kg': f"{req.weight_kg} kg",
            'bmi': f"{bmi:.1f} ({get_bmi_category(bmi)})",
            'sleep_hours': f"{req.sleep_hours:.1f} hrs/night",
            'gender_enc': req.gender,
            'smoking_enc': normalized_smoking,
            'alcohol_enc': normalized_alcohol,
            'physical_enc': normalized_activity,
            'fam_hypertension': "Yes" if 'Hypertension' in fam_set else "No",
            'fam_diabetes': "Yes" if 'Diabetes' in fam_set else "No",
            'fam_heart_disease': "Yes" if 'Heart Disease' in fam_set else "No",
            'fam_stroke': "Yes" if 'Stroke' in fam_set else "No",
            'fam_cancer': "Yes" if ('Cancer' in fam_set or has_other_fam) else "No",
            'symptom_fatigue': "Present" if 'Fatigue' in sym_set else "Absent",
            'symptom_chest_pain': "Present" if 'Chest Pain' in sym_set else "Absent",
            'symptom_excessive_thirst': "Present" if 'Excessive Thirst' in sym_set else "Absent",
            'symptom_frequent_urination': "Present" if 'Frequent Urination' in sym_set else "Absent",
            'symptom_shortness_of_breath': "Present" if 'Shortness of Breath' in sym_set else "Absent",
            'symptom_dizziness': "Present" if 'Dizziness' in sym_set else "Absent",
            'symptom_headache': "Present" if 'Headache' in sym_set else "Absent",
            'symptom_other': (req.other_symptom.strip() if req.other_symptom else "Present") if has_other_sym else "Absent"
        }
        
        return df_row, bmi, raw_values_display, normalized_smoking, normalized_alcohol, normalized_activity

    def predict(self, req: BasicAssessmentRequest) -> PredictionResponse:
        return self.predict_and_explain(req)

    def predict_and_explain(self, req: BasicAssessmentRequest) -> PredictionResponse:
        X_df, bmi, raw_display, norm_smoking, norm_alcohol, norm_activity = self.transform_input(req)
        feature_names = list(X_df.columns)
        
        # 1. XGBoost Probabilities & Class
        proba = self.model.predict_proba(X_df)[0]
        class_names = self.pipeline_meta['risk_level_names']
        proba_dict = {name: round(float(p), 4) for name, p in zip(class_names, proba)}
        
        pred_idx = int(np.argmax(proba))
        risk_level = class_names[pred_idx]
        
        # Calculate continuous overall risk score (0 to 100 scale)
        weights = [12.0, 38.0, 72.0, 96.0]
        continuous_score = float(np.sum(proba * weights))
        continuous_score = min(100.0, max(5.0, continuous_score))
        
        # Determine Primary Risk Category
        sym_set = set(req.symptoms)
        fam_set = set(req.family_history)
        if risk_level == 'Low':
            risk_category = "General Preventive Health"
            risk_desc = "Your health indicators are currently in a good range. Maintaining healthy daily habits will help prevent future health risks."
        elif risk_level == 'Moderate':
            risk_category = "Moderate Health Risk"
            risk_desc = "You may have a moderate risk of developing health problems. It is recommended to make positive lifestyle adjustments and monitor your health."
        else:
            risk_category = "Elevated Health Risk"
            risk_desc = "You may have a higher risk of developing health problems. It is recommended to take preventive action and consult a healthcare professional."
            
        # 2. SHAP Explanations
        shap_raw = self.explainer.shap_values(X_df)
        
        # Handle SHAP multi-class output structure (list of arrays or 3D array)
        if isinstance(shap_raw, list):
            target_class_shap = shap_raw[pred_idx][0]
        elif len(np.shape(shap_raw)) == 3:
            target_class_shap = shap_raw[0, :, pred_idx]
        else:
            target_class_shap = shap_raw[0]
            
        expected_val = self.explainer.expected_value
        if isinstance(expected_val, (list, np.ndarray)):
            base_val = float(expected_val[pred_idx])
        else:
            base_val = float(expected_val)
            
        abs_sum = float(np.sum(np.abs(target_class_shap))) + 1e-6
        all_factors: List[SHAPFactor] = []
        
        for idx, col in enumerate(feature_names):
            val = float(target_class_shap[idx])
            disp_name = FEATURE_DISPLAY_NAMES.get(col, col.replace('_', ' ').title())
            raw_val_str = str(raw_display.get(col, ''))
            
            impact_type = 'risk_increasing' if val > 0 else 'protective'
            pct = round((abs(val) / abs_sum) * 100, 1)
            
            if val > 0:
                if 'bmi' in col:
                    note = f"Elevated BMI of {bmi:.1f} ({get_bmi_category(bmi)}) increases health strain."
                elif 'smoking' in col and norm_smoking != 'Non-smoker':
                    note = f"{norm_smoking} adds cardiovascular and endothelial strain."
                elif 'chest_pain' in col and 'Chest Pain' in sym_set:
                    note = "Active chest discomfort is a critical cardiac risk indicator."
                elif 'shortness_of_breath' in col and 'Shortness of Breath' in sym_set:
                    note = "Dyspnea signals potential pulmonary or cardiac resistance."
                elif 'thirst' in col or 'urination' in col:
                    note = "Classic symptoms pointing towards glucose regulation imbalance."
                elif 'sleep' in col and req.sleep_hours < 6.0:
                    note = f"Insufficient sleep ({req.sleep_hours}h) elevates stress markers."
                elif 'physical' in col and norm_activity in ['Sedentary', 'Light']:
                    note = "Low physical activity increases chronic disease susceptibility."
                elif 'fam' in col and ('Yes' in raw_val_str):
                    note = f"Family history of {disp_name.replace('Family History: ', '')}."
                else:
                    note = f"{disp_name} contributes positively to predicted risk."
            else:
                if 'physical' in col and norm_activity in ['Moderate', 'Active']:
                    note = f"Physical activity ({norm_activity}) serves as a protective factor."
                elif 'smoking' in col and norm_smoking == 'Non-smoker':
                    note = "Zero tobacco exposure protects cardiovascular integrity."
                elif 'sleep' in col and 7.0 <= req.sleep_hours <= 8.5:
                    note = f"Healthy sleep duration ({req.sleep_hours}h) supports restoration."
                elif 'bmi' in col and 18.5 <= bmi <= 24.9:
                    note = f"Normal BMI ({bmi:.1f}) provides metabolic protection."
                else:
                    note = f"Healthy status for {disp_name} lowers risk."
                    
            all_factors.append(SHAPFactor(
                feature_key=col,
                feature_name=disp_name,
                feature_value=raw_val_str,
                shap_value=round(val, 4),
                impact=impact_type,
                percentage_contribution=pct,
                clinical_note=note
            ))
            
        top_risk = sorted([f for f in all_factors if f.shap_value > 0.001], key=lambda x: x.shap_value, reverse=True)[:5]
        top_protective = sorted([f for f in all_factors if f.shap_value < -0.001], key=lambda x: x.shap_value)[:5]
        
        # Build clean bullet points for Image 2 UI matching
        important_factors_bullets = []
        
        # BMI Category Inclusion (Overweight, Underweight, Normal, Obese)
        if bmi >= 30.0:
            important_factors_bullets.append(f"High Body Weight (BMI: {bmi:.1f} - Obese)")
        elif bmi >= 25.0:
            important_factors_bullets.append(f"High Body Weight (BMI: {bmi:.1f} - Overweight)")
        elif bmi < 18.5:
            important_factors_bullets.append(f"Low Body Weight (BMI: {bmi:.1f} - Underweight)")
        else:
            important_factors_bullets.append(f"Body Weight Status (BMI: {bmi:.1f} - Normal)")
            
        if norm_activity in ['Sedentary', 'Light']:
            important_factors_bullets.append("Low Physical Activity")
        if len(fam_set) > 0 and 'None' not in fam_set:
            important_factors_bullets.append("Family History of Disease")
        if 'Fatigue' in sym_set:
            important_factors_bullets.append("Reports of Fatigue")
        if 'Chest Pain' in sym_set:
            important_factors_bullets.append("Reports of Chest Pain")
        if 'Shortness of Breath' in sym_set:
            important_factors_bullets.append("Shortness of Breath")
        if 'Excessive Thirst' in sym_set or 'Frequent Urination' in sym_set:
            important_factors_bullets.append("Frequent Urination or Thirst Symptoms")
        if norm_smoking in ['Regular Smoker', 'Occasional Smoker']:
            important_factors_bullets.append("Active Tobacco Smoking")
        if norm_alcohol in ['Moderate', 'Frequent']:
            important_factors_bullets.append("Alcohol Consumption")
        if req.sleep_hours < 6.0:
            important_factors_bullets.append("Insufficient Sleep Duration")
        if req.age >= 50:
            important_factors_bullets.append("Age Factor (Above 50 Years)")
            
        # Default fallback if healthy
        if len(important_factors_bullets) <= 1:
            important_factors_bullets.extend([
                "Adequate Sleep Duration",
                "Non-Smoking Status",
                "Absence of Chronic Symptoms"
            ])
            
        # Build clean guidance bullets for Image 2 UI matching
        guidance_bullets = [
            "Maintain regular physical activity (at least 30 minutes daily).",
            "Follow a balanced and healthy diet with fruits and vegetables.",
            "Monitor your weight and other health parameters regularly.",
            "Avoid smoking and limit alcohol consumption.",
            "Get regular health check-ups and consult a doctor if symptoms persist."
        ]
        
        # 3. Generate Detailed Preventive Guidance Items
        guidance = generate_preventive_guidance(
            risk_level=risk_level,
            risk_category=risk_category,
            bmi=bmi,
            top_risk_factors=top_risk,
            assessment_data={
                'age': req.age,
                'gender': req.gender,
                'height_cm': req.height_cm,
                'weight_kg': req.weight_kg,
                'smoking_habit': norm_smoking,
                'alcohol_consumption': norm_alcohol,
                'physical_activity': norm_activity,
                'sleep_hours': req.sleep_hours,
                'family_history': req.family_history,
                'symptoms': req.symptoms
            }
        )
        
        # 4. Generate HIPAA Safe Harbor Anonymization & Privacy Metadata
        privacy_data = anonymizer.anonymize(
            age=req.age,
            gender=req.gender,
            height_cm=req.height_cm,
            weight_kg=req.weight_kg,
            bmi=bmi
        )

        # 5. Calculate Specific Disease Risk Breakdown Estimates
        cad_score = min(95.0, max(5.0, (continuous_score * 0.45) + (35.0 if 'Chest Pain' in sym_set else 0) + (15.0 if 'Shortness of Breath' in sym_set else 0) + (15.0 if 'Heart Disease' in fam_set else 0) + (10.0 if norm_smoking != 'Non-smoker' else 0)))
        diabetes_score = min(95.0, max(5.0, (continuous_score * 0.40) + (25.0 if bmi >= 25 else 0) + (20.0 if ('Excessive Thirst' in sym_set or 'Frequent Urination' in sym_set) else 0) + (15.0 if 'Diabetes' in fam_set else 0)))
        hypertension_score = min(95.0, max(5.0, (continuous_score * 0.42) + (20.0 if req.age >= 45 else 0) + (15.0 if ('Dizziness' in sym_set or 'Headache' in sym_set) else 0) + (15.0 if 'Hypertension' in fam_set else 0) + (10.0 if req.sleep_hours < 6.0 else 0)))
        
        disease_breakdown = {
            "Cardiovascular Disease (CAD)": round(cad_score, 1),
            "Type-2 Diabetes": round(diabetes_score, 1),
            "Hypertension": round(hypertension_score, 1)
        }

        # 6. Evaluate Single Recommended Specialist for Critical Patients Only
        recommended_specialist = evaluate_critical_specialist(
            risk_level=risk_level,
            continuous_score=continuous_score,
            disease_breakdown=disease_breakdown,
            sym_set=sym_set,
            fam_set=fam_set,
            norm_smoking=norm_smoking,
            bmi=bmi,
            age=req.age
        )

        return PredictionResponse(
            risk_level=f"{risk_level} Risk",
            risk_score=round(continuous_score, 1),
            risk_category=risk_category,
            risk_description=risk_desc,
            probabilities=proba_dict,
            disease_breakdown=disease_breakdown,
            bmi=bmi,
            bmi_category=get_bmi_category(bmi),
            important_factors_bullets=important_factors_bullets,
            guidance_bullets=guidance_bullets,
            top_risk_factors=top_risk,
            top_protective_factors=top_protective,
            all_shap_factors=sorted(all_factors, key=lambda x: abs(x.shap_value), reverse=True),
            base_value=round(base_val, 4),
            guidance=guidance,
            recommended_specialist=recommended_specialist,
            privacy=PrivacyMetadata(**privacy_data),
            smoking_habit=norm_smoking,
            disclaimer=DISCLAIMER_TEXT,
            timestamp=datetime.utcnow().isoformat() + "Z"
        )

_predictor_instance = None

def get_predictor() -> HealthcarePredictor:
    global _predictor_instance
    if _predictor_instance is None:
        _predictor_instance = HealthcarePredictor()
    return _predictor_instance
