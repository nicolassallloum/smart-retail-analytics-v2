# Hadoop Notes (Skill Coverage)

Hadoop ecosystem basics:
- HDFS: distributed storage layer
- YARN: cluster resource manager
- MapReduce: older processing framework

How Spark fits:
- Spark can run on:
  - Standalone cluster
  - YARN (Hadoop)
  - Kubernetes
- Spark can read/write HDFS data (lake) and create curated datasets (Parquet)

In this project:
- We simulate the Hadoop pattern by using Spark for distributed-style processing.
- In a production upgrade, raw/processed files would live in HDFS (or S3 lake),
  and Spark jobs would run on YARN to process national-scale datasets.
