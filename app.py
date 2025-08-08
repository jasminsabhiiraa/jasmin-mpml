import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load('model.pkl')

st.set_page_config(page_title="Student Performance Prediction", layout="centered")
st.title('🎓 Prediksi Indeks Performa Siswa')

st.write("Masukkan data berikut untuk memprediksi performa siswa:")

# Input form
with st.form("prediction_form"):
    hours = st.slider('Hours Studied', 0.0, 10.0, step=0.1)
    previous_scores = st.slider('Previous Scores', 0, 100, step=1)
    extra = st.selectbox('Extracurricular Activities', ['Yes', 'No'])
    sleep = st.slider('Sleep Hours', 0.0, 12.0, step=0.1)
    papers = st.slider('Sample Question Papers Practiced', 0, 10, step=1)
    submitted = st.form_submit_button("Predict")

# Proses prediksi
if submitted:
    # Buat DataFrame input user
    input_df = pd.DataFrame({
        'Hours Studied': [hours],
        'Previous Scores': [previous_scores],
        'Extracurricular Activities': [extra],
        'Sleep Hours': [sleep],
        'Sample Question Papers Practiced': [papers]
    })

    # Prediksi
    prediction = model.predict(input_df)[0]

    st.success(f"🎯 Prediksi Performance Index Siswa: **{prediction:.2f}**")
