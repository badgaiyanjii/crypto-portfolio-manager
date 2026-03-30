import sqlite3
import pandas as pd

def save_report():

    conn = sqlite3.connect("crypto_reports.db")

    df = pd.read_csv("final_report.csv")

    df.to_sql("reports", conn, if_exists="append", index=False)

    conn.commit()

    conn.close()

    print("Report saved to database")