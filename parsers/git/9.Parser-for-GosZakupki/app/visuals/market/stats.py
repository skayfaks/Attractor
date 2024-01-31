# Internal
from backend.connection.connector import DB
# External
import pandas as pd
import plotly.graph_objects as go


def get_top_customers(region: int, industry: str, subindustry: int,
                      date_start: str, date_end: str) -> pd.DataFrame:
    query = fr"""
    SELECT  customer_inn, currency,
            count(*) total_purchases,
            round(sum(start_price_kopeks)/1e5, 2) total_start_price,
            round(sum(end_price_kopeks)/1e5, 2) total_end_price,
            round(avg(end_price_kopeks/start_price_kopeks::decimal), 2)-1 avg_price_change,
            round(avg(num_participants), 2) avg_num_participants
    FROM    public.regions r
    INNER   JOIN (SELECT * FROM public.industries) i USING (purchase_id)
    INNER   JOIN (SELECT * FROM public.purchases) p USING (purchase_id)
    INNER   JOIN (SELECT purchase_id, customer_inn, name customer_name FROM public.customers c
                  INNER JOIN public.entities e ON c.customer_inn = e.inn) c USING (purchase_id)
    WHERE   region_id = {region}
            AND industry = '{industry}'
            AND subindustry_id = {subindustry}
            AND publication_date BETWEEN '{date_start}' AND '{date_end}'
    GROUP   BY  customer_inn, currency
    ORDER   BY  total_purchases DESC
    """
    result = DB.execute(query)
    return result


def get_top_suppliers(region: int, industry: str, subindustry: int,
                      date_start: str, date_end: str) -> pd.DataFrame:
    query = fr"""
    SELECT  winner_inn supplier_inn, currency,
            count(*) total_purchases,
            sum(start_price_kopeks)/1e5 total_start_price,
            sum(end_price_kopeks)/1e5 total_end_price,
            round(avg(end_price_kopeks/start_price_kopeks::decimal), 2)-1 avg_price_change,
            round(avg(num_participants), 2) avg_num_participants
    FROM    public.regions r
    INNER   JOIN (SELECT * FROM public.industries) i USING (purchase_id)
    INNER   JOIN (SELECT * FROM public.purchases) p USING (purchase_id)
    INNER   JOIN (SELECT * FROM public.entities) e ON (e.inn = p.winner_inn)
    WHERE   region_id = {region}
            AND industry = '{industry}'
            AND subindustry_id = {subindustry}
            AND publication_date BETWEEN '{date_start}' AND '{date_end}'
    GROUP   BY  supplier_inn, currency
    ORDER   BY  total_purchases DESC
    """
    result = DB.execute(query)
    return result


def get_top_objects(region: int, industry: str, subindustry: int,
                    date_start: str, date_end: str) -> pd.DataFrame:
    query = f"""
    SELECT  code_type, code,
            sum(amount) total_purchase_number,
            round(avg(unit_price_kopeks/1e5), 2) avg_unit_price,
            round(sum(total_price_kopeks/1e5), 2) total_purchase_price
    FROM    public.regions r
    INNER   JOIN (SELECT * FROM public.industries) i USING (purchase_id)
    INNER   JOIN (SELECT * FROM public.purchases) p USING (purchase_id)
    INNER   JOIN (SELECT * FROM public.objects) o USING (purchase_id)
    WHERE   region_id = {region}
            AND industry = '{industry}'
            AND subindustry_id = {subindustry}
            AND publication_date BETWEEN '{date_start}' AND '{date_end}'
    GROUP BY code_type, code
    ORDER BY total_purchase_price DESC
    """
    result = DB.execute(query)
    return result


def get_plot_change_prices(region: int, industry: str, subindustry: int,
                           date_start: str, date_end: str) -> go.Figure:
    query = fr"""
    SELECT  purchase_id, publication_date::date,
            round(end_price_kopeks / start_price_kopeks::decimal, 2)-1 price_change
    FROM    public.purchases p
    INNER   JOIN (SELECT * FROM public.regions) r USING (purchase_id)
    INNER   JOIN (SELECT * FROM public.industries) i USING (purchase_id)
    WHERE   region_id = {region}
            AND industry = '{industry}'
            AND subindustry_id = {subindustry}
            AND publication_date BETWEEN '{date_start}' AND '{date_end}'
    """
    data = DB.execute(query)

    fig = go.Figure()
    fig.add_trace(go.Histogram(x=data['price_change'], opacity=0.5))
    fig.update_layout(
        bargap=0.1,
        legend_x=0,
        legend_y=1,
        legend_bgcolor='rgba(255,255,255,0.3)',
        font_size=15,
        font_family='Roboto',
        font_color='#333'
    )
    fig.update_layout(
        margin=dict(l=0, t=0, r=0, b=0),
        xaxis_title='Изменение цены',
        yaxis_title='Количество заказов'
    )
    return fig


def get_plot_prices(region: int, industry: str, subindustry: int,
                    date_start: str, date_end: str) -> go.Figure:
    query = fr"""
    SELECT  purchase_id, start_price_kopeks/1e5 start_price, end_price_kopeks/1e5 end_price
    FROM    public.purchases p
    INNER   JOIN (SELECT * FROM public.regions) r USING (purchase_id)
    INNER   JOIN (SELECT * FROM public.industries) i USING (purchase_id)
    WHERE   region_id = {region}
            AND industry = '{industry}'
            AND subindustry_id = {subindustry}
            AND publication_date BETWEEN '{date_start}' AND '{date_end}'
    """
    data = DB.execute(query)

    fig = go.Figure()
    fig.add_trace(go.Histogram(name='Начальная цена', x=data['start_price'], opacity=0.5))
    fig.add_trace(go.Histogram(name='Конечная цена', x=data['end_price'], opacity=0.5))
    fig.update_layout(
        bargap=0.1,
        legend_x=0,
        legend_y=1,
        legend_bgcolor='rgba(255,255,255,0.3)',
        font_size=15,
        font_family='Roboto',
        font_color='#333'
    )
    fig.update_layout(
        margin=dict(l=0, t=0, r=0, b=0),
        xaxis_title='Цены [тыс.руб.]',
        yaxis_title='Количество заказов',
    )

    return fig
