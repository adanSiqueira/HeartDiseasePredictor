from dash import Dash, dcc, html
from dash.dependencies import Output, Input
import dash_bootstrap_components as dbc
import pages
from app import app


nav = dbc.Nav(
    [   dbc.NavItem(dbc.NavLink("Heart Disease Prediction", href="/form")),
        dbc.NavItem(dbc.NavLink("Graphic Analysis", href="/charts")),       
    ],
    pills=True,
)

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    nav,
    html.Div(id='content')
])

@app.callback(
        Output('content', 'children'),
        Input('url', 'pathname')     
)


def show_page(pathname):
    if pathname == '/form':
        return pages.form.layout
    elif pathname == '/charts':
        return pages.charts.layout
        # return html.P('pages')
    else:
        return html.P('homepage')
    
app.run(debug = True)