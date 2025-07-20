# app.py
import streamlit as st
import pandas as pd
import numpy as np
import joblib
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Load iris dataset
iris = load_iris()
# Load the trained model
model_path = os.path.join(os.path.dirname(__file__), 'iris_model.pkl')
model = joblib.load(model_path)

st.title("🌸 Iris Flower Predictor")
st.write("Enter the features below to predict the Iris flower type:")

# Sidebar input
sepal_length = st.slider("Sepal Length (cm)", 4.0, 8.0, 5.4)
sepal_width = st.slider("Sepal Width (cm)", 2.0, 4.5, 3.4)
petal_length = st.slider("Petal Length (cm)", 1.0, 7.0, 1.3)
petal_width = st.slider("Petal Width (cm)", 0.1, 2.5, 0.2)

# Prediction
input_data = pd.DataFrame([[sepal_length, sepal_width, petal_length, petal_width]],
                          columns=iris.feature_names)
prediction = model.predict(input_data)[0]
prediction_proba = model.predict_proba(input_data)

# Show results
st.subheader("Prediction:")
st.write(f"The predicted Iris flower is **{iris.target_names[prediction]}**.")

st.subheader("Prediction Probability:")
st.bar_chart(prediction_proba[0])

# Visualize training data
st.subheader("📊 Sepal Length vs Petal Length (Iris Dataset)")
fig, ax = plt.subplots()
sns.scatterplot(x=iris.data[:, 0], y=iris.data[:, 2], hue=iris.target_names[iris.target], ax=ax)
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")
st.pyplot(fig)


st.markdown("---")
st.markdown(
    "<div style='text-align: center; font-size: 14px;'>"
    "👨‍💻 Made by <strong>Vanij Prasher</strong> at Celebal Tech Internship"
    "</div>",
    unsafe_allow_html=True
)