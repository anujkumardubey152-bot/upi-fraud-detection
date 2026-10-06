# 💳 UPI Fraud Detection System

An end-to-end Machine Learning project that predicts the **fraud risk of UPI transactions** based on transaction and behavioral features.

The project combines data preprocessing, exploratory data analysis, machine learning, fraud probability prediction, and an interactive web interface into a complete ML application.

---

## 🚀 Project Overview

Digital payment systems such as UPI have become an important part of everyday transactions. With the increasing volume of digital payments, detecting potentially fraudulent transactions is an important challenge.

This project uses Machine Learning to analyze transaction-related features and estimate the likelihood that a transaction may be fraudulent.

### Key Features

- 🔍 Fraud-risk prediction
- 📊 Fraud probability estimation
- ⚠️ Risk-level classification
- 📈 Exploratory data analysis and visualizations
- 🤖 Machine Learning classification models
- 🌐 Interactive prediction interface

> **Note:** This project is an educational ML prototype and is not intended for real-world financial fraud detection without further validation and security testing.

---

## 🎯 Objectives

The main objectives of this project are:

1. Analyze UPI transaction data.
2. Identify patterns associated with fraudulent transactions.
3. Preprocess and prepare the dataset for Machine Learning.
4. Train classification models.
5. Compare different ML approaches.
6. Predict fraud probability for new transactions.
7. Classify transactions into different risk levels.
8. Build an easy-to-use interface for predictions.

---

## 🧠 Machine Learning Models

### 1. Logistic Regression

Used as a baseline classification model to estimate the probability of a transaction being fraudulent.

### 2. Random Forest

An ensemble learning algorithm used to capture more complex relationships between transaction features and fraud.

---

## 🔄 Machine Learning Pipeline

```text
Raw Transaction Data
        ↓
Data Cleaning
        ↓
Data Preprocessing
        ↓
Exploratory Data Analysis
        ↓
Feature Analysis
        ↓
Train-Test Split
        ↓
Model Training
        ↓
Model Evaluation
        ↓
Fraud Probability Prediction
        ↓
Risk Classification
        ↓
Interactive Web Application


---

📊 Exploratory Data Analysis

The dataset was analyzed to understand:

Fraud vs. legitimate transactions

Transaction behavior

Failed transaction patterns

Transaction amount patterns

Relationships between different features

Factors associated with increased fraud risk


Visualizations were created to identify patterns and relationships within the dataset.


---

⚠️ Risk Classification

The application converts the predicted fraud probability into an understandable risk level.

Fraud Probability	Risk Level

Low probability	🟢 Low Risk
Moderate probability	🟡 Medium Risk
High probability	🔴 High Risk


The thresholds can be configured according to the project requirements.


---

🌐 Application

The trained Machine Learning model is integrated into an interactive application where users can enter transaction information and receive a fraud-risk prediction.

Example Output

Transaction Status: Legitimate
Fraud Probability: 38.46%
Risk Level: Medium Risk


---

🛠️ Tech Stack

Programming Language

Python


Libraries

Pandas

NumPy

Scikit-learn

Matplotlib

Seaborn


Machine Learning

Logistic Regression

Random Forest


Development

Jupyter Notebook

Interactive Web Application



---

📁 Project Structure

UPI-Fraud-Detection/
│
├── data/
│   └── dataset.csv
│
├── notebooks/
│   └── fraud_detection.ipynb
│
├── model/
│   └── trained_model.pkl
│
├── app/
│   └── app.py
│
├── images/
│   ├── dashboard.png
│   ├── prediction.png
│   └── analysis.png
│
├── requirements.txt
│
└── README.md

> Update the structure above according to the actual files in your repository.




---

⚙️ Installation

Clone the repository:

git clone YOUR_GITHUB_REPOSITORY_URL

Move into the project directory:

cd UPI-Fraud-Detection

Install the required dependencies:

pip install -r requirements.txt


---

▶️ Running the Project

If the project uses a Python application:

python app.py

If the project uses Streamlit:

streamlit run app.py

Then open the local URL displayed in the terminal.


---

📈 Model Evaluation

The models can be evaluated using:

Accuracy

Precision

Recall

F1-Score

ROC-AUC

Confusion Matrix


Model Performance

Model	Accuracy	Precision	Recall	F1-Score	ROC-AUC

Logistic Regression	Add Value	Add Value	Add Value	Add Value	Add Value
Random Forest	Add Value	Add Value	Add Value	Add Value	Add Value


> Replace the placeholder values with the actual results obtained from the project.




---

📸 Project Screenshots

🖥️ Prediction Interface



🔍 Prediction Result



📊 Data Analysis




---

💡 Key Learnings

Through this project, I gained practical experience in:

Data preprocessing

Exploratory Data Analysis

Feature analysis

Classification algorithms

Model comparison

Fraud-risk prediction

Model evaluation

ML model integration

Building an end-to-end Machine Learning workflow



---

🚀 Future Improvements

[ ] Hyperparameter tuning

[ ] Cross-validation

[ ] SHAP-based model explainability

[ ] Better fraud-risk calibration

[ ] Real-time transaction monitoring

[ ] Advanced ensemble models

[ ] Improved handling of class imbalance

[ ] Model monitoring and drift detection

[ ] Cloud deployment

[ ] API-based prediction service



---

⚠️ Disclaimer

This project is developed for educational and portfolio purposes.

It does not connect to real UPI payment networks and should not be used to make real financial or security decisions without extensive validation, security testing, and appropriate regulatory compliance.


---

👨‍💻 Author

Anuj Kumar Dubey

Aspiring AI/ML Engineer passionate about Machine Learning, Artificial Intelligence, and building practical technology solutions.




---

⭐ Support

If you find this project useful or interesting, consider giving the repository a ⭐ on GitHub.
