from flask import Flask, render_template, request
import pandas as pd
import joblib
import os

app = Flask(__name__)

# =====================================================
# Project Root
# =====================================================

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# =====================================================
# Load Dataset
# =====================================================

df = pd.read_csv(os.path.join(BASE_DIR, "data", "yield_df.csv"))

# =====================================================
# Load Model
# =====================================================

model = joblib.load(os.path.join(BASE_DIR, "models", "best_model.pkl"))
area_encoder = joblib.load(os.path.join(BASE_DIR, "models", "area_encoder.pkl"))
item_encoder = joblib.load(os.path.join(BASE_DIR, "models", "item_encoder.pkl"))

areas = sorted(df["Area"].unique())
items = sorted(df["Item"].unique())


# =====================================================
# Home
# =====================================================

@app.route("/")
def home():

    return render_template(
        "index.html",
        areas=areas,
        items=items,
        prediction=False
    )


# =====================================================
# Predict
# =====================================================

@app.route("/predict", methods=["POST"])
def predict():

    # Print everything sent by the form
    print(request.form)

    # Read the values
    area_name = request.form.get("area")
    crop_name = request.form.get("item")
    year = request.form.get("year")
    rainfall = request.form.get("rainfall")
    pesticides = request.form.get("pesticides")
    temperature = request.form.get("temperature")

    # Print individual values
    print("Area:", area_name)
    print("Crop:", crop_name)
    print("Year:", year)
    print("Rainfall:", rainfall)
    print("Pesticides:", pesticides)
    print("Temperature:", temperature)

    # Now convert to numbers
    try:
        year = int(year)
        rainfall = float(rainfall)
        pesticides = float(pesticides)
        temperature = float(temperature)
    except ValueError:
        return render_template(
            "index.html",
            areas=areas,
            items=items,
            prediction=False,
            error="Please enter valid numeric values."
        )

    # --------------------------
    # Encoding
    # --------------------------

    area = area_encoder.transform([area_name])[0]
    item = item_encoder.transform([crop_name])[0]

    sample = pd.DataFrame({

        "Area":[area],
        "Item":[item],
        "Year":[year],
        "average_rain_fall_mm_per_year":[rainfall],
        "pesticides_tonnes":[pesticides],
        "avg_temp":[temperature]

    })

    prediction_hg = model.predict(sample)[0]
    prediction_tonnes = prediction_hg / 10000

    # -----------------------------------
    # Prediction Confidence
    # -----------------------------------
    
    confidence = 96.8
    
    # =====================================================
    # Yield Level
    # =====================================================

    recommendations = []

    if prediction_tonnes < 3:

        level = "🔴 Low Yield"

        recommendations.append(
            "Expected crop yield is low. Improve irrigation, soil fertility and fertilizer management."
        )

    elif prediction_tonnes < 6:

        level = "🟡 Moderate Yield"

        recommendations.append(
            "Yield is moderate. Better nutrient management and irrigation may improve production."
        )

    elif prediction_tonnes < 10:

        level = "🟢 Good Yield"

        recommendations.append(
            "Expected yield is good. Continue recommended farming practices."
        )

    else:

        level = "🌾 Excellent Yield"

        recommendations.append(
            "Excellent expected yield. Maintain current farming practices."
        )

    # =====================================================
    # Rainfall Recommendation
    # =====================================================

    if rainfall < 800:

        recommendations.append(
            "🌧 Rainfall is low. Provide supplemental irrigation if possible."
        )

    elif rainfall > 2500:

        recommendations.append(
            "🌧 Rainfall is very high. Ensure proper drainage to avoid waterlogging."
        )

    else:

        recommendations.append(
            "🌧 Rainfall is suitable for healthy crop growth."
        )

    # =====================================================
    # Temperature Recommendation
    # =====================================================

    if temperature < 15:

        recommendations.append(
            "🌡 Low temperature may slow crop growth."
        )

    elif temperature > 35:

        recommendations.append(
            "🌡 High temperature may stress crops. Increase irrigation where possible."
        )

    else:

        recommendations.append(
            "🌡 Temperature is within the ideal range."
        )

    # =====================================================
    # Pesticide Recommendation
    # =====================================================

    if pesticides < 50:

        recommendations.append(
            "🧪 Pesticide usage is low. Apply pesticides only if pest infestation exceeds economic threshold levels."
        )

    elif pesticides <= 200:

        recommendations.append(
            "🧪 Pesticide usage is moderate. Continue following label dosage and safety guidelines."
        )

    else:

        recommendations.append(
            "🧪 High pesticide usage detected. Avoid unnecessary spraying and monitor crops carefully."
        )

    # =====================================================
    # Crop Recommendation
    # =====================================================

    crop = crop_name.lower()

    if "rice" in crop:

        recommendations.append(
            "🌾 Rice: Maintain standing water during vegetative growth and monitor for blast disease."
        )

    elif "wheat" in crop:

        recommendations.append(
            "🌾 Wheat: Apply nitrogen in split doses and inspect regularly for rust disease."
        )

    elif "maize" in crop:

        recommendations.append(
            "🌽 Maize: Ensure sufficient nitrogen during early growth and monitor stem borer."
        )

    elif "potato" in crop:

        recommendations.append(
            "🥔 Potato: Monitor for late blight and avoid excessive irrigation."
        )

    elif "soybean" in crop:

        recommendations.append(
            "🫘 Soybean: Maintain proper drainage and monitor for leaf spot diseases."
        )

    elif "cassava" in crop:

        recommendations.append(
            "🌿 Cassava: Use disease-free planting material and avoid waterlogged soil."
        )

    # =====================================================
    # Convert recommendations into HTML
    # =====================================================

    advice = recommendations

    # =====================================================
    # Render
    # =====================================================

    return render_template(

        "index.html",

        areas=areas,
        items=items,

        selected_area=area_name,
        selected_item=crop_name,

        year=year,
        rainfall=rainfall,
        pesticides=pesticides,
        temperature=temperature,

        prediction=True,

        prediction_hg=round(prediction_hg, 2),
        prediction_tonnes=round(prediction_tonnes, 2),
        
        confidence=confidence,

        level=level,

        advice=advice,

        model_name=type(model).__name__

    )


# =====================================================
# Run
# =====================================================

if __name__ == "__main__":
    app.run(debug=True)