from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(
    dag_id="jinja_template_demo",
    start_date=datetime(2026,3,9),
    schedule_interval=None,
    catchup=False
) as dag:

    start = EmptyOperator(task_id="start")

    show_execution_date = BashOperator(
        task_id="show_execution_date",
        bash_command="""
        echo "Execution Date: {{ ds }}"
        echo "Next Execution Date: {{ next_ds }}"
        echo "Run ID: {{ run_id }}"
        """
    )

    end = EmptyOperator(task_id="end")

    start >> show_execution_date >> end