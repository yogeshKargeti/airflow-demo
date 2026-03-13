from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.utils.task_group import TaskGroup
from datetime import datetime

with DAG(
    dag_id="taskgroup_demo",
    start_date=datetime(2026,3,6),
    schedule_interval=None,
    catchup=False
) as dag:

    start = EmptyOperator(task_id="start")

    with TaskGroup("processing_tasks") as processing_tasks:

        task1 = EmptyOperator(task_id="task1")
        task2 = EmptyOperator(task_id="task2")
        task3 = EmptyOperator(task_id="task3")

        task1 >> task2 >> task3

    end = EmptyOperator(task_id="end")

    start >> processing_tasks >> end