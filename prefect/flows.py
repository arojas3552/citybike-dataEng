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

if __name__ == "__main__":
    # creates a deployment and stays running to monitor for work instructions generated on the server

    api_call.serve(name="my-first-deployment",
                      tags=["onboarding"],
                      interval=60)