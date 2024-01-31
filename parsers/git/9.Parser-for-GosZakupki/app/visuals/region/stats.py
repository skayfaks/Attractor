# Internal
from backend.connection.connector import DB
# External
import pandas as pd


def get_region_stats(region: int, date_start: str, date_end: str) -> pd.DataFrame:
    query = fr"""
    SELECT  law,
            industry,
            subindustry_id,
            count(DISTINCT customer_inn) customers,
            count(DISTINCT winner_inn) winners,
            round(sum(end_price_kopeks)/1e5, 2) total_purchases,
            round(avg(end_price_kopeks/start_price_kopeks::decimal), 2)-1 avg_price_change
    FROM    public.regions r
    LEFT JOIN (SELECT * FROM public.customers) c USING (purchase_id)
    LEFT JOIN (SELECT * FROM public.industries) i USING (purchase_id)
    LEFT JOIN (SELECT purchase_id, law, publication_date, start_price_kopeks, end_price_kopeks, winner_inn
                FROM public.purchases) p USING (purchase_id)
    WHERE   region_id = {region}
            AND publication_date BETWEEN '{date_start}' AND '{date_end}' 
    GROUP BY law, industry, subindustry_id
    """
    result = DB.execute(query)
    result.rename(columns={
        'law': 'ФЗ',
        'industry': 'Сегмент',
        'subindustry_id': 'Субсегмент',
        'customers': 'Заказчиков',
        'winners': 'Победителей',
        'total_purchases': 'Закупок [т.р.]',
        'avg_price_change': 'Ср. изменение цены'
    }, inplace=True)
    return result
