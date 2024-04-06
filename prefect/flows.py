#prefect flow definitions and calls

from prefect import flow,task

@task
def task_api():
    from etl.etl_requests import call_api
    call_api()

@task
def task_query():
    from etl.queries import query_call
    query_call()

@flow(log_prints=True)
def api_call():
    print("Calling ETL")
    state = task_api(return_state=True)

    try:
        result = state.result()
    except ValueError:
        print("Oh no! The state raised the error!")
    else: 
        print("All good no errors")
        #call qieries.py
        task_query()
    
    return True



#if __name__ == "__main__":
#    api_call.serve(name="bike_deploy",interval = 300)