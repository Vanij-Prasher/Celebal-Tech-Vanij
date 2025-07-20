# Week 4: Titanic EDA – Cleaned and Enhanced

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df = sns.load_dataset("titanic")

# -------------------- 📄 Basic Data Inspection --------------------
print("📄 Dataset Info:")
print(df.info())
print("\n📊 Statistical Summary:")
print(df.describe(include='all'))
print("\n❓ Missing Values:")
print(df.isnull().sum())

# -------------------- 📊 Age Distribution --------------------
plt.figure(figsize=(8, 5))
sns.histplot(df['age'].dropna(), bins=30, kde=True, color='skyblue')
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Count")
plt.tight_layout()
plt.show()

# -------------------- 🎯 Age by Passenger Class --------------------
plt.figure(figsize=(8, 5))
sns.boxplot(x='pclass', y='age', data=df)
plt.title("Age Distribution by Passenger Class")
plt.xlabel("Passenger Class")
plt.ylabel("Age")
plt.tight_layout()
plt.show()

# -------------------- 🔍 Correlation Heatmap --------------------
plt.figure(figsize=(10, 6))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap (Numeric Features)")
plt.tight_layout()
plt.show()

# -------------------- 🧍 Survival Count --------------------
plt.figure(figsize=(6, 4))
sns.countplot(x='survived', data=df)
plt.title("Survival Count (0 = No, 1 = Yes)")
plt.xlabel("Survived")
plt.ylabel("Count")
plt.tight_layout()
plt.show()

# -------------------- 🧑 Survival by Sex --------------------
plt.figure(figsize=(7, 4))
sns.countplot(x='sex', hue='survived', data=df)
plt.title("Survival by Gender")
plt.xlabel("Gender")
plt.ylabel("Count")
plt.legend(title="Survived", labels=["No", "Yes"])
plt.tight_layout()
plt.show()