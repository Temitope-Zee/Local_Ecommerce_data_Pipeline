from datetime import datetime, timedelta
from airflow import DAG
from airflow.providers.standard.operators.bash import BashOperator

default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "email_on_failure": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

with DAG(
    "ecommerce_elt_pipeline",
    default_args=default_args,
    description="Local ELT pipeline using Python, DuckDB, and dbt",
    schedule="@daily",
    start_date=datetime(2026, 1, 1),
    catchup=False,
) as dag:

    extract_and_load = BashOperator(
        task_id="extract_and_load",
        bash_command="python3 /opt/airflow/scripts/extract.py",
    )

    dbt_run = BashOperator(
        task_id="dbt_run",
        bash_command="cd /opt/airflow/transform_project && dbt run --profiles-dir .",
    )

    dbt_test = BashOperator(
        task_id="dbt_test",
        bash_command="cd /opt/airflow/transform_project && dbt test --profiles-dir .",
    )

    extract_and_load >> dbt_run >> dbt_test
