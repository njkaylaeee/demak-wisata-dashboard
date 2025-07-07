import streamlit as st
from model import train_model, predict_value
from helper import load_data
import matplotlib.pyplot as plt

st.set_page_config(page_title="Prediksi Wisatawan", layout="centered")
st.title("📊 Prediksi Jumlah Wisatawan")

# Load data dan latih model
df = load_data()
model, score = train_model(df)

# Informasi model
with st.expander("ℹ️ Tentang Model"):
    st.write(f"""
        Model menggunakan regresi linier berdasarkan data bulan Januari–Juni 2025.
        Skor akurasi (R²): **{score:.2f}**
    """)

# Input form
st.subheader("🧮 Form Input Prediksi")
bulan_ke = st.slider("Pilih Bulan ke-", min_value=7, max_value=12, value=7, step=1, help="Misal: 7 untuk Juli")
submit = st.button("🎯 Prediksi Sekarang")

if submit:
    hasil = predict_value(model, bulan_ke)
    st.success(f"📍 Prediksi jumlah wisatawan bulan ke-{bulan_ke}: **{int(hasil):,} orang**")

    # Tambahan grafik prediksi
    fig, ax = plt.subplots()
    ax.bar([f"Bulan ke-{bulan_ke}"], [hasil], color='orange')
    ax.set_ylabel("Jumlah Wisatawan")
    ax.set_title("Hasil Prediksi")
    st.pyplot(fig)
