# Iris Flower Classification

## Overview
Classification model to predict Iris flower species (setosa, versicolor, virginica) based on sepal and petal measurements. Built as part of the Oasis Infobyte Data Science internship (Task 1).

## Dataset
The classic Iris dataset — 150 samples, 4 numeric features (sepal length/width, petal length/width), 3 target classes.

## Approach
- Checked for nulls and duplicates, removed duplicate rows
- EDA: class distribution, pairplot, boxplots/violin plots by species, correlation heatmap, and a petal length vs. petal width scatter plot to visually assess class separability
- Built preprocessing + model pipelines (imputer, scaler, encoder) for two classifiers: Logistic Regression and Random Forest
- Tuned both models using GridSearchCV (5-fold cross-validation)

## Key Findings
- Petal length and petal width are the most discriminative features — setosa is fully separable from the other two species on these alone, with versicolor and virginica showing only slight overlap
- After tuning, both models performed similarly on cross-validation (~95.7% CV accuracy), but Random Forest generalized slightly better on the held-out test set

## Results

| Model | CV Accuracy | Test Accuracy | Test F1 | Test Precision | Test Recall |
|---|---|---|---|---|---|
| Random Forest | 95.69% | 96.67% | 96.66% | 96.97% | 96.67% |
| Logistic Regression | 95.72% | 93.33% | 93.33% | 93.33% | 93.33% |

**Final model: Random Forest** — chosen for its higher test accuracy, F1, and precision despite near-identical CV scores, suggesting it generalizes slightly better to unseen data.

## Tools Used
Python, pandas, scikit-learn, seaborn, matplotlib, joblib

## Files
- `IRIS_CLASS.ipynb` — full notebook (EDA, preprocessing, modeling, tuning, evaluation)
- `RF_IRIS.pkl` — saved final model
