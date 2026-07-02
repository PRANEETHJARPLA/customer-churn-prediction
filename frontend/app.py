import streamlit as st
import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_BASE_URL = os.getenv("API_BASE_URL", "http://localhost:8000")

st.set_page_config(page_title="Customer Churn Prediction", page_icon="📊", layout="centered")
st.title("📊 Customer Churn Prediction Dashboard")
st.write("Enter customer details to predict their likelihood of churning.")

st.header("Customer Information")

col1, col2 = st.columns(2)

with col1:
    gender = st.selectbox("Gender", ["Male", "Female"])
    SeniorCitizen = st.selectbox("Senior Citizen", [0, 1])
    Partner = st.selectbox("Has Partner", ["Yes", "No"])
    Dependents = st.selectbox("Has Dependents", ["Yes", "No"])
    tenure = st.number_input("Tenure (months)", min_value=0, max_value=100, value=12)
    PhoneService = st.selectbox("Phone Service", ["Yes", "No"])
    MultipleLines = st.selectbox("Multiple Lines", ["Yes", "No", "No phone service"])
    InternetService = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
    OnlineSecurity = st.selectbox("Online Security", ["Yes", "No", "No internet service"])
    OnlineBackup = st.selectbox("Online Backup", ["Yes", "No", "No internet service"])

with col2:
    DeviceProtection = st.selectbox("Device Protection", ["Yes", "No", "No internet service"])
    TechSupport = st.selectbox("Tech Support", ["Yes", "No", "No internet service"])
    StreamingTV = st.selectbox("Streaming TV", ["Yes", "No", "No internet service"])
    StreamingMovies = st.selectbox("Streaming Movies", ["Yes", "No", "No internet service"])
    Contract = st.selectbox("Contract", ["Month-to-month", "One year", "Two year"])
    PaperlessBilling = st.selectbox("Paperless Billing", ["Yes", "No"])
    PaymentMethod = st.selectbox("Payment Method", ["Electronic check", "Mailed check", "Bank transfer (automatic)", "Credit card (automatic)"])
    MonthlyCharges = st.number_input("Monthly Charges ($)", min_value=0.0, max_value=200.0, value=65.0)
    TotalCharges = st.number_input("Total Charges ($)", min_value=0.0, max_value=10000.0, value=1000.0)
if st.button("Predict Churn", type="primary"):
    payload = {
        "gender": gender,
        "SeniorCitizen": SeniorCitizen,
        "Partner": Partner,
        "Dependents": Dependents,
        "tenure": tenure,
        "PhoneService": PhoneService,
        "MultipleLines": MultipleLines,
        "InternetService": InternetService,
        "OnlineSecurity": OnlineSecurity,
        "OnlineBackup": OnlineBackup,
        "DeviceProtection": DeviceProtection,
        "TechSupport": TechSupport,
        "StreamingTV": StreamingTV,
        "StreamingMovies": StreamingMovies,
        "Contract": Contract,
        "PaperlessBilling": PaperlessBilling,
        "PaymentMethod": PaymentMethod,
        "MonthlyCharges": MonthlyCharges,
        "TotalCharges": TotalCharges
    }

    try:
        with st.spinner("Predicting..."):
            response = requests.post(f"{API_BASE_URL}/predict", json=payload)
            response.raise_for_status()
            result = response.json()

        if result["churn_prediction"] == "Yes":
            st.error(f"⚠️ High Risk: {result['churn_probability']*100:.1f}% probability of churn")
        else:
            st.success(f"✅ Low Risk: {result['churn_probability']*100:.1f}% probability of churn")

    except requests.exceptions.ConnectionError:
        st.error("Could not connect to the prediction API. Is the backend server running?")
    except requests.exceptions.HTTPError as e:
        st.error(f"API returned an error: {e}")