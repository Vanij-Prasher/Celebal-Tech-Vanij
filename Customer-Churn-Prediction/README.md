<<<<<<< HEAD

# ⚡ Customer Churn Prediction Web App

Welcome to the **Customer Churn Prediction Web App**! This project predicts whether a customer is likely to churn based on their service usage details and visualizes customer churn patterns using interactive dashboards.

## 🚀 Project Features
- Churn prediction using a trained machine learning model.
- Interactive Streamlit web app.
- Dashboard with KPIs and visualizations.
- Easy navigation using Streamlit Option Menu.

## 📊 Key Performance Indicators (KPIs)
- **Churn Rate:** Percentage of customers likely to churn.
- **Total Customers:** Total number of customers in the dataset.
- **Average Tenure:** Average duration (in months) that customers stay with the service.

## 📈 Visualizations
- **Churn Count Distribution:** Bar chart showing churn vs. non-churn customers.
- **Churn by Contract Type:** Pie chart depicting churn distribution across contract types.
- **Tenure Distribution by Churn:** Histogram showing tenure differences between churned and non-churned customers.

## 🛠️ Tech Stack
- Python
- Streamlit
- Scikit-learn
- Plotly
- Pandas
- Streamlit Option Menu

## ⚙️ Setup Instructions

1. **Clone the repository:**
```bash
git clone https://github.com/Vanij-Prasher/Customer-Churn-Prediction.git
cd Customer-Churn-Prediction
```

2. **Install the dependencies:**
```bash
pip install -r requirements.txt
```

3. **Run the app:**
```bash
streamlit run app.py
```

## 🗂️ Project Structure
```
├── app.py                  # Streamlit web app
├── churn_model.joblib      # Trained ML model
├── WA_Fn-UseC_-Telco-Customer-Churn.csv # Dataset
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
```

## 👨‍💻 Developer

**Vanij Prasher**  
📧 Email: 2004vanij.prasher@gmail.com  
🌐 [GitHub](https://github.com/Vanij-Prasher)  
🔗 [LinkedIn](https://www.linkedin.com/in/vanij-prasher)

---

=======
# 🎓 Celebal Tech Internship – Python & Data Science Projects

[![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python)](https://www.python.org/)
[![Internship](https://img.shields.io/badge/Internship-Celebal%20Tech-%23007ACC?logo=github)](https://www.celebaltech.com/)
[![GitHub Repo](https://img.shields.io/badge/Repository-Vanij--Prasher/Celebal--Tech--Vanij-blue?logo=github)](https://github.com/Vanij-Prasher/Celebal-Tech-Vanij)

Welcome to my GitHub repository for the **Celebal Tech Data Science Internship**.  
This repo showcases my weekly progress, learning, and projects in Python, OOP, and data science foundations.

---

## 🔍 Overview

This internship involves solving hands-on problems using Python and essential CS fundamentals.  
Each task is structured to strengthen:

- 🐍 Python Programming
- 🧱 Data Structures & Algorithms
- 🧠 Object-Oriented Design
- 📈 Data Science Foundations
- 🛠️ Git & GitHub Project Workflows

---

## 🧠 Concepts Used

- `for` loops and range-based iteration
- String multiplication and spacing
- Printing formatted output to the console
- Data structures: Linked Lists
- Exploratory Data Analysis (EDA)
- Data Cleaning and Imputation
- Data Visualization using Seaborn and Matplotlib
- Correlation analysis and outlier detection
- Supervised Machine Learning (Regression)
- Hyperparameter Tuning using RandomizedSearchCV
- Feature Engineering
- Classification metrics: Accuracy, Precision, Recall, F1-score
- GridSearchCV & RandomizedSearchCV


---

## 📚 Weekly Tasks & Explanations

### 📘 Week 1 – Pattern Printing with Python

**Goal:** Learn basic control structures (`for` loops) and output formatting.  
**Task:** Create 3 console-based patterns using `"*"`:

- **Lower Triangular Pattern**  
- **Upper Triangular Pattern**  
- **Pyramid Pattern**

**Concepts Used:**  
`for` loops, `range()`, string multiplication, alignment using spaces.

📌 **Purpose:**  
Build comfort with basic syntax and GitHub push-pull workflow.

---

### 🔹 Lower Triangular Pattern
```
* 
* * 
* * * 
* * * * 
* * * * *
```

### 🔹 Upper Triangular Pattern

```
* * * * * 
* * * * 
* * * 
* * 
*
```

### 🔹 Pyramid Pattern
```
    *
   * * 
  * * * 
 * * * * 
* * * * * 
```
---
### 📘 Week 2 – Singly Linked List using OOP

**Goal:** Understand and implement linked data structures with classes.  
**Task:** Create a Singly Linked List with:

- Node & LinkedList classes
- `add_node()` – Add node to end  
- `print_list()` – Print the linked list  
- `delete_nth_node(n)` – Delete the nth node (1-based index)
- Exception handling for empty list / invalid index

**Concepts Used:**  
Classes, object references, method definition, edge case handling.

---
### 📘 Week 3 – Titanic Dataset Visualization

**Goal:** Perform data visualization using Seaborn and Matplotlib on the Titanic dataset.  
**Task:** Load the Titanic dataset and generate multiple plots for EDA (Exploratory Data Analysis):

- Survival count (`countplot`)
- Survival by gender
- Survival by passenger class
- Age distribution by survival (`histplot`)
- Heatmap of missing values (`heatmap`)
- Save screenshots of each plot

**Concepts Used:**  
DataFrames, Seaborn visualizations, `matplotlib.pyplot`, categorical and continuous data plotting.

### 🖼️ Sample Visualizations

You’ll find the code and screenshots in the [`assignment3/`](assignment3/) folder.
___
### 📘 Week 4 – Advanced Titanic Data Visualization and Preprocessing

**Goal:** Perform in-depth data analysis, cleaning, imputation, outlier detection, and complex visualization using the Titanic dataset.

**Task:**  
=> Load the Titanic dataset using Seaborn.  
=> Handle missing values using heatmaps and imputation techniques.  
=> Impute missing ages based on passenger class.  
=> Drop irrelevant columns like `deck` and rows with remaining missing data.  
=> Perform univariate and multivariate visualizations:
- Survival count
- Gender distribution
- Passenger class distribution
- Age and fare distribution
- Boxplot for outlier detection
- Survival distribution by gender and class
- Violin plot for survival and age distribution
- Correlation heatmap (numeric columns only)

**Concepts Used:**
- Missing value handling and imputation
- Advanced Seaborn visualizations: violin plots, boxplots, heatmaps
- Outlier detection
- Correlation analysis
- Data cleaning workflows

**Purpose:**  
This task builds on Week 3 and introduces real-world data preprocessing steps, handling missing data, and advanced exploratory data analysis using visual techniques.

### 🖼️ Sample Visualizations

You’ll find the code and screenshots in the [`assignment4/`](assignment4/) folder.

---

### 📘 Week 5 – House Price Prediction using Machine Learning

**Goal:** Build a machine learning model to predict house prices using the Kaggle dataset:  
[House Prices - Advanced Regression Techniques](https://www.kaggle.com/competitions/house-prices-advanced-regression-techniques/data)

**Task:**
- Load and preprocess the data (handle missing values, label encoding)
- Perform feature engineering:
  - Total bathrooms
  - Total porch area
  - House age
- Train Random Forest Regressor
- Evaluate model using RMSE
- Generate final submission CSV

**Concepts Used:**
- Data preprocessing and imputation
- Label encoding for categorical variables
- Feature engineering for better model performance
- Supervised learning: Random Forest Regressor
- Model tuning using RandomizedSearchCV

📝 Files:
- `price_predict.py`: Python code for the entire pipeline
- `Final_submission.csv`: Generated submission file
- `train.csv`, `test.csv`: Dataset files

---

### 📘 Week 6 – Model Evaluation & Hyperparameter Tuning

**Goal:** Train and evaluate multiple machine learning classification models using various evaluation metrics, and optimize their performance using hyperparameter tuning techniques.

**Task:**
=> Load a classification dataset and split it into training and testing sets  
=> Train the following models:
- Logistic Regression
- Random Forest Classifier
- Support Vector Machine (SVM)

=> Evaluate each model using metrics:
- Accuracy
- Precision
- Recall
- F1-score

=> Perform hyperparameter tuning:
- `GridSearchCV` for Random Forest
- `RandomizedSearchCV` for SVM

=> Analyze results and select the best-performing model  
=> Evaluate tuned models on the test set

**Concepts Used:**
- Classification algorithms
- Evaluation metrics for classifiers
- Cross-validation
- Hyperparameter tuning with `GridSearchCV` and `RandomizedSearchCV`
- Model comparison and result analysis

### 🖼️ Sample Output

You’ll find the code and screenshots in the [`assignment6/`](assignment6/) folder.



---

## 📁 File Structure
```text
Celebal-Tech-Vanij/
├── Week1.py                         # Pattern printing in Python
├── Week2.py                         # Singly Linked List using OOP
├── assignment3/
│   ├── data_visualization_week3.py  # Titanic dataset visualizations (Week 3)
│   ├── Screenshot...                # Week 3 visualizations
├── assignment4/
│   ├── week4.py                     # Advanced Titanic EDA (Week 4)
│   ├── Screenshot...                # Week 4 visualizations
├── Week5-house-prices-advanced-regression-techniques/
│   ├── price_predict.py             # House price prediction code (Week 5)
│   ├── Final_submission.csv         # Final submission CSV (Week 5)
│   ├── train.csv                    # Training dataset
│   ├── test.csv                     # Test dataset
│   ├── sample_submission.csv        # Sample submission file
│   ├── Screenshot....               # Screenshots (if applicable)
├── assignment6/
│   ├── week6.py                     # Classification and hyperparameter tuning (Week 6)
│   ├── week6_output.png             # Screenshot of Week 6 model results
├── README.md                        # Internship overview and task breakdown

```
## 🙋‍♂️ Author
**Vanij Prasher**  
B.E. in Computer Science & Engineering (Artificial Intelligence & Machine Learning) – 4th Year  
**Intern @ [Celebal Tech](https://www.celebaltech.com/)**  
🌐 GitHub: [github.com/Vanij-Prasher](https://github.com/Vanij-Prasher)
---

## 📅 Internship Info

**Company**: Celebal Tech  
**Role**: Data Science Intern  
**Week**: 4 --Completed--  
**Focus**: Python basics and GitHub project structure

---

## 🔗 How to Run

1. Clone this repo:
   ```bash
   git clone https://github.com/your-username/Celebal-Tech-Vanij.git
   cd Celebal-Tech-Vanij
>>>>>>> 3cffd9ec8bdac42208d3d3709387f0634bf5ddc3

