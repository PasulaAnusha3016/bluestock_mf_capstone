import pandas as pd
from pathlib import Path

raw_path = Path("data/raw")
processed_path = Path("data/processed")

files = [
    "01_fund_master.csv",
    "03_aum_by_fund_house.csv",
    "04_monthly_sip_inflows.csv",
    "05_category_inflows.csv",
    "06_industry_folio_count.csv",
    "09_portfolio_holdings.csv",
    "10_benchmark_indices.csv"
]

for file in files:
    df = pd.read_csv(raw_path / file)

    # Basic cleaning
    df = df.drop_duplicates()

    output_file = file.replace(".csv", "_clean.csv")

    df.to_csv(
        processed_path / output_file,
        index=False
    )

    print(f"Saved: {output_file}")

print("All files cleaned successfully!")