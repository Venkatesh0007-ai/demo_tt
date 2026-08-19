# Test Bundle - Sample Files

This bundle includes sample files for testing Declarative Automation Bundle deployment.

## Bundle Structure

```
test_bundle/
├── databricks.yml                        # Main bundle configuration
├── README.md                             # This file
├── resources/                            # Resource definitions
│   ├── sample_job.job.yml               # Sample job configuration
│   └── sample_pipeline.pipeline.yml      # Sample pipeline configuration
└── src/                                  # Source code
    ├── notebooks/
    │   └── sample_etl                    # Sample ETL notebook
    └── pipeline_code.py                  # Sample pipeline code
```

## Sample Resources

### 1. Sample ETL Notebook (`src/notebooks/sample_etl`)
A simple ETL notebook that demonstrates:
* Creating sample data with Spark
* Transforming data (adding tax calculation)
* Writing to Delta tables (commented out for testing)

### 2. Sample Job (`resources/sample_job.job.yml`)
A scheduled job that:
* Runs the sample ETL notebook
* Uses job cluster configuration
* Scheduled to run daily at 9 AM UTC (starts paused)
* Sends email notifications on failure
* Uses variables for catalog and schema

### 3. Sample Pipeline (`resources/sample_pipeline.pipeline.yml`)
A Lakeflow Spark Declarative Pipeline that:
* Implements a medallion architecture (Bronze → Silver → Gold)
* Includes data quality expectations
* Uses Photon for acceleration
* Sends notifications on failures

### 4. Pipeline Code (`src/pipeline_code.py`)
Pipeline implementation with:
* Bronze layer: Raw data ingestion
* Silver layer: Data cleaning and validation
* Gold layer: Business aggregations
* Data quality expectations using `@dlt.expect_or_drop`

## Configuration

### Variables
The bundle uses these variables (defined in `databricks.yml`):
* `catalog`: Unity Catalog name (default: "main")
* `schema`: Schema name (default: "default")

### Targets
* **dev** (default): Development environment
* **prod**: Production environment

## Testing the Bundle

### 1. Validate the Bundle
```bash
databricks bundle validate --target dev
```

### 2. Deploy the Bundle
```bash
databricks bundle deploy --target dev
```

### 3. Run the Job
```bash
databricks bundle run --target dev sample_job
```

### 4. View Deployed Resources
```bash
databricks bundle summary --target dev
```

## Customization

To customize for your environment:

1. **Update variables**: Modify `catalog` and `schema` in `databricks.yml` under the target configuration
2. **Modify cluster configuration**: Update `node_type_id` and `spark_version` in `sample_job.job.yml`
3. **Adjust schedule**: Change `quartz_cron_expression` in `sample_job.job.yml`
4. **Add more resources**: Create additional `.yml` files in the `resources/` directory

## Next Steps

* Uncomment the table write logic in `sample_etl` notebook after configuring your catalog/schema
* Add more tasks to the sample job
* Extend the pipeline with additional layers
* Add alerts, dashboards, or other resources
* Configure production environment variables