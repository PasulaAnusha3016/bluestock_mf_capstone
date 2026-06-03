import pandas as pd

df = pd.read_csv("data/raw/07_scheme_performance.csv")

# Convert return columns to numeric
return_cols = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct",
    "benchmark_3yr_pct",
    "alpha",
    "beta",
    "sharpe_ratio",
    "sortino_ratio",
    "std_dev_ann_pct",
    "max_drawdown_pct",
    "aum_crore",
    "expense_ratio_pct"
]

for col in return_cols:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# Flag invalid expense ratios
anomalies = df[
    ~df["expense_ratio_pct"].between(0.1, 2.5)
]

print("Expense Ratio Anomalies:")
print(anomalies[["amfi_code", "scheme_name", "expense_ratio_pct"]])

# Remove rows with invalid expense ratios
df = df[
    df["expense_ratio_pct"].between(0.1, 2.5)
]

# Remove duplicates
df = df.drop_duplicates()

# Save cleaned data
df.to_csv(
    "data/processed/scheme_performance_clean.csv",
    index=False
)

print("Scheme Performance cleaned successfully")