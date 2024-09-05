#!/bin/bash
set -e

# Initialize the database if it doesn't exist
if [ ! -f "/opt/airflow/airflow.db" ]; then
    airflow db init
    airflow users create \
        --username admin \
        --firstname Admin \
        --lastname User \
        --role Admin \
        --email admin@example.com \
        --password admin
fi

# Start the web server
if [ "$1" = "webserver" ]; then
    exec airflow webserver
# Start the scheduler
elif [ "$1" = "scheduler" ]; then
    exec airflow scheduler
else
    exec airflow "$@"
fi