# Day 1 Data Quality Summary

Datasets Loaded:
- 01_fund_master.csv
- 02_nav_history.csv
- 03_aum_by_fund_house.csv
- 04_monthly_sip_inflows.csv
- 05_category_inflows.csv
- 06_industry_folio_count.csv
- 07_scheme_performance.csv
- 08_investor_transactions.csv
- 09_portfolio_holdings.csv
- 10_benchmark_indices.csv

Fund Master:
- Shape: (40,15)
- AMFI codes available
- Fund houses identified
- Categories identified
- Risk categories identified

AMFI Validation:
- Compared amfi_code between fund_master and nav_history
- Validation completed

Live NAV:
- HDFC Top 100 Direct fetched from MFAPI

Additional NAV Data:
- SBI Bluechip
- ICICI Bluechip
- Nippon Large Cap
- Axis Bluechip
- Kotak Bluechip