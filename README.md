# Heart Disease Prediction Dashboard
<a target="_blank" href="https://cookiecutter-data-science.drivendata.org/">
    <img src="https://img.shields.io/badge/CCDS-Project%20template-328F97?logo=cookiecutter" />
</a>

<br>This web application allows users to input clinical data of a patient, such as age, sex, blood pressure, cholesterol, and others, to predict whether the patient is at risk of heart disease using a machine learning model.

## Features
The app contains two main sections:
1. **Heart Disease Prediction**:
   - Users can input various clinical metrics.
   - The application uses an **XGBoost** model to predict whether a patient is at risk for heart disease based on these inputs.
   - The model was trained using data from the Cleveland Clinic Heart Disease dataset.

2. **Graphic Analysis**:
   - Visualizes exploratory analysis of the dataset.
   - Uses **Plotly** to generate graphs, exploring relationships between features like age, sex, cholesterol, and more, in relation to the occurrence of heart disease.

## Technologies Used:
- **Dash** and **Dash Bootstrap** for the web framework and UI components.
- **Pandas** and **NumPy** for data manipulation.
- **Plotly** for interactive visualizations.
- **XGBoost** for building the machine learning model.
- **ucimlrepo API** to fetch the dataset.

## Project Structure:
```plaintext
.env
.gitignore
app.py
main.py
Makefile
pyproject.toml
README.md
requirements.txt
__init__.py

├───data
│   ├───data_loader.py
│   └───__init__.py

├───model
│   ├───model_HD.pkl
│   └───model_training.py

├───notebooks
│   └───HeartDisease_Predictions.ipynb

├───pages
│   ├───charts.py
│   ├───form.py
│   └───__init__.py

├───src
│   ├───dataset.py
│   └───__init__.py
