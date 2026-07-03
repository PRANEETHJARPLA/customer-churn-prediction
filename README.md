# 📊 Customer Churn Prediction Dashboard

An end-to-end machine learning project that predicts customer churn for a telecom business, served via a FastAPI backend and visualized through an interactive Streamlit dashboard.

**Resume line:** Built and deployed a churn prediction model (XGBoost) achieving 81% recall on the churn class, served via an interactive Streamlit dashboard for business stakeholders.

## Project Status
✅ Core pipeline complete — data processing, model training, backend API, and frontend dashboard all functional and tested locally. Deployment in progress.

## Key Results

| Model | Recall | Precision | F1-Score |
|---|---|---|---|
| Logistic Regression (baseline) | 0.57 | 0.65 | 0.61 |
| XGBoost (default) | 0.53 | 0.58 | 0.55 |
| XGBoost (tuned, F1-optimized) | **0.81** | 0.49 | **0.61** |

Recall was prioritized as the primary metric since a missed churner (false negative) costs the business significantly more than an unnecessary retention offer (false positive).

## Key EDA Findings
- **Contract type** is the strongest churn driver: month-to-month customers churn at a dramatically higher rate than those on 1-2 year contracts.
- **Tenure** matters heavily: churned customers had a median tenure of just 10 months, vs. 38 months for retained customers.
- **Fiber optic internet** customers churn at nearly 42%, compared to ~19% for DSL and ~7% for customers with no internet service — likely a combination of higher cost and higher service expectations.

## Tech Stack
- **Language:** Python 3.13
- **ML Libraries:** Pandas, NumPy, Scikit-learn, XGBoost
- **Backend:** FastAPI, Pydantic, Uvicorn
- **Frontend:** Streamlit
- **Testing:** Pytest
- **Deployment:** Render (API) + Streamlit Community Cloud (Dashboard)

## Architecture

This project uses a decoupled architecture: the FastAPI backend serves predictions via a REST API, independent of the Streamlit frontend, which consumes that API via HTTP requests. This mirrors real-world production ML systems and allows either component to be tested, deployed, or replaced independently.
User → Streamlit Dashboard → HTTP Request → FastAPI Backend → XGBoost Model → Prediction → back to Dashboard

## Project Structure
customer-churn-prediction/
├── backend/            # FastAPI application (main.py, schemas.py)
├── data/                # Raw and processed datasets
├── frontend/            # Streamlit dashboard
├── models/              # Saved trained model, scaler, column list
├── notebooks/           # EDA and model development notebook
├── src/                 # Reusable preprocessing logic
└── tests/               # Automated tests (pytest)

## Setup Instructions

1. Clone the repository:
git clone https://github.com/PRANEETHJARPLA/customer-churn-prediction.git
cd customer-churn-prediction

2. Create and activate a virtual environment:
python -m venv venv
venv\Scripts\Activate      # Windows

3. Install dependencies:
pip install -r requirements.txt

4. Set up environment variables:
copy .env.example .env

5. Run the backend (in one terminal):
uvicorn backend.main:app --reload

6. Run the frontend (in a separate terminal):
streamlit run frontend/app.py

7. Open `http://localhost:8501` in your browser.

## Running Tests
pytest tests/

## Dataset
[Telco Customer Churn Dataset](https://www.kaggle.com/datasets/blastchar/telco-customer-churn) (IBM sample dataset, via Kaggle).

## Future Improvements
- Batch prediction support (upload a CSV of multiple customers)
- Model monitoring / drift detection
- CI/CD pipeline via GitHub Actions

## License
MIT

## Author
Praneeth Jarpla

## 🔗 Live Demo
- **Dashboard:** [Streamlit App](https://customer-churn-prediction-yyogd4kjnq8kfqepr27fp7.streamlit.app/)
- **API Docs:** [https://customer-churn-prediction-szjl.onrender.com/docs](https://customer-churn-prediction-szjl.onrender.com/docs)

> Note: The API is hosted on Render's free tier and may take 30-60 seconds to wake up on first request after a period of inactivity.