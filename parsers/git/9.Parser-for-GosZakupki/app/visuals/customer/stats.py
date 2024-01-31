# Internal
from backend.connection.connector import DB
# External
import pandas as pd


def get_customers():
    query = """
    SELECT  customer_inn, name
    FROM    public.customers c
    LEFT    JOIN public.entities e ON c.customer_inn=e.inn
    """
    customers = DB.execute(query)
    return customers


def get_suppliers_relation(inn: int) -> pd.DataFrame:
    query = """
        SELECT  date_part('year', publication_date::date) as purchase_year,
                inn as supplier_inn,
                name as supplier_name,
                round(sum(start_price_kopeks)/1e5, 2) as start_prices,
                round(sum(end_price_kopeks)/1e5, 2) as end_prices,
                round(1-(sum(end_price_kopeks)/sum(start_price_kopeks)::decimal), 2) as price_change,
                round(avg(num_participants), 2) as avg_participants
        FROM    public.customers c
        INNER   JOIN public.purchases p ON c.purchase_id=p.purchase_id
        INNER   JOIN public.entities e ON p.winner_inn=e.inn
        WHERE   customer_inn = '7808043833'
        GROUP BY purchase_year, supplier_inn, supplier_name
        ORDER BY purchase_year DESC, end_prices DESC
        """
    data = DB.execute(query)
    return data

