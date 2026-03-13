from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.operators.python import BranchPythonOperator
from airflow.utils.trigger_rule import TriggerRule
from datetime import datetime


def choose_branch():
    return "task_a"   # task_b will be skipped


with DAG(
    dag_id="trigger_rule_none_failed_demo",
    start_date=datetime(2026,3,6),
    schedule_interval=None,
    catchup=False
) as dag:

    start = EmptyOperator(task_id="start")

    branch = BranchPythonOperator(
        task_id="branch",
        python_callable=choose_branch
    )

    task_a = EmptyOperator(task_id="task_a")
    task_b = EmptyOperator(task_id="task_b")

    # Default trigger rule (all_success)
    all_success_task = EmptyOperator(
        task_id="all_success_task"
    )

    # Demonstrates none_failed
    none_failed_task = EmptyOperator(
        task_id="none_failed_task",
        trigger_rule=TriggerRule.NONE_FAILED
    )

    start >> branch
    branch >> [task_a, task_b]

    [task_a, task_b] >> all_success_task
    [task_a, task_b] >> none_failed_task