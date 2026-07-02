# Mutual Fund Analytics - Data Dictionary

## Overview

This document describes the datasets used in the Mutual Fund Analytics project, including column names, data types, business definitions, and data sources.

---

# 01_fund_master.csv

| Column | Data Type | Description |
|---------|-----------|-------------|
| amfi_code | Integer | Unique AMFI scheme code |
| fund_house | Text | Asset Management Company (AMC) |
| scheme_name | Text | Mutual fund scheme name |
| category | Text | Fund category |
| sub_category | Text | Fund sub-category |
| risk_category | Text | Risk classification |

Source: AMFI Master Data

---

# 02_nav_history.csv

| Column | Data Type | Description |
|---------|-----------|-------------|
| amfi_code | Integer | Mutual fund scheme code |
| date | Date | NAV date |
| nav | Float | Net Asset Value |

Source: Historical NAV Dataset

---

# 03_aum_by_fund_house.csv

| Column | Data Type | Description |
|---------|-----------|-------------|
| month | Date | Reporting month |
| fund_house | Text | AMC name |
| aum_crore | Float | Assets Under Management (Crores) |

Source: AUM Dataset

---

# 04_monthly_sip_inflows.csv

| Column | Data Type | Description |
|---------|-----------|-------------|
| month | Date | Reporting month |
| sip_inflow_crore | Float | Monthly SIP inflow |
| active_sip_accounts_crore | Float | Active SIP accounts |
| new_sip_accounts_lakh | Float | Newly registered SIP accounts |
| sip_aum_lakh_crore | Float | SIP Assets Under Management |
| yoy_growth_pct | Float | Year-over-Year growth percentage |

Source: SIP Dataset

---

# 05_category_inflows.csv

| Column | Data Type | Description |
|---------|-----------|-------------|
| month | Date | Reporting month |
| category | Text | Mutual fund category |
| net_inflow_crore | Float | Net inflow in crores |

Source: Category Inflows Dataset

---

# 06_industry_folio_count.csv

| Column | Data Type | Description |
|---------|-----------|-------------|
| month | Date | Reporting month |
| total_folios_crore | Float | Total folios |
| equity_folios_crore | Float | Equity folios |
| debt_folios_crore | Float | Debt folios |
| hybrid_folios_crore | Float | Hybrid folios |
| others_folios_crore | Float | Other folios |

Source: Industry Folio Dataset

---

# 07_scheme_performance.csv

| Column | Data Type | Description |
|---------|-----------|-------------|
| amfi_code | Integer | Mutual fund code |
| scheme_name | Text | Scheme name |
| return_1yr_pct | Float | 1-Year Return |
| return_3yr_pct | Float | 3-Year Return |
| return_5yr_pct | Float | 5-Year Return |
| expense_ratio_pct | Float | Expense ratio |
| aum_crore | Float | Assets Under Management |
| risk_grade | Text | Risk category |

Source: Scheme Performance Dataset

---

# 08_investor_transactions.csv

| Column | Data Type | Description |
|---------|-----------|-------------|
| investor_id | Text | Investor identifier |
| transaction_date | Date | Transaction date |
| amfi_code | Integer | Scheme code |
| transaction_type | Text | SIP / Lumpsum / Redemption |
| amount_inr | Float | Transaction amount |
| state | Text | Investor state |
| city | Text | Investor city |
| payment_mode | Text | Payment mode |
| kyc_status | Text | KYC verification status |

Source: Investor Transactions Dataset

---

# 09_portfolio_holdings.csv

| Column | Data Type | Description |
|---------|-----------|-------------|
| amfi_code | Integer | Scheme code |
| stock_symbol | Text | Stock symbol |
| stock_name | Text | Company name |
| sector | Text | Industry sector |
| weight_pct | Float | Portfolio weight |
| market_value_cr | Float | Market value |
| current_price_inr | Float | Current stock price |
| portfolio_date | Date | Portfolio reporting date |

Source: Portfolio Holdings Dataset

---

# 10_benchmark_indices.csv

| Column | Data Type | Description |
|---------|-----------|-------------|
| date | Date | Trading date |
| index_name | Text | Benchmark index |
| close_value | Float | Closing value |

Source: Benchmark Index Dataset
