import streamlit as st
import joblib
import numpy as np


# Load the model
model = joblib.load("model/heart_risk_model.pkl")

# Page settings
st.set_page_config(page_title="Heart Risk Prediction", page_icon="❤️", layout="wide")

# Title
st.markdown("<h1 style='text-align:center; color:#FF4B4B;'>❤️ Heart Risk Prediction App</h1>", unsafe_allow_html=True)
st.write("Your heart health matters,see how healthy your heart is today.", layout="wide")
st.markdown("---")

# Layout: Two columns for cleaner look
col1, col2 = st.columns(2)

with col1:
    st.subheader("🧍 Personal Information")
    gender = st.radio("Gender", ["Male", "Female"])
    age = st.number_input("Age", min_value=1, max_value=120, value=30)
    education = st.selectbox("Education Level", ["Some High School", "High School Graduate", "Some College", "College Graduate", "Postgraduate"])

    st.subheader("🩺 Health Information")
    smoker = st.radio("Currently Smokes?", ["Yes", "No"])
    bpm_meds = st.radio("On BP Medication?", ["Yes", "No"])
    stroke = st.radio("Previous Stroke?", ["Yes", "No"])
    hypertension = st.radio("Hypertension?", ["Yes", "No"])
    diabetes = st.radio("Diabetes?", ["Yes", "No"])

with col2:
    st.subheader("📊 Health Metrics")
    cigs_per_day = st.number_input("Cigarettes Per Day", min_value=0, max_value=100, value=0)
    tot_chol = st.number_input("Total Cholesterol (mg/dL)", min_value=100, max_value=600, value=200)
    sys_bp = st.number_input("Systolic BP", min_value=80, max_value=250, value=120)
    dia_bp = st.number_input("Diastolic BP", min_value=50, max_value=150, value=80)
    bmi = st.number_input("BMI", min_value=10.0, max_value=60.0, value=25.0)
    heart_rate = st.number_input("Heart Rate", min_value=40, max_value=200, value=70)
    glucose = st.number_input("Glucose Level (mg/dL)", min_value=50, max_value=300, value=100)

# Map user inputs to numeric values
gender_map = {"Male": 1, "Female": 0}
edu_map = {"Some High School": 1, "High School Graduate": 2, "Some College": 3, "College Graduate": 4, "Postgraduate": 5}
yes_no_map = {"Yes": 1, "No": 0}

# Convert to numeric for the model
input_data = [[
    gender_map[gender],
    edu_map[education],
    yes_no_map[smoker],
    cigs_per_day,
    yes_no_map[bpm_meds],
    yes_no_map[stroke],
    yes_no_map[hypertension],
    yes_no_map[diabetes],
    tot_chol,
    sys_bp,
    dia_bp,
    bmi,
    heart_rate,
    glucose,
    age
]]

# Predict button
if st.button("🔍 Predict Risk"):
    prediction = model.predict(input_data)[0]
    confidence = model.predict_proba(input_data)[0][prediction] * 100

    st.markdown("---")
    st.subheader("Results")
    if prediction == 1:
        st.error(f"⚠️ Heart Risk Detected with {confidence:.2f}% confidence")
    else:
        st.success(f"✅ No Heart Risk with {confidence:.2f}% confidence")

    