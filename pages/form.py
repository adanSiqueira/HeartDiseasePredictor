from dash import Dash, html, dcc
from dash.dependencies import Output, Input, State
import dash_bootstrap_components as dbc
from app import app

form = dbc.Container([
        dbc.Row([
            dbc.Col([
            #age 
                dbc.CardGroup([
                    dbc.Label('Age'),
                    dbc.Input(id = 'age', type = 'number', placeholder= 'Type the age')],
                    class_name='mb-3'), 
            #sex 
                dbc.CardGroup([
                    dbc.Label('Sex'),
                    dbc.Select(id='sex', options=[
                    {'label': 'Male', 'value': '1'},
                    {'label': 'Female', 'value': '0'}])],
                    class_name='mb-3'),
            #cp    
                dbc.CardGroup([
                    dbc.Label('Chest Pain'),
                    dbc.Select(id='cp', options=[
                        {'label': 'Typical angina', 'value': '1'},
                        {'label': 'Atypical angina', 'value': '2'},
                        {'label': 'Non-anginal pain', 'value': '3'},
                        {'label': 'Asymptomat', 'value': '4'}])],
                        class_name='mb-3'),
            #trestbps
                dbc.CardGroup([
                    dbc.Label('Resting Blood Pressure'),
                    dbc.Input(id = 'trestbps', type = 'number', placeholder= 'Type the resting blood pressure (mmHg)')],
                    class_name='mb-3'),
            #chol
                dbc.CardGroup([
                    dbc.Label('Cholesterol'),
                    dbc.Input(id = 'chol', type = 'number', placeholder= 'Type serum cholestoral (mg/dL)')],
                    class_name='mb-3'),
            #fbs 
                dbc.CardGroup([
                    dbc.Label('Fasting Blood Sugar (Upper 120 mg/dL)'),
                    dbc.Select(id='fbs', options=[
                    {'label': 'Yes', 'value': '1'},
                    {'label': 'No', 'value': '0'}])],
                    class_name='mb-3'),
            #restecg 
                dbc.CardGroup([
                    dbc.Label('Resting electrocardiographic results'),
                    dbc.Select(id='restecg', options=[
                    {'label': 'Normal', 'value': '0'},
                    {'label': 'Having ST-T wave abnormality (T wave inversions and/or ST elevation or depression of > 0.05 mV)', 'value': '1'},
                    {'label': 'Showing probable or definite left ventricular hypertrophy by Estes criteria', 'value': '2'}])],
                    class_name='mb-3')
            ]),
            dbc.Col([
            #thalach
                dbc.CardGroup([
                    dbc.Label('Maximum heart rate achieved'),
                    dbc.Input(id = 'thalach', type = 'number', placeholder= 'Type maximum heart rate achieved (bpm)')],
                    class_name='mb-3'),
            #exang 
                dbc.CardGroup([
                    dbc.Label('Exercise induced angina'),
                    dbc.Select(id='exang', options=[
                    {'label': 'Yes', 'value': '1'},
                    {'label': 'No', 'value': '0'}])],
                    class_name='mb-3'),
            #oldpeak
                dbc.CardGroup([
                    dbc.Label('ST depression induced by exercise relative to rest'),
                    dbc.Input(id = 'oldpeak', type = 'number', placeholder= 'Type ST depression (mm)')],
                    class_name='mb-3'),
            #slope 
                dbc.CardGroup([
                    dbc.Label('Slope of the peak exercise ST segment'),
                    dbc.Select(id='slope', options=[
                    {'label': 'Upsloping', 'value': '1'},
                    {'label': 'Flat', 'value': '2'},
                    {'label': 'Downsloping', 'value': '3'}])],
                    class_name='mb-3'),
            #ca
                dbc.CardGroup([
                    dbc.Label('Major vessels colored by flourosopy'),
                    dbc.Input(id = 'ca', type = 'number', placeholder= 'Type the number of major vessels colored by flourosopy(0-3)')],
                    class_name='mb-3'),
            #thal
                dbc.CardGroup([
                    dbc.Label('Thalassemia'),
                    dbc.Input(id = 'thal', type = 'number', placeholder= 'Type thalassemia (3 = normal; 6 = fixed defect; 7 = reversable defect)')],
                    class_name='mb-3'),
            #predict button
                dbc.CardGroup([
                    dbc.Button('Predict', id='predict-button', color='success', n_clicks=0)
                ], className='mb-3')
            ])
        ])
    ])

state_values= [
    State('age', 'value'),
    State('sex', 'value'),
    State('cp', 'value'),
    State('trestbps', 'value'),
    State('chol', 'value'),
    State('fbs', 'value'),
    State('restecg', 'value'),
    State('thalach', 'value'),
    State('exang', 'value'),
    State('oldpeak', 'value'),
    State('slope', 'value'),
    State('ca', 'value'),
    State('thal', 'value')
]

layout = html.Div([
    html.H1('Heart Disease Prediction', className='text-center text-dark mb-2 mt-3', style={'fontWeight': '500'}),
    html.P('Fill the following info below and click to predict if you are in a risk group of developing Heart Disease', className='text-center mb-3'),
    form,
    html.Div(id='prediction')
    ])

@app.callback(
    Output('prediction', 'children'),
    Input('predict-button', 'n_clicks'),
    state_values,
    prevent_initial_call = True
)

def predict_disease(n_clicks, age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal):
    if n_clicks == 0:
        return ''
    import joblib
    import pandas as pd
    import numpy as np

    model = joblib.load('model\model_HD.pkl')

    data = pd.DataFrame({
        'age': [age], 'sex': [sex], 'cp': [cp], 'trestbps': [trestbps], 'chol': [chol], 'fbs': [fbs], 'restecg': [restecg],
        'thalach': [thalach], 'exang': [exang], 'oldpeak': [oldpeak], 'slope': [slope], 'ca': [ca], 'thal': [thal]
    })

    data['oldpeak'] = data['oldpeak'].astype(np.float64)
    for col in data.columns: 
        if col != 'oldpeak':
            data[col] = data[col].astype(int)
    
    # dtest = xgb.DMatrix(data)
    prediction = model.predict(data)[0]
    if prediction == 1:
        message = f'You are in th risk group \n of having heart disease (80% accuracy)'
        allert_color = 'danger'
    else:
        message =  f'You are not in risk group'
        allert_color = 'success'
    
    alert = dbc.Alert(message, color = allert_color, class_name='d-flex mt-3')
    return alert