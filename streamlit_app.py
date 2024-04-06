import streamlit as st
import os
from google.cloud import bigquery
import google.auth
from google.oauth2 import service_account
 
credentials = service_account.Credentials.from_service_account_info(
        st.secrets.gcp_service_account,
        scopes=["https://www.googleapis.com/auth/bigquery"])
client = bigquery.Client(credentials=credentials)

st.set_page_config(page_title="Streamlit: City Bikes", layout="wide")
st.write("""
# City Bikes
Interactive world map*
""")

@st.cache_data(ttl=600)
def run_query(query):
    query_job = client.query(query)
    rows_raw = query_job.result()
    # Convert to list of dicts. Required for st.cache_data to hash the return value.
    rows = [dict(row) for row in rows_raw]
    return rows

latlong = run_query("SELECT longitude, latitude FROM `city-bikes11.bike_dataset.stations_stage`")

st.map(latlong,zoom=1,use_container_width=True)

