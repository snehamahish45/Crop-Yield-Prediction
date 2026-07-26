import joblib
import numpy as np
import matplotlib.pyplot as plt

from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

# =====================================
# Load Model
# =====================================

model = joblib.load("models/best_model.pkl")

# =====================================
# Load Test Data
# =====================================

X_test = joblib.load("models/X_test.pkl")
y_test = joblib.load("models/y_test.pkl")

# =====================================
# Prediction
# =====================================

prediction = model.predict(X_test)

# =====================================
# Evaluation Metrics
# =====================================

mae = mean_absolute_error(y_test, prediction)

mse = mean_squared_error(y_test, prediction)
rmse = np.sqrt(mse)

r2 = r2_score(y_test, prediction)

print("="*50)
print("MODEL EVALUATION")
print("="*50)

print(f"MAE  : {mae:.2f}")
print(f"RMSE : {rmse:.2f}")
print(f"R²   : {r2:.4f}")

# =====================================
# Actual vs Predicted Plot
# =====================================

plt.figure(figsize=(8,6))

plt.scatter(y_test, prediction)

plt.xlabel("Actual Yield")
plt.ylabel("Predicted Yield")
plt.title("Actual vs Predicted Yield")

# Perfect prediction line
plt.plot(
    [y_test.min(), y_test.max()],
    [y_test.min(), y_test.max()],
    'r--'
)

plt.tight_layout()

plt.savefig("outputs/actual_vs_predicted.png")

plt.show()

print("\nEvaluation Completed Successfully.")