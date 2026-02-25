🚀 Smart Retail Analytics Platform
📌 Project Overview
This project simulates a real-world retail data engineering platform.
It demonstrates how raw transactional data is transformed into analytics-ready insights using modern data engineering tools.
The platform includes:
Data generation


ETL processing


Dimensional data warehousing


Spark-based analytics


NoSQL event tracking


Containerized infrastructure


Pipeline automation



🏗 Architecture

                        ┌─────────────────────────┐
                        │   Raw Sales Generator   │
                        │  (Python + Faker CSV)   │
                        └─────────────┬───────────┘
                                      │
                                      ▼
                        ┌─────────────────────────┐
                        │   Python ETL Layer      │
                        │ - Cleaning              │
                        │ - Validation            │
                        │ - Business Metrics      │
                        └─────────────┬───────────┘
                                      │
                                      ▼
                    ┌────────────────────────────────┐
                    │ PostgreSQL Data Warehouse      │
                    │                                │
                    │  ⭐ Star Schema                 │
                    │  - dim_date                    │
                    │  - dim_customer                │
                    │  - dim_product                 │
                    │  - fact_sales                  │
                    └─────────────┬──────────────────┘
                                  │
                                  ▼
                    ┌────────────────────────────────┐
                    │ Apache Spark Analytics Layer   │
                    │                                │
                    │ - Revenue KPIs                 │
                    │ - Top Products                 │
                    │ - RFM Segmentation             │
                    └─────────────┬──────────────────┘
                                  │
                                  ▼
                    ┌────────────────────────────────┐
                    │ Analytics Outputs              │
                    │ - KPI CSVs                    │
                    │ - Customer Segments           │
                    └────────────────────────────────┘


                    ┌────────────────────────────────┐
                    │ MongoDB (NoSQL Layer)          │
                    │ - User Events                  │
                    │ - Product Views                │
                    │ - Clickstream Simulation       │
                    └────────────────────────────────┘


                    ┌────────────────────────────────┐
                    │ Automation Layer               │
                    │ - Linux Scripts                │
                    │ - Docker Containers            │
                    │ - Airflow DAG (optional)       │
                    └────────────────────────────────┘

🧰 Tech Stack
Layer
Technology
Data Generation
Python + Faker
ETL
Python (Pandas, SQLAlchemy)
Warehouse
PostgreSQL (Star Schema)
Big Data Processing
Apache Spark (PySpark)
NoSQL
MongoDB
Containerization
Docker
Automation
Bash Scripts
Orchestration
Apache Airflow (Optional)
OS
Linux (WSL)


⭐ Data Warehouse Design
Star Schema:
dim_date


dim_customer


dim_product


fact_sales


Optimized with:
Indexing


FK constraints


Performance tuning


Row verification



📊 Analytics Implemented
Using Apache Spark:
Revenue by day


Top selling products


Revenue by city


Customer RFM segmentation


Return rate calculation



🗂 NoSQL Layer
MongoDB stores:
Product views


Session events


Clickstream simulation


Aggregation queries



▶️ How to Run
docker compose up -d
bash linux/run_pipeline.sh

Verify warehouse:
docker exec -it sra_postgres psql -U postgres -d smart_retail_dw -c "SELECT COUNT(*) FROM fact_sales;"


💡 Skills Demonstrated
SQL


Data Warehousing


ETL


Linux Commands


Database Design


Database Administration


Apache Spark


Apache Airflow


Apache Hadoop (conceptual integration)


NoSQL


Data Science fundamentals



🎯 Business Value
The platform converts raw retail transactions into:
Revenue insights


Customer behavior segmentation


Product performance analysis


Event tracking analytics



