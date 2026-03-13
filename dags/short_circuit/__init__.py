"python package"
from datetime import datetime

"airflow package"
from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator, ShortCircuitOperator

from short_circuit.py_files.read_file import read_json


def circuit(user):
    if user.lower() in ("yogesh","yogi"):
        print("Running")
        return True
    else:
        print("Skipping")
        return False


default_arguments = {
    'owner': 'yogesh',
    'retries': 2

}


with DAG("short_circuit_python_dag",
         start_date=datetime(2024, 3, 12),
         default_args=default_arguments,
         schedule='0 5 * * *',
         catchup=False,
         max_active_runs=1
         ):

    start = EmptyOperator(task_id="start")

    check_short = ShortCircuitOperator(task_id="check_short",
                                       python_callable=circuit,
                                       op_args=["raj"])

    bash_task = BashOperator(task_id="bash_script",
                             bash_command="pwd")

    py_task = PythonOperator(task_id="python_script",
                             python_callable=read_json,
                             op_kwargs={"path": "/home/codespace/extrass/data_file.json"})

    end = EmptyOperator(task_id="end")

    start >> check_short >> bash_task >> py_task >> end