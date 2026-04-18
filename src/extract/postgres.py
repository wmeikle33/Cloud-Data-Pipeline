
import pandas as pd
import psycopg2

def extract_table(query: str, conn) -> pd.DataFrame:
    return pd.read_sql(query, conn)
