import os
import json
import requests # type: ignore
import pandas as pd
from pandas import DataFrame
import pandas_gbq
from datetime import datetime,timezone
from sqlalchemy.types import DECIMAL, String
from typing import Dict

import google.auth
from google.cloud import bigquery

#PROJECT_ID = "city-bikes11"
#os.environ["GCLOUD_PROJECT"] = PROJECT_ID
#credentials, project_id = google.auth.default()

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
    

def create_df(jstruct)-> DataFrame:
    current_date = datetime.now(timezone.utc)

    df = pd.json_normalize(jstruct,"networks") #convert to df
    #print(df.columns)

    df= df.assign(uploadTime = current_date)
    print(df.columns)

    return df

# todo: implement later!
def define_table_schema() -> Dict[str,type]:
	schema_definition = {
		"Company":String(64),
		"Href":String(64),
		"id": DECIMAL(8, 6),
        "Name": DECIMAL(8, 6),
		"City":String(64),
		"Country":String(64),
		"Source":String(64)
    }
     
	return schema_definition

def call_big_query(dataframe: DataFrame, schema_definition: Dict[str,type])-> None:
    bike_df.to_gbq(
         destination_table="cb11.data",
         if_exists="replace",
         table_schema=schema_def,
    )

    print("1")

#if __name__ != "__main__":
call_api()
