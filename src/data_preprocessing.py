import pandas as pd

# Load dataset
df = pd.read_csv("data/yield_df.csv")

print("=" * 50)
print("Dataset Loaded Successfully")
print("=" * 50)

print("\nFirst 5 Rows")
print(df.head())

print("\nDataset Shape")
print(df.shape)

print("\nColumn Names")
print(df.columns)

print("\nInformation")
print(df.info())

print("\nMissing Values")
print(df.isnull().sum())

# Remove duplicate rows
df.drop_duplicates(inplace=True)

# Fill numerical missing values
numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns
df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())

print("\nDataset Shape After Cleaning")
print(df.shape)

# Save cleaned dataset
df.to_csv("data/cleaned_yield.csv", index=False)

print("\nCleaned dataset saved successfully.")