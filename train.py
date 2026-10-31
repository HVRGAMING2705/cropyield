import json, numpy as np
from sklearn.linear_model import Ridge
from sklearn.model_selection import cross_val_predict, KFold
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error

rng = np.random.default_rng(42)
n = 600
rainfall = rng.uniform(300, 1200, n)      # mm per season
temp = rng.uniform(18, 32, n)             # average temperature (C)
fertilizer = rng.uniform(0, 300, n)       # kg per hectare
soil_ph = rng.uniform(5.0, 8.0, n)        # soil pH
irrigation = rng.integers(0, 2, n)        # 0 = rain-fed, 1 = irrigated
# Generative yield (quintals per hectare): more rain and fertilizer help,
# irrigation adds a fixed boost, yield drops as soil pH drifts from 6.5.
y = (10 + 0.02 * rainfall + 0.05 * fertilizer + 6.0 * irrigation
     - 2.0 * np.abs(soil_ph - 6.5) + 0.3 * (temp - 20)
     + rng.normal(0, 3, n))
y = np.clip(y, 5, 60)
X = np.column_stack([rainfall, temp, fertilizer, soil_ph, irrigation])
names = ["rainfall_mm", "avg_temp_c", "fertilizer_kg_ha", "soil_ph", "irrigation"]
mu, sd = X.mean(0), X.std(0)
Xs = (X - mu) / sd
model = Ridge(alpha=1.0).fit(Xs, y)
kf = KFold(5, shuffle=True, random_state=42)
pred_cv = cross_val_predict(Ridge(alpha=1.0), Xs, y, cv=kf)
r2 = float(r2_score(y, pred_cv)); mae = float(mean_absolute_error(y, pred_cv))
rmse = float(np.sqrt(mean_squared_error(y, pred_cv)))
base_mae = float(mean_absolute_error(y, np.full(n, y.mean())))
print(f"CV R2={r2:.3f} MAE={mae:.2f} RMSE={rmse:.2f} baseline_MAE={base_mae:.2f} mean_yield={y.mean():.1f}")
print("coef", model.coef_, "intercept", model.intercept_)
mj = {"features": names, "means": mu.tolist(), "stds": sd.tolist(),
      "coef": model.coef_.tolist(), "intercept": float(model.intercept_),
      "metrics": {"cv_r2": r2, "cv_mae": mae, "cv_rmse": rmse, "baseline_mae": base_mae, "mean_yield": float(y.mean()), "n": n}}
with open("model.json", "w") as f: json.dump(mj, f, indent=1)

def predict(v):
    z = (np.array(v) - mu) / sd
    return float(model.intercept_ + z @ model.coef_)
samples = [[800, 26, 150, 6.5, 1], [400, 30, 50, 5.5, 0], [1000, 24, 250, 6.8, 1],
           [600, 22, 100, 7.5, 0], [1100, 27, 200, 6.2, 1]]
for s in samples: print(s, round(predict(s), 2))
