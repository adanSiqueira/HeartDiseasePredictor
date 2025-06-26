from ucimlrepo import fetch_ucirepo
import pandas as pd
import plotly.express as px
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
from src import dataset, graph_components

df = dataset.df

fig_hist_age_ill = graph_components.hist_age_ill
fig_boxplot_age_ill = graph_components.box_age_ill
fig_hist_sex_ill = graph_components.hist_sex_ill
fig_hist_chol_sex = graph_components.hist_chol_sex


div_histogram_age_ill = html.Div([
        dcc.Graph(figure=fig_hist_age_ill)])
div_boxplot_age_ill = html.Div([
        dcc.Graph(figure=fig_boxplot_age_ill)])
div_histogram_sex_ill = html.Div([
        dcc.Graph(figure=fig_hist_sex_ill)])
div_hist_chol_sex = html.Div([
        dcc.Graph(figure=fig_hist_chol_sex)])

layout = html.Div([
    html.H4('Data Analysis of UCI Repository Heart Disease', className='text-center text-dark mb-2 mt-3'),
    dbc.Container([
        dbc.Row([
            # html.H4('Heart Disease Distribution per Age', style={'fontWeight': 'bold'}, className='mb-4 mt-3'),
            dbc.Col([div_histogram_age_ill]),
            dbc.Col([div_boxplot_age_ill]) 
        ]),
        dbc.Row([
            dbc.Col(#[html.H4('Heart Disease Distribution per Sex',
                            # style={'fontWeight': 'bold'},
                            # className='mb-6 mt-3'),
                            div_histogram_sex_ill),
            dbc.Col(#[html.H4('Cholesterol Distribution per Sex',
                            # style={'fontWeight': 'bold'},
                            # className='mb-6 mt-3'),
                            div_hist_chol_sex) 
        ])
    ]) 
])