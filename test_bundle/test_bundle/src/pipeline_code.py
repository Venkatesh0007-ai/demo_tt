# Databricks notebook source
# MAGIC %md
# MAGIC # Sample Pipeline Code
# MAGIC This is a sample Python file for Lakeflow Spark Declarative Pipeline

# COMMAND ----------

import dlt
from pyspark.sql import functions as F

# COMMAND ----------

# MAGIC %md
# MAGIC ## Bronze Layer - Raw Data Ingestion

# COMMAND ----------

@dlt.table(
    name="bronze_sample_data",
    comment="Raw sample data ingested into bronze layer"
)
def bronze_sample_data():
    """Ingest raw sample data"""
    data = [
        (1, "Order A", 100.50, "2024-01-01", "completed"),
        (2, "Order B", 250.75, "2024-01-02", "completed"),
        (3, "Order C", 175.25, "2024-01-03", "pending"),
        (4, "Order D", 300.00, "2024-01-04", "completed"),
        (5, "Order E", 125.50, "2024-01-05", "cancelled")
    ]
    
    return spark.createDataFrame(
        data, 
        ["order_id", "order_name", "amount", "order_date", "status"]
    )

# COMMAND ----------

# MAGIC %md
# MAGIC ## Silver Layer - Cleaned and Validated Data

# COMMAND ----------

@dlt.table(
    name="silver_sample_data",
    comment="Cleaned and validated sample data"
)
@dlt.expect_or_drop("valid_amount", "amount > 0")
@dlt.expect_or_drop("valid_status", "status IN ('completed', 'pending', 'cancelled')")
def silver_sample_data():
    """Clean and validate bronze data"""
    return (
        dlt.read("bronze_sample_data")
        .withColumn("order_date", F.to_date("order_date"))
        .withColumn("processed_timestamp", F.current_timestamp())
    )

# COMMAND ----------

# MAGIC %md
# MAGIC ## Gold Layer - Business Aggregations

# COMMAND ----------

@dlt.table(
    name="gold_order_summary",
    comment="Daily order summary statistics"
)
def gold_order_summary():
    """Aggregate orders by date and status"""
    return (
        dlt.read("silver_sample_data")
        .groupBy("order_date", "status")
        .agg(
            F.count("order_id").alias("order_count"),
            F.sum("amount").alias("total_amount"),
            F.avg("amount").alias("avg_amount")
        )
        .orderBy("order_date", "status")
    )