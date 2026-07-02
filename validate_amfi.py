import pandas as pd

print("=" * 70)
print("AMFI CODE VALIDATION")
print("=" * 70)

# Load datasets
fund_master = pd.read_csv("data/raw/01_fund_master.csv")
nav_history = pd.read_csv("data/raw/02_nav_history.csv")

# Unique AMFI codes
fund_codes = set(fund_master["amfi_code"])
nav_codes = set(nav_history["amfi_code"])

# Find missing codes
missing_codes = fund_codes - nav_codes

print(f"\nFund Master AMFI Codes : {len(fund_codes)}")
print(f"NAV History AMFI Codes : {len(nav_codes)}")
print(f"Missing Codes          : {len(missing_codes)}")

if len(missing_codes) == 0:
    print("\n✅ All AMFI codes from Fund Master exist in NAV History.")
else:
    print("\n❌ Missing AMFI Codes:")
    for code in sorted(missing_codes):
        print(code)
        