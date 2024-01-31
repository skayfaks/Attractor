# Dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
# Internal
from app import app, server
# Components
from components import navigation
# Pages
from pages import main
from pages import region
from pages import market
from pages import customer
from pages import supplier


# Main View
location = dcc.Location(id="url", refresh=False)
content = html.Div(id='page-content')
app.layout = html.Div([location, navigation.sidebar, content], id='layout')


# SPA Controller updates content without refreshing
@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname == '/':
        return main.layout
    elif pathname == '/region/':
        return region.layout
    elif pathname == '/market/':
        return market.layout
    elif pathname == '/customer/':
        return customer.layout
    else:
        return pathname
    return '404'
