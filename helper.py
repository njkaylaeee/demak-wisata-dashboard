import pandas as pd
import matplotlib.pyplot as plt

def load_data(path="data_wisata.csv"):
    return pd.read_csv(path)

def plot_data(df):
    df_group = df.groupby("BULAN")[["NUS", "MAN"]].sum()
    df_group.plot(kind='bar', figsize=(10, 4), title="Kunjungan Wisata per Bulan")
    plt.xticks(rotation=45)
    plt.tight_layout()
    return plt
