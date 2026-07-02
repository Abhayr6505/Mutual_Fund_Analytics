-- =========================================================
-- 1. Top 5 Funds by AUM
-- =========================================================

SELECT
    scheme_name,
    fund_house,
    aum_crore
FROM 07_scheme_performance
ORDER BY aum_crore DESC
LIMIT 5;


-- =========================================================
-- 2. Average NAV per Month
-- =========================================================

SELECT
    substr(date,1,7) AS month,
    AVG(nav) AS average_nav
FROM 02_nav_history
GROUP BY month
ORDER BY month;


-- =========================================================
-- 3. Monthly SIP Inflow Trend
-- =========================================================

SELECT
    month,
    sip_inflow_crore
FROM 04_monthly_sip_inflows
ORDER BY month;


-- =========================================================
-- 4. Transactions by State
-- =========================================================

SELECT
    state,
    COUNT(*) AS total_transactions
FROM 08_investor_transactions
GROUP BY state
ORDER BY total_transactions DESC;


-- =========================================================
-- 5. Funds with Expense Ratio less than 1%
-- =========================================================

SELECT
    scheme_name,
    expense_ratio_pct
FROM 07_scheme_performance
WHERE expense_ratio_pct < 1
ORDER BY expense_ratio_pct;


-- =========================================================
-- 6. Average Returns by Fund House
-- =========================================================

SELECT
    fund_house,
    AVG(return_1yr_pct) AS avg_return_1yr
FROM 07_scheme_performance
GROUP BY fund_house
ORDER BY avg_return_1yr DESC;


-- =========================================================
-- 7. Risk Grade Distribution
-- =========================================================

SELECT
    risk_grade,
    COUNT(*) AS total_funds
FROM 07_scheme_performance
GROUP BY risk_grade;


-- =========================================================
-- 8. Top 10 Stocks by Market Value
-- =========================================================

SELECT
    stock_name,
    market_value_cr
FROM 09_portfolio_holdings
ORDER BY market_value_cr DESC
LIMIT 10;


-- =========================================================
-- 9. Benchmark Average Closing Value
-- =========================================================

SELECT
    index_name,
    AVG(close_value) AS average_close
FROM 10_benchmark_indices
GROUP BY index_name;


-- =========================================================
-- 10. Category-wise Monthly Inflows
-- =========================================================

SELECT
    category,
    SUM(net_inflow_crore) AS total_inflow
FROM 05_category_inflows
GROUP BY category
ORDER BY total_inflow DESC;

