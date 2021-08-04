from datetime import time, timedelta
from botocore.client import Config
from airflow import DAG
from airflow.utils.dates import days_ago
from airflow.providers.postgres.operators.postgres import PostgresOperator
from airflow.operators.python_operator import PythonOperator
from airflow.providers.amazon.aws.hooks.lambda_function import AwsLambdaHook


DAG_NAME = "lambda_trigger"
DEFAULT_ARGS = {
    "owner": "airflow",
    "depends_on_past": False,
    "catchup": False,
    "start_date": days_ago(0),
    "email": ["airflow@example.com"],
    "retries": 0,
    "email_on_failure": False,
    "email_on_retry": False,
}


def lambda1(ds, **kwargs):
    hook = AwsLambdaHook(
        aws_conn_id="aws_default",
        function_name="lambda",
        region_name="us-east-1",
        invocation_type="RequestResponse",
        log_type="None",
        qualifier="$LATEST",
        config=Config(
            connect_timeout=300, read_timeout=300, retries={"max_attempts": 0}
        ),
    )

    response = hook.invoke_lambda(payload="null")

    print(f"response: {response}")


with DAG(
    dag_id=DAG_NAME,
    default_args=DEFAULT_ARGS,
    dagrun_timeout=timedelta(minutes=8),
    schedule_interval=None,
) as dag:

    delete_from_db = PostgresOperator(
        task_id='delete_tables_from_db',
        sql='sql_files/delete_tables.sql',
        postgres_conn_id='pg_conn',
        autocommit=True,        
    )


    trigger_lambda = PythonOperator(
        task_id="trigger_lambda",
        python_callable=lambda1,
    )

    delete_from_db >> trigger_lambda
