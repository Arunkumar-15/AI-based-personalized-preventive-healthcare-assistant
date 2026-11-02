"""
FastAPI Backend Application for AI-Based Preventive Healthcare Assistant.
Supports Live Anonymized Database Persistence & Admin Clinical Repository.
"""

import sys
import os
import datetime
from typing import List
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager

# Add parent directory to path so absolute imports work
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from backend.app.schemas import (
    BasicAssessmentRequest, PredictionResponse, ModelMetricsResponse
)
from backend.app.inference import get_predictor

# Live In-Memory Anonymized Database Store (Privacy-Preserving Repository for User Inputs & Predictions Only)
ANONYMIZED_DB_STORE = []


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Eagerly initialize model predictor and SHAP explainer on startup
    print("[FastAPI] Initializing Healthcare ML Predictor and SHAP Explainer...")
    predictor = get_predictor()
    print(f"[FastAPI] Model loaded successfully. Metrics available: {bool(predictor.get_metrics())}")
    yield
    print("[FastAPI] Shutting down healthcare assistant service.")

app = FastAPI(
    title="AI-Based Preventive Healthcare Assistant API",
    description="Backend API supporting Assessment, XGBoost Prediction, SHAP Explainer, and Anonymized Admin Database.",
    version="1.0.0",
    lifespan=lifespan
)

# Enable CORS for React frontend (Vite & local dev ports)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "AI-Based Preventive Healthcare Assistant",
        "milestone": "Full Operational MVP",
        "components": {
            "basic_assessment": "active",
            "xgboost_model": "active",
            "shap_explainer": "active",
            "anonymized_database": "active"
        }
    }

@app.get("/api/model-info", response_model=ModelMetricsResponse)
def get_model_info():
    predictor = get_predictor()
    metrics = predictor.get_metrics()
    if not metrics:
        raise HTTPException(status_code=503, detail="Model metrics not yet computed or loaded.")
    return metrics

@app.get("/api/admin/records")
def get_admin_records():
    """Returns all anonymized clinical patient records saved in the database."""
    return {
        "status": "success",
        "total_records": len(ANONYMIZED_DB_STORE),
        "records": ANONYMIZED_DB_STORE
    }

@app.post("/api/predict", response_model=PredictionResponse)
def predict_health_risk(request: BasicAssessmentRequest):
    try:
        predictor = get_predictor()
        response = predictor.predict_and_explain(request)

        # Save Anonymized Record into Database Store (Zero PHI / De-Identified Token)
        age_b = f"{request.age - (request.age%5)} – {request.age - (request.age%5)+4} Years"
        new_record = {
            "id": response.privacy.anonymous_id if response.privacy else "ANON-9999-XXXX",
            "age_bracket": age_b,
            "gender": request.gender,
            "bmi_category": f"{response.bmi_category} ({response.bmi:.1f} kg/m²)",
            "biomarkers": {
                "bp": f"{getattr(request, 'systolic_bp', 120)}/{getattr(request, 'diastolic_bp', 80)} mmHg",
                "glucose": f"{getattr(request, 'fasting_glucose', 95)} mg/dL",
                "hba1c": f"{getattr(request, 'hba1c', 5.4)}%",
                "cholesterol": f"{getattr(request, 'total_cholesterol', 180)} mg/dL"
            },
            "symptoms": request.symptoms if request.symptoms else ["None Reported"],
            "risk_level": response.risk_level,
            "risk_score": response.risk_score,
            "cad_risk": f"{response.disease_breakdown.get('Cardiovascular Disease (CAD)', 50.0)}%" if response.disease_breakdown else "50.0%",
            "top_driver": response.important_factors_bullets[0] if response.important_factors_bullets else "Age & Lifestyle Factor",
            "date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        }
        ANONYMIZED_DB_STORE.insert(0, new_record)
        print(f"[Anonymized DB] Saved new assessment entry: {new_record['id']} | Risk: {new_record['risk_level']}")

        return response
    except Exception as e:
        import traceback
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=f"Inference error: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("backend.app.main:app", host="127.0.0.1", port=8000, reload=True)
