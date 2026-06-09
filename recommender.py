import pandas as pd

df = pd.read_csv(
    "data/processed/scheme_performance_clean.csv"
)

risk = input("Enter Risk (Low/Moderate/High): ")

result = df[
    df['risk_grade'].str.lower()
    ==
    risk.lower()
]

result = result.sort_values(
    'sharpe_ratio',
    ascending=False
)

print(
    result[
        [
            'scheme_name',
            'fund_house',
            'sharpe_ratio',
            'risk_grade'
        ]
    ].head(3)
)