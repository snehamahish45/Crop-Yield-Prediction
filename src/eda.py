import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Create outputs folder if it doesn't exist
os.makedirs("outputs", exist_ok=True)

# Load cleaned dataset
df = pd.read_csv("data/yield_df.csv")

print("="*60)
print("Dataset Loaded Successfully")
print("="*60)

print(df.head())

# ----------------------------
# Dataset Information
# ----------------------------

print("\nShape:", df.shape)

print("\nColumns:")
print(df.columns.tolist())

print("\nStatistics:")
print(df.describe())

# ----------------------------
# Missing Values
# ----------------------------

print("\nMissing Values")
print(df.isnull().sum())

# ----------------------------
# Correlation Heatmap
# ----------------------------

plt.figure(figsize=(10,7))

numeric_df = df.select_dtypes(include=['int64','float64'])

sns.heatmap(numeric_df.corr(),
            annot=True,
            cmap="YlGnBu")

plt.title("Correlation Heatmap")
plt.tight_layout()

plt.savefig("outputs/correlation_heatmap.png")
plt.show()

# ----------------------------
# Yield Distribution
# ----------------------------

plt.figure(figsize=(8,5))

sns.histplot(df["hg/ha_yield"],
             bins=30,
             kde=True)

plt.title("Yield Distribution")

plt.savefig("outputs/yield_distribution.png")
plt.show()

# ----------------------------
# Rainfall vs Yield
# ----------------------------

plt.figure(figsize=(8,5))

sns.scatterplot(
    x="average_rain_fall_mm_per_year",
    y="hg/ha_yield",
    data=df
)

plt.title("Rainfall vs Yield")

plt.savefig("outputs/rainfall_vs_yield.png")

plt.show()

# ----------------------------
# Temperature vs Yield
# ----------------------------

plt.figure(figsize=(8,5))

sns.scatterplot(
    x="avg_temp",
    y="hg/ha_yield",
    data=df
)

plt.title("Temperature vs Yield")

plt.savefig("outputs/temp_vs_yield.png")

plt.show()

# ----------------------------
# Pesticides vs Yield
# ----------------------------

plt.figure(figsize=(8,5))

sns.scatterplot(
    x="pesticides_tonnes",
    y="hg/ha_yield",
    data=df
)

plt.title("Pesticides vs Yield")

plt.savefig("outputs/pesticides_vs_yield.png")

plt.show()

print("\nEDA Completed Successfully!")
print("Graphs saved in outputs folder.")