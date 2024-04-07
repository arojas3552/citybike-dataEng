
# City Bike Project
## Data Engineering Project

Personal project designed to improve my skills in data engineering.

It focuses on developing data pipelines that extract, transform, and load data into data warehouses. Additionally, it involves creating a dashboard with visualizations in Streamlit.

In this product, live worldwide city bike data is displayed on an interactive map with city bike details such as location, company, and city bike name.

[Click this link to view the app](https://citybike-data-engine.streamlit.app/)

Check out project log (project_log.txt) for older updates, current, and future updates. 
#### Tools:
Prefect | 
Streamlit

### Database:
BigQuery

### Pipeline: 
(Orchastrated with Prefect)
- Data is extracted from [City Bike API using Rapid API](https://rapidapi.com/eskerda/api/citybikes) with Python.
- Data is moved from Python to BigQuery Database.
- BigQuery SQL Queries clean and transform data.
- Data is migrated for visualizations on Streamlit.

### CI/CD
Github Actions
CodeQL is used to scan the repository for vulnerabilities in the Python packages.

### More
Future plans include drawing more data from different sources and styles, implementing docker images, more advanced CI/CD processes.
