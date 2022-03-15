What is Apache Airflow ? And how to run instance of Apache Airflow using docker.
 - https://www.youtube.com/watch?v=2v9AKewyUEo&ab_channel=soumilshah1995

Steps to write an Airflow DAG
 - A DAG file, which is basically a python script, is a configuration file specifying the DAG's structure as code
 - There are only 5 steps for writing an Airflow DAG or workflows:
  - Importing required modules
  - Default arguments
  - Instantiate a DAG
  - Tasks
  - Setting up Dependencies

from datetime import timedelta
import airflow
from airflow import DAG
from airflow.operators.bash_operator import BashOpertator

default_args = {
    'owner': 'airflow',
    'start_date': airflow.utils.dates.days_ago(2),
    # 'end_date': datetime(2022,3,14),
    'depends_on_past': False,
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    # time gap between retries
    'retry_delay': timedelta(minutes=5),
}
