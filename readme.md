# Financial Health & SIP Backtester 📈

## Project Overview
An end-to-end data pipeline built to analyze personal spending habits and simulate wealth growth using historical market data (Nifty 50).

## Tech Stack
- **Languages:** Python (Pandas, NumPy)
- **Database Logic:** Relational schema design (3NF)
- **Visualization:** Matplotlib, Seaborn
- **Data Source:** Kaggle (Personal Finance Tracker), Yahoo Finance API

## Features
1. **Automated ETL:** Cleans and standardizes raw financial CSVs.
2. **Anomaly Detection:** Identifies spending outliers using the IQR method.
3. **Backtesting:** Compares 7% Fixed Deposit returns vs. historical Market trends.

## Visual Results
![Investment Growth](outputs/investment_growth_comparison.png)

## How to Run
1. Clone the repo: `git clone https://github.com/yourusername/repo-name.git`
2. Install dependencies: `pip install -r requirements.txt`
3. Run `python main.py`