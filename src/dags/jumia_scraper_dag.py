from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators.bash_operator import BashOperator
import os
import subprocess

# Define the path to your project
PROJECT_PATH = "/path/to/your/project"
DB_PATH = f"{PROJECT_PATH}/src/backend/deals.db"


def delete_old_db():
    if os.path.exists(DB_PATH):
        os.remove(DB_PATH)
        print(f"Deleted old database: {DB_PATH}")
    else:
        print(f"No existing database found at {DB_PATH}")


def run_scraper():
    os.chdir(f"{PROJECT_PATH}/src")
    subprocess.run(["scrapy", "crawl", "jumia"], check=True)
    print("Scraper completed successfully")


def restart_production_server():
    # Kill existing Gunicorn process
    subprocess.run(["pkill", "-f", "gunicorn"], check=False)

    # Start new Gunicorn process
    os.chdir(PROJECT_PATH)
    subprocess.Popen(
        ["gunicorn", "-w", "4", "-b", "0.0.0.0:5050", "src.backend.app:app"]
    )
    print("Production server restarted")


default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "start_date": datetime(2023, 1, 1),
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

dag = DAG(
    "jumia_scraper_dag",
    default_args=default_args,
    description="A DAG to scrape Jumia deals and update the production site",
    schedule_interval=timedelta(days=1),
)

delete_db_task = PythonOperator(
    task_id="delete_old_db",
    python_callable=delete_old_db,
    dag=dag,
)

run_scraper_task = PythonOperator(
    task_id="run_scraper",
    python_callable=run_scraper,
    dag=dag,
)

restart_server_task = PythonOperator(
    task_id="restart_production_server",
    python_callable=restart_production_server,
    dag=dag,
)

delete_db_task >> run_scraper_task >> restart_server_task
