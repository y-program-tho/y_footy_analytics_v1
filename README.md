# y_footy_analytics_v1

## Project Description
y_footy_analytics_v1 is an Analytics application that is built upon a batch data pipeline in which data is ingested from various sources that will visualised to analyze the performance of football players, teams and leagues. 

The application is designed to provide insights into player statistics, team performance, and match outcomes through interactive dashboards and visualizations.

v1 is the MVP. There will be v2 and v3 that will build up on the current version with more features and functionalities.

----------------------------|----------------------------------------------------------------------------------------------------|
Layer	                    | Technology                                                                                         |
----------------------------|----------------------------------------------------------------------------------------------------|
Language	                | Python 3.11 (PySpark)                                                                              |
---------------------------------------------------------------------------------------------------------------------------------|
Data Source	                | CSV files (fixtures, results, standings)                                                           |
---------------------------------------------------------------------------------------------------------------------------------|
Processing Engine	        | Apache Spark (PySpark, local mode for dev / standalone or EMR-style cluster for larger runs)       |
---------------------------------------------------------------------------------------------------------------------------------|
Data Lake / Object Storage	| Amazon S3                                                                                          |
---------------------------------------------------------------------------------------------------------------------------------|
Data Warehouse	            | ClickHouse                                                                                         |
---------------------------------------------------------------------------------------------------------------------------------|
Warehouse Loading	        | ClickHouse's native S3 table function / S3 table engine (INSERT INTO ... SELECT FROM s3(...))      |
---------------------------------------------------------------------------------------------------------------------------------|
Orchestration/Scheduling	| Apache Airflow                                                                                     |
---------------------------------------------------------------------------------------------------------------------------------|
Data Validation	            | PySpark schema enforcement + Great Expectations                                                    |
---------------------------------------------------------------------------------------------------------------------------------|
Front-end	                | Streamlit                                                                                          |
---------------------------------------------------------------------------------------------------------------------------------|
Visualization	            | Plotly (via st.plotly_chart)                                                                       |
---------------------------------------------------------------------------------------------------------------------------------|
Secrets Management	        | .env + a secrets manager pattern (e.g. AWS Secrets Manager) for S3/ClickHouse credentials          |
---------------------------------------------------------------------------------------------------------------------------------|
Version Control	            | Git + GitHub                                                                                       |
---------------------------------------------------------------------------------------------------------------------------------|
Testing	                    | pytest (for PySpark transform logic, using local Spark sessions)                                   |
---------------------------------------------------------------------------------------------------------------------------------|
Logging	                    | Python logging + Spark's own job logs                                                              |
---------------------------------------------------------------------------------------------------------------------------------|
Code Quality	            | ruff + black                                                                                       |
---------------------------------------------------------------------------------------------------------------------------------|
Environment/Packaging	    | venv + requirements.txt; a Spark-compatible base image if containerized                            |
---------------------------------------------------------------------------------------------------------------------------------|          
