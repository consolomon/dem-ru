import time
from datetime import datetime, timedelta
import logging
import requests


import google.oauth2.credentials
from json import dump
from airflow import DAG
from airflow.operators.python import PythonOperator


# # # Logger settings # # #
task_logger = logging.getLogger('airflow.task')

# # # Secret file settings # # #
# This variable specifies the name of a file that contains credentials of this session
CREDENTIALS_FILE = "/opt/airflow/api_keys/credentials_yt_api.json"


def youtube_auth(ti):
    task_logger.info('trying to authorize')
    requests.post('http://localhost:7070/authorize')
    time.sleep(10)
    response = requests.get('http://localhost:7070/get_credentials')
    response.raise_for_status()
    task_logger.info('authorization complete, downloading credentials')
    credentials = response.content
    with open(CREDENTIALS_FILE, 'w', encoding="utf-8") as file:
        dump(obj=credentials, fp=file)
    ti.xcom_push(key='credentials', value=credentials)
    task_logger.info('credentials accepted and now available by file path:')
    task_logger.info(CREDENTIALS_FILE)


# DAG definition
with DAG(
        dag_id='youtube_auth',
        start_date=datetime.today() - timedelta(hours=4),
        catchup=False,
        dagrun_timeout=timedelta(minutes=1)
) as dag:
    youtube_auth = PythonOperator(
        task_id='youtube_auth',
        python_callable=youtube_auth,
        dag=dag
    )

    youtube_auth
