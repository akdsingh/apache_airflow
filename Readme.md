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

Operators and Tasks
 - DAGs do not perform any actual computation. Instead Operators determine what actually gets done.
 - Task: Once and operator is instantiated, it is referred to as task. An operator describes a single task in a workflow.
   - Instantiating a task requires providing a unique task_id and a DAG container.
 
 - A DAG is a container that is used to organise tasks and set their execution context (i.e. which task is dependent on which one or they can be excute in parallel).

dag = DAG(
    'tutorial',
    default_args=default_args,
    description='A simple tutorial DAG',
    schedule_interval=timedelta(days=1),
)

 - here t2 and t3 are the two tasks in the container dag
 t2 = BashOperator(
    task_id='sleep',
    depends_on_past=False,
    bash_command='sleep 5',
    dag=dag,
)
t3 = BashOperator(
    task_id='templated',
    depends_on_past=False,
    bash_command=templated_command,
    params={'my_param': 'Parameter I passed in'},
    dag=dag,
)

Operators Categories
 - Sensors
  - A certain type of operator that will keep running until a certain criteria is met. Example, wating for certain time, external file or upstream data source. Some of them are :-
   - Hdfssensor: Waits for file or folder to land in HDFS.
   - NamedHivePartitionSensor: check whether the most recent partition of a Hive table is available for downstream processing.

 - Operators
  - Triggers a certain action (e.g run a bash command, execute python code, or execute a Hive Query). Some of them are :-
   - BashOperator
   - PythonOperator
   - HiveOperator
   - BigQueryOperator

 - Transfers
  - moves data from one location to another.
   - MySqlToHiveTransfer
   - S3ToRedShiftTransfer
