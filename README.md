![Demonstration](banner.png)
<h1 align="center">Heart Disease Prediction Dashboard</h1>
<p align="center">
  <img src="https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue">
  <img src="https://img.shields.io/badge/Pandas-2C2D72?style=for-the-badge&logo=pandas&logoColor=white">
  <img src="https://img.shields.io/badge/Numpy-777BB4?style=for-the-badge&logo=numpy&logoColor=white">
  <img src="https://img.shields.io/badge/Plotly-239120?style=for-the-badge&logo=plotly&logoColor=white">
  <img src="https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white">
  <img src="https://img.shields.io/badge/scikit_learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white">
</p>

This project presents a dynamic and interactive web application for predicting the risk of heart disease based on clinical data. The model and dashboard are built upon a well-known dataset from the [UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/45/heart+disease), derived from angiographic results of 303 patients at the Cleveland Clinic Foundation, Ohio.

---

## 🔍 Project Overview

This application is divided into two main pages:

### 1. **Heart Disease Prediction**

A form-based interface allows users to input patient information such as:
- Age, Sex
- Blood pressure and cholesterol levels
- Fasting blood sugar
- Electrocardiogram results
- Maximum heart rate
- Exercise-induced angina
- ST depression, among others

Once submitted, these values are passed to a machine learning model trained using **Logistic Regression**, which classifies whether the patient is at risk of having heart disease.

### 2. **Graphic Analysis**

This page provides multiple interactive visualizations using **Plotly**, enabling users to explore trends and patterns from the dataset, such as:
- Heart disease distribution by age and sex
- Relationship between cholesterol or blood pressure and heart disease
- Blood sugar and ECG pattern analysis

These charts offer valuable insights into the clinical features correlated with heart conditions.

---

## 🧠 Model Development and Performance

The initial phase included training and evaluating multiple classification models. After experimentation, **Logistic Regression** was selected for final deployment. The model was trained using a robust pipeline with:

- **StandardScaler** for feature normalization  
- **Bayesian optimization** (`BayesSearchCV`) for hyperparameter tuning  
- **Nested cross-validation** for unbiased performance estimation

**Voting Classifier (Soft Voting)**, an ensemble model combining **Logistic Regression**, **Random Forest**, and **XGBoost**, was also tested. After optimizing each model individually, the ensemble model achieved solid performance in identifying heart disease, leveraging the complementary strengths of each individual model.

📈 **Final test set performance (class 1 = heart disease):**

| Metric    | Class 0 | Class 1 |
|-----------|---------|---------|
| Precision | 0.90    | 0.86    |
| Recall    | 0.88    | 0.89    |
| F1-Score  | 0.89    | 0.88    |

The model achieved **0.89 recall on class 1**, meaning it correctly identified 89% of patients with heart disease — a crucial metric for medical prediction tasks where false negatives are costly.

The ```model``` folder contains a Jupyter Notebook detailing the model development process, including training, evaluation, and optimization.

---

## 🚀 Why This Project Matters

Heart disease remains one of the leading causes of death worldwide. A predictive tool like this can help medical professionals, students, and data enthusiasts identify risk patterns more quickly and efficiently. By combining explainable machine learning with a user-friendly interface, this project demonstrates the power of applied AI in healthcare diagnostics and education.

---

## 🛠️ Technologies Used

- **Dash** & **Dash Bootstrap Components**: For web app development  
- **Pandas** & **NumPy**: For data manipulation  
- **Plotly**: For interactive visualizations  
- **XGBoost**, **RandomForest**, and **Scikit-Learn**: For model training and tuning  
- **ucimlrepo API**: For accessing the UCI dataset programmatically  
- **Jupyter Notebook**: For exploratory data analysis and model development  

---

## 📺 Project Demonstration

![Demonstration](projectDemo.gif)

---

## 🧪 How to Run Locally

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/your-repository-name.git
   cd your-repository-name

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   
3. Run the app:
   ```bash
   python main.py 
   
