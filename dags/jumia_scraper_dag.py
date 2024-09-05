from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
import subprocess


def delete_db_file():
    db_path = "/app/src/jumia_deals_viewer/jumia_deals.db"
    try:
        subprocess.run(["sudo", "rm", "-f", db_path], check=True)
        print(f"Successfully deleted {db_path}")
    except subprocess.CalledProcessError as e:
        print(f"Failed to delete {db_path}: {e}")
    except Exception as e:
        print(f"An error occurred while trying to delete {db_path}: {str(e)}")


default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

with DAG(
    "jumia_scraper",
    default_args=default_args,
    description="A DAG to scrape Jumia deals",
    schedule_interval=timedelta(days=1),
    start_date=datetime(2023, 1, 1),
    catchup=False,
) as dag:

    delete_db = PythonOperator(
        task_id="delete_existing_db",
        python_callable=delete_db_file,
    )

    scrape_task = BashOperator(
        task_id="scrape_jumia_deals",
        bash_command="cd /app/src/jumia_deals_viewer && scrapy crawl jumia",
    )

    restart_backend = BashOperator(
        task_id="restart_backend",
        bash_command='docker restart jumia_backend_container || (echo "Failed to restart container" && exit 1)',
    )

    delete_db >> scrape_task >> restart_backend
