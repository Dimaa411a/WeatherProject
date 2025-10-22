from airflow.sensors.base import BaseSensorOperator
from sqlalchemy.orm import sessionmaker
from sqlalchemy import select
from models.db import engine
from models.table import workers_table

class PetroSensor(BaseSensorOperator):
    def poke(self, context):
        Session = sessionmaker(bind=engine)
        with Session() as session:
            query = select(workers_table).where(workers_table.c.name == 'Petro')
            result = session.execute(query).fetchone()
            return result is not None
