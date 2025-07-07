import pandas as pd

def predict_next(df):
    bulanan = df.groupby("BULAN")[["NUS", "MAN"]].sum()
    bulanan["TOTAL"] = bulanan["NUS"] + bulanan["MAN"]
    prediksi = int(bulanan["TOTAL"].rolling(3).mean().dropna().iloc[-1])
    return pd.DataFrame({
        "Bulan Prediksi": ["JULI 2025"],
        "Prediksi Total Wisatawan": [prediksi]
    })
