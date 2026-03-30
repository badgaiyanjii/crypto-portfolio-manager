import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import sqlite3

from prediction_model import predict_next_price
from investment_mix_calculator import InvestmentMixCalculator


st.set_page_config(page_title="Crypto Portfolio Manager", layout="wide")

st.title(" Crypto Portfolio Management Dashboard")


# ==========================================
# Sidebar Navigation
# ==========================================

section = st.sidebar.radio(
    "Navigation",
    [
        "Investment Mix Advisor",
        "Risk Analysis",
        "Crypto Trends",
        "Price Prediction",
        "Saved Reports"
    ]
)

# ==========================================
# 1️⃣ Investment Mix Advisor
# ==========================================

if section == "Investment Mix Advisor":

    st.header(" Investment Mix Calculator")

    total_investment = st.number_input(
        "Total Investment ($)",
        min_value=0.0
    )

    risk_profile = st.selectbox(
        "Risk Preference",
        ["Low", "Medium", "High"]
    )

    if st.button("Generate Portfolio"):

        try:

            risk_df = pd.read_csv("final_report.csv")
            risk_metrics = risk_df.to_dict("records")

            calculator = InvestmentMixCalculator(
                risk_metrics,
                total_investment,
                risk_profile
            )

            allocation = calculator.calculate_allocation()

            df = pd.DataFrame(allocation)

            st.dataframe(df)

            fig, ax = plt.subplots()

            ax.pie(
                df["allocated_amount"],
                labels=df["coin_id"],
                autopct="%1.1f%%"
            )

            ax.set_title("Portfolio Allocation")

            st.pyplot(fig)

        except:
            st.error("Run risk pipeline first")


# ==========================================
# 2️⃣ Risk Analysis
# ==========================================

elif section == "Risk Analysis":

    st.header("⚠ Crypto Risk Analysis")

    try:

        df = pd.read_csv("final_report.csv")

        st.dataframe(df)

        fig, ax = plt.subplots()

        ax.bar(df["coin_id"], df["risk_score"])

        ax.set_title("Risk Score by Crypto")

        st.pyplot(fig)

    except:
        st.warning("Risk report not available")


# ==========================================
# 3️⃣ Crypto Trends
# ==========================================

elif section == "Crypto Trends":

    st.header(" Crypto Price Trends")

    try:

        df = pd.read_csv("historical_prices_clean.csv")

        coins = df["coin_id"].unique()

        selected_coin = st.selectbox(
            "Select Cryptocurrency",
            coins
        )

        coin_df = df[df["coin_id"] == selected_coin]

        fig, ax = plt.subplots()

        ax.plot(coin_df["date"], coin_df["close"])

        ax.set_title(f"{selected_coin} Price Trend")

        ax.set_xlabel("Date")
        ax.set_ylabel("Price")

        st.pyplot(fig)

    except:
        st.error("Historical data not found")


# ==========================================
# 4️⃣ Price Prediction
# ==========================================

elif section == "Price Prediction":

    st.header(" Next Day Price Prediction")

    coin = st.selectbox(
        "Select Coin",
        ["bitcoin", "ethereum", "solana"]
    )

    if st.button("Predict Price"):

        try:

            price = predict_next_price(coin)

            st.success(
                f"Predicted Next Day Price for {coin}: ${price}"
            )

        except:
            st.error("Prediction failed")


# ==========================================
# 5️⃣ Saved Reports (Database)
# ==========================================

elif section == "Saved Reports":

    st.header(" Saved Risk Reports")

    try:

        conn = sqlite3.connect("crypto_reports.db")

        df = pd.read_sql(
            "SELECT * FROM reports",
            conn
        )

        st.dataframe(df)

        conn.close()

    except:
        st.warning("No reports stored in database")