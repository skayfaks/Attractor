# Dash components
import dash_bootstrap_components as dbc
import dash_core_components as dcc
from dash.dependencies import Input, Output, State
# Internal
from visuals.customer import stats
from app import app
# External
import plotly.graph_objects as go




@app.callback(
    Output('page_customer_plot_suppliers_relation', 'figure'),
    [Input('page_customer_suppliers_relation_slider', 'value')]
)
def render_suppliers_relation(year):
    data = stats.get_suppliers_relation(inn=1)

    # Build the figure
    fig = go.Figure()
    selected = data.query(f"purchase_year == {year}")
    fig.add_trace(go.Pie(
        labels=selected['supplier_name'],
        values=selected['end_prices'],
        customdata=selected['supplier_inn'],
        hoverinfo='label+percent',
        textinfo='percent',
        hovertemplate=r"""<b>%{label}</b>
        <br><b>ИНН</b>: %{customdata}
        <br><b>Контрактов</b>: %{value} т.р.
        <br><b>Доля</b>: %{percent}%
        """
    ))
    fig.update_layout(
        margin=dict(l=0, t=0, r=0, b=0),
        font_size=15,
        font_family='Roboto',
        font_color='#333'
    )

    return fig


slider = dcc.Slider(
    min=2015,
    max=2020,
    value=2020,
    marks={i: i for i in range(2015, 2021)},
    id='page_customer_suppliers_relation_slider'
)


layout = \
    dbc.Container([
        dbc.Row([
            dbc.Col([]),
        ], md=12),
        dbc.Row([
            dbc.Col([
                dbc.Card([
                    dbc.CardHeader("Основные поставщики"),
                    dbc.CardBody([
                        dcc.Graph(id="page_customer_plot_suppliers_relation"),
                        slider
                    ]),
                ]),
            ], md=12),
        ]),
    ])
