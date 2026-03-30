import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import sqlite3

from investment_mix_calculator import InvestmentMixCalculator
from prediction_model import predict_next_price


st.set_page_config(
    page_title="Crypto Portfolio Manager",
    layout="wide"
)

st.title("🚀 Crypto Portfolio Management Dashboard")

# ======================================
# Sidebar
# ======================================

menu = st.sidebar.selectbox(
    "Navigation",
    [
        "Dashboard Overview",
        "Investment Advisor",
        "Risk Analysis",
        "Crypto Trends",
        "Price Prediction",
        "Saved Reports"
    ]
)

# ======================================
# 1️⃣ DASHBOARD OVERVIEW
# ======================================

if menu == "Dashboard Overview":

    st.header("📊 System Overview")

    col1, col2, col3 = st.columns(3)

    try:

        risk_df = pd.read_csv("final_report.csv")

        total_coins = len(risk_df)

        avg_volatility = risk_df["volatility"].mean()

        high_risk = len(risk_df[risk_df["risk_category"]=="HIGH"])

    except:

        total_coins = 0
        avg_volatility = 0
        high_risk = 0


    col1.metric("Total Cryptos", total_coins)
    col2.metric("Average Volatility", round(avg_volatility,4))
    col3.metric("High Risk Coins", high_risk)

    st.subheader("Risk Distribution")

    if total_coins > 0:

        fig, ax = plt.subplots()

        risk_counts = risk_df["risk_category"].value_counts()

        ax.pie(
            risk_counts,
            labels=risk_counts.index,
            autopct="%1.1f%%"
        )

        st.pyplot(fig)

    else:

        st.warning("Run risk pipeline first")


# ======================================
# 2️⃣ INVESTMENT ADVISOR
# ======================================

elif menu == "Investment Advisor":

    st.header("💰 AI Investment Mix Advisor")

    investment = st.number_input(
        "Total Investment ($)",
        min_value=0.0
    )

    profile = st.selectbox(
        "Risk Profile",
        ["Low","Medium","High"]
    )

    if st.button("Generate Portfolio"):

        try:

            risk_df = pd.read_csv("final_report.csv")

            risk_metrics = risk_df.to_dict("records")

            calc = InvestmentMixCalculator(
                risk_metrics,
                investment,
                profile
            )

            allocation = calc.calculate_allocation()

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

            st.error("Risk data not available. Run risk pipeline first.")


# ======================================
# 3️⃣ RISK ANALYSIS
# ======================================

elif menu == "Risk Analysis":

    st.header("⚠ Crypto Risk Analysis")

    try:

        df = pd.read_csv("final_report.csv")

        st.dataframe(df)

        fig, ax = plt.subplots()

        ax.bar(
            df["coin_id"],
            df["volatility"]
        )

        ax.set_title("Volatility by Crypto")

        st.pyplot(fig)

    except:

        st.error("Risk report not found")


# ======================================
# 4️⃣ CRYPTO TRENDS
# ======================================

elif menu == "Crypto Trends":

    st.header("📈 Crypto Price Trends")

    try:

        df = pd.read_csv("historical_prices_clean.csv")

        coins = df["coin_id"].unique()

        selected = st.selectbox(
            "Select Coin",
            coins
        )

        coin_df = df[df["coin_id"] == selected]

        fig, ax = plt.subplots()

        ax.plot(
            coin_df["date"],
            coin_df["close"]
        )

        ax.set_title(f"{selected} Price Trend")

        ax.set_xlabel("Date")
        ax.set_ylabel("Price")

        st.pyplot(fig)

    except:

        st.error("Historical price data missing")


# ======================================
# 5️⃣ PRICE PREDICTION
# ======================================

elif menu == "Price Prediction":

    st.header("🔮 Crypto Price Prediction")

    coin = st.selectbox(
        "Select Crypto",
        ["bitcoin","ethereum","solana"]
    )

    if st.button("Predict Next Day Price"):

        try:

            price = predict_next_price(coin)

            st.success(
                f"Predicted Next Price for {coin}: ${price}"
            )

        except:

            st.error("Prediction model failed")


# ======================================
# 6️⃣ DATABASE REPORTS
# ======================================

elif menu == "Saved Reports":

    st.header("📂 Saved Reports Database")

    try:

        conn = sqlite3.connect("crypto_reports.db")

        df = pd.read_sql(
            "SELECT * FROM reports",
            conn
        )

        st.dataframe(df)

        conn.close()

    except:

        st.warning("No reports found in database")