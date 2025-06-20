<h1 align="center">Heart Disease Prediction Dashboard</h1>
<p align="center">
  <img src="https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue">
  <img src="https://img.shields.io/badge/Pandas-2C2D72?style=for-the-badge&logo=pandas&logoColor=white">
  <img src="https://img.shields.io/badge/Numpy-777BB4?style=for-the-badge&logo=numpy&logoColor=white">
  <img src="https://img.shields.io/badge/Plotly-239120?style=for-the-badge&logo=plotly&logoColor=white">
  <img src="https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white">
  <img src="https://img.shields.io/badge/scikit_learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white">
</p>

<br>This web application allows users to input clinical data of a patient, such as age, sex, blood pressure, cholesterol, and others, to predict whether the patient is at risk of heart disease using a machine learning model.

## Features
The app contains two main sections:
1. **Heart Disease Prediction**:
   - Users can input various clinical metrics.
   - The application uses an **XGBoostClassifier** model to predict whether a patient is at risk for heart disease based on these inputs.
   - The model was trained using data from the Cleveland Clinic Heart Disease dataset: https://archive.ics.uci.edu/dataset/45/heart+disease

2. **Graphic Analysis**:
   - Visualizes exploratory analysis of the dataset.
   - Uses **Plotly** to generate graphs, exploring relationships between features like age, sex, cholesterol, and more, in relation to the occurrence of heart disease.

## Technologies Used:
- **Dash** and **Dash Bootstrap** for the web framework and UI components.
- **Pandas** and **NumPy** for data manipulation.
- **Plotly** for interactive visualizations.
- **XGBoost** for building the machine learning model.
- **ucimlrepo API** to fetch the dataset.

## Project Demonstration:
![Demonstration](msedge_xYJKkdIWwN.gif)
