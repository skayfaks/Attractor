# Dash Components
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_table
from dash.dependencies import Input, Output, State

# Internal
from app import app
from components import inputs
from visuals.market import stats


@app.callback(
    Output('page_market_table_top_customers', 'children'),
    [Input('inputs_submit', 'n_clicks')],
    [State('inputs_region_selector', 'value'),
     State('inputs_industry_selector', 'value'),
     State('inputs_subindustry_selector', 'value'),
     State('inputs_date_range', 'start_date'),
     State('inputs_date_range', 'end_date')]
)
def render_table_top_customers(click, region, industry, subindustry, start_date, end_date):
    data = stats.get_top_customers(region, industry, subindustry, start_date, end_date)
    rename = {'customer_inn': 'ИНН',
              'currency': 'Валюта',
              'total_purchases': 'Закупок',
              'total_start_price': 'Сум. нач. цен [т.р.]',
              'total_end_price': 'Сум. кон. цен [т.р.]',
              'avg_price_change': 'Ср. изменение цены',
              'avg_num_participants': 'Ср. конкуренция'}
    columns = [{"name": rename[column], "id": column, "deletable": False, "selectable": False}
               for column in data.columns]
    data = data.to_dict('records')
    table = dash_table.DataTable(
        id="table_top_customers",
        columns=columns,
        data=data,
        filter_action="native",
        sort_action="native",
        sort_mode="multi",
        page_action="native",
        page_current=0,
        page_size=10,
        style_as_list_view=True,
        style_data_conditional=[{'if': {'row_index': 'odd'},
                                 'backgroundColor': 'rgb(245, 245, 245)'}],
        style_header={'backgroundColor': 'rgb(220, 220, 220)',
                      'fontWeight': 'bold'},
        style_cell={'whiteSpace': 'normal', 'height': 'auto'}
    )
    return table


@app.callback(
    Output('page_market_table_top_suppliers', 'children'),
    [Input('inputs_submit', 'n_clicks')],
    [State('inputs_region_selector', 'value'),
     State('inputs_industry_selector', 'value'),
     State('inputs_subindustry_selector', 'value'),
     State('inputs_date_range', 'start_date'),
     State('inputs_date_range', 'end_date')]
)
def render_table_top_suppliers(click, region, industry, subindustry, start_date, end_date):
    data = stats.get_top_suppliers(region, industry, subindustry, start_date, end_date)
    rename = {'supplier_inn': 'ИНН',
              'currency': 'Валюта',
              'total_purchases': 'Всего закупок',
              'total_start_price': 'Сум. ныч. цен [т.р.]',
              'total_end_price': 'Сум. кон. цен [т.р.]',
              'avg_price_change': 'Ср. изменение цены',
              'avg_num_participants': 'Ср. конкуренция'}
    columns = [{"name": rename[column], "id": column, "deletable": False, "selectable": False}
               for column in data.columns]
    data = data.to_dict('records')
    table = dash_table.DataTable(
        id="table_top_suppliers",
        columns=columns,
        data=data,
        filter_action="native",
        sort_action="native",
        sort_mode="multi",
        page_action="native",
        page_current=0,
        page_size=10,
        style_as_list_view=True,
        style_data_conditional=[{'if': {'row_index': 'odd'},
                                 'backgroundColor': 'rgb(245, 245, 245)'}],
        style_header={'backgroundColor': 'rgb(220, 220, 220)',
                      'fontWeight': 'bold'},
        style_cell={'whiteSpace': 'normal', 'height': 'auto'}
    )
    return table


@app.callback(
    Output('page_market_table_top_objects', 'children'),
    [Input('inputs_submit', 'n_clicks')],
    [State('inputs_region_selector', 'value'),
     State('inputs_industry_selector', 'value'),
     State('inputs_subindustry_selector', 'value'),
     State('inputs_date_range', 'start_date'),
     State('inputs_date_range', 'end_date')]
)
def render_table_top_objects(click, region, industry, subindustry, start_date, end_date):
    data = stats.get_top_objects(region, industry, subindustry, start_date, end_date)
    rename = {
        'code_type': 'Тип',
        'code': 'Код',
        'total_purchase_number': 'Закупок',
        'avg_unit_price': 'Ср. цена за ед. [т.р.]',
        'total_purchase_price': 'Суммы закупок [т.р.]'
    }
    columns = [{"name": rename[column], "id": column, "deletable": False, "selectable": False}
               for column in data.columns]
    data = data.to_dict('records')
    table = dash_table.DataTable(
        id="table_top_objects",
        columns=columns,
        data=data,
        filter_action="native",
        sort_action="native",
        sort_mode="multi",
        page_action="native",
        page_current=0,
        page_size=10,
        style_as_list_view=True,
        style_data_conditional=[{'if': {'row_index': 'odd'},
                                 'backgroundColor': 'rgb(245, 245, 245)'}],
        style_header={'backgroundColor': 'rgb(220, 220, 220)',
                      'fontWeight': 'bold'},
        style_cell={'whiteSpace': 'normal', 'height': 'auto'}
    )
    return table


@app.callback(
    Output('page_market_plot_change_prices', 'figure'),
    [Input('inputs_submit', 'n_clicks')],
    [State('inputs_region_selector', 'value'),
     State('inputs_industry_selector', 'value'),
     State('inputs_subindustry_selector', 'value'),
     State('inputs_date_range', 'start_date'),
     State('inputs_date_range', 'end_date')]
)
def render_plot_change_prices(click, region, industry, subindustry, start_date, end_date):
    plot = stats.get_plot_change_prices(region, industry, subindustry, start_date, end_date)
    return plot


@app.callback(
    Output('page_market_plot_prices', 'figure'),
    [Input('inputs_submit', 'n_clicks')],
    [State('inputs_region_selector', 'value'),
     State('inputs_industry_selector', 'value'),
     State('inputs_subindustry_selector', 'value'),
     State('inputs_date_range', 'start_date'),
     State('inputs_date_range', 'end_date')]
)
def render_plot_prices(click, region, industry, subindustry, start_date, end_date):
    plot = stats.get_plot_prices(region, industry, subindustry, start_date, end_date)
    return plot


@app.callback(
    Output('debugger_div', 'children'),
    [Input('page_market_plot_change_prices', 'selectedData')]
)
def selected_data(selected):
    print(selected)


# View
layout = \
    dbc.Container([
        inputs.layout,
        dbc.Row([
            dbc.Col([
                dbc.Card([
                    dbc.CardHeader("Заказчики"),
                    dbc.CardBody([
                        html.Div(id="page_market_table_top_customers", className='data-table'),
                    ]),
                ]),
            ], md=12),
        ]),
        dbc.Row([
            dbc.Col([
                dbc.Card([
                    dbc.CardHeader("Поставщики"),
                    dbc.CardBody([
                        html.Div(id="page_market_table_top_suppliers", className='data-table'),
                    ]),
                ]),
            ], md=12),
        ]),
        dbc.Row([
            dbc.Col([
                dbc.Card([
                    dbc.CardHeader("Объекты закупок"),
                    dbc.CardBody([
                        html.Div(id="page_market_table_top_objects", className='data-table'),
                    ]),
                ]),
            ], md=12),
        ]),
        dbc.Row([
            dbc.Col([
                dbc.Card([
                    dbc.CardHeader("Гистограмма изменения цен"),
                    dbc.CardBody([
                        dcc.Graph(id="page_market_plot_change_prices"),
                    ]),
                ]),
            ], md=12),
        ]),
        dbc.Row([
            dbc.Col([
                dbc.Card([
                    dbc.CardHeader("Гистограмма распределения цен"),
                    dbc.CardBody([
                        dcc.Graph(id="page_market_plot_prices"),
                    ]),
                ]),
            ], md=12),
        ]),
        html.P(id='debugger_div')
    ])
