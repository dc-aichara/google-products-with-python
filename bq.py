"""
This python script uses pandas_gbq python package to extract data
from Google BigQuery as pandas frame .
"""
import pandas_gbq

PROJECT_ID = "Your Project ID"
data_Set = "bigquery-public-data"  # Replace this with your data set name
sub_data_set = "ml_datasets"   # Replace this with your sub  data set name
data_table = "census_adult_income"  # Replace this with your table name


query = """
SELECT
  *
FROM
  [{0}:{1}.{2}]
"""

query = query.format(data_Set, sub_data_set, data_table)

df = pandas_gbq.read_gbq(query, project_id=PROJECT_ID, dialect="legacy")

print(df.head())

