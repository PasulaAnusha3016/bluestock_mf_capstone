print("Running ETL Pipeline...")

exec(open("scripts/clean_nav_history.py").read())
exec(open("scripts/clean_investor_transactions.py").read())
exec(open("scripts/clean_scheme_performance.py").read())

print("ETL Completed Successfully")