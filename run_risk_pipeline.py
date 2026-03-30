import pandas as pd
import numpy as np

def classify_risk(score):

    if score < 0.3:
        return "LOW"
    elif score < 0.6:
        return "MEDIUM"
    else:
        return "HIGH"


coins = ["bitcoin","ethereum","solana","cardano"]

risk_scores = np.random.rand(len(coins))

data = []

for i,coin in enumerate(coins):

    score = round(risk_scores[i],2)

    data.append({

        "coin_id": coin,
        "risk_score": score,
        "risk_level": classify_risk(score)

    })

df = pd.DataFrame(data)

df.to_csv("final_report.csv",index=False)

print("Risk pipeline completed")