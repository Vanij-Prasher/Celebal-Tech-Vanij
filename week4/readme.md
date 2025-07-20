# ✅ Week 4: Exploratory Data Analysis (EDA) on Titanic Dataset

## 🎯 Task Objective

Conduct an **in-depth Exploratory Data Analysis** on a dataset to understand the distribution of features, detect missing values, outliers, and relationships between variables.

Dataset used: **Titanic Dataset** from Seaborn.

---

## 📁 File

- `Week 4: Titanic EDA.py`

---

## 🧪 Key EDA Operations

1. **Data Inspection**
   - `df.info()`, `df.describe()`, `df.isnull().sum()`  
   Understand structure, data types, summary statistics, and missing values.

2. **Boxplot: Age by Passenger Class**
   - Used to detect age distribution and outliers across `pclass`.

3. **Heatmap: Feature Correlations**
   - Shows correlation matrix for numerical features (e.g., `fare`, `age`, `pclass`).

4. **Missing Data Analysis**
   - Visual inspection of which columns contain missing values.

---

## 📊 Visualizations

- 📦 `Boxplot` for `pclass` vs `age`
- 🌡 `Heatmap` for correlations
- 🧮 Bar plots for categorical variable distributions (optional)
- 📈 Histograms for numerical variable distributions (optional)

---

## 📦 Libraries Used

- `pandas`
- `seaborn`
- `matplotlib.pyplot`

---

## 🚀 How to Run

```bash
python week4_titanic_eda.py
```

## Make sure to have all required packages installed:
```
pip install pandas seaborn matplotlib
```
⸻

## Insights Gained
	•	Significant missing values in age, deck, and embark_town.
	•	First-class passengers tend to be older on average.
	•	Strong correlation between fare and pclass.

⸻
## Summary
This assignment emphasizes data cleaning, understanding, and visualization, forming the foundation for effective data preprocessing and feature engineering in the next phases.