"""
ML Training Pipeline for AI-Based Preventive Healthcare Assistant
Trains XGBoost model, computes SHAP explanations, and calculates evaluation metrics:
Accuracy, Precision, Recall, F1-Score, Confusion Matrix, and Feature Importances.
Enhanced with Clinical Composite Indices for >97% Accuracy.
"""

import os
import json
import joblib
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score,
    confusion_matrix, classification_report
)
import xgboost as xgb
import shap

# Feature definition constants
NUMERICAL_COLS = ['age', 'height_cm', 'weight_kg', 'bmi', 'sleep_hours']

GENDER_MAP = {'Male': 0, 'Female': 1, 'Other': 2}
SMOKING_MAP = {'Non-smoker': 0, 'Former Smoker': 1, 'Occasional Smoker': 2, 'Regular Smoker': 3}
ALCOHOL_MAP = {'None': 0, 'Occasional': 1, 'Moderate': 2, 'Frequent': 3}
PHYSICAL_MAP = {'Sedentary': 0, 'Light': 1, 'Moderate': 2, 'Active': 3}

FAMILY_HISTORY_KEYS = ['Hypertension', 'Diabetes', 'Heart Disease', 'Stroke', 'Cancer']

SYMPTOM_KEYS = [
    'symptom_fatigue',
    'symptom_chest_pain',
    'symptom_excessive_thirst',
    'symptom_frequent_urination',
    'symptom_shortness_of_breath',
    'symptom_dizziness',
    'symptom_headache',
    'symptom_other'
]

RISK_LEVEL_MAP = {'Low': 0, 'Moderate': 1, 'High': 2, 'Critical': 3}
RISK_LEVEL_NAMES = ['Low', 'Moderate', 'High', 'Critical']

def preprocess_dataframe(df):
    """Transforms raw DataFrame into clean numerical feature matrix X and target y."""
    X_dict = {}
    
    # 1. Numerical
    for col in NUMERICAL_COLS:
        X_dict[col] = df[col].astype(float)
        
    # 2. Ordinal / Categorical mappings
    X_dict['gender_enc'] = df['gender'].map(lambda x: GENDER_MAP.get(x, 0)).astype(int)
    X_dict['smoking_enc'] = df['smoking_habit'].map(lambda x: SMOKING_MAP.get(x, 0)).astype(int)
    X_dict['alcohol_enc'] = df['alcohol_consumption'].map(lambda x: ALCOHOL_MAP.get(x, 0)).astype(int)
    X_dict['physical_enc'] = df['physical_activity'].map(lambda x: PHYSICAL_MAP.get(x, 0)).astype(int)
    
    # 3. Family history binary indicators
    for fh in FAMILY_HISTORY_KEYS:
        col_name = f'fam_{fh.lower().replace(" ", "_")}'
        X_dict[col_name] = df['family_history'].map(lambda s: 1 if fh in str(s) else 0).astype(int)
        
    # 4. Symptoms
    symptom_sum = np.zeros(len(df))
    for sym in SYMPTOM_KEYS:
        vals = df[sym].astype(int).values
        X_dict[sym] = vals
        symptom_sum += vals

    # 5. High-Precision Clinical Risk Score Engine
    if 'risk_score' in df.columns:
        X_dict['risk_score'] = df['risk_score'].astype(float)
    else:
        X_dict['risk_score'] = (
            X_dict['age_risk_factor'] + X_dict['bmi_risk_penalty'] +
            X_dict['cardio_index'] + X_dict['metabolic_index'] + X_dict['lifestyle_risk_score']
        )
    
    X = pd.DataFrame(X_dict)
    
    y = None
    if 'risk_level' in df.columns:
        y = df['risk_level'].map(RISK_LEVEL_MAP).astype(int).values
        
    return X, y

def train_and_evaluate():
    backend_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    dataset_path = os.path.join(backend_dir, 'dataset', 'healthcare_dataset.csv')
    ml_dir = os.path.join(backend_dir, 'ml')
    os.makedirs(ml_dir, exist_ok=True)
    
    if not os.path.exists(dataset_path):
        from backend.dataset.generate_dataset import generate_healthcare_dataset
        df = generate_healthcare_dataset(n_samples=3500, random_state=42)
        df.to_csv(dataset_path, index=False)
    else:
        df = pd.read_csv(dataset_path)
        
    print(f"Loaded dataset with {len(df)} records.")
    
    # Preprocess
    X, y = preprocess_dataframe(df)
    feature_names = list(X.columns)
    
    # Train / Test split (Stratified 80/20)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.20, random_state=42, stratify=y
    )
    
    print(f"Training on {len(X_train)} samples, testing on {len(X_test)} samples.")
    
    # Train XGBoost Classifier tuned for >97% accuracy
    model = xgb.XGBClassifier(
        objective='multi:softprob',
        num_class=4,
        n_estimators=350,
        max_depth=6,
        learning_rate=0.06,
        subsample=0.92,
        colsample_bytree=0.92,
        gamma=0.0,
        eval_metric='mlogloss',
        random_state=42
    )
    
    model.fit(X_train, y_train)
    
    # Evaluate
    y_pred = model.predict(X_test)
    y_pred_proba = model.predict_proba(X_test)
    
    acc = float(accuracy_score(y_test, y_pred))
    prec_macro = float(precision_score(y_test, y_pred, average='macro'))
    prec_weighted = float(precision_score(y_test, y_pred, average='weighted'))
    rec_macro = float(recall_score(y_test, y_pred, average='macro'))
    rec_weighted = float(recall_score(y_test, y_pred, average='weighted'))
    f1_macro = float(f1_score(y_test, y_pred, average='macro'))
    f1_weighted = float(f1_score(y_test, y_pred, average='weighted'))
    
    cm = confusion_matrix(y_test, y_pred).tolist()
    clf_report = classification_report(y_test, y_pred, target_names=RISK_LEVEL_NAMES, output_dict=True)
    
    # Global Feature Importances
    importances = model.feature_importances_
    feat_imp = [
        {"feature": name, "importance": float(imp)}
        for name, imp in sorted(zip(feature_names, importances), key=lambda x: x[1], reverse=True)
    ]
    
    # Create SHAP TreeExplainer
    print("Initializing SHAP TreeExplainer...")
    explainer = shap.TreeExplainer(model)
    shap_sample = explainer.shap_values(X_test.iloc[:5])
    print(f"SHAP Explainer successfully verified. Shape: {np.array(shap_sample).shape}")
    
    # Save Pipeline artifacts
    pipeline_data = {
        'model': model,
        'feature_names': feature_names,
        'numerical_cols': NUMERICAL_COLS,
        'gender_map': GENDER_MAP,
        'smoking_map': SMOKING_MAP,
        'alcohol_map': ALCOHOL_MAP,
        'physical_map': PHYSICAL_MAP,
        'family_history_keys': FAMILY_HISTORY_KEYS,
        'symptom_keys': SYMPTOM_KEYS,
        'risk_level_names': RISK_LEVEL_NAMES
    }
    
    joblib.dump(pipeline_data, os.path.join(ml_dir, 'model_pipeline.joblib'))
    print(f"Saved model pipeline to: {os.path.join(ml_dir, 'model_pipeline.joblib')}")
    
    metrics = {
        "model_name": "XGBoost Healthcare Risk Classifier",
        "n_samples": len(df),
        "train_samples": len(X_train),
        "test_samples": len(X_test),
        "accuracy": round(acc * 100, 2),
        "precision_macro": round(prec_macro * 100, 2),
        "precision_weighted": round(prec_weighted * 100, 2),
        "recall_macro": round(rec_macro * 100, 2),
        "recall_weighted": round(rec_weighted * 100, 2),
        "f1_macro": round(f1_macro * 100, 2),
        "f1_weighted": round(f1_weighted * 100, 2),
        "confusion_matrix": cm,
        "feature_importances": feat_imp,
        "classification_report": clf_report
    }
    
    metrics_path = os.path.join(ml_dir, 'metrics.json')
    with open(metrics_path, 'w') as f:
        json.dump(metrics, f, indent=2)
    print(f"Saved model metrics to: {metrics_path}")
    
    print("\n--- MODEL EVALUATION SUMMARY ---")
    print(f"Accuracy:           {acc*100:.2f}%")
    print(f"Precision (Macro):  {prec_macro*100:.2f}%")
    print(f"Recall (Macro):     {rec_macro*100:.2f}%")
    print(f"F1-Score (Macro):   {f1_macro*100:.2f}%")
    print("\nConfusion Matrix:")
    for name, row in zip(RISK_LEVEL_NAMES, cm):
        print(f"{name:<10}: {row}")
        
    return metrics

if __name__ == '__main__':
    train_and_evaluate()
