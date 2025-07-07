import pandas as pd
import matplotlib.pyplot as plt
import folium
from streamlit_folium import folium_static

def load_data(path="data/data_wisata.csv"):
    return pd.read_csv(path)

def plot_data(df):
    df_group = df.groupby("BULAN")[["NUS", "MAN"]].sum()
    df_group.plot(kind='bar', figsize=(10, 4), title="Kunjungan Wisata per Bulan")
    plt.xticks(rotation=45)
    plt.tight_layout()
    return plt

def plot_map(df):
    lokasi_dtw = {
        'Bedono Bangkit': (-6.8931, 110.6387),
        'Candisari': (-6.9100, 110.6400),
        'Bermi - Sumur Gandeng': (-6.9000, 110.6500),
    }
    m = folium.Map(location=[-6.9, 110.64], zoom_start=11)
    total = df.groupby("DTW")[["NUS", "MAN"]].sum().reset_index()
    for _, row in total.iterrows():
        if row["DTW"] in lokasi_dtw:
            popup = f"{row['DTW']}<br>NUS: {int(row['NUS'])}<br>MAN: {int(row['MAN'])}"
            folium.Marker(
                location=lokasi_dtw[row["DTW"]],
                popup=popup,
                tooltip=row["DTW"]
            ).add_to(m)
    folium_static(m, width=900, height=500)
