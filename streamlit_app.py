import streamlit as st
import pandas as pd
import plotly.express as px

from google.oauth2 import service_account
from google.cloud import bigquery

st.set_page_config(page_title="Streamlit: City Bikes", layout="wide")
st.write("""
# City Bikes
Interactive world map*
""")
#px.set_mapbox_access_token(open(".mapbox_token").read())

credentials = service_account.Credentials.from_service_account_file('/Users/almarojas/Desktop/Documents/Projects/DataEngineering/citybike-dataEng/local/city-bikes11-key.json',)
client = bigquery.Client(credentials=credentials)

@st.cache_data(ttl=600)
def run_query(query):
    query_job = client.query(query)
    rows_raw = query_job.result()
    # Convert to list of dicts. Required for st.cache_data to hash the return value.
    rows = [dict(row) for row in rows_raw]
    return rows

latlong = run_query("SELECT location_long as longitude, location_lat as latitude, * FROM `city-bikes11.bike_dataset.stations_stage`")


st.map(latlong,zoom=1,use_container_width=True)

