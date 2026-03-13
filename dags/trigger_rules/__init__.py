from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.empty import EmptyOperator
from datetime import datetime
from airflow.utils.trigger_rule import TriggerRule


def success_task():
    print("Task succeeded")


def fail_task():
    raise Exception("Intentional failure")


with DAG(
    dag_id="trigger_rule_demo",
    start_date=datetime(2026,3,6),
    schedule_interval=None,
    catchup=False
) as dag:

    start = EmptyOperator(task_id="start")

    task_success = PythonOperator(
        task_id="task_success",
        python_callable=success_task
    )

    task_fail = PythonOperator(
        task_id="task_fail",
        python_callable=success_task
    )

    # Runs only if ALL upstream tasks succeed (default)
    all_success_task = EmptyOperator(
        task_id="all_success_task"
    )

    # Runs if at least ONE upstream task succeeds
    one_success_task = EmptyOperator(
        task_id="one_success_task",
        trigger_rule=TriggerRule.ONE_SUCCESS
    )

    # Runs regardless of success or failure
    always_run_task = EmptyOperator(
        task_id="ONE_FAILED",
        trigger_rule=TriggerRule.ONE_FAILED
    )

    start >> [task_success, task_fail]

    task_success >> all_success_task
    task_fail >> all_success_task

    [task_success, task_fail] >> one_success_task
    [task_success, task_fail] >> always_run_task