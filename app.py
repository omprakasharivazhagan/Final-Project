import streamlit as st
import pandas as pd
import numpy as np
import joblib
import os

# --- Load Model Safely ---
model_path = os.path.join(os.path.dirname(__file__), "ww2_model.pkl")
features_path = os.path.join(os.path.dirname(__file__), "model_features.pkl")

if not os.path.exists(model_path):
    st.error("❌ 'ww2_model.pkl' not found in the project directory.")
    st.stop()

if not os.path.exists(features_path):
    st.error("❌ 'model_features.pkl' not found in the project directory.")
    st.stop()

model = joblib.load(model_path)
feature_names = joblib.load(features_path)

# --- Streamlit UI ---
st.title("✈️ WWII Aircraft Mission Outcome Predictor")

st.markdown("Fill in the mission details below:")

user_input = {}
for feature in feature_names:
    user_input[feature] = st.number_input(f"{feature}", value=0)

if st.button("Predict Outcome"):
    input_df = pd.DataFrame([user_input])

    # Ensure columns match
    input_df = input_df[feature_names]

    # Predict
    prediction = model.predict(input_df)[0]
    pred_label = "Aircraft Failed" if prediction == 1 else "Aircraft Successful"

    st.success(f"🚀 **Prediction**: {pred_label}")