import dash_bootstrap_components as dbc
import dash_html_components as html

layout = \
    dbc.Container([
        dbc.Row([
            dbc.Col([
                html.Div(id="main-logo"),
                html.P(f"Welcome!", id="main-brand")
            ], id="main-col")
        ])
    ], fluid=True)
