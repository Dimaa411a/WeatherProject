from airflow import DAG
from airflow.operators.python import PythonOperator
import datetime

from utilits.fetch_weather_data import fetch_weather_data
from utilits.process_weather_data import pivot_weather_data, calculate_all_diffs
from utilits.plot_weather import plot_weather

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime.datetime(2025, 9,30),
}

def process_and_plot():
    df = fetch_weather_data()

    df_pivot = pivot_weather_data(df)

    plot_weather(df_pivot)


with DAG(
    dag_id='weather_temperature_dag',
    schedule = '0 0 * * *',
    catchup = True,
    start_date = datetime.datetime(2025, 9, 30),
) as dag:

    task_process_and_plot = PythonOperator(
        task_id='process_and_plot',
        python_callable=process_and_plot
    )
