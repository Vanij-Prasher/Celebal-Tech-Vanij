# ✅ Week 3: Titanic Data Visualization

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Load the Titanic dataset directly from seaborn
df = sns.load_dataset("titanic")

# -------------------------------
# 🧾 Overview of the Dataset
# -------------------------------
print("🔍 First 5 Rows of the Dataset:")
print(df.head())

print("\n🧮 Basic Info:")
print(df.info())

print("\n📊 Summary Statistics:")
print(df.describe(include='all'))

# -------------------------------
# 📈 Plot 1: Passenger Class Distribution
# -------------------------------
plt.figure(figsize=(8, 5))
sns.countplot(x='class', data=df, palette='viridis')
plt.title("Passenger Class Distribution")
plt.xlabel("Class")
plt.ylabel("Number of Passengers")
plt.tight_layout()
plt.show()

# -------------------------------
# 📊 Plot 2: Age Distribution
# -------------------------------
plt.figure(figsize=(8, 5))
sns.histplot(df['age'].dropna(), kde=True, color='skyblue')
plt.title("Age Distribution of Passengers")
plt.xlabel("Age")
plt.ylabel("Count")
plt.tight_layout()
plt.show()

# -------------------------------
# 📊 Plot 3: Gender Distribution
# -------------------------------
plt.figure(figsize=(6, 4))
sns.countplot(x='sex', data=df, palette='pastel')
plt.title("Gender Distribution")
plt.xlabel("Sex")
plt.ylabel("Count")
plt.tight_layout()
plt.show()

# -------------------------------
# 📊 Plot 4: Survival by Class
# -------------------------------
plt.figure(figsize=(8, 5))
sns.countplot(x='class', hue='survived', data=df, palette='Set2')
plt.title("Survival by Passenger Class")
plt.xlabel("Class")
plt.ylabel("Count")
plt.legend(title="Survived", labels=["No", "Yes"])
plt.tight_layout()
plt.show()

# -------------------------------
# 📊 Plot 5: Heatmap of Correlations
# -------------------------------
plt.figure(figsize=(10, 6))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.show()