from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator

def task_failure_alert(context):
    ti = context.get('task_instance')
    print(f"[ERROR ALERT] Task '{ti.task_id}' failed in DAG '{ti.dag_id}' on run {ti.run_id}.")

default_args = {
    'owner': 'data_engineer',
    'depends_on_past': False,
    'email_on_failure': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
    'on_failure_callback': task_failure_alert,
}

with DAG(
    'local_ecommerce_pipeline',
    default_args=default_args,
    description='A local end-to-end e-commerce data pipeline',
    schedule=timedelta(days=1),
    start_date=datetime(2026, 10, 1),
    catchup=False,
) as dag:

    extract_task = BashOperator(
        task_id='extract_data',
        bash_command='python3 /opt/airflow/scripts/extract.py',
    )

    load_task = BashOperator(
        task_id='load_to_duckdb',
        bash_command='python3 /opt/airflow/scripts/load_to_duckdb.py',
    )

    transform_task = BashOperator(
        task_id='dbt_run',
        bash_command='cd /opt/airflow/transform_project && dbt run',
    )

    test_task = BashOperator(
        task_id='dbt_test',
        bash_command='cd /opt/airflow/transform_project && dbt test',
    )

    extract_task >> load_task >> transform_task >> test_task
