import numpy as np
import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.pipeline import Pipeline
import joblib
import plotly.express as px
import openpyxl
import streamlit as st
import zipfile
# Preprocess class for data transformation
class Preprocess(BaseEstimator, TransformerMixin):

   def __init__(self, mean, std):
       self.mean = mean
       self.std = std

   def fit(self):
    return self

   def transform(self, XX):
    X = XX.copy()
    X['BalanceProductNumRatio'] = X['balance'] / X['products_number']
    con_col = [
        'credit_score',
        'age',
        'tenure',
        'balance',
        'products_number',
        'estimated_salary',
        'BalanceProductNumRatio'
        ]
    feature = [
          'credit_score', 'age', 'tenure', 'balance', 'products_number', 'credit_card',
          'active_member', 'estimated_salary', 'country_France', 'country_Germany',
          'country_Spain', 'gender_Female', 'gender_Male', 'BalanceProductNumRatio'
        ]
    X[con_col] = (X[con_col] - self.mean) / self.std
    X_endoded = X.replace({0: -1})
    X_endoded.loc[X_endoded['credit_card'] == 0, 'credit_card'] = -1
    X_endoded.loc[X_endoded['active_member'] == 0, 'active_member'] = -1
    final_input = {f: X.get(f, 0) for f in feature}

    return pd.DataFrame(final_input)

# The main app

# Set the size of the layout
st.set_page_config(layout="wide")

# Load model
with zipfile.ZipFile("final_model (2).zip", "r") as model_exctract:
   with model_exctract.open('final_model (2).pkl') as file:
      model = joblib.load(file)
mean = joblib.load('mean (1).pkl')
std = joblib.load('std (1).pkl')

#  Class to Preprocess the input(class Preprocess)

# Title bagian atas(Customer churn prediction)
st.title("Customer churn prediction")

# Fist page of the app: Getting the input
st.header("User Input Features")
feature = [
          'credit_score', 'age', 'tenure', 'balance', 'products_number', 'credit_card',
          'active_member', 'estimated_salary', 'country', 'gender', 'BalanceProductNumRatio'
        ]
binary_cols  = [
     'credit_card', 'active_member'
]
Numerical_cols = [
        'credit_score',
        'age',
        'tenure',
        'balance',
        'products_number',
        'estimated_salary',
        ]

# default value
default_value = [
    100, 23, 3, 2000.123, 2, 1, 0, 100000.78, 1, 0, 0, 1, 0
]

user_inputs = {}

for i, col in enumerate(feature):
    if col in Numerical_cols:
        if col == 'balance' or col == 'estimated_salary':
            user_inputs[col] = st.number_input(col, value=default_value[i], step = 0.01)
            continue
        user_inputs[col] = st.number_input(col, value=default_value[i], step = 1)
    elif col in binary_cols:
        user_inputs[col] = st.selectbox(col, ['Yes', 'No'])
        user_inputs[col] = 1 if user_inputs[col] == 'Yes' else 0
    elif col == 'country':
        country = st.selectbox(col, ['Germany', 'Spain', 'France'])
        user_inputs[f'country_{country}'] = 1 if country == 'Germany' else 0
    elif col == 'gender':
        gender = st.selectbox(col, ['Female', 'Male'])
        user_inputs[f'gender_{gender}'] = 1 if gender == 'Female' else 0



input_data = pd.DataFrame([user_inputs])
preprocess_input = Preprocess(mean, std)

# Second page of the app: Doing prediction
st.header("Prediction")
if st.button("Predict"):

    # Get the predicted value
    prediction = model.predict(preprocess_input.transform(input_data))
    prediction_label = "Churn" if prediction == 1 else "Not churn"

    # Get the prediction probabilities
    pred_prob = model.predict_proba(preprocess_input.transform(input_data))

    # Display result
    st.subheader(f"Prediction: {prediction_label}")
    st.write(f"Prediction Probability: {pred_prob[0][1]:.2f} (churn)")
    st.write(f"Prediction Probability: {pred_prob[0][0]:.2f} (Not churn)")

# Third page of the app: Feature importance
st.header("Feature Importance")
# Load the feature importance data
feature_importance_data = pd.read_excel('feature_importance.xlsx', usecols = ["Feature", "Feature Importance Score"])
fig = px.bar(
        feature_importance_data.sort_values(by="Feature Importance Score", ascending=False),
        x="Feature Importance Score",
        y="Feature",
        orientation="h",
        title="Feature Importance",
        labels={"Feature Importance Score": "Importance", "Feature": "Features"},
        width=400,  # Set custom width
        height=500  # Set custom height
    )
st.plotly_chart(fig)

# TO DO LIST 20/06/26:
# DEPLOY BERHASIL YEYY
# Tinggal membernarkan si readme github
#   1. notebook collab nya kita ganti karena gak bisa dibuka
#   2. add penjelaskan tentang kualitas model supaya lebih detail di github
