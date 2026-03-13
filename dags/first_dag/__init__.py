from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import time

def start_task():
    print("Pipeline started")

def processing_task():
    print("Processing data...")
    time.sleep(5)

def end_task():
    print("Pipeline completed")

with DAG(
    dag_id="sample_demo_dag",
    start_date=datetime(2026,3,5),
    schedule_interval=None,
    catchup=False,
    tags=["demo"]
) as dag:

    start = PythonOperator(
        task_id="start_task",
        python_callable=start_task
    )

    process = PythonOperator(
        task_id="processing_task",
        python_callable=processing_task
    )

    end = PythonOperator(
        task_id="end_task",
        python_callable=end_task
    )

    start >> process >> end