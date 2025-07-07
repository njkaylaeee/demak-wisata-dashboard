import streamlit as st
from model import train_model, predict_value
from helper import load_data
import matplotlib.pyplot as plt

st.title("🧮 Form Prediksi Jumlah Wisatawan")
st.write("Gunakan form ini untuk memprediksi jumlah total kunjungan wisatawan bulan ke-7 dan seterusnya.")

# Load data dan model
df = load_data()
model, score = train_model(df)

# Skor akurasi
st.info(f"Model Regresi Linier (R²): **{score:.2f}**")

# Input bulan
bulan = st.slider("📆 Pilih Bulan ke- (7 = Juli, dst)", min_value=7, max_value=12, value=7)

# Input asumsi tambahan (opsional)
promo = st.checkbox("🟢 Apakah ada promosi pariwisata bulan ini?")
cuaca = st.selectbox("🌤️ Perkiraan cuaca?", ["Normal", "Cerah", "Hujan"])

# Tombol prediksi
if st.button("🎯 Prediksi Wisatawan"):
    hasil = predict_value(model, bulan)

    # Efek asumsi (simulatif)
    if promo: hasil *= 1.10
    if cuaca == "Hujan": hasil *= 0.90
    elif cuaca == "Cerah": hasil *= 1.05

    st.success(f"📍 Prediksi kunjungan wisatawan bulan ke-{bulan}: **{int(hasil):,} orang**")

    # Grafik hasil
    fig, ax = plt.subplots()
    ax.bar([f"Bulan ke-{bulan}"], [hasil], color='teal')
    ax.set_ylabel("Jumlah Wisatawan")
    ax.set_title("Grafik Hasil Prediksi")
    st.pyplot(fig)

    with st.expander("📘 Penjelasan"):
        st.markdown("""
        - Prediksi ini berdasarkan tren enam bulan pertama.
        - Faktor seperti promosi dan cuaca memengaruhi hasil.
        - Model yang digunakan adalah **Regresi Linier**.
        """)
