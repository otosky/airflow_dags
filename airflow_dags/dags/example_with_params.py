from datetime import datetime

from airflow import DAG
from airflow.decorators import task
from airflow.models.param import Param


@task(task_id="print_text")
def print_text(text):
    print(text)
    return text


with DAG(
    "example_with_params",
    description="An example DAG to demonstrate adhoc runs with parameters.",
    tags=["demo"],
    start_date=datetime(2024, 2, 1),
    schedule=None,
    catchup=False,
    params={"text_to_print": Param("Lacinato Kale", type="string")},
    render_template_as_native_obj=True,
) as dag:
    print_text("{{ params.text_to_print }}")
