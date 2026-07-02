import pandas as pd
import joblib
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_COLUMNS_PATH = os.path.join(BASE_DIR, '..', 'models', 'model_columns.pkl')

def preprocess_input(raw_df: pd.DataFrame) -> pd.DataFrame:
    """
    Applies the same encoding steps used during training to raw input data.
    Expects raw_df to have the original, human-readable column values
    (e.g., 'Male'/'Female', 'Yes'/'No', 'Month-to-month', etc.)
    """
    df = raw_df.copy()

    df['gender'] = df['gender'].map({'Female': 0, 'Male': 1})

    yes_no_cols = ['Partner', 'Dependents', 'PhoneService', 'PaperlessBilling']
    for col in yes_no_cols:
        df[col] = df[col].map({'No': 0, 'Yes': 1})

    multi_cat_cols = ['MultipleLines', 'InternetService', 'OnlineSecurity', 'OnlineBackup',
                       'DeviceProtection', 'TechSupport', 'StreamingTV', 'StreamingMovies',
                       'Contract', 'PaymentMethod']
    df = pd.get_dummies(df, columns=multi_cat_cols, drop_first=True)

    model_columns = joblib.load(MODEL_COLUMNS_PATH)
    df = df.reindex(columns=model_columns, fill_value=0)

    return df