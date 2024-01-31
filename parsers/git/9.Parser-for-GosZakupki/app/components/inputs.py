# Python
from datetime import date
# Dash components
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
# Internal
from components.names import REGION_NAMES
from backend.connection.connector import DB
from app import app

# TODO: Refactor all this shit ...


def render_region_selector() -> dcc.Dropdown:
    query = """
        SELECT DISTINCT region_id
        FROM public.regions
        ORDER BY region_id
        """
    regions = DB.execute(query).region_id.values
    options = [{'label': label, 'value': value}
               for value, label in REGION_NAMES.items() if value in regions]
    selector = dcc.Dropdown(options=options,
                            value=78,
                            id='inputs_region_selector')
    return selector


def render_industry_selector() -> dcc.Dropdown:
    query = """
    SELECT DISTINCT industry
    FROM public.industries
    ORDER BY industry
    """
    industries = DB.execute(query).industry.values
    options = [{'label': industry, 'value': industry} for industry in industries]
    selector = dcc.Dropdown(options=options,
                            value='Медицина',
                            id='inputs_industry_selector')
    return selector


def render_subindustry_selector() -> dcc.Dropdown:
    return dcc.Dropdown(options=[], value=0, id='inputs_subindustry_selector')


def render_date_range() -> dcc.DatePickerRange:
    date_picker = dcc.DatePickerRange(
        start_date_placeholder_text='Начало периода',
        end_date_placeholder_text='Конец периода',
        display_format='YYYY-MM-DD',
        first_day_of_week=1,
        start_date=date.today().replace(month=1, day=1),
        end_date=date.today(),
        id='inputs_date_range'
    )
    return date_picker


@app.callback(
    [Output('inputs_subindustry_selector', 'options'),
     Output('inputs_subindustry_selector', 'value')],
    [Input('inputs_industry_selector', 'value')]
)
def update_subindustry_selector(industry: str):
    query = fr"""
    SELECT DISTINCT subindustry_id
    FROM public.industries
    WHERE industry = '{industry or ''}'
    ORDER BY subindustry_id
    """
    subindustries = DB.execute(query).subindustry_id.values
    options = [{'label': subindustry, 'value': subindustry} for subindustry in subindustries]
    return options, options[0]['value']


layout =\
    dbc.Row([
        dbc.Col([html.P('Регион'), render_region_selector()], md=4),
        dbc.Col([html.P('Рынок'), render_industry_selector(), render_subindustry_selector()], md=4),
        dbc.Col([html.P('Период'), render_date_range()], md=4),
        dbc.Col(dbc.Button("Поиск", outline=True, color="primary", id='inputs_submit'), md=12)
    ], id='page_region_inputs')


