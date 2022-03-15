from datetime import timedelta,datetime
import pandas as pd
from airflow import DAG
from airflow.operators.python_operator import PythonOperator

def readDataFrame(**context):
    print("Loading and converting data to data frame")
    data = [{"name":"Ankit","title":"Full Stack Software Engineer"}, { "name":"Abhay","title":"Full Stack Software Engineer"},]
    userData = pd.DataFrame(data)
    context['ti'].xcom_push(key='users',value=userData)
    print("-----------------Main Function------------------------------")
    print(context)
    print("-----------------Main Function------------------------------")


def printDataFrame(**context):
    userData = context.get('ti').xcom_pull(key='users')
    print("-----------------------------------------------",context)
    print(userData.head())
    print("-----------------------------------------------")

default_args = {
            "owner": "airflow",
            "retries": 1,
            "retry_delay": timedelta(minutes=5),
            "start_date": datetime(2021, 1, 1),
        },

with DAG(
        dag_id="processDataFrame",
        schedule_interval="@daily",
        default_args={
            "owner": "airflow",
            "retries": 1,
            "retry_delay": timedelta(minutes=5),
            "start_date": datetime(2021, 1, 1),
        },
        catchup=False) as f:

    readDataFrame = PythonOperator(
        task_id="readDataFrame",
        python_callable=readDataFrame,
        provide_context=True,
        op_kwargs={"name":"Ankit Singh"},
    )

    printDataFrame = PythonOperator(
        task_id="printDataFrame",
        python_callable=printDataFrame,
        provide_context=True,
    )

readDataFrame >> printDataFrame