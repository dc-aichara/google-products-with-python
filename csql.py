"""
This python script can be used to get data from google cloud sql database
by querying with python package sqlalchemy.
"""
import sqlalchemy
import pandas as pd
# ----------------------------------------------------------------------------------------------------------------------
login = 'USERNAME'  # Replace USERNAME with actual username

passwd = 'PASSWORD'  # Replace PASSWORD with actual password

server = 'SEVER_IP:3306'  # Replace SEVER_IP with actual server IP
db = 'Your database name'  # Write your database name

# ----------------------------------------------------------------------------------------------------------------------
# Cloud SQL Query
engine_str = 'mysql+pymysql://{}:{}@{}/{}'.format(login, passwd, server, db)
engine = sqlalchemy.create_engine(engine_str)

query = """
SELECT
 
FROM
   
WHERE

"""
# ----------------------------------------------------------------------------------------------------------------------
# Extraction of user details and Total Acquisition
result = engine.execute(query)

df = pd.DataFrame(result, columns=['col1', 'col2', ..., 'coln'])  # convert to pandas dataframe
print(df.head())
print(df.shape)

df.to_csv('csql_data.csv', index=False)

