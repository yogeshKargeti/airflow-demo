"python package"
from datetime import datetime

"airflow package"
from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.operators.python import PythonOperator, BranchPythonOperator

from branch_python_test.py_files.script1 import extract_odd
from branch_python_test.py_files.script2 import extract_even

default_arguments = {
    'owner': 'yogesh',
    'retries': 2

}


def branch_decision():
    today_date = datetime.today().day
    print("today's date", today_date)

    if today_date % 2 == 0:
        print("even script will run.")
        return 'Script_1'
    else:
        print("odd script will run.")
        return 'Script_2'


with DAG("branch_python_dag",
         start_date=datetime(2026, 3, 3),
         default_args=default_arguments,
         schedule='0 * * * *',
         catchup=False,
         max_active_runs=1
         ):

    start = EmptyOperator(task_id="start")

    decision = BranchPythonOperator(task_id='decision',
                                    python_callable=branch_decision)

    python_script1 = PythonOperator(task_id='Script_1',
                                    python_callable=extract_even,
                                    op_kwargs={"li":[12, 9, 113, 46, 55]})

    python_script2 = PythonOperator(task_id='Script_2',
                                    python_callable=extract_odd,
                                    op_args=[[12, 9, 113, 46, 55]])

    """ trigger rule example"""
    end2 = EmptyOperator(task_id="end_2")

    end = EmptyOperator(task_id="end")

    start >> decision >> python_script1 >> end
    start >> decision >> python_script2 >> end2