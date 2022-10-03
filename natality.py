#!/usr/bin/python
"""Create a Google BigQuery linear regression input table by querying the
public "natality" dataset.

In the code below, the following actions are taken:
  * A new dataset is created "natality_regression."
  * A new table "regression_input" is created to hold the inputs for our linear
    regression.
  * A query is run against the public dataset,
    bigquery-public-data.samples.natality, selecting only the data of interest
    to the regression, the output of which is stored in the "regression_input"
    table.
  * The output table is moved over the wire to the user's default project via
    the built-in BigQuery Connector for Spark that bridges BigQuery and Cloud
    Dataproc.

The original version is at
https://cloud.google.com/dataproc/docs/tutorials/bigquery-sparkml.
"""

from google.cloud import bigquery
from google.cloud.bigquery import job
from google.cloud.bigquery import SchemaField
from google.cloud.bigquery.table import *

# Create a new Google BigQuery client using Google Cloud Platform project
# defaults.
bq = bigquery.Client()

# Create a new BigQuery dataset.
dataset_ref = bq.dataset("natality_regression")
dataset = bigquery.Dataset(dataset_ref)
dataset = bq.create_dataset(dataset)

# In the new BigQuery dataset, create a new table.
table_ref = dataset.table('regression_input')
# The table needs a schema before it can be created and accept data.
# We create an ordered list of the columns using SchemaField objects.
schema = []
schema.append(SchemaField("weight_pounds", "float"))
schema.append(SchemaField("mother_age", "integer"))
schema.append(SchemaField("father_age", "integer"))
schema.append(SchemaField("gestation_weeks", "integer"))
schema.append(SchemaField("weight_gain_pounds", "integer"))
schema.append(SchemaField("apgar_5min", "integer"))

# We assign the schema to the table and create the table in BigQuery.
table = bigquery.Table(table_ref, schema=schema)
table = bq.create_table(table)

# Next, we issue a query in StandardSQL.
# The query selects the fields of interest.
query = """
SELECT weight_pounds, mother_age, father_age, gestation_weeks,
weight_gain_pounds, apgar_5min
from `bigquery-public-data.samples.natality`
where weight_pounds is not null
and mother_age is not null and father_age is not null
and gestation_weeks is not null
and weight_gain_pounds is not null
and apgar_5min is not null
LIMIT 10000
"""

# We create a query job to save the data to a new table.
job_config = bigquery.QueryJobConfig()
job_config.write_disposition = 'WRITE_TRUNCATE'
job_config.destination = table_ref

# 'Submit the query.
query_job = bq.query(query, job_config=job_config)
