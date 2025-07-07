import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

def encode_bulan(bulan):
    urut = ['JANUARI','FEBRUARI','MARET','APRIL','MEI','JUNI']
    return [urut.index(b) + 1 for b in bulan]

def train_model(df):
    df = df.copy()
    df["BULAN_ENCODE"] = encode_bulan(df["BULAN"])
    bulanan = df.groupby("BULAN_ENCODE")[["NUS", "MAN"]].sum()
    bulanan["TOTAL"] = bulanan["NUS"] + bulanan["MAN"]

    X = bulanan.index.values.reshape(-1, 1)
    y = bulanan["TOTAL"].values

    model = LinearRegression()
    model.fit(X, y)
    return model, r2_score(y, model.predict(X))

def predict_value(model, bulan_ke):
    return model.predict([[bulan_ke]])[0]
