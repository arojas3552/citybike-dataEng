import os

import requests
import pandas as pd


import google.auth
from google.cloud import secretmanager, bigquery
from pandas import DataFrame


url = "https://rapidapi.com/eskerda/api/citybikes"

querystring = {"system":"valenbisi"}

headers = {
    "X-RapidAPI-Key": "e57256ad3bmsh961d5d4759787c2p19b799jsn7db5a12f3bdf",
    "X-RapidAPI-Host": "community-citybikes.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)