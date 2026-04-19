from prefect import flow, task

from pipelines.training_data.build_dataset import run as build_data
from pipelines.model.train import run as train_model


@task
def build_dataset_task():
    build_data()


@task
def train_task():
    train_model()


@flow
def training_flow():
    build_dataset_task()
    train_task()


if __name__ == "__main__":
    training_flow()
