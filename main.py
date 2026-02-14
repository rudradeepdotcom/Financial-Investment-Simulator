import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Define the ticker (Nifty 50 is ^NSEI)
ticker = "^NSEI"

# 2. Download 5 years of data
print("Downloading market data...")
market_data = yf.download(ticker, start="2021-01-01", end="2026-02-15")

# 3. Save it so you don't have to download it again
market_data.to_csv("nifty_50_historical.csv")
print("Success! Market data saved as nifty_50_historical.csv")

# 4. Look at the first few rows
print(market_data.head())

# Load your downloaded CSV
df = pd.read_csv(r"C:\Users\rmcsi\Desktop\Finance_Project\my_spending.csv")

# 1. See the 'Health Report' of your data
print("--- Data Info ---")
print(df.info()) # Shows data types and missing values

# 2. Check for missing values
print("\n--- Missing Values ---")
print(df.isnull().sum())

# 1. Fix Dates: Convert 'Date' column from a string to a proper Python Date object
df['date'] = pd.to_datetime(df['date'])

# 2. Handle Missing Values: 
# If 'Amount' is missing, we fill it with the average (Mean)
df['monthly_expense_total'] = df['monthly_expense_total'].fillna(df['monthly_expense_total'].mean())

# 3. Standardize Categories: Make sure 'food', 'Food', and 'FOOD' are treated as the same
df['category'] = df['category'].str.lower().str.strip()

# 1. Calculate the 'Normal' range for spending
Q1 = df['monthly_expense_total'].quantile(0.25) # The 25th percentile
Q3 = df['monthly_expense_total'].quantile(0.75) # The 75th percentile
IQR = Q3 - Q1

lower_limit = Q1 - 1.5 * IQR
upper_limit = Q3 + 1.5 * IQR

# 2. Flag the "Anomalies" (Transactions outside the normal range)
anomalies = df[(df['monthly_expense_total'] < lower_limit) | (df['monthly_expense_total'] > upper_limit)]
print(f"\nDetected {len(anomalies)} suspicious expense records!")
print(anomalies[['date', 'category', 'monthly_expense_total']].head())

df.to_csv("cleaned_spending.csv", index=False)
print("\nPhase 2 Complete: Cleaned data saved as 'cleaned_spending.csv'")


# Let's take the first user's data for a 12-month simulation
user_data = df[df['user_id'] == 1001].sort_values('date').head(12)

# Parameters
initial_investment = 0
fd_rate = 0.07 / 12  # Monthly FD rate

# Tracking variables
fd_wealth = [initial_investment]
market_wealth = [initial_investment]

# Loop through months
for i, row in user_data.iterrows():
    investment = row['actual_savings']
    
    # 1. FD Calculation
    new_fd_val = (fd_wealth[-1] + investment) * (1 + fd_rate)
    fd_wealth.append(new_fd_val)
    
    # 2. Market Calculation (Simplified for the 'noob' phase)
    # We assume a 1% monthly market growth for now
    new_market_val = (market_wealth[-1] + investment) * (1.01) 
    market_wealth.append(new_market_val)

print(f"Final FD Wealth: {fd_wealth[-1]:.2f}")
print(f"Final Market Wealth: {market_wealth[-1]:.2f}")

# 1. Set the visual style (makes it look professional)
sns.set_theme(style="whitegrid")
plt.figure(figsize=(12, 6))

# 2. Plot the two wealth paths
plt.plot(fd_wealth, label='Fixed Deposit (7%)', color='#2ecc71', linewidth=3, marker='o')
plt.plot(market_wealth, label='Market Strategy (12%)', color='#3498db', linewidth=3, marker='s')

# 3. Add labels and Title (The "Story")
plt.title('Investment Growth Comparison: FD vs. Market Strategy', fontsize=16, fontweight='bold')
plt.xlabel('Months', fontsize=12)
plt.ylabel('Wealth Amount (₹)', fontsize=12)
plt.legend()

# 4. Save the plot for your portfolio
plt.savefig('investment_growth_comparison.png', dpi=300)
print("Phase 4 Complete: Visualization saved as 'investment_growth_comparison.png'")
plt.show()