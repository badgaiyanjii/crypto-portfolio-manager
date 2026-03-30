# 🚀 Crypto Portfolio Management System

## 📌 Project Overview
The Crypto Portfolio Management System is an end-to-end application designed to help users make informed investment decisions in the cryptocurrency market. 

The system integrates data analysis, risk assessment, portfolio optimization, and machine learning-based price prediction into a single interactive dashboard.

---

## 🎯 Objectives

- Analyze cryptocurrency risk using historical data
- Classify assets into Low, Medium, and High risk categories
- Generate optimized portfolio allocation based on user risk preference
- Visualize crypto price trends using interactive graphs
- Predict future prices using machine learning
- Store and retrieve reports using database

---

## 🧩 System Architecture
User Interface (Frontend - Streamlit)
↓
Backend Processing (Python Modules)
↓
Data Layer (CSV + SQLite Database)

---

## ⚙️ Modules Description

### 🔹 1. Data Collection & Processing
- Fetches and processes cryptocurrency historical data
- Cleans and prepares data for analysis

### 🔹 2. Risk Analysis Engine
- Calculates:
  - Daily Returns
  - Volatility
  - Risk Score
- Classifies coins into:
  - LOW Risk
  - MEDIUM Risk
  - HIGH Risk

---

### 🔹 3. Portfolio Allocation Module
- Uses risk-based allocation strategy
- Distributes investment based on user profile:
  - Low Risk Investor
  - Medium Risk Investor
  - High Risk Investor

---

### 🔹 4. Machine Learning Prediction
- Uses Linear Regression model
- Predicts next-day cryptocurrency prices
- Based on historical trends

---

### 🔹 5. Interactive Dashboard (Frontend)
Built using Streamlit:
- Portfolio allocation visualization
- Risk analysis graphs
- Crypto trend charts
- Price prediction interface

---

### 🔹 6. Database Integration
- Stores reports in SQLite database
- Allows retrieval of previous analysis

---

## 📊 Key Features

✔ Risk Classification (Low / Medium / High)  
✔ Portfolio Optimization  
✔ Interactive Visualizations (Plotly)  
✔ Machine Learning Prediction  
✔ Real-time Dashboard Interface  
✔ Database Storage  

---

## 🛠️ Tech Stack

| Category        | Technology Used |
|----------------|---------------|
| Language       | Python        |
| Data Analysis  | Pandas, NumPy |
| Visualization  | Matplotlib, Plotly |
| ML Model       | Scikit-learn  |
| Frontend       | Streamlit     |
| Database       | SQLite        |

---

## 📂 Project Structure
crypto-portfolio-manager

├── backend/
├── frontend/
├── data/
├── docs/
├── README.md
├── LICENSE
├── requirements.txt


---

## ▶️ How to Run the Project

pip install -r requirements.txt
python backend/run_risk_pipeline.py
streamlit run frontend/dashboard.py


----
📈 Sample Outputs
Risk Analysis Report
Portfolio Allocation Chart
Crypto Price Trends
Predicted Price Output

-----
🧠 Agile Methodology

This project follows Agile practices:

Sprint-based development
Modular design
Incremental feature addition
📌 Sprints:
Sprint 1: Data Collection
Sprint 2: Risk Analysis
Sprint 3: Dashboard Development
Sprint 4: ML Integration & Testing
----
🔐 License

This project is licensed under the MIT License.
---
👩‍💻 Author

Aanya Badgaiyan
-----

💡 Future Enhancements
Live crypto API integration
Advanced ML models (LSTM, ARIMA)
Real-time portfolio tracking
User authentication system
Cloud deployment

-----
⭐ Conclusion

This system provides a complete solution for cryptocurrency investment analysis by combining financial analytics, machine learning, and interactive visualization in a single platform.

