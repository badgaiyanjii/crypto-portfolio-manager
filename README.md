# 🚀 Crypto Portfolio Manager  
### End-to-End Financial Analytics & Investment Intelligence System

---

## 📌 Overview

The Crypto Portfolio Manager is a full-stack cryptocurrency analytics system that simulates real-world quantitative finance platforms.

It integrates data pipelines, risk analysis, portfolio optimization, machine learning predictions, and an interactive dashboard into one unified application.

---

## 🔄 Complete Data Pipeline

API Ingestion → Data Storage → Historical Processing → Risk Engine → Parallel Computation → Portfolio Allocation → AI Prediction → Dashboard Visualization → PDF Reporting

---

## 🧠 System Architecture

Presentation Layer (Streamlit UI, Auth, Alerts)
        ↓
Analytics Layer (Risk Engine + ML Models)
        ↓
Data Layer (CoinGecko API + Yahoo Finance)
        ↓
Storage Layer (SQLite + CSV Files)

---

## 📂 Project Structure

CRYPTO-PORTFOLIO-MANAGER/

app.py  
database_manager.py  
notifications.py  
predictor.py  
styles.py  
requirements.txt  
.env.example  
README.md  
LICENSE  

core/  
  collect_data.py  
  fetch_historical.py  
  investment_mix_calculator.py  
  parallel_risk.py  
  risk_engine.py  
  test_investment_mix.py  

data/  
  crypto.db  
  historical_prices.csv  
  eda_coins.csv  
  market_snapshot.csv  

docs/  
  reports & diagrams  

---

## ⚙️ Core Modules

### Data Ingestion Layer
- Fetches live crypto data from APIs
- Stores structured data in CSV and SQLite

### Historical Data Processing
- Downloads 1-year OHLCV data
- Maps crypto IDs to trading symbols

### Risk Analytics Engine
- Calculates daily returns and volatility
- Generates risk scores
- Classifies assets into Low, Medium, High risk

### Parallel Computation
- Multithreaded processing for faster analysis

### Portfolio Allocation
- Risk-based investment allocation
- Supports Low, Medium, High risk strategies

### Machine Learning Prediction
- Linear Regression model
- Predicts next 7-day price trend

### Dashboard (Frontend)
- Portfolio visualization
- Risk charts
- Market trends
- Prediction output
- PDF reports

### Database & Authentication
- SQLite database with WAL mode
- Thread-safe operations
- OTP-based login system
- SHA-256 password hashing

### Notifications System
- Email alerts
- OTP verification
- PDF report generation

---

## 📊 Key Features

✔ Real-time crypto analysis  
✔ Risk classification system  
✔ Portfolio optimization  
✔ Multithreaded computation  
✔ Machine learning predictions  
✔ Secure authentication  
✔ Email alerts  
✔ PDF reporting  
✔ Interactive dashboard  

---

## 🛠️ Tech Stack

Language: Python  
Data: Pandas, NumPy  
Visualization: Plotly, Matplotlib  
Machine Learning: Scikit-learn  
Frontend: Streamlit  
Database: SQLite  
APIs: CoinGecko, Yahoo Finance  

---

## ▶️ How to Run

Step 1: Clone repository
git clone https://github.com/your-username/crypto-portfolio-manager.git
cd crypto-portfolio-manager

Step 2: Create virtual environment
python -m venv venv

Activate:
Windows → venv\Scripts\activate  
Mac/Linux → source venv/bin/activate  

Step 3: Install dependencies
pip install -r requirements.txt

Step 4: Setup environment variables
copy .env.example .env

Add credentials:
EMAIL_USER=your-email@gmail.com  
EMAIL_PASS=your-app-password  

Step 5: Run data pipeline
python core/collect_data.py  
python core/fetch_historical.py  

Step 6: Launch dashboard
streamlit run app.py  

---

## 🔐 Environment Variables

EMAIL_USER → Sender email  
EMAIL_PASS → App password  
SMTP_SERVER → SMTP server  
SMTP_PORT → Port number  

Note: .env file is not uploaded to GitHub for security.

---

## 📈 Data Flow

API → CSV/Database → Risk Engine → Parallel Compute → Portfolio Allocation → ML Prediction → Dashboard

---

## 💡 Features Implemented

- OTP Authentication  
- Secure password hashing  
- API data integration  
- Historical analysis  
- Risk engine  
- Portfolio allocation  
- ML prediction  
- Email alerts  
- PDF reports  

---

## 🚀 Future Enhancements

- Sharpe Ratio  
- Monte Carlo Simulation  
- Real-time data streaming  
- Cloud deployment  
- REST API  
- Advanced ML models  

---

## 📚 Project Scope

This project demonstrates:

- Data engineering  
- Financial analytics  
- Risk modeling  
- Parallel computing  
- Portfolio optimization  
- Dashboard development  
- Machine learning  

---

## 👩‍💻 Author

Aanya Badgaiyan  

---

## ⚖️ License

This project is licensed under the MIT License.

---

## ⭐ Final Note

This project simulates a real-world crypto investment platform combining analytics, AI, and visualization into one system.
