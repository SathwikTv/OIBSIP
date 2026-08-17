# Unemployment Analysis in India (Time Series)

## Overview
Time series analysis and forecasting of unemployment rates across Indian states/regions, including a COVID-19 impact comparison. Built as part of the Oasis Infobyte Data Science internship (Task 2).

## Dataset
"Unemployment in India" dataset (Kaggle) — monthly regional unemployment rate, estimated employed count, and labour participation rate by state/region and area (urban/rural).

## Approach
1. Data cleaning: handled nulls, removed duplicates, parsed dates, standardized column names
2. EDA: distribution analysis (histograms, boxplots), scatterplots against unemployment rate, categorical breakdowns by region, region-wise average unemployment, top 10 states by unemployment, monthly trends, time-series comparison across states, correlation heatmap, and a pre- vs. post-COVID comparison
3. Feature engineering: time-based features (year, month, quarter, cyclical month encoding), lag features (1/2/3/6-month lags), rolling mean features (3/6-month)
4. Time-based train/test split (train: before Apr 2020, test: from Apr 2020 onward)
5. Modeling: two baselines (naive forecast, 3-month moving average) plus three ML models (Linear Regression, Random Forest, Gradient Boosting)
6. Walk-forward validation across 3 validation dates to compare model stability over time
7. Final model selection, error analysis, and model saved for reuse

## Key Findings
- **COVID-19 impact:** average unemployment rate jumped from 9.61% (pre-COVID) to 20.19% (post-COVID) — a +10.58 percentage point increase
- Random Forest was the best-performing model in both walk-forward validation (Mean MAE: 2.32) and final test evaluation (MAE: 12.59), outperforming Linear Regression, Gradient Boosting, and both baselines

## Results

**Walk-Forward Validation (Mean MAE / RMSE across 3 validation periods):**

| Model | Mean MAE | Mean RMSE |
|---|---|---|
| Random Forest | 2.32 | 3.24 |
| Gradient Boosting | 2.46 | 3.51 |
| Linear Regression | 2.74 | 4.17 |

**Final Test Set Comparison:**

| Model | MAE | RMSE | R² |
|---|---|---|---|
| Random Forest | 12.59 | 18.12 | -0.27 |
| 3-Month Moving Average | 13.31 | 18.51 | -0.32 |
| Linear Regression | 13.40 | 19.48 | -0.46 |
| Naive Forecast | 14.56 | 20.05 | -0.55 |

**Final Model: Random Forest** — lowest error across both walk-forward and final test evaluation.

## Error Analysis (Final Model)
- Mean Error: 7.55
- Mean Absolute Error: 12.59
- Maximum Error: 74.46

## Tools Used
Python, pandas, scikit-learn, seaborn, matplotlib, joblib

## Files
- `Unemployment_Time_Series_df.ipynb` — full notebook (EDA, feature engineering, modeling, walk-forward validation, error analysis)
- `unemployment_random_forest_final.pkl` — saved final model
