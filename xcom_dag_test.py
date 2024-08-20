from airflow import DAG
from airflow.decorators import task

from datetime import datetime

with DAG('dag_xcom', start_date=datetime(2024, 1, 1 ),
        description='XCOM share data between tasks', tags=['data_analytics'],
        schedule='@daily', catchup=False): 
    
    @task
    def peter_task(ti=None):
        return 'iphone'
    
    @task
    def bryan_task(mobile_phone):
        print(mobile_phone)

    bryan_task(peter_task())