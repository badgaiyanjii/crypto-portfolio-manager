import pandas as pd
from sklearn.linear_model import LinearRegression

def predict_next_price(coin):

    df = pd.read_csv("historical_prices_clean.csv")

    coin_df = df[df["coin_id"] == coin]

    coin_df["day"] = range(len(coin_df))

    X = coin_df[["day"]]
    y = coin_df["close"]

    model = LinearRegression()
    model.fit(X,y)

    next_day = [[len(coin_df)]]

    prediction = model.predict(next_day)

    return round(prediction[0],2)