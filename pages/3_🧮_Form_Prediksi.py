import streamlit as st
from model import train_model, predict_value
from helper import load_data

st.title("🧮 Form Prediksi Wisatawan")

df = load_data()
model, _ = train_model(df)

bulan = st.number_input("Masukkan bulan ke- (7 = Juli, dst)", min_value=7, max_value=12, value=7)

if st.button("Prediksi Sekarang"):
    hasil = predict_value(model, bulan)
    st.success(f"📍 Prediksi jumlah wisatawan bulan ke-{bulan}: {int(hasil):,} orang")

