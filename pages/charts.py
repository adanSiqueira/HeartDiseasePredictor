from ucimlrepo import fetch_ucirepo
import pandas as pd
import plotly.express as px
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
from src import dataset

df = dataset.df

fig_hist = px.histogram(df, x = 'age', color = 'ill', barmode = 'group')
fig_boxplot = px.box(df, x='age', y = 'ill', color = 'ill')

div_histogram = html.Div([
        dcc.Graph(figure=fig_hist)])

div_boxplot = html.Div([
        dcc.Graph(figure=fig_boxplot)])

layout = html.Div([
    html.H4('Data Analysis of UCI Repository Heart Disease', className='text-center text-dark mb-2 mt-3'),
    dbc.Container([
        dbc.Row([
            html.H4('Heart Disease Distribution per Age', style={'fontWeight': 'bold'}, className='mb-2 mt-3'),
            dbc.Col([div_histogram]),
            dbc.Col([div_boxplot]) 
        ])
    ]) 
])