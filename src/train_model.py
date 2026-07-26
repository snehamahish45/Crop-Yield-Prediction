import os
import joblib
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

from xgboost import XGBRegressor

# ====================================
# Create folders
# ====================================

os.makedirs("models", exist_ok=True)
os.makedirs("outputs", exist_ok=True)

# ====================================
# Load Training Data
# ====================================

X_train = joblib.load("models/X_train.pkl")
X_test = joblib.load("models/X_test.pkl")
y_train = joblib.load("models/y_train.pkl")
y_test = joblib.load("models/y_test.pkl")

print("=" * 60)
print("Training Models")
print("=" * 60)

# ====================================
# Dictionary of Models
# ====================================

models = [
    ("Linear Regression", LinearRegression()),

    ("Random Forest", RandomForestRegressor(
        n_estimators=50,
        random_state=42
    )),

    ("XGBoost", XGBRegressor(
        objective="reg:squarederror",
        n_estimators=300,
        learning_rate=0.05,
        max_depth=8,
        random_state=42
    ))
]

results = {}

best_model = None
best_score = -999

# ====================================
# Train Models
# ====================================

for name, model in models:
    print("\n", "=" * 50)
    print(name)
    print("=" * 50)

    model.fit(X_train, y_train)

    prediction = model.predict(X_test)

    mae = mean_absolute_error(y_test, prediction)

    mse = mean_squared_error(y_test, prediction)
    rmse = np.sqrt(mse)

    r2 = r2_score(y_test, prediction)

    results[name] = {
        "MAE": mae,
        "RMSE": rmse,
        "R2": r2
    }

    print("MAE :", round(mae, 2))
    print("RMSE:", round(rmse, 2))
    print("R2  :", round(r2, 4))

    if r2 > best_score:
        best_score = r2
        best_model = model

# ====================================
# Save Best Model
# ====================================

joblib.dump(best_model, "models/best_model.pkl")

print("\n")
print("=" * 60)
print("Best Model Saved Successfully")
print("=" * 60)

# ====================================
# Results Table
# ====================================

results_df = pd.DataFrame(results).T

print("\nModel Comparison\n")
print(results_df)

results_df.to_csv(
    "outputs/model_results.csv"
)

# ====================================
# Model Comparison Graph
# ====================================

plt.figure(figsize=(8,5))

plt.bar(
    results_df.index,
    results_df["R2"]
)

plt.title("Model Comparison (R² Score)")
plt.ylabel("R² Score")

plt.tight_layout()

plt.savefig(
    "outputs/model_comparison.png"
)

plt.show()

# ====================================
# Feature Importance
# ====================================

if hasattr(best_model, "feature_importances_"):

    features = X_train.columns

    importance = best_model.feature_importances_

    importance_df = pd.DataFrame({

        "Feature": features,

        "Importance": importance

    })

    importance_df = importance_df.sort_values(
        by="Importance",
        ascending=False
    )

    print("\nFeature Importance\n")

    print(importance_df)

    plt.figure(figsize=(10,6))

    plt.barh(
        importance_df["Feature"],
        importance_df["Importance"]
    )

    plt.title("Feature Importance")

    plt.tight_layout()

    plt.savefig(
        "outputs/feature_importance.png"
    )

    plt.show()

print("\nTraining Completed Successfully.")