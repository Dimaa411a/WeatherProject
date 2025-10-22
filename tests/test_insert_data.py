import pytest
from airflow.models import DagBag

def test_dag_loaded():
    dag_bag = DagBag()
    dag = dag_bag.get_dag('insert_weather_dag')

    assert dag is not None, "DAG не завантажився"
    assert len(dag.tasks) == 1, "Очікується одна таска"

def test_task_exists():
    dag_bag = DagBag()
    dag = dag_bag.get_dag('insert_weather_dag')
    task_ids = [t.task_id for t in dag.tasks]


    assert 'fetch_insert_weather' in task_ids, "Нема таски fetch_insert_weather"
