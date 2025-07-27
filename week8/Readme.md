<<<<<<< HEAD
# 📊 Loan RAG Q&A Chatbot

This is an interactive chatbot that uses **RAG (Retrieval-Augmented Generation)** to intelligently answer user questions from a **Loan CSV dataset**. It combines local **LLMs (like Mistral 7B)** with **LangChain**, **FAISS vector store**, and **Streamlit** to provide insightful, document-based answers.

---

## 💡 Features

- 💬 Ask questions from a loan dataset in natural language.
- 🔍 Retrieves relevant chunks using **FAISS** vector store.
- 🧠 Generates context-aware responses using **Llama.cpp-powered Mistral 7B** model.
- 📜 Maintains chat history in session.
- 📁 Fully local, privacy-respecting architecture.
- 🎨 Clean and informative **Streamlit UI**.

---

## 🛠️ Tech Stack

| Technology             | Usage                        |
|------------------------|------------------------------|
| Python                 | Backend logic                |
| Streamlit              | Frontend UI                  |
| LangChain              | RAG orchestration            |
| LlamaCpp               | Local LLM inference engine   |
| FAISS                  | Vector store for retrieval   |
| HuggingFace Embeddings | Sentence embedding           |
| dotenv                 | Secure config loading        |

---

## 📂 Folder Structure

```bash
.
├── app.py                    # Streamlit frontend
├── rag_chatbot.py           # RAG logic using LangChain
├── data/
│   └── Training Dataset.csv.xls
├── .env                     # Model path and secrets
└── requirements.txt         # Python dependencies
```
---

## ⚙️ Setup Instructions

1. **Clone the repository**:

```bash
git clone https://github.com/Vanij-Prasher/Loan-RAG-Bot.git
cd Loan-RAG-Bot
```
2.	**Install dependencies**:
```bash
pip install -r requirements.txt
```
3.	**Download and setup your local model (e.g., Mistral-7B) and update the .env**:
```bash
MODEL_PATH=/absolute/path/to/your/mistral-7b.Q4_K_M.gguf
```
4.	**Run the chatbot**:
```bash
streamlit run app.py
```
### 🙋‍♂️ **About the Developer**

**Vanij Prasher**
👨‍💻 Data Science Intern at Celebal Technologies
💡 Passionate about AI, LLMs,Data Science and Real-world Applications
📫 GitHub- https://github.com/Vanij-Prasher | LinkedIn- https://www.linkedin.com/in/vanij-prasher/

---

## 📸 Screenshots

### 🔹 Homepage UI
![UI Screenshot](Screenshorts/Homepage.png)

### 🔹 Basic UI
![Basic UI](Screenshorts/Basic-UI.png)

### 🔹 Answer
![Answer ](Screenshorts/Answer.png)

### 🔹 Chat History
![Chat History](Screenshorts/Chat-History.png)
=======
# 🚀 Celebal Tech Data Science Internship Portfolio – Vanij Prasher

Welcome to my internship repository for Celebal Technologies (Summer 2025), where I explored and implemented various **Data Science**, **Machine Learning**, and **Deployment** concepts. This repository reflects my weekly progress, hands-on projects, and real-world implementation of data-centric solutions.

---

## 🙋‍♂️ About Me

I am **Vanij Prasher**, a passionate Data Science enthusiast with a strong inclination towards building **end-to-end data-driven applications**. During this internship, I focused on:
- Strengthening my understanding of machine learning workflows
- Performing deep data analysis and model optimization
- Learning deployment techniques using **Streamlit**

🔗 [LinkedIn](https://www.linkedin.com/in/vanij-prasher) • 📫 [2004vanij.prasher@gmail.com](mailto:vanijprasher@gmail.com)

---

## 🏢 About Celebal Technologies

**Celebal Technologies** is a premier AI and Big Data company that provides cutting-edge solutions to global enterprises. This internship helped me:
- Apply theoretical knowledge to practical problems
- Learn software development best practices
- Work on real-world data science workflows

---

# 🛠️ Skills Acquired During the Celebal Tech Internship

Throughout the internship, I worked on a series of weekly projects that helped me build and sharpen my skills across multiple domains in Data Science, Machine Learning, and Deployment. Here's a summary of the skills I acquired:

---

## 👨‍💻 Python Programming
- Writing clean, readable, and modular Python code
- Applying Object-Oriented Programming (OOP) concepts
- Handling files and exceptions efficiently

---

## 📊 Data Analysis & Visualization
- Performing Exploratory Data Analysis (EDA) using:
  - `pandas` for data manipulation
  - `matplotlib` and `seaborn` for visualizations
- Creating insightful charts such as:
  - Histograms, boxplots, scatter plots, heatmaps
- Understanding distributions, correlations, and data patterns

---

## 🤖 Machine Learning
- Implementing supervised learning models including:
  - Random Forest, Logistic Regression, and Support Vector Machines (SVM)
- Evaluating model performance using:
  - Accuracy, Precision, Recall, F1-Score
- Splitting datasets and managing training/testing workflow

---

## 🧠 Model Optimization
- Tuning hyperparameters using:
  - `GridSearchCV`
  - `RandomizedSearchCV`
- Comparing model scores to select the best-performing model

---

## 🌐 Model Deployment
- Deploying Machine Learning models using **Streamlit**
- Creating interactive UI for predictions
- Saving and loading trained models with `joblib`
- Designing a complete ML web app

---

## 📁 Project & Code Management
- Organizing weekly assignments into structured folders
- Writing reusable functions and clean scripts
- Following good naming conventions and commenting practices

---

## 🌀 Version Control (Git & GitHub)
- Initializing and managing Git repositories
- Committing, pushing, and managing branches
- Handling merge conflicts and restoring deleted work

---

## 📝 Documentation & Communication
- Writing detailed and professional `README.md` files
- Documenting objectives, methodologies, and outcomes
- Using markdown effectively to improve project presentation

---

> ✅ These skills reflect my hands-on experience across the full **Data Science Lifecycle** — from raw data to deployed application.

## 📁 Repository Structure

Each week includes a focused project or task with accompanying code and documentation.
```
Celebal-Tech-Vanij/
├── week1                           # Triangle Pattern Printing
├── week2                           # Singly Linked List with OOP
├── week3                           # Titanic Dataset Visualizations
├── week4                           # Titanic Dataset EDA
├── week5                           # House Price Prediction Model
├── week6                           # Model Evaluation & Hyperparameter Tuning
├── week7                           # Iris Classifier Streamlit App
├── README.md                       # General Overview (This file)
```
---

## 📚 Weekly Task Overview

| Week | Task Title                                       | Focus Area                                      |
|------|--------------------------------------------------|--------------------------------------------------|
| 1️⃣  | Pattern Printing                                  | Python Basics, Control Structures               |
| 2️⃣  | Singly Linked List                                | Object-Oriented Programming (OOP)               |
| 3️⃣  | Data Visualization (Titanic Dataset)              | Seaborn, Matplotlib, EDA                        |
| 4️⃣  | Exploratory Data Analysis (Titanic)               | Correlation, Null Handling, Boxplots, Heatmaps  |
| 5️⃣  | House Price Prediction                            | Feature Engineering, Regression, Random Forest  |
| 6️⃣  | Model Evaluation & Tuning                         | Metrics, GridSearchCV, RandomizedSearchCV       |
| 7️⃣  | Streamlit ML App – Iris Flower Predictor.         | Deployment, Streamlit, UI/UX, Joblib            |

Each week's code includes a `README.md` with explanations, sample outputs, and methodology used.

---

## 🧠 Skills Demonstrated

- 🐍 Python (OOP, File Handling, Control Structures)
- 📊 Data Analysis with Pandas & NumPy
- 📈 Data Visualization with Seaborn & Matplotlib
- 🤖 Machine Learning (Classification, Regression, Evaluation)
- 🎯 Hyperparameter Tuning (GridSearchCV, RandomizedSearchCV)
- 🌐 Deployment using Streamlit
- 🗂️ Code Structuring & Git Version Control

---

## 💼 Key Takeaways

✅ Practiced hands-on ML model building  
✅ Performed real-world data cleaning and feature analysis  
✅ Built a complete ML web app with live predictions  
✅ Enhanced understanding of EDA and business insights  
✅ Developed professional documentation and code workflow

---

## 🤝 Acknowledgments

- Huge thanks to Celebal Tech mentors and internship coordinators for the opportunity and constant support 🙌
- Special appreciation to peers and contributors for collaborative learning during this internship period

---

## 📬 Contact

For queries, collaborations or internship insights:

- 📧 2004vanij.prasher@gmail.com
- 🌐 [LinkedIn – Vanij Prasher](https://www.linkedin.com/in/vanij-prasher)

---

Made with 💙 by Vanij Prasher | Celebal Technologies – Data Science Internship 2025
>>>>>>> 5413da60c633b95ab5e8adcec34c778125499742
