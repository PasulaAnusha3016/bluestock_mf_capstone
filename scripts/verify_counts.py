import pandas as pd

print("Fund Master Rows:",
      len(pd.read_csv("data/raw/01_fund_master.csv")))

print("NAV Rows:",
      len(pd.read_csv("data/processed/nav_history_clean.csv")))

print("Transaction Rows:",
      len(pd.read_csv("data/processed/investor_transactions_clean.csv")))

print("Performance Rows:",
      len(pd.read_csv("data/processed/scheme_performance_clean.csv")))