import pandas as pd

df = pd.read_csv("data/raw/08_investor_transactions.csv")

# Convert date
df["transaction_date"] = pd.to_datetime(
    df["transaction_date"],
    errors="coerce"
)

# Standardize transaction type
df["transaction_type"] = (
    df["transaction_type"]
    .astype(str)
    .str.upper()
    .str.strip()
)

# Keep valid transaction types
valid_types = ["SIP", "LUMPSUM", "REDEMPTION"]

df = df[
    df["transaction_type"].isin(valid_types)
]

# Amount must be positive
df = df[df["amount_inr"] > 0]

# Standardize KYC status
df["kyc_status"] = (
    df["kyc_status"]
    .astype(str)
    .str.upper()
    .str.strip()
)

print("Unique KYC Values:")
print(df["kyc_status"].unique())

# Remove duplicates
df = df.drop_duplicates()

# Save cleaned file
df.to_csv(
    "data/processed/investor_transactions_clean.csv",
    index=False
)

print("Cleaned file saved successfully")