# ✅ Week 5: House Price Prediction – Preprocessing & Random Forest Model

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

# -------------------- 📄 Load and Preview Dataset --------------------
try:
    house_df = pd.read_csv("week5/train.csv")  # ✅ Ensure correct path
    print("✅ Dataset loaded successfully.\n")
except FileNotFoundError:
    print("❌ Error: Dataset not found. Check the path 'week5/train.csv'")
    exit()

print("📋 Initial shape:", house_df.shape)
print("🔍 Missing values (top 10):\n", house_df.isnull().sum().sort_values(ascending=False).head(10))

# -------------------- 🧹 Keep Numeric Only & Drop Missing --------------------
numeric_df = house_df.select_dtypes(include=[np.number])
clean_df = numeric_df.dropna()
print("\n✅ Cleaned shape (numeric only, no NaNs):", clean_df.shape)

# -------------------- 🎯 Split Features and Target --------------------
if 'SalePrice' not in clean_df.columns:
    print("❌ Error: 'SalePrice' column not found in the dataset.")
    exit()

X = clean_df.drop('SalePrice', axis=1)
y = clean_df['SalePrice']

# -------------------- 🔀 Train-Test Split --------------------
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print("🔀 Data split: ", X_train.shape, X_test.shape)

# -------------------- 🏗️ Model Training --------------------
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# -------------------- 📈 Prediction and Evaluation --------------------
y_pred = model.predict(X_test)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
print("\n✅ Root Mean Squared Error (RMSE):", round(rmse, 2))

# -------------------- 📊 Feature Importance (Optional) --------------------
plt.figure(figsize=(12, 6))
importances = pd.Series(model.feature_importances_, index=X.columns)
importances.nlargest(10).plot(kind='barh', color='steelblue')
plt.title("Top 10 Important Features")
plt.xlabel("Feature Importance Score")
plt.tight_layout()
plt.show()