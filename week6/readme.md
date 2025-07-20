# 🔍 Week 6: Model Evaluation and Hyperparameter Tuning (Iris Dataset)

## 🎯 Task Objective

Train multiple machine learning models on the **Iris dataset**, evaluate their performance using classification metrics, and optimize them using **hyperparameter tuning techniques** like `GridSearchCV` and `RandomizedSearchCV`.

---

## 📁 File

- `week6_model_evaluation_and_tuning.py`

---

## 📊 Models Used

- **Random Forest Classifier**
- **Support Vector Machine (SVM)**
- **Logistic Regression**

---

## 🧪 Evaluation Metrics

Each model is evaluated using:
- **Accuracy**
- **Precision**
- **Recall**
- **F1-Score**

Displayed using the `classification_report` from `sklearn`.

---

## 🔧 Hyperparameter Tuning

Two techniques are used for tuning:

1. **GridSearchCV** (for SVM)
   - Parameters tuned: `C`, `kernel`, `gamma`

2. **RandomizedSearchCV** (for Random Forest)
   - Parameters tuned: `n_estimators`, `max_depth`, `min_samples_split`, `min_samples_leaf`

---

## 📦 Libraries Used

- `pandas`
- `numpy`
- `seaborn`
- `matplotlib`
- `sklearn` modules: `datasets`, `metrics`, `model_selection`, `svm`, `ensemble`, `linear_model`

---

## 💻 How to Run

```bash
python Week 6: Model Evaluation and Hyperparameter Tuning (Iris Dataset).py
```
## Install dependencies with:
```
pip install pandas numpy seaborn matplotlib scikit-learn
```

## 🧠 Dataset
	•	Iris dataset from sklearn.datasets
	•	A classic dataset for classification tasks containing 150 samples of iris flowers from three species.

⸻

## 🔢 Sample Output

Displays:
	•	Performance metrics of each model before tuning
	•	Best model parameters after tuning
	•	Updated classification report with tuned models

⸻
## ✅ Summary

This week emphasizes:
	•	Training multiple classifiers
	•	Evaluating using classification metrics
	•	Improving performance via hyperparameter tuning