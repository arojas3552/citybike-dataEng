import streamlit as st
from google.cloud import bigquery
from google.oauth2 import service_account
import plotly.express as px
from datetime import datetime
 
credentials = service_account.Credentials.from_service_account_info(
        st.secrets.gcp_service_account,
        )
client = bigquery.Client(credentials=credentials)

#st.set_page_config(page_title="City Bikes Interactive World Map", layout="wide")

with st.container():
    st.title("""City Bikes Interactive World Map""")

    def get_suffix(day):
        if 10 < day % 100 < 20:
            suffix = "th"
        else:
            suffix = {1: "st", 2: "nd", 3: "rd"}.get(day % 10, "th")
        return suffix

    current_date = datetime.now()
    day = current_date.day
    suffix = get_suffix(day)
    formatted_day = str(day).lstrip("0")
    formatted_date = current_date.strftime("%B ") + formatted_day + suffix + current_date.strftime(", %Y")

    st.write(f"{formatted_date}")

with st.container():
    @st.cache_data(ttl=600)
    def run_query(query):
        query_job = client.query(query)
        rows_raw = query_job.result()
        # Convert to list of dicts. Required for st.cache_data to hash the return value.
        rows = [dict(row) for row in rows_raw]
        return rows

    def display_map(latlong):
        fig = px.scatter_mapbox(latlong, lat="latitude", lon="longitude", hover_name="name", hover_data=["company", "location_city", "location_country"], color_discrete_sequence=["fuchsia"], zoom=2, height=600, width=1200)
        fig.update_layout(mapbox_style="open-street-map")
        return fig

    latlong = run_query("SELECT * FROM `city-bikes11.bike_dataset.stations_stage`")
    city_map = display_map(latlong)
    st.plotly_chart(city_map)
