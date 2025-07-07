import streamlit as st
from helper import load_data, plot_data

st.title("🏠 Beranda Dashboard Wisata Demak")

st.markdown("""
Selamat datang di dashboard **Prediksi Kunjungan Wisata Kabupaten Demak 2025**.
Di sini, kamu bisa:
- 📊 Menjelajahi data kunjungan wisata Nusantara & Mancanegara
- 🤖 Melatih model prediksi berdasarkan data riil
- 🧮 Mengisi form interaktif untuk prediksi bulan-bulan selanjutnya
""")

with st.expander("ℹ️ Sumber Data"):
    st.write("Data diperoleh dari Dinas Pariwisata Kabupaten Demak tahun 2025, per bulan Januari–Juni.")

df = load_data()
st.pyplot(plot_data(df))
st.dataframe(df, use_container_width=True)
