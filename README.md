# CropYield — Crop Yield Predictor

A 2nd-year B.Tech AI/ML project by Vikranth Reddy (Woxsen University).

## What it does
Predicts crop yield in quintals per hectare from season rainfall, average temperature, fertilizer use, soil pH and irrigation.

## Model
- Ridge regression (alpha = 1.0) on standardised features
- Trained on 600 synthetic farm seasons (seed 42)
- 5-fold cross-validation: R² = 0.844, MAE = 2.50 q/ha, RMSE = 3.13 q/ha
- Baseline (predict the mean): MAE = 6.45 q/ha — the model is ~2.6x better

## Files
- `train.py` — generates data, trains the model, writes `model.json`
- `model.json` — learned means, standard deviations, coefficients, intercept
- `index.html` — interactive demo; the browser runs the exact same weights as Python

## Live demo
https://cropyield-sigma.vercel.app
