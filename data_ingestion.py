import os
import pandas as pd

# Path to raw data folder
DATA_PATH = "data/raw"

# Get all CSV files
csv_files = [f for f in os.listdir(DATA_PATH) if f.endswith(".csv")]

print("=" * 80)
print("MUTUAL FUND ANALYTICS - DATA INGESTION")
print("=" * 80)

for file in csv_files:

    print("\n" + "=" * 80)
    print(f"Dataset : {file}")
    print("=" * 80)

    df = pd.read_csv(os.path.join(DATA_PATH, file))

    print("\nShape")
    print(df.shape)

    print("\nData Types")
    print(df.dtypes)

    print("\nFirst 5 Rows")
    print(df.head())

    print("\nMissing Values")
    print(df.isnull().sum())

print("\n")
print("=" * 80)
print("All datasets loaded successfully.")
print("=" * 80)
print("\n")
print("="*80)
print("FUND MASTER EXPLORATION")
print("="*80)

fund_master = pd.read_csv("data/raw/01_fund_master.csv")

print("\nUnique Fund Houses")
print(fund_master["fund_house"].unique())

print("\nCategories")
print(fund_master["category"].unique())

print("\nSub Categories")
print(fund_master["sub_category"].unique())

print("\nRisk Categories")
print(fund_master["risk_category"].unique())
