import pytest
from plugins.custom_operators.fetch_weather_operator import FetchWeatherOperator

def test_operator_init():
    op = FetchWeatherOperator(
        task_id='test_task',
        cities=['Kyiv', 'Lviv']
    )
    assert op.task_id == 'test_task'
    assert isinstance(op.cities, list)
    assert 'Kyiv' in op.cities
