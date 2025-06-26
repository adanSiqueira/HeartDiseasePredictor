from dash import html, dcc
import dash_bootstrap_components as dbc
from src import graph_components

fig_hist_age_ill = graph_components.hist_age_ill
fig_boxplot_age_ill = graph_components.box_age_ill
fig_hist_sex_ill = graph_components.hist_sex_ill
fig_hist_chol_sex = graph_components.hist_chol_sex
fig_hist_thalach_ill = graph_components.hist_thalach_ill
fig_boxplot_thalach_sex = graph_components.box_thalach_sex
fig_hist_cp_sex = graph_components.hist_cp_sex
fig_hist_cp_sex_not_ill = graph_components.hist_cp_sex_not_ill

div_histogram_age_ill = html.Div([
        dcc.Graph(figure=fig_hist_age_ill)])
div_boxplot_age_ill = html.Div([
        dcc.Graph(figure=fig_boxplot_age_ill)])

div_histogram_sex_ill = html.Div([
        dcc.Graph(figure=fig_hist_sex_ill)])
div_hist_chol_sex = html.Div([
        dcc.Graph(figure=fig_hist_chol_sex)])

div_hist_thalach_ill = html.Div([
        dcc.Graph(figure=fig_hist_thalach_ill)])
div_box_thalach_sex = html.Div([
        dcc.Graph(figure=fig_boxplot_thalach_sex)])

div_hist_cp_sex = dcc.Graph(figure = fig_hist_cp_sex)

div_hist_cp_sex_not_ill = dcc.Graph(figure=fig_hist_cp_sex_not_ill)


layout = html.Div([
    html.H4('Data Analysis of UCI Repository Heart Disease', className='text-center text-dark mb-4 mt-4'),

    dbc.Container([

        # 🔹 Row 1 - Age vs Ill
        dbc.Row([
            dbc.Col(div_histogram_age_ill, md=6),
            dbc.Col(div_boxplot_age_ill, md=6),
        ], className='mb-5'),

        # 🔹 Row 2 - Sex vs Ill and Cholesterol vs Sex
        dbc.Row([
            dbc.Col(div_histogram_sex_ill, md=6),
            dbc.Col(div_hist_chol_sex, md=6),
        ], className='mb-5'),

        # 🔹 Row 3 - Thalach vs Ill and Thalach vs Sex
        dbc.Row([
            dbc.Col(div_hist_thalach_ill, md=6),
            dbc.Col(div_box_thalach_sex, md=6),
        ], className='mb-5'),

        # 🔹 Row 4 - Cp vs Sex - Ill
        dbc.Row([
        dbc.Col(html.Div([dcc.Graph(figure=fig_hist_cp_sex)]), md=12)
        ], 
        
        className='mb-5'),

        # 🔹 Row 5 - Cp vs Sex - Not Ill
        dbc.Row([
        dbc.Col(html.Div([dcc.Graph(figure=fig_hist_cp_sex_not_ill)]), md=12)
        ])
    ], fluid=True),
    
])
