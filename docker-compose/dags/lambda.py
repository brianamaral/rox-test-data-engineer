from datetime import time, timedelta

from airflow import DAG
from airflow.utils.dates import days_ago
from airflow.providers.http.operators.http import SimpleHttpOperator
from airflow.operators.python_operator import PythonOperator
from airflow.providers.amazon.aws.hooks.lambda_function import AwsLambdaHook


DAG_NAME = "lambda_trigger"
DEFAULT_ARGS = {
    "owner": "airflow",
    "depends_on_past": False,
    "start_date": days_ago(0),
    "email": ["airflow@example.com"],
    "retries": 3,
    "retry_delay": timedelta(minutes=10),
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
    )

    response = hook.invoke_lambda(payload="null")

    print(f"response: {response}")


with DAG(
    dag_id=DAG_NAME,
    default_args=DEFAULT_ARGS,
    dagrun_timeout=timedelta(minutes=8),
    schedule_interval=timedelta(hours=1),
) as dag:

    trigger_lambda = PythonOperator(
        task_id="trigger_lambda",
        python_callable=lambda1,
        provide_context=True,
    )

    trigger_lambda
