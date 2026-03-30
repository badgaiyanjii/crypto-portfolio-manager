import pandas as pd
import re

df = pd.read_csv("historical_prices.csv")

def extract(value):

    if pd.isna(value):
        return None

    match = re.search(r"[-+]?\d*\.\d+|\d+",str(value))

    return float(match.group()) if match else None


for col in ["open","high","low","close","volume"]:
    df[col] = df[col].apply(extract)

df.to_csv("historical_prices_clean.csv",index=False)

print("CSV cleaned")