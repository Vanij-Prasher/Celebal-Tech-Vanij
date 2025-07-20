# 🏠 Week 5: House Price Prediction – Preprocessing

## 🎯 Task Objective

Perform data preprocessing and build a basic machine learning model to predict house prices using a regression algorithm.

Dataset used: [House Prices: Advanced Regression Techniques](https://www.kaggle.com/competitions/house-prices-advanced-regression-techniques/data) from Kaggle (`train.csv`).

---

## 📁 File

- `week5_house_price_prediction.py`

---

## 🔍 Steps Covered

1. **Load the Dataset**
   - Load `train.csv` and keep only numeric columns.
   - Handle missing values by dropping rows with nulls.

2. **Feature and Target Selection**
   - `X` → All numerical features except `SalePrice`
   - `y` → Target variable `SalePrice`

3. **Train-Test Split**
   - Split the dataset into training and testing sets (80-20 split).

4. **Model Building**
   - Model: `RandomForestRegressor`
   - Fit the model to training data

5. **Evaluation**
   - Predict on test data
   - Evaluate using **Root Mean Squared Error (RMSE)**

---

## 📦 Libraries Used

- `pandas`
- `numpy`
- `sklearn.model_selection`
- `sklearn.ensemble`
- `sklearn.metrics`

---

## 🚀 How to Run

Make sure you have the `train.csv` file in the `week5/` directory.

```bash
python week5_house_price_prediction.py
```
## Install dependencies using:
```
pip install pandas numpy scikit-learn
```

## 📈 Output

Displays the RMSE (Root Mean Squared Error), which indicates the prediction error margin of the model.

⸻

## ✅ Summary

This week’s task focuses on cleaning, preprocessing, feature selection, and training a regression model. It sets the foundation for model tuning and evaluation, which will be explored in Week 6.