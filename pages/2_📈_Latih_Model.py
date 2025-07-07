import streamlit as st
from model import train_model
from helper import load_data

st.title("📈 Pelatihan Model Prediksi")

df = load_data()
model, score = train_model(df)

st.success(f"✅ Model berhasil dilatih. Skor akurasi (R²): {score:.2f}")

