import os

import requests # type: ignore
import pandas as pd

import google.auth
from google.cloud import secretmanager, bigquery

#class DataRetrieval:
def _call_api()->str:
    url = "https://rapidapi.com/eskerda/api/citybikes"
    querystring = {"system":"valenbisi"}
    api_key = os.getenv('RAP_KEY')
    headers = {
        "X-RapidAPI-Key": api_key,
        "X-RapidAPI-Host": "community-citybikes.p.rapidapi.com"
    }
    response = requests.request("GET", url, headers=headers,    params=querystring)
    response = requests.get("http://api.citybik.es/v2/networks/")

    return response.json()
    
def _call_big_query()->int:
    client = bigquery.Client()

    return 1

#if __name__ != "__main__":
print(_call_api())
_call_big_query()