import pandas as pd

df = pd.read_csv("data/yield_df.csv")

print("===== Available Areas =====")
print(sorted(df["Area"].unique()))

print("\n===== Available Crops =====")
print(sorted(df["Item"].unique()))