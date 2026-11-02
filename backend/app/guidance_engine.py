"""
Preventive Guidance Recommendation Engine.
Synthesizes predicted risk level, individual contributing SHAP factors, and user health biometrics
into prioritized, actionable, personalized preventive guidance.
"""

from typing import List, Dict
from backend.app.schemas import PreventiveGuidanceItem, SHAPFactor

DISCLAIMER_TEXT = (
    "Disclaimer: This assistant provides automated preventive health insights for informational "
    "and screening purposes only. It does NOT constitute medical diagnosis, clinical evaluation, "
    "or prescription. If you experience severe symptoms such as chest pain or breathing difficulties, "
    "consult a qualified medical physician or emergency care provider immediately."
)

def get_bmi_category(bmi: float) -> str:
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 24.9:
        return "Normal Weight"
    elif bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

def generate_preventive_guidance(
    risk_level: str,
    risk_category: str,
    bmi: float,
    top_risk_factors: List[SHAPFactor],
    assessment_data: Dict
) -> List[PreventiveGuidanceItem]:
    guidance: List[PreventiveGuidanceItem] = []
    
    # 1. Critical & Clinical Actions (Urgent priority based on risk level and acute symptoms)
    symptoms = assessment_data.get('symptoms', [])
    has_chest_pain = 'Chest Pain' in symptoms
    has_sob = 'Shortness of Breath' in symptoms
    has_thirst_or_urination = 'Excessive Thirst' in symptoms or 'Frequent Urination' in symptoms
    
    if risk_level == 'Critical' or has_chest_pain or has_sob:
        guidance.append(PreventiveGuidanceItem(
            id="urgent_clinical_consult",
            category="clinical",
            priority="critical" if has_chest_pain else "high",
            title="Priority Medical Evaluation Recommended",
            description=(
                "Based on the presence of cardiopulmonary risk indicators (such as chest pain or shortness of breath), "
                "we strongly recommend scheduling an in-person clinical consultation with a physician or cardiologist."
            ),
            action_steps=[
                "Schedule an in-person general medical exam and ECG / cardiovascular evaluation.",
                "Seek immediate emergency medical care if chest pain radiates to arm/jaw or worsens with exertion.",
                "Avoid intense strenuous physical exertion until cleared by your physician."
            ],
            target_factor="Cardiopulmonary Symptoms"
        ))
    elif risk_level in ['High', 'Moderate']:
        guidance.append(PreventiveGuidanceItem(
            id="routine_clinical_screening",
            category="clinical",
            priority="high",
            title="Comprehensive Preventive Health Checkup",
            description="Your screening indicates moderate-to-high health risk markers that benefit from baseline diagnostic lab tests.",
            action_steps=[
                "Request a comprehensive metabolic panel, fasting blood glucose / HbA1c, and lipid panel.",
                "Monitor resting blood pressure over 7 consecutive days.",
                "Review your family medical history with your primary care provider."
            ],
            target_factor="Preventive Screening"
        ))
    else:
        guidance.append(PreventiveGuidanceItem(
            id="annual_wellness_checkup",
            category="clinical",
            priority="info",
            title="Routine Annual Wellness Maintenance",
            description="Your risk indicators are currently well-balanced within the low-risk range. Continue preventive checkups.",
            action_steps=[
                "Maintain scheduled annual wellness visits with your primary healthcare provider.",
                "Keep preventive dental, optical, and routine health checks up to date."
            ],
            target_factor="General Wellness"
        ))
        
    # 2. Metabolic & Blood Sugar Screening
    if has_thirst_or_urination or any('diabetes' in f.feature_key.lower() for f in top_risk_factors) or (bmi >= 28):
        guidance.append(PreventiveGuidanceItem(
            id="metabolic_screening",
            category="clinical",
            priority="high" if has_thirst_or_urination else "medium",
            title="Glycemic & Metabolic Screening",
            description="Symptoms such as excessive thirst or elevated BMI are classic early indicators for insulin resistance.",
            action_steps=[
                "Get a Fasting Blood Glucose (FBG) and HbA1c test completed at a certified lab.",
                "Track daily refined sugar and sweetened beverage intake.",
                "Discuss prediabetes screening with your healthcare provider."
            ],
            target_factor="Metabolic Markers"
        ))
        
    # 3. Nutrition & Dietary Optimization
    if bmi >= 25.0 or any('bmi' in f.feature_key.lower() for f in top_risk_factors):
        guidance.append(PreventiveGuidanceItem(
            id="dietary_management_overweight",
            category="diet",
            priority="high" if bmi >= 30.0 else "medium",
            title="Cardiometabolic Nutrition & Caloric Balance",
            description=f"Your current BMI of {bmi:.1f} ({get_bmi_category(bmi)}) represents a key driver of systemic risk.",
            action_steps=[
                "Adopt a Mediterranean or whole-food plant-forward dietary pattern rich in dietary fiber (30g+/day).",
                "Reduce ultra-processed foods, saturated fats, and high-glycemic carbohydrates.",
                "Target a modest, sustainable 500 kcal daily deficit aimed at 5-7% gradual weight reduction."
            ],
            target_factor="Body Mass Index (BMI)"
        ))
    else:
        guidance.append(PreventiveGuidanceItem(
            id="balanced_nutrition",
            category="diet",
            priority="info",
            title="Nutrient-Dense Nutritional Foundation",
            description="Maintaining a balanced intake of micronutrients, lean proteins, and prebiotic fiber protects long-term vitality.",
            action_steps=[
                "Ensure minimum 5 servings of diversified colorful vegetables and low-sugar fruits daily.",
                "Hydrate adequately with 2.5 to 3.0 liters of clean water daily.",
                "Limit sodium intake to under 2,000 mg/day to support optimal vascular elasticity."
            ],
            target_factor="Nutritional Health"
        ))
        
    # 4. Physical Activity & Cardiorespiratory Fitness
    activity = assessment_data.get('physical_activity', 'Sedentary')
    if activity in ['Sedentary', 'Light']:
        guidance.append(PreventiveGuidanceItem(
            id="activity_activation",
            category="activity",
            priority="high",
            title="Progressive Physical Activity Protocol",
            description="Sedentary lifestyles significantly increase cardiovascular and all-cause metabolic risk over time.",
            action_steps=[
                "Build up to at least 150 minutes of moderate-intensity aerobic exercise (brisk walking, cycling) per week.",
                "Incorporate 2 weekly sessions of full-body resistance or bodyweight strength training.",
                "Break up prolonged sitting every 45 minutes with a 3-minute walking break (aim for 7,500+ daily steps)."
            ],
            target_factor="Physical Activity"
        ))
    else:
        guidance.append(PreventiveGuidanceItem(
            id="activity_maintenance",
            category="activity",
            priority="info",
            title="Active Regimen & Recovery Optimization",
            description="Your active lifestyle is a powerful protective factor against chronic metabolic decline.",
            action_steps=[
                "Maintain your regular exercise regimen while including active recovery and mobility work.",
                "Integrate zone-2 cardio training for mitochondrial density and cardiac efficiency."
            ],
            target_factor="Cardiorespiratory Fitness"
        ))
        
    # 5. Smoking & Respiratory Interventions
    smoking = assessment_data.get('smoking_habit', 'Non-smoker')
    if smoking in ['Regular Smoker', 'Occasional Smoker']:
        guidance.append(PreventiveGuidanceItem(
            id="smoking_cessation",
            category="lifestyle",
            priority="high",
            title="Pulmonary & Vascular Protection Strategy",
            description="Tobacco and inhalation smoke are major drivers of vascular stiffness, plaque formation, and respiratory decline.",
            action_steps=[
                "Consult a smoking cessation counselor or discuss nicotine replacement therapy (NRT) options.",
                "Set a structured quit timeline and identify alternative stress-management coping habits.",
                "Undergo spirometry / lung capacity assessment if experiencing persistent morning cough or shortness of breath."
            ],
            target_factor="Smoking Habit"
        ))
        
    # 6. Sleep Hygiene & Circadian Health
    sleep_hours = assessment_data.get('sleep_hours', 7.0)
    if sleep_hours < 6.0 or sleep_hours > 9.0 or 'Fatigue' in symptoms:
        guidance.append(PreventiveGuidanceItem(
            id="sleep_circadian_hygiene",
            category="lifestyle",
            priority="medium",
            title="Circadian Rhythm & Sleep Restoration",
            description=f"Recorded sleep duration of {sleep_hours:.1f} hrs/night disrupts hormonal balance and systemic recovery.",
            action_steps=[
                "Aim for 7 to 8.5 hours of consistent, uninterrupted restorative sleep nightly.",
                "Eliminate blue-light screens and stimulating digital media 60 minutes prior to bedtime.",
                "Maintain fixed wake and sleep times across both weekdays and weekends."
            ],
            target_factor="Sleep Duration & Rest"
        ))
        
    # 7. Alcohol Moderation
    alcohol = assessment_data.get('alcohol_consumption', 'None')
    if alcohol in ['Moderate', 'Frequent']:
        guidance.append(PreventiveGuidanceItem(
            id="alcohol_moderation",
            category="lifestyle",
            priority="medium",
            title="Alcohol Intake Moderation & Liver Support",
            description="Frequent or heavy alcohol consumption elevates triglycerides, liver enzymes, and blood pressure.",
            action_steps=[
                "Limit alcohol intake to no more than 1 standard drink/day for women or 2 for men.",
                "Designate at least 3-4 completely alcohol-free days per week.",
                "Request a liver function test (ALT, AST, GGT) during your next blood screening."
            ],
            target_factor="Alcohol Consumption"
        ))
        
    return guidance
