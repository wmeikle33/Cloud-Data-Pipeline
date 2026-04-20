
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

from pipelines.training_data.build_dataset import run as build_data
from pipelines.model.train import run as train_model


with DAG(
    dag_id="ml_training_pipeline",
    start_date=datetime.now(),
    schedule_interval="@daily",
    catchup=False,
) as dag:

    build_dataset_task = PythonOperator(
        task_id="build_dataset",
        python_callable=build_data,
    )

    train_task = PythonOperator(
        task_id="train_model",
        python_callable=train_model,
    )

    build_dataset_task >> train_task
