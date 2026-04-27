import streamlit as st
import joblib
import pandas as pd
import numpy as np

@st.cache_resource
def load_model():
    model = joblib.load('model.joblib')
    ct = joblib.load('ct.joblib')
    return model, ct

model, ct = load_model()

st.title("Heart Disease Prediction")

#'Age', 'Gender', 'BloodPressure', 'Cholesterol', 'HeartRate', 'QuantumPatternFeature', 'HeartDisease'

age = st.slider('Age', min_value=0, max_value=100,step=1, value=0)
gender = st.radio('Gender', ['Female', 'Male'])
gender = 1 if gender == "Male" else 0
bloodPressure = st.slider('BloodPressure',min_value=60, max_value=200,step=10, value=90)
cholesterol = st.number_input('Cholesterol')
heartRate = st.number_input('HeartRate')
quantumPatternFeature = st.slider('QuantumPatternFeature',min_value=5,max_value=10,step=1,value=5)

input_data = pd.DataFrame([{
    'Age': age,
    'Gender': gender,
    'BloodPressure': bloodPressure,
    'Cholesterol': cholesterol,
    'HeartRate': heartRate,
    'QuantumPatternFeature': quantumPatternFeature
}])

if st.button('Predict'):
    features = ct.transform(input_data)
    prediction = model.predict(features)
    if prediction == 1:
        st.write("Heart Disease")
    else:
        st.write("No Heart Disease")