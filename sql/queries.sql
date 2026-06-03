-- 1. Top 5 funds by AUM
SELECT scheme_name, aum_crore
FROM fact_performance
ORDER BY aum_crore DESC
LIMIT 5;

-- 2. Average NAV
SELECT AVG(nav) AS avg_nav
FROM fact_nav;

-- 3. Transaction count by type
SELECT transaction_type, COUNT(*)
FROM fact_transactions
GROUP BY transaction_type;

-- 4. Funds with expense ratio below 1%
SELECT scheme_name, expense_ratio_pct
FROM fact_performance
WHERE expense_ratio_pct < 1;

-- 5. Total transaction amount
SELECT SUM(amount_inr)
FROM fact_transactions;

-- 6. Average NAV by fund
SELECT amfi_code, AVG(nav)
FROM fact_nav
GROUP BY amfi_code;

-- 7. Fund count by fund house
SELECT fund_house, COUNT(*)
FROM dim_fund
GROUP BY fund_house;

-- 8. Risk category distribution
SELECT risk_category, COUNT(*)
FROM dim_fund
GROUP BY risk_category;

-- 9. Average 3-year return
SELECT AVG(return_3yr_pct)
FROM fact_performance;

-- 10. Top performing funds by 5-year return
SELECT scheme_name, return_5yr_pct
FROM fact_performance
ORDER BY return_5yr_pct DESC
LIMIT 5;