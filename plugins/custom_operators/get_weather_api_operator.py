from airflow.models import BaseOperator
import requests
import datetime
from airflow.providers.postgres.hooks.postgres import PostgresHook

class GetWeatherAPIOperator(BaseOperator):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def execute(self, context):
        pg_hook = PostgresHook(postgres_conn_id="my_db1")

        cities = [
            'Berlin', 'Kyiv', 'Lviv', 'Ivano-Frankivsk',
            'Warsaw', 'California', 'Chicago', 'Paris'
        ]
        url = "https://api.openweathermap.org/data/2.5/weather"
        records = []

        for city in cities:
            params = {
                'appid': 'f146304767163d3f82beaf03b6e5cfae',
                'q': city,
                'units': 'metric'
            }
            try:
                response = requests.get(url, params=params)
                response.raise_for_status()
                data = response.json()

                records.append((
                    data['name'],
                    data['main']['temp'],
                    data['weather'][0]['description'],
                    datetime.datetime.fromtimestamp(data['dt']),
                    datetime.datetime.fromtimestamp(data['sys']['sunrise']),
                    datetime.datetime.fromtimestamp(data['sys']['sunset'])
                ))

            except requests.exceptions.RequestException as e:
                self.log.error("Error fetching data for %s: %s", city, e)

        if records:
            pg_hook.insert_rows(
                table="weather",
                rows=records,
                target_fields=["city","temperature","description","time","sunrise","sunset"]
            )
            self.log.info("Inserted %d weather records into DB", len(records))
        else:
            self.log.warning("No records to insert")

