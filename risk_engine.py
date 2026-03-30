import numpy as np

RISK_FREE_RATE = 0.02/252

def calculate_risk(coin_df,coin_id):

    returns = coin_df["daily_return"].dropna()

    mean_return = returns.mean()
    volatility = returns.std()

    sharpe = 0

    if volatility != 0:
        sharpe = (mean_return-RISK_FREE_RATE)/volatility

    risk_score = volatility*100

    if risk_score > 5:
        level = "HIGH"
    elif risk_score > 2:
        level = "MEDIUM"
    else:
        level = "LOW"

    return {
        "coin_id":coin_id,
        "mean_return":round(mean_return,5),
        "volatility":round(volatility,5),
        "sharpe_ratio":round(sharpe,2),
        "risk_score":round(risk_score,2),
        "risk_level":level
    }