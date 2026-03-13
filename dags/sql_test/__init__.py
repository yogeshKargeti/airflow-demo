from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.providers.postgres.operators.postgres import PostgresOperator
from datetime import datetime
from airflow.operators.python import PythonOperator

from sql_test.py.run_query import fetch_employees

with DAG(
    dag_id="postgres_demo_dag",
    start_date=datetime(2026,3,1),
    schedule_interval=None,
    catchup=False,
    tags=["demo"]
) as dag:

    start = EmptyOperator(task_id="start")

    query_data = PostgresOperator(
        task_id="query_data",
        postgres_conn_id="test_postgres_conn",
        sql="SELECT * FROM employees;"
    )

    create_table = PostgresOperator(
        task_id="create_table",
        postgres_conn_id="test_postgres_conn",
        sql="sql/script.sql"
    )

    """insert_data = PostgresOperator(
        task_id="insert_data",
        postgres_conn_id="test_postgres_conn",
        sql="sql/script2.sql"
    )"""

    """data = PostgresOperator(
        task_id="data",
        postgres_conn_id="test_postgres_conn",
        sql="sql/script3.sql"
    )"""

    run_python = PythonOperator(task_id='run_python',
                                    python_callable=fetch_employees)

    end = EmptyOperator(task_id="end")

    start >> query_data >> create_table >> run_python >> end