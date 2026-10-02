from datetime import datetime

from airflow.sdk import DAG
from airflow.providers.standard.operators.bash import BashOperator


with DAG(
    dag_id="superstore_pipeline",
    start_date=datetime(2026, 1, 1),
    schedule=None,
    catchup=False,
    tags=["superstore", "dbt", "duckdb"],
) as dag:

    load_to_ods = BashOperator(
        task_id="load_to_ods",
        bash_command="cd /app && python scripts/load_to_ods.py",
    )

    dbt_staging = BashOperator(
        task_id="dbt_staging",
        bash_command=(
            "cd /app/dbt/superstore_dbt && "
            "dbt run --select stg_orders"
        ),
    )

    dbt_marts = BashOperator(
        task_id="dbt_marts",
        bash_command=(
            "cd /app/dbt/superstore_dbt && "
            "dbt run --select dim_customer dim_product dim_location "
            "dim_ship_mode dim_segment dim_date fact_order_line"
        ),
    )

    dbt_tests = BashOperator(
        task_id="dbt_tests",
        bash_command=(
            "cd /app/dbt/superstore_dbt && "
            "dbt test"
        ),
    )

    load_to_ods >> dbt_staging >> dbt_marts >> dbt_tests


