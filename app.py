import streamlit as st
from helper import load_data, plot_data, plot_map
from model import predict_next

st.set_page_config(layout="wide")
st.title("📈 Dashboard Prediksi Kunjungan Wisata Demak 2025")

df = load_data()

st.subheader("📊 Data Kunjungan Wisata")
st.dataframe(df)

st.subheader("📉 Grafik Kunjungan Bulanan")
st.pyplot(plot_data(df))

st.subheader("🤖 Prediksi Bulan Berikutnya")
st.dataframe(predict_next(df))

st.subheader("🗺️ Peta Interaktif Destinasi Wisata")
plot_map(df)
