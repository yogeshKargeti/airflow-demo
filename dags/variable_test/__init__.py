from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.models import Variable
from datetime import datetime

def read_config():

    config = Variable.get("demo_config", deserialize_json=True)

    print("Config:", config)
    print("Table:", config["table"])

with DAG(
    dag_id="json_variable_demo",
    start_date=datetime(2026,3,6),
    schedule_interval=None,
    catchup=False
) as dag:

    task = PythonOperator(
        task_id="read_variable",
        python_callable=read_config
    )