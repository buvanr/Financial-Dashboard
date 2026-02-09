import pandas as pd
import numpy as np

# Generating 365 Days of sample data
dates = pd.date_range(start="2024-01-01", periods=12, freq='M')
rent = 25000

# Simulating the financial values
data = {
    "Date": dates,
    "Revenue": np.random.randint(500000, 1000000, size=12),
    "Salary Payments": np.random.randint(500000, 700000, size=12),
    "Rent": rent,
    "Debt": np.random.randint(10000, 25000, size=12),
    "Miscellaneous Costs": np.random.randint(5000, 7500, size=12)
}

df = pd.DataFrame(data)
df["Profit"] = df["Revenue"] - df["Salary Payments"] - df["Rent"] - df["Debt"] - df["Miscellaneous Costs"]

# Save to CSV
df.to_csv("data/sample_data.csv", index=False)

print("Sample data saved to 'Data/Sample_data.csv'")