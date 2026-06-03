import pandas as pd

df = pd.read_csv("data/raw/02_nav_history.csv")

# Convert date column
df["date"] = pd.to_datetime(df["date"])

# Sort by fund and date
df = df.sort_values(
    ["amfi_code", "date"]
)

# Forward fill NAV values
df["nav"] = (
    df.groupby("amfi_code")["nav"]
    .ffill()
)

# Keep only valid NAVs
df = df[df["nav"] > 0]

# Remove duplicates
df = df.drop_duplicates()

# Save cleaned file
df.to_csv(
    "data/processed/nav_history_clean.csv",
    index=False
)

print("NAV History cleaned successfully")