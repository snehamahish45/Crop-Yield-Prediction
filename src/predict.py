import joblib
import pandas as pd

# =====================================
# Load Saved Model
# =====================================

model = joblib.load("models/best_model.pkl")

# Load Encoders
area_encoder = joblib.load("models/area_encoder.pkl")
item_encoder = joblib.load("models/item_encoder.pkl")

print("=" * 60)
print("Crop Yield Prediction System")
print("=" * 60)

# =====================================
# User Input
# =====================================

df = pd.read_csv("data/yield_df.csv")

print("\nAvailable Areas:")
print(", ".join(sorted(df["Area"].unique())[:20]))
print("...")

print("\nAvailable Crops:")
print(", ".join(sorted(df["Item"].unique())[:20]))
print("...")

area = input("\nEnter Area exactly as shown: ").strip()
item = input("Enter Crop exactly as shown: ").strip()

year = int(input("Enter Year: "))
rainfall = float(input("Average Rainfall (mm/year): "))
pesticides = float(input("Pesticides Used (tonnes): "))
temperature = float(input("Average Temperature (°C): "))

# =====================================
# Encode Categorical Variables
# =====================================

try:
    area_encoded = area_encoder.transform([area])[0]
    item_encoded = item_encoder.transform([item])[0]
except ValueError:
    print("\nError: Area or Crop not found in training dataset.")
    exit()

# =====================================
# Create Input DataFrame
# =====================================

input_data = pd.DataFrame({
    "Area": [area_encoded],
    "Item": [item_encoded],
    "Year": [year],
    "average_rain_fall_mm_per_year": [rainfall],
    "pesticides_tonnes": [pesticides],
    "avg_temp": [temperature]
})

# =====================================
# Predict
# =====================================

prediction = model.predict(input_data)

print("\n" + "=" * 60)
print(f"Predicted Crop Yield : {prediction[0]:.2f} hg/ha")
print("=" * 60)