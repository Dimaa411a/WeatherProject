import datetime
from airflow import DAG
from custom_operators.get_weather_api_operator import GetWeatherAPIOperator
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime.datetime(2025, 9,23),
}

with DAG(
    'weather_actions_DAG',
    default_args=default_args,
    schedule = '0 * * * *',
    catchup = True,
    tags = ['weather_actions']
) as dag:
    task1 = GetWeatherAPIOperator(
        task_id='get_weather_api',
    )
