# Python
from pathlib import Path

# Dash Components
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State

# Internal
from app import app


# Check all pages existing in /pages folder
pages_location = Path(__file__).parent.parent / 'pages'
pages_names = [page.name.replace('.py', '') for page in pages_location.glob('*.py')]
pages_excluded = ['main']
pages = [page for page in pages_names if page not in pages_excluded]


sidebar_header = dbc.Row(
    [
        dbc.Col(dbc.NavLink("Parser", href="/", className="navbar-brand")),
        dbc.Col(
            [
                html.Button(
                    html.Span(className="navbar-toggler-icon"),
                    className="navbar-toggler",
                    id="navbar-toggle",
                ),
                html.Button(
                    html.Span(className="navbar-toggler-icon"),
                    className="navbar-toggler",
                    id="sidebar-toggle",
                ),
            ],
            width="auto",
            align="center",
        ),
    ]
)

links = dbc.Nav(
    [dbc.NavLink([html.I(className="icon ion-ios-clipboard"), page.capitalize()],
                 href=f"/{page}/", id=f"page-{page}-link")
     for page in pages],
    vertical=True,
    pills=True,
)
pathnames = [link.href for link in links.children]

sidebar = html.Div(
    [
        sidebar_header,
        # we wrap the horizontal rule and short blurb in a div that can be
        # hidden on a small screen
        html.Div(
            html.Hr(),
            id="blurb",
        ),
        # use the Collapse component to animate hiding / revealing links
        dbc.Collapse(
            links,
            id="collapse",
        ),
    ],
    id="sidebar",
)


# Active states in Menu
@app.callback(
    [Output(f"page-{page}-link", "active") for page in pages],
    [Input("url", "pathname")],
)
def toggle_active_links(pathname):
    return [pathname == path for path in pathnames]


@app.callback(
    Output("sidebar", "className"),
    [Input("sidebar-toggle", "n_clicks")],
    [State("sidebar", "className")],
)
def toggle_classname(n, classname):
    if n and classname == "":
        return "collapsed"
    return ""


@app.callback(
    Output("collapse", "is_open"),
    [Input("navbar-toggle", "n_clicks")],
    [State("collapse", "is_open")],
)
def toggle_collapse(n, is_open):
    if n:
        return not is_open
    return is_open
