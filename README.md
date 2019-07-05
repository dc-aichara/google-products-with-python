
This repository has python scripts to access google products (Big Query, Cloud SQL,Google sheets, Google Analytics).
***
```text
To access BigQuery, Cloud SQL, Google Analytics, you must have a project on google cloud platform and a service account.

```
How to get a project and a service account ?

See documentation for help [here](https://cloud.google.com/iam/docs/creating-managing-service-accounts) and [here](https://cloud.google.com/resource-manager/docs/creating-managing-projects)


```text
To access Google Analytics, you must have permissions to view google analytics account [user account is sufficient]. 
```
```text
To access google sheets, you must have permission to edit google sheet to be accessed. 
```

## Usage
### 1. [Extracting data from Google Big Query as pandas DataFrame](https://github.com/dc-aichara/google-products-with-python/blob/master/bq.py)
When you run `bq.py` for the first time, it will produce a link to authorize and ask to enter authorization code. Copy & paste url in browser and authorize application.    
```text
$ cd google-products-with-python

$ python3 bq.py 

   age workclass  functional_weight education  education_num       marital_status occupation  ...    race      sex capital_gain  capital_loss  hours_per_week  native_country income_bracket
0   34         ?             164309      11th              7   Married-civ-spouse          ?  ...   White   Female            0             0               8   United-States          <=50K
1   21         ?             212888      11th              7   Married-civ-spouse          ?  ...   White   Female            0             0              56   United-States          <=50K
2   28         ?             308493   HS-grad              9   Married-civ-spouse          ?  ...   White   Female            0             0              17        Honduras          <=50K
3   47         ?             331650   HS-grad              9   Married-civ-spouse          ?  ...   White   Female            0             0               8   United-States           >50K
4   22         ?              35448   HS-grad              9   Married-civ-spouse          ?  ...   White   Female            0             0              22   United-States          <=50K

```

### 2. [Extracting data from google cloud sql database as pandas DataFrame](https://github.com/dc-aichara/google-products-with-python/blob/master/csql.py)
```text
$ cd google-products-with-python
# Replace credentials and database server details with your credentials and database server details in csql.py.
$ python3 csql.py
```
### 3. [Automating Google Sheets with python](https://github.com/dc-aichara/google-products-with-python/blob/master/gs.py)
`gs.py` is a self explanatory python script.  
To learn more, please read [Medium](https://medium.com/@dcaichara/play-with-google-spreadsheets-with-python-301dd4ee36eb) article. 

### 4. [Getting Google Analytics data with python ](https://github.com/dc-aichara/google-products-with-python/blob/master/ga.py)
- Get view id from your google analytics account and get client secret from google service account. 
- Replace view id and client secret path in `ga.py`.
- Edit start and end dates in `ga.py`.
- Edit metrics on `ga.py`.

# References : 
```text
1. https://cloud.google.com/sql/docs/mysql/connect-external-app#python
2. https://cloud.google.com/bigquery/docs/pandas-gbq-migration
3. https://pygsheets.readthedocs.io/en/latest/index.html
4. https://developers.google.com/analytics/devguides/reporting/core/v4/quickstart/service-py

```