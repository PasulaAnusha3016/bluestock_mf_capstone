# Data Dictionary

## 01_fund_master.csv

### amfi_code

Type: Integer
Definition: Unique AMFI scheme identifier.

### fund_house

Type: Text
Definition: Mutual fund company managing the scheme.

### scheme_name

Type: Text
Definition: Name of the mutual fund scheme.

### category

Type: Text
Definition: Mutual fund category.

### risk_category

Type: Text
Definition: Risk classification of the scheme.

---

## 02_nav_history.csv

### date

Type: Date
Definition: NAV reporting date.

### nav

Type: Decimal
Definition: Net Asset Value of the scheme.

---

## 08_investor_transactions.csv

### transaction_type

Type: Text
Definition: SIP, Lumpsum, or Redemption.

### amount_inr

Type: Decimal
Definition: Transaction amount in Indian Rupees.

### kyc_status

Type: Text
Definition: Investor KYC verification status.

---

## 07_scheme_performance.csv

### return_1yr_pct

Type: Decimal
Definition: One-year return percentage.

### return_3yr_pct

Type: Decimal
Definition: Three-year return percentage.

### return_5yr_pct

Type: Decimal
Definition: Five-year return percentage.

### expense_ratio_pct

Type: Decimal
Definition: Annual expense ratio charged by the fund.
