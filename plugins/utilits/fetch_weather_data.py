from airflow.providers.postgres.hooks.postgres import PostgresHook
import pandas as pd


def fetch_weather_data():
    db_hook = PostgresHook(postgres_conn_id='my_db1')

    sql = """
          SELECT city,  time, temperature
          FROM weather
          WHERE time >= CURRENT_DATE - INTERVAL '7 days'; \
          """

    df = db_hook.get_pandas_df(sql)
    return df
