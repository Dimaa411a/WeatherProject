import sys

sys.path.append('/')

from airflow import DAG
from datetime import datetime
from plugins.custom_operators.fetch_weatherAPI_operator import FetchWeatherAPIOperator

with DAG(
    dag_id='insert_weather_dag',
    schedule='0 * * * *',
    catchup=False,
    description='Insert data into database',
    start_date=datetime(2025, 7, 20),
    ) as dag:
        task1 = FetchWeatherAPIOperator(
            task_id='fetch_insert_weather',
            cities = ['Kyiv', 'Lviv', '48.91902196240606,24.723477542074683','Kalush','Prague','California','Toronto']
        )
