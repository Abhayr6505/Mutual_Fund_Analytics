import pandas as pd
import os

RAW = "data/raw"
PROCESSED = "data/processed"

os.makedirs(PROCESSED, exist_ok=True)

print("=" * 70)
print("Cleaning benchmark_indices.csv")
print("=" * 70)

benchmark = pd.read_csv(
    os.path.join(RAW, "10_benchmark_indices.csv")
)

# Convert date column
benchmark["date"] = pd.to_datetime(benchmark["date"])

# Sort by index and date
benchmark = benchmark.sort_values(
    ["index_name", "date"]
)

# Remove duplicate rows
before = len(benchmark)
benchmark = benchmark.drop_duplicates()

duplicates = before - len(benchmark)

# Keep only valid close values
benchmark = benchmark[
    benchmark["close_value"] > 0
]

# Forward-fill missing close values
benchmark["close_value"] = benchmark.groupby(
    "index_name"
)["close_value"].ffill()

# Save cleaned file
benchmark.to_csv(
    os.path.join(PROCESSED, "10_benchmark_indices.csv"),
    index=False
)

print("Duplicate Rows Removed :", duplicates)
print("Final Rows :", len(benchmark))

print("\n✅ benchmark_indices.csv cleaned successfully.")
