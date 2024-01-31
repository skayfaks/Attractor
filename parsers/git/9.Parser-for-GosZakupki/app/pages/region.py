# Dash Components
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_table
from dash.dependencies import Input, Output, State

# Internal
from app import app
from components import inputs
from visuals.region import stats


@app.callback(
    Output('page_region_table_stats', 'children'),
    [Input('inputs_submit', 'n_clicks')],
    [State('inputs_region_selector', 'value'),
     State('inputs_industry_selector', 'value'),
     State('inputs_subindustry_selector', 'value'),
     State('inputs_date_range', 'start_date'),
     State('inputs_date_range', 'end_date')]
)
def render_table_region_stats(click, region, industry, subindustry, start_date, end_date):
    data = stats.get_region_stats(region, start_date, end_date)
    columns = [{"name": column, "id": column, "deletable": False, "selectable": False}
               for column in data.columns]
    data = data.to_dict('records')
    table = dash_table.DataTable(
        id="table_region_stats",
        columns=columns,
        data=data,
        filter_action="native",
        sort_action="native",
        sort_mode="multi",
        page_action="native",
        page_current=0,
        page_size=20,
        style_as_list_view=True,
        style_data_conditional=[{'if': {'row_index': 'odd'},
                                 'backgroundColor': 'rgb(245, 245, 245)'}],
        style_header={'backgroundColor': 'rgb(220, 220, 220)',
                      'fontWeight': 'bold'},
    )
    return table


# View
layout = \
    dbc.Container([
        inputs.layout,
        dbc.Row([
            dbc.Col([
                dbc.Card([
                    dbc.CardHeader("Статистика по региону"),
                    dbc.CardBody([
                        html.Div(id="page_region_table_stats", className='data-table'),
                    ]),
                ]),
            ], md=12),
        ]),
    ])
