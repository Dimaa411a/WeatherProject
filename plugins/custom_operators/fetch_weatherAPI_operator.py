from models.db import engine
from models.pogoda import metadataobj,pogoda

from airflow.models import BaseOperator
from sqlalchemy import insert
from sqlalchemy.orm import sessionmaker


class FetchWeatherAPIOperator(BaseOperator):
    def __init__(self,cities,**kwargs):
        super().__init__(**kwargs)
        self.cities = cities

    def execute(self, context):

        import requests

        self.log.info('Fetching weather data')

        metadataobj.create_all(engine)

        url = 'https://api.openweathermap.org/data/2.5/forecast'
        api_key = 'f146304767163d3f82beaf03b6e5cfae',
        for city in self.cities:
            parameters = {
                'appid': api_key,
                'q': city,
                'units': 'metric'
            }
            response = requests.get(url,parameters)

            data = response.json()

            if response.status_code != 200:
                self.log.error(f"API call failed for {city}: {response.text}")
                continue

            stmd = (
                insert(pogoda).values(
                    Data=data['list'][0]['dt_txt'],
                    city_name=data['city']['name'],
                    temperature=data['list'][0]['main']['temp']
                )
            )
            Session = sessionmaker(bind=engine)
            with Session() as session:
                session.execute(stmd)
                session.commit()
            self.log.info('data inserted')
