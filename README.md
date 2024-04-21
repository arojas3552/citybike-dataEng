
# City Bike Project
## Data Engineering Project

Personal project designed to improve my skills in data engineering. <br>

It focuses on developing data pipelines that extract, transform, and load data into data warehouses. Additionally, it involves creating a dashboard with visualizations in Streamlit. <br>

In this product, live worldwide city bike data is displayed on an interactive map with city bike details such as location, company, and city bike name.<br>

[Click this link to view the app](https://citybike-data-engine.streamlit.app/) <br>

Check out changelog for older, current, and future updates. 
#### Tools:
Prefect | 
Streamlit | 
Docker |
Google Cloud

### Database:
BigQuery

### Pipeline: 
(Orchastrated with Prefect) <br>
- Data is extracted from [City Bike API using Rapid API](https://rapidapi.com/eskerda/api/citybikes) with Python.
- Data is moved from Python to BigQuery Database.
- BigQuery SQL Queries clean and transform data.
- Data is migrated for visualizations on Streamlit.

### CI/CD
Github Actions <br>
CodeQL is used to scan the repository for vulnerabilities in the Python packages. <br>

Building, pushing, and deploying the Streamlit Docker image takes place across three jobs:
- Build the image
- Push the image to Artifact Registry
- Deploy the image to Cloud Run

### More
Future plans include drawing more data from different sources and styles, more advanced CI/CD processes, and implementing more security. Check changelog for more info.
