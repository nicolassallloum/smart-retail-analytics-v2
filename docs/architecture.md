# Architecture

Raw Sales (CSV) ? Python ETL ? PostgreSQL Warehouse (Star Schema)
                              ? Spark jobs (KPIs + RFM) ? outputs
Events (JSON) ? MongoDB (NoSQL events/logs)

Automation:
- Linux bash scripts to run pipeline, backup database, health checks
- Airflow DAG included for orchestration demonstration
