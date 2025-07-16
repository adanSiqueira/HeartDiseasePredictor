from dash import dcc, html
from dash.dependencies import Output, Input
import dash_bootstrap_components as dbc
import pages
from app import app
import os


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
    elif pathname == '/' or pathname == '':
        return html.Div([
            html.H3('Use the tabs above to navigate', className='text-center text-dark mb-2 mt-3', style={'fontWeight': '200'}),
            html.Img(src='/assets/banner.png', style={'width': '100%', 'height': 'auto'})
        ])
    else:
        return html.P("Page not found.") 
    
# app.run(debug = False)
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8050))
    app.run(host="0.0.0.0", port=port, debug=False)