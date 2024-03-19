from prefect import flow,task


@flow(log_prints=True)
def hello_world(name: str = "world", goodbye: bool = False):
    print(f"Hello {name} from Prefect! 🤗")

    if goodbye:
        print(f"Goodbye {name}!")

@task
def task_imports():
    from etl.etl_requests import call_api

@flow(log_prints=True)
def api_call():
    print("Calling ETL")
    a = task_imports()
