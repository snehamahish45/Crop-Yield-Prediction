import pandas as pd
import joblib
import os

from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

# ----------------------------------
# Create models folder
# ----------------------------------

os.makedirs("models", exist_ok=True)

# ----------------------------------
# Load Dataset
# ----------------------------------

df = pd.read_csv("data/yield_df.csv")

print("=" * 60)
print("Feature Engineering Started")
print("=" * 60)

# ----------------------------------
# Label Encoding
# ----------------------------------

area_encoder = LabelEncoder()
item_encoder = LabelEncoder()

df["Area"] = area_encoder.fit_transform(df["Area"])
df["Item"] = item_encoder.fit_transform(df["Item"])

# Save Encoders

joblib.dump(area_encoder, "models/area_encoder.pkl")
joblib.dump(item_encoder, "models/item_encoder.pkl")

print("\nLabel Encoding Completed")

# ----------------------------------
# Features and Target
# ----------------------------------

X = df[[
    "Area",
    "Item",
    "Year",
    "average_rain_fall_mm_per_year",
    "pesticides_tonnes",
    "avg_temp"
]]

y = df["hg/ha_yield"]

print("\nFeatures Selected")

print(X.head())

print("\nTarget")

print(y.head())

# ----------------------------------
# Train Test Split
# ----------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)

print("\nTrain Shape :", X_train.shape)
print("Test Shape  :", X_test.shape)

# ----------------------------------
# Save Processed Data
# ----------------------------------

joblib.dump(X_train, "models/X_train.pkl")
joblib.dump(X_test, "models/X_test.pkl")
joblib.dump(y_train, "models/y_train.pkl")
joblib.dump(y_test, "models/y_test.pkl")

print("\nProcessed data saved successfully.")

print("\nFeature Engineering Completed Successfully.")