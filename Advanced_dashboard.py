import streamlit as st
import pandas as pd
import plotly.express as px
import sqlite3

from auth import *
from otp_verification import *
from prediction_model import predict_next_price
from investment_mix_calculator import InvestmentMixCalculator


st.set_page_config(
    page_title="Crypto Portfolio Manager",
    layout="wide"
)

create_user_table()


# ---------------------------
# LOGIN SYSTEM
# ---------------------------

menu = st.sidebar.selectbox(
    "Account",
    ["Login","Signup"]
)

if menu == "Signup":

    st.title("Create Account")

    email = st.text_input("Email")
    password = st.text_input("Password",type="password")

    if st.button("Signup"):

        add_user(email,password)

        st.success("Account Created")


elif menu == "Login":

    st.title("Login")

    email = st.text_input("Email")
    password = st.text_input("Password",type="password")

    if st.button("Login"):

        result = login_user(email,password)

        if result:

            st.session_state["logged"] = True

        else:

            st.error("Invalid credentials")


# ---------------------------
# MAIN DASHBOARD
# ---------------------------

if "logged" in st.session_state:

    st.sidebar.title("Crypto Dashboard")

    section = st.sidebar.radio(

        "Navigation",

        [

            "Portfolio Allocation",

            "Risk Analysis",

            "Market Trends",

            "AI Price Prediction",

            "Saved Reports"

        ]

    )


    # Portfolio Allocation

    if section == "Portfolio Allocation":

        st.header("Portfolio Optimizer")

        total = st.number_input("Investment Amount")

        profile = st.selectbox(

            "Risk Profile",

            ["Low","Medium","High"]

        )

        if st.button("Generate Portfolio"):

            df = pd.read_csv("final_report.csv")

            metrics = df.to_dict("records")

            calc = InvestmentMixCalculator(

                metrics,

                total,

                profile

            )

            allocation = calc.calculate_allocation()

            df = pd.DataFrame(allocation)

            fig = px.pie(

                df,

                values="allocated_amount",

                names="coin_id",

                title="Portfolio Allocation"

            )

            st.plotly_chart(fig,use_container_width=True)

            st.dataframe(df)


    # Risk Analysis

    elif section == "Risk Analysis":

        st.header("Crypto Risk Dashboard")

        df = pd.read_csv("final_report.csv")

        fig = px.bar(

            df,

            x="coin_id",

            y="risk_score",

            color="risk_level",

            title="Crypto Risk Analysis"

        )

        st.plotly_chart(fig,use_container_width=True)

        st.dataframe(df)


    # Market Trends

    elif section == "Market Trends":

        st.header("Crypto Price Trends")

        df = pd.read_csv("historical_prices_clean.csv")

        coins = df["coin_id"].unique()

        coin = st.selectbox("Select Coin",coins)

        coin_df = df[df["coin_id"]==coin]

        fig = px.line(

            coin_df,

            x="date",

            y="close",

            title=f"{coin} Price Trend"

        )

        st.plotly_chart(fig,use_container_width=True)


    # Price Prediction

    elif section == "AI Price Prediction":

        st.header("AI Crypto Prediction")

        coin = st.selectbox(

            "Select Coin",

            ["bitcoin","ethereum","solana"]

        )

        if st.button("Predict"):

            price = predict_next_price(coin)

            st.success(

                f"Predicted Price: ${price}"

            )


    # Saved Reports

    elif section == "Saved Reports":

        conn = sqlite3.connect(

            "crypto_reports.db"

        )

        df = pd.read_sql(

            "SELECT * FROM reports",

            conn

        )

        st.dataframe(df)

        conn.close()