"""
Pydantic Data Models and Validation Schemas for Healthcare Assistant API.
"""

from typing import List, Optional, Dict
from pydantic import BaseModel, Field

class BasicAssessmentRequest(BaseModel):
    age: int = Field(..., ge=1, le=120, description="Age in years")
    gender: str = Field("Male", description="Gender: Male, Female, Other")
    height_cm: float = Field(..., ge=50, le=250, description="Height in centimeters")
    weight_kg: float = Field(..., ge=20, le=300, description="Weight in kilograms")
    smoking_habit: str = Field("No", description="Yes, No, Non-smoker, Regular Smoker, etc.")
    alcohol_consumption: str = Field("No", description="Yes, No, None, Occasional, Moderate, Frequent")
    physical_activity: str = Field("Moderate", description="Sedentary, Light, Moderate, Active")
    sleep_hours: float = Field(..., ge=1.0, le=24.0, description="Average sleep hours per night")
    family_history: List[str] = Field(default_factory=list, description="List of family conditions: Heart Disease, Diabetes, Hypertension, Other")
    symptoms: List[str] = Field(default_factory=list, description="List of selected symptoms: Fatigue, Chest Pain, Shortness of Breath, Excessive Thirst, Frequent Urination, Dizziness, Headache")
    other_symptom: Optional[str] = Field(None, description="Optional custom symptom text")

class SHAPFactor(BaseModel):
    feature_key: str
    feature_name: str
    feature_value: str
    shap_value: float
    impact: str  # 'risk_increasing' or 'protective'
    percentage_contribution: float
    clinical_note: str

class PreventiveGuidanceItem(BaseModel):
    id: str
    category: str  # 'clinical', 'diet', 'activity', 'lifestyle'
    priority: str  # 'critical', 'high', 'medium', 'info'
    title: str
    description: str
    action_steps: List[str]
    target_factor: Optional[str] = None

class RecommendedSpecialist(BaseModel):
    specialty_name: str
    specialty_name_ta: str
    doctor_title: str
    urgency: str
    highest_disease_name: str
    highest_disease_score: float
    clinical_reason: str
    clinical_reason_ta: str
    recommended_tests: List[str]
    questions_to_ask: List[str]
    clinic_type: str

class PrivacyMetadata(BaseModel):
    anonymous_id: str
    k_anonymity_bracket: str
    compliance_standard: str
    privacy_guarantee: str
    phi_persisted: bool

class PredictionResponse(BaseModel):
    risk_level: str  # 'Low', 'Moderate', 'High', 'Critical'
    risk_score: float  # 0 to 100
    risk_category: str
    risk_description: str
    probabilities: Dict[str, float]
    disease_breakdown: Optional[Dict[str, float]] = None
    bmi: float
    bmi_category: str
    important_factors_bullets: List[str]
    guidance_bullets: List[str]
    top_risk_factors: List[SHAPFactor]
    top_protective_factors: List[SHAPFactor]
    all_shap_factors: List[SHAPFactor]
    base_value: float
    guidance: List[PreventiveGuidanceItem]
    recommended_specialist: Optional[RecommendedSpecialist] = None
    privacy: Optional[PrivacyMetadata] = None
    smoking_habit: Optional[str] = None
    disclaimer: str
    timestamp: str

class ModelMetricsResponse(BaseModel):
    model_name: str
    train_samples: int
    test_samples: int
    features_count: int
    accuracy: float
    precision_macro: float
    precision_weighted: float
    recall_macro: float
    recall_weighted: float
    f1_macro: float
    f1_weighted: float
    confusion_matrix: Dict[str, object]
    classification_report: Dict[str, object]
    feature_importances: List[Dict[str, object]]
