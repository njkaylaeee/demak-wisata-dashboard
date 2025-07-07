import streamlit as st
from helper import load_data, plot_data

st.title("🏠 Beranda")
st.write("Halaman ini menampilkan data kunjungan wisata Kabupaten Demak bulan Januari–Juni 2025.")

df = load_data()
st.pyplot(plot_data(df))
st.dataframe(df)
