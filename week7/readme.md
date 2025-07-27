# 🌸 Week 7: Deploying ML Models with Streamlit – Iris Flower Predictor

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://celebal-tech-vanij-yplc9kqhptzlt5ztdelg4k.streamlit.app/)

🔗 **Live Demo:** [Click here to open the deployed app](https://celebal-tech-vanij-yplc9kqhptzlt5ztdelg4k.streamlit.app/)

---


## 🎯 Project Goal

Build and deploy a **Machine Learning Web Application** using **Streamlit** that predicts the **species of an Iris flower** based on user-input features. The app uses a trained classifier and visualizations to enhance interactivity and explainability.

---

## 🛠️ Features

- 🌐 **Interactive Web App** built with Streamlit  
- 📊 Real-time prediction of Iris flower species  
- 📈 Probability distribution chart of predictions  
- 📉 Visualization of training data (sepal length vs petal length)  
- 🤖 Pre-trained model loaded with `joblib`  
- 👨‍💻 Designed as part of Celebal Tech Internship by **Vanij Prasher**

---

## 📂 Folder Structure
```
Week7-Deploying-ML-Models-with-Streamlit/
├── iris_model.pkl                  # Trained machine learning model
├── app.py                          # Streamlit app code
├── requirements.txt                # Dependencies
└── README.md                       # Project documentation (this file)
```
---

## 📦 Dependencies

Install all dependencies using:

```bash
pip install -r requirements.txt
```

## 🧠 Model Information
	•	Dataset: Iris (from sklearn.datasets)
	•	Model Used: RandomForestClassifier
	•	Training Script: (can be created separately to generate iris_model.pkl)

## 🚀 Running the App
```bash
streamlit run app.py
```
# 🌐 Application UI

## 🎯 Title & Description
	•	Shows app title and instructions
	•	Uses emojis for a fun experience

## 🖱️ Sidebar Inputs

Users can adjust sliders for:
	•	Sepal Length (cm)
	•	Sepal Width (cm)
	•	Petal Length (cm)
	•	Petal Width (cm)

## 🤖 Model Prediction
	•	Displays the predicted species: Setosa, Versicolor, or Virginica
	•	Also shows the probability bar chart for all classes

## 📈 Training Data Visualization
	•	Sepal Length vs Petal Length scatter plot
	•	Points colored by species
	•	Built using Seaborn and Matplotlib

## ✨ Footer
	•	Custom footer message:
👨‍💻 Made by Vanij Prasher at Celebal Tech Internship

## 🔚 Summary

This project demonstrates:
	•	End-to-end ML deployment
	•	UI creation with Streamlit
	•	Real-time model inference
	•	Clean and modular code

✅ A great step forward in building interactive machine learning apps.

## Made with ❤️ by Vanij Prasher | Celebal Tech Internship 2025