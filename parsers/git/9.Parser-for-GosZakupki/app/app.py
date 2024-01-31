# Flask
from flask import Flask
# Dash
from dash import Dash
import dash_bootstrap_components as dbc

#######################################################################################
# APP, SERVER
#######################################################################################

# Custom CSS
ionicons = {'href': 'https://unpkg.com/ionicons@4.5.10-0/dist/css/ionicons.min.css',
            'rel': 'stylesheet'}
bootstrap = dbc.themes.BOOTSTRAP
external_css = [bootstrap, ionicons]
# Meta tags
meta_tags = [{"name": "viewport", "content": "width=device-width, initial-scale=1"}]

# Init server
server = Flask(__name__)
# Init App
app = Dash(__name__,
           external_stylesheets=external_css,
           meta_tags=meta_tags,
           server=server)
app.title = 'Parser'
app.config.suppress_callback_exceptions = True  # Todo: Fix suppression?

