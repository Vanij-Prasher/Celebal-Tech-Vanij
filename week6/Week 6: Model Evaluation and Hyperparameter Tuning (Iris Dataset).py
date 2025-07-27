# ✅ Week 6: Model Evaluation and Hyperparameter Tuning (Iris Dataset)

import pandas as pd
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split, GridSearchCV, RandomizedSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.metrics import classification_report
from sklearn.linear_model import LogisticRegression

# Load dataset
iris = load_iris()
X = pd.DataFrame(iris.data, columns=iris.feature_names)
y = pd.Series(iris.target)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# ========== 1. Train Multiple Models ==========
models = {
    "Random Forest": RandomForestClassifier(),
    "SVM": SVC(),
    "Logistic Regression": LogisticRegression(max_iter=1000)
}

print("📊 Model Performance Before Tuning\n")
for name, model in models.items():
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    print(f"🔹 {name}")
    print(classification_report(y_test, y_pred, target_names=iris.target_names))
    print("-" * 60)

# ========== 2. Hyperparameter Tuning ==========
# GridSearchCV for SVM
svm_params = {
    'C': [0.1, 1, 10],
    'kernel': ['linear', 'rbf']
}
grid_svm = GridSearchCV(SVC(), svm_params, cv=3)
grid_svm.fit(X_train, y_train)

# RandomizedSearchCV for Random Forest
rf_params = {
    'n_estimators': [50, 100, 150],
    'max_depth': [2, 4, 6, None]
}
random_rf = RandomizedSearchCV(RandomForestClassifier(), rf_params, n_iter=5, cv=3, random_state=42)
random_rf.fit(X_train, y_train)

# ========== 3. Final Evaluation ==========
print("\n✅ Best SVM Model Evaluation")
svm_best = grid_svm.best_estimator_
y_pred_svm = svm_best.predict(X_test)
print(classification_report(y_test, y_pred_svm, target_names=iris.target_names))

print("\n✅ Best Random Forest Model Evaluation")
rf_best = random_rf.best_estimator_
y_pred_rf = rf_best.predict(X_test)
print(classification_report(y_test, y_pred_rf, target_names=iris.target_names))