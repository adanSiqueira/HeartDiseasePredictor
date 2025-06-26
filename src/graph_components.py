import plotly.express as px
from src import dataset

df = dataset.df
df_ill = dataset.df_ill
df_not_ill = dataset.df_not_ill

custom_colors = ['#4C78A8', '#F58518']

#Ill x Age histogram
hist_age_ill = px.histogram(
    df,
    x='age',
    color='ill',
    barmode='overlay', #group
    color_discrete_sequence=custom_colors,
    histnorm='percent'  # <<--- normaliza para porcentagem
)
newnames = {'0': 'Non risk group', '1': 'Risk group'}
hist_age_ill.for_each_trace(lambda t: t.update(
    name=newnames[t.name],
    legendgroup=newnames[t.name],
    hovertemplate=t.hovertemplate.replace(t.name, newnames[t.name])
))
hist_age_ill.update_layout(
    title={
        'text': 'Percentage Distribution of Heart Disease Risk by Age',
        'y': 0.95,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top'
    },
    xaxis_title='Age',
    yaxis_title='Percentage (%)',
    legend_title='Risk Group',
    template='plotly_white',
    font=dict(family='Arial', size=14, color='black'),
    bargap=0.1,
    margin=dict(l=40, r=40, t=80, b=40)
)
# IllxAge Boxplot
box_age_ill = px.box(
    df,
    x='ill',
    y='age',
    color='ill',
    color_discrete_sequence=custom_colors,
    points='all',  # exibe todos os pontos (opcional: 'outliers', 'suspectedoutliers', False)
)

box_age_ill.for_each_trace(lambda t: t.update(
    name=newnames[t.name],
    legendgroup=newnames[t.name],
    hovertemplate=t.hovertemplate.replace(t.name, newnames[t.name])
))
box_age_ill.update_layout(
    title={
        'text': 'Age Distribution by Heart Disease Risk Group',
        'y': 0.95,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top'
    },
    xaxis_title='Risk Group',
    yaxis_title='Age',
    legend_title='Risk Group',
    template='plotly_white',
    font=dict(family='Arial', size=14, color='black'),
    margin=dict(l=40, r=40, t=80, b=40)
)


# 🔵 Novas cores (ex: roxo e verde)
custom_colors_sex = ['#7A5195', '#43AA8B']  # Feminino (0), Masculino (1)

# Legendas adaptadas
newnames_sex = {'0': 'Female (Non risk)', '1': 'Male (Risk)'}

# Histograma de distribuição percentual por sexo
hist_sex_ill = px.histogram(
    df,
    x='sex',
    color='ill',
    barmode='group',
    color_discrete_sequence=custom_colors_sex,
    histnorm='percent'
)

hist_sex_ill.for_each_trace(lambda t: t.update(
    name=newnames[str(int(t.name))],
    legendgroup=newnames[str(int(t.name))],
    hovertemplate=t.hovertemplate.replace(t.name, newnames[str(int(t.name))])
))
hist_sex_ill.update_layout(
    title={
        'text': 'Percentage Distribution of Risk Group by Sex',
        'y': 0.95,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top'
    },
    xaxis_title='Sex (0 = Female, 1 = Male)',
    yaxis_title='Percentage (%)',
    legend_title='Risk Group',
    template='plotly_white',
    font=dict(family='Arial', size=14, color='black'),
    bargap=0.2,
    margin=dict(l=40, r=40, t=80, b=40)
)

#histograma chol
newnames_chol_sex = {'0': 'Female', '1': 'Male'}

# Histogram of cholesterol distribution by sex (in percentage)
hist_chol_sex = px.histogram(
    df,
    x='chol',
    color='sex',
    barmode='overlay',
    color_discrete_sequence=custom_colors_sex,
    histnorm='percent'
)

# Update trace names for legend and hover
hist_chol_sex.for_each_trace(lambda t: t.update(
    name=newnames_chol_sex[str(int(t.name))],
    legendgroup=newnames_chol_sex[str(int(t.name))],
    hovertemplate=t.hovertemplate.replace(t.name, newnames_chol_sex[str(int(t.name))])
))

# Layout formatting
hist_chol_sex.update_layout(
    title={
        'text': 'Percentage Distribution of Cholesterol Levels by Sex',
        'y': 0.95,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top'
    },
    xaxis_title='Cholesterol (mg/dL)',
    yaxis_title='Percentage (%)',
    legend_title='Sex',
    template='plotly_white',
    font=dict(family='Arial', size=14, color='black'),
    bargap=0.1,
    margin=dict(l=40, r=40, t=80, b=40)
)

custom_colors_thalach = ['#1B2A41', '#BF1A2F']  # Azul escuro e vermelho escuro

# Histogram: Max Heart Rate by Risk Group
hist_thalach_ill = px.histogram(
    df,
    x='thalach',
    color='ill',
    barmode='overlay',
    color_discrete_sequence=custom_colors_thalach,
    histnorm='percent'
)

hist_thalach_ill.for_each_trace(lambda t: t.update(
    name=newnames[t.name],
    legendgroup=newnames[t.name],
    hovertemplate=t.hovertemplate.replace(t.name, newnames[t.name])
))

hist_thalach_ill.update_layout(
    title={
        'text': 'Percentage Distribution of Risk Group by Maximum Heart Rate',
        'y': 0.95,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top'
    },
    xaxis_title='Maximum Heart Rate (thalach)',
    yaxis_title='Percentage (%)',
    legend_title='Risk Group',
    template='plotly_white',
    font=dict(family='Arial', size=14, color='black'),
    bargap=0.1,
    margin=dict(l=40, r=40, t=80, b=40)
)

# Boxplot: Max Heart Rate by Sex
box_thalach_sex = px.box(
    df,
    x='sex',
    y='thalach',
    color='sex',
    color_discrete_sequence=custom_colors_thalach,
    points='all'
)

# Nome das classes de sexo
newnames_sex_simple = {'0': 'Female', '1': 'Male'}

box_thalach_sex.for_each_trace(lambda t: t.update(
    name=newnames_sex_simple[str(int(t.name))],
    legendgroup=newnames_sex_simple[str(int(t.name))],
    hovertemplate=t.hovertemplate.replace(t.name, newnames_sex_simple[str(int(t.name))])
))

box_thalach_sex.update_layout(
    title={
        'text': 'Maximum Heart Rate Distribution by Sex',
        'y': 0.95,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top'
    },
    xaxis_title='Sex (0 = Female, 1 = Male)',
    yaxis_title='Maximum Heart Rate (thalach)',
    legend_title='Sex',
    template='plotly_white',
    font=dict(family='Arial', size=14, color='black'),
    margin=dict(l=40, r=40, t=80, b=40)
)

# 🔸 Cores para sexo: rosa e azul claro
custom_colors_cp_sex = ['#E76F51', '#2A9D8F']  # 0: Female, 1: Male

# 🔸 Legenda formatada para sexo
newnames_cp_sex = {'0': 'Female', '1': 'Male'}

# 🔸 Histograma de distribuição percentual de tipos de dor no peito por sexo
hist_cp_sex = px.histogram(
    df_ill,
    x='cp',
    color='sex',
    barmode='group',
    color_discrete_sequence=custom_colors_cp_sex,
    histnorm='percent'
)

# Atualiza nomes da legenda e tooltip
hist_cp_sex.for_each_trace(lambda t: t.update(
    name=newnames_cp_sex[str(int(t.name))],
    legendgroup=newnames_cp_sex[str(int(t.name))],
    hovertemplate=t.hovertemplate.replace(t.name, newnames_cp_sex[str(int(t.name))])
))

# Estilo e formatação
hist_cp_sex.update_layout(
    title={
        'text': 'Percentage Distribution of Chest Pain Types by Sex (Patients with Heart Disease)',
        'y': 0.95,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top'
    },
    xaxis_title='Chest Pain Type',
    yaxis_title='Percentage (%)',
    legend_title='Sex',
    template='plotly_white',
    font=dict(family='Arial', size=14, color='black'),
    bargap=0.2,
    margin=dict(l=40, r=40, t=80, b=40),
    xaxis=dict(
        tickmode='array',
        tickvals=[1, 2, 3, 4],
        ticktext=[
            'Typical angina',
            'Atypical angina',
            'Non-anginal pain',
            'Asymptomatic'
        ]
    )
)

# 🔹 Cores alternativas para representar sexo em grupo saudável
custom_colors_cp_sex_not_ill = ['#A3A3C2', '#87CEEB']  # Female: lilás claro, Male: azul claro

# 🔹 Legenda adaptada
newnames_cp_sex = {'0': 'Female', '1': 'Male'}

# 🔹 Histograma para pacientes SEM doença cardíaca
hist_cp_sex_not_ill = px.histogram(
    df_not_ill,  # <- mudança aqui
    x='cp',
    color='sex',
    barmode='group',
    color_discrete_sequence=custom_colors_cp_sex_not_ill,
    histnorm='percent'
)

# Atualiza nomes da legenda e tooltip
hist_cp_sex_not_ill.for_each_trace(lambda t: t.update(
    name=newnames_cp_sex[str(int(t.name))],
    legendgroup=newnames_cp_sex[str(int(t.name))],
    hovertemplate=t.hovertemplate.replace(t.name, newnames_cp_sex[str(int(t.name))])
))

# Estilo e formatação do layout
hist_cp_sex_not_ill.update_layout(
    title={
        'text': 'Percentage Distribution of Chest Pain Types by Sex (Patients without Heart Disease)',
        'y': 0.95,
        'x': 0.5,
        'xanchor': 'center',
        'yanchor': 'top'
    },
    xaxis_title='Chest Pain Type',
    yaxis_title='Percentage (%)',
    legend_title='Sex',
    template='plotly_white',
    font=dict(family='Arial', size=14, color='black'),
    bargap=0.2,
    margin=dict(l=40, r=40, t=80, b=40),
    xaxis=dict(
        tickmode='array',
        tickvals=[1, 2, 3, 4],
        ticktext=[
            'Typical angina',
            'Atypical angina',
            'Non-anginal pain',
            'Asymptomatic'
        ]
    )
)