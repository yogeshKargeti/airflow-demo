from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime


def push_value(ti):
    message = "Hello from XCom"
    
    # Push value to XCom
    ti.xcom_push(key="abc_key",value="yogesh")


def pull_value(ti):
    
    # Pull value from XCom
    message = ti.xcom_pull(task_ids="push_task",key="abc_key")
    
    print("Received from XCom:", message)


with DAG(
    dag_id="xcom_demo_dag",
    start_date=datetime(2026,3,8),
    schedule_interval=None,
    catchup=False
) as dag:

    push_task = PythonOperator(
        task_id="push_task",
        python_callable=push_value
    )

    pull_task = PythonOperator(
        task_id="pull_task",
        python_callable=pull_value
    )

    push_task >> pull_task