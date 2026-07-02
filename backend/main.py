import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from fastapi import FastAPI
import joblib
import pandas as pd
from backend.schemas import CustomerData
from src.data_preprocessing import preprocess_input

app = FastAPI(title="Customer Churn Prediction API")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, '..', 'models', 'churn_model.pkl')
model = joblib.load(MODEL_PATH)

@app.get("/")
def read_root():
    return {"message": "Customer Churn Prediction API is running."}

@app.post("/predict")
def predict_churn(customer: CustomerData):
    input_df = pd.DataFrame([customer.model_dump()])
    processed_df = preprocess_input(input_df)

    prediction = model.predict(processed_df)[0]
    probability = model.predict_proba(processed_df)[0][1]

    return {
        "churn_prediction": "Yes" if prediction == 1 else "No",
        "churn_probability": round(float(probability), 4)
    }