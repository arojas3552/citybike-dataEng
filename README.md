
# City Bike Project
## Data Engineering Project

Personal project designed to improve my skills in data engineering.

It focuses on developing data pipelines that extract, transform, and load data into data warehouses. Additionally, it involves creating a dashboard with visualizations in Streamlit.

In this product, live worldwide city bike data is displayed on an interactive map with city bike details such as location, company, and city bike name.

The viewable product on Streamlit is currently being tested for data leaks. Here is a screenshot on local host of the application: 
<img width="1388" alt="Screenshot 2024-03-26 at 12 47 27 PM" src="https://github.com/arojas3552/citybike-dataEng/assets/54590853/63f79d1d-4a1e-4436-9b27-36b5f7792fba">

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
Github Actions --WIP

### More
Synk is used to scan the repository for vulnerabilities in the Python packages.

Future plans include drawing more data from different sources and styles, implementing docker images, more advanced CI/CD processes.
