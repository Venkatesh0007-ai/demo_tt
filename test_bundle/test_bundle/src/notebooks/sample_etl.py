# Databricks notebook source
# DBTITLE 1,Sample ETL Notebook
# MAGIC %md
# MAGIC # Sample ETL Notebook
# MAGIC
# MAGIC This is a sample notebook for testing the bundle deployment.
# MAGIC
# MAGIC It demonstrates a simple ETL workflow:
# MAGIC 1. Read sample data
# MAGIC 2. Transform data
# MAGIC 3. Write to Delta table

# COMMAND ----------

# DBTITLE 1,Create sample data
from pyspark.sql import functions as F
from datetime import datetime

# Create sample data new comment added 22222222222222222222222222222222222222222
data = [
    (1, "Product A", 100.50, "2024-01-01"),
    (2, "Product B", 250.75, "2024-01-02"),
    (3, "Product C", 175.25, "2024-01-03"),
    (4, "Product D", 300.00, "2024-01-04"),
    (5, "Product E", 125.50, "2024-01-05")
]

df = spark.createDataFrame(data, ["id", "product_name", "price", "date"])
print(f"Created sample dataset with {df.count()} rows")
df.show()

# COMMAND ----------

# DBTITLE 1,Transform data
# Apply transformations
transformed_df = df.withColumn(
    "price_with_tax", 
    F.col("price") * 1.1
).withColumn(
    "processed_date",
    F.current_timestamp()
)

print("Data transformed successfully")
transformed_df.show()

# COMMAND ----------

# DBTITLE 1,Write to catalog (commented out for testing)
# Uncomment these lines after configuring catalog and schema variables
# catalog = spark.conf.get("catalog", "main")
# schema = spark.conf.get("schema", "default")
# 
# transformed_df.write.format("delta").mode("overwrite").saveAsTable(
#     f"{catalog}.{schema}.sample_products"
# )
# print(f"Data written to {catalog}.{schema}.sample_products")

print("✓ ETL job completed successfully")

# COMMAND ----------

