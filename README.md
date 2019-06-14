
This repository has python scripts to access google products (Big Query, Cloud SQL,Google sheets, Google Analytics).
***
```text
To access BigQuery, Cloud SQL, Google Analytics, you must have a project on google cloud platform and a service account.

```
How to get a project and a service account ?

[See documentation for help](https://cloud.google.com/iam/docs/creating-managing-service-accounts)


```text
To access Google Analytics, you must have permissions to view google analytics account [user account is sufficient]. 
```
```text
To access google sheets, you must have permission to edit google sheet to be accessed. 
```

## Usage
### 1. Extracting data from Google Big Query as pandas dataframe
When you run bq.py for the first time, it will produce a link to authorize and ask to enter authorization code. Copy & paste url in browser and authorize application.    
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

### 2. Extracting data from google cloud sql database as pandas dataframe
```text
$ cd google-products-with-python
# Replace credentials and database server details with your credentials and database server details in csql.py.
$ python3 csql.py
```

