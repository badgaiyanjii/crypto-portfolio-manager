import pandas as pd


def run_parallel_risk(df):

    results = []

    coins = df["coin_id"].unique()

    for coin in coins:

        coin_df = df[df["coin_id"] == coin]

        volatility = coin_df["daily_return"].std()

        if volatility < 0.02:
            risk = "LOW"

        elif volatility < 0.05:
            risk = "MEDIUM"

        else:
            risk = "HIGH"

        results.append({

            "coin_id": coin,
            "volatility": volatility,
            "risk_category": risk
        })

    return pd.DataFrame(results)