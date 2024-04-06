# bigquery sql code that transforms and updates data housed on bq
#scheduled to run after data send in 

import google.auth
from google.cloud import bigquery

credentials, project_id = google.auth.default()
client = bigquery.Client(credentials=credentials)

def query_call():
  # Perform a query.
  QUERY = """
    #create staged table for analysis
  CREATE OR REPLACE TABLE `city-bikes11.bike_dataset.stations_stage` AS (
    SELECT
      company,
      name,
      location_city,
      location_country,
      cast(location_long as float64) as longitude,
      cast(location_lat as float64) as latitude
    FROM city-bikes11.bike_dataset.stations);
  """
  query_job = client.query(QUERY)  # API request
  rows = query_job.result()  # Waits for query to finish

  print("QUERY JOB COMPLETE")
