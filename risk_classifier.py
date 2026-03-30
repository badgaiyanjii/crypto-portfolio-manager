import pandas as pd

def classify_risk():

    df=pd.read_csv("risk_report.csv")

    def classify(v):

        if v<0.02:
            return "LOW RISK"
        elif v<0.05:
            return "MEDIUM RISK"
        else:
            return "HIGH RISK"

    df["risk_level"]=df["volatility"].apply(classify)

    df.to_csv("final_report.csv",index=False)

    print("Risk classification complete")