
# City Bike Project
## Data Engineering Project

Personal project designed to improve my skills in data engineering.

It focuses on developing data pipelines that extract, transform, and load data into data warehouses. Additionally, it involves creating a dashboard with visualizations in Streamlit.

#### Tools:
Cloud Scheduler
Streamlit

### Database:
BigQuery

### Pipeline: 
(Orchastrated with Prefect)
- Data is extracted from [City Bike API using Rapid API](https://rapidapi.com/eskerda/api/citybikes) with Python.
- Data is moved from Python to BigQuery Database.
- BigQuery SQL Queries clean and transform data.
- Data is migrated for visualizations.

### CI/CD
Github Actions
WIP

### More
Synk is used to scan the repository for vulnerabilities in the Python packages.
