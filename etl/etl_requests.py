import os
import json
import requests # type: ignore
import pandas as pd
from pandas import DataFrame
import pandas_gbq
from datetime import datetime,timezone
from sqlalchemy.types import DECIMAL, String
from typing import Dict
from google.oauth2 import service_account

service_key = os.getenv('GOOGLE_APPLICATION_CREDENTIALS')
print(service_key,'SERVICE KEY\t\t\t\t')
credentials = service_account.Credentials.from_service_account_file('/Users/almarojas/Desktop/Documents/Projects/DataEngineering/citybike-dataEng/local/city-bikes11-key.json',)
credentials = credentials.with_scopes(
     [
        'https://www.googleapis.com/auth/drive',
        'https://www.googleapis.com/auth/cloud-platform',
    ],
)

def call_api()->str:
    url = "https://rapidapi.com/eskerda/api/citybikes"
    querystring = {"system":"valenbisi"}
    api_key = os.getenv('RAP_KEY')
    headers = {
        "X-RapidAPI-Key": api_key,
        "X-RapidAPI-Host": "community-citybikes.p.rapidapi.com"
    }

    response = requests.get("http://api.citybik.es/v2/networks")
    #print(response.text)

    json_res = response.json() #json format
    text = json.dumps(json_res, sort_keys=True, indent=4) #text format
    jstruct=json.loads(text) #dict format
    #print(text) #data check
    
    create_df(jstruct)
    return 0

    #return response.json()["response"][0]
    

def create_df(jstruct)-> str:
    current_date = datetime.now(timezone.utc)

    df = pd.json_normalize(jstruct,"networks") #convert to df
    #print(df.columns)

    df= df.assign(uploadTime = current_date)

    df = df.rename(columns={"location.city":"location_city","location.country":"location_country","location.latitude":"location_lat","location.longitude":"location_long","license.name":"license_name","license.url":"license_url"})
    print(df.dtypes)

    call_big_query(df)

    return 0

def define_table_schema() -> list[dict[str, str]]:
	schema_definition = [
		{'name': 'company', 'type': 'STRING'},
		{'name': 'href', 'type': 'STRING'},
		{'name': 'id', 'type': 'STRING'},
        {'name': 'name', 'type': 'STRING'},
		{'name': 'location_city', 'type': 'STRING'},
		{'name': 'location_country', 'type': 'STRING'},
		{'name': 'location_lat', 'type': 'FLOAT64'},
        {'name': 'location_long', 'type': 'FLOAT64'},
		{'name': 'source', 'type': 'STRING'},
		{'name': 'gbfs_href', 'type': 'STRING'},
        {'name': 'license_name', 'type': 'STRING'},
		{'name': 'license_url', 'type': 'STRING'},
		{'name': 'ebikes', 'type': 'INT64'},
		{'name': 'uploadTime', 'type': 'DATETIME'},
    ]
     
	return schema_definition

def call_big_query(df: DataFrame)-> None:
   
    df = df.astype(str)

    pandas_gbq.to_gbq(
         df,
         'bike_dataset.stations',
         project_id='city-bikes11',
         if_exists="replace",
         credentials=credentials,

    )

    print("Successfully sent to Big Query!")

#if __name__ != "__main__":
call_api()
