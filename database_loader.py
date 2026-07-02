import sqlite3
import pandas as pd
import os
from sqlalchemy import create_engine

print("=" * 70)
print("CREATING SQLITE DATABASE")
print("=" * 70)

# ==========================================================
# Delete old database if it exists
# ==========================================================

if os.path.exists("bluestock_mf.db"):
    os.remove("bluestock_mf.db")
    print("Old database removed.")

# ==========================================================
# Create SQLite Database
# ==========================================================

conn = sqlite3.connect("bluestock_mf.db")
cursor = conn.cursor()

print("Database created successfully.")

# ==========================================================
# Read schema.sql
# ==========================================================

with open("sql/schema.sql", "r") as file:
    schema = file.read()

# ==========================================================
# Execute SQL Schema
# ==========================================================

cursor.executescript(schema)

conn.commit()

print("All tables created successfully.")

# ==========================================================
# Verify Tables
# ==========================================================

cursor.execute("""
SELECT name
FROM sqlite_master
WHERE type='table';
""")

tables = cursor.fetchall()

print("\nTables Created:")
print("-" * 30)

for table in tables:
    print(table[0])

# ==========================================================
# Close SQLite Connection
# ==========================================================

conn.close()

# ==========================================================
# Load Cleaned CSVs into SQLite using SQLAlchemy
# ==========================================================

print("\n" + "=" * 70)
print("LOADING CLEANED DATASETS")
print("=" * 70)

engine = create_engine("sqlite:///bluestock_mf.db")

processed_path = "data/processed"

files = [
    "01_fund_master.csv",
    "02_nav_history.csv",
    "03_aum_by_fund_house.csv",
    "04_monthly_sip_inflows.csv",
    "05_category_inflows.csv",
    "06_industry_folio_count.csv",
    "07_scheme_performance.csv",
    "08_investor_transactions.csv",
    "09_portfolio_holdings.csv",
    "10_benchmark_indices.csv"
]

for file in files:

    df = pd.read_csv(os.path.join(processed_path, file))

    table_name = file.replace(".csv", "")

    df.to_sql(
        table_name,
        engine,
        if_exists="replace",
        index=False
    )

    print(f"✓ {table_name} loaded ({len(df)} rows)")

# ==========================================================
# Verify Row Counts
# ==========================================================

print("\n" + "=" * 70)
print("VERIFYING ROW COUNTS")
print("=" * 70)

for file in files:

    df = pd.read_csv(os.path.join(processed_path, file))

    table = file.replace(".csv", "")

    rows = pd.read_sql(
        f"SELECT COUNT(*) AS total FROM '{table}'",
        engine
    )

    print(f"{table}: Source={len(df)} | Database={rows.iloc[0, 0]}")

print("\n" + "=" * 70)
print("DATABASE SETUP COMPLETED SUCCESSFULLY")
print("=" * 70)
