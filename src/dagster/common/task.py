"""Set of common, re-useable tasks.

"""
from typing import Optional

from airflow.operators.empty import EmptyOperator
import airflow


def start(dag: airflow.DAG, default_args: Optional[dict]) -> EmptyOperator:
    """Task `start` book-end definition."""
    return empty(dag, default_args, "start")


def end(dag: airflow.DAG, default_args: Optional[dict]) -> EmptyOperator:
    """Task `end` book-end definition."""
    return empty(dag, default_args, "end")


def empty(dag: airflow.DAG, default_args: Optional[dict], name: str) -> EmptyOperator:
    """Task `name` book-end definition."""
    return EmptyOperator(task_id=name, default_args=default_args, dag=dag)
