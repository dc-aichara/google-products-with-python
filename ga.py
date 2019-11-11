"""Hello Analytics Reporting API V4."""
########################################################################################################################
# This python script would be used to get Google analytics data such as user, sessions etc on particular website
# This uses Google Analytics API V4
# Get VIEW_ ID From you Google Analytics web account
# You can modify range of data or what data you want
########################################################################################################################
import argparse

from apiclient.discovery import build
import httplib2
from oauth2client import client
from oauth2client import file
from oauth2client import tools
from datetime import datetime

date = datetime.now().strftime('%Y-%m-%d')
SCOPES = ['https://www.googleapis.com/auth/analytics.readonly']
DISCOVERY_URI = ('https://analyticsreporting.googleapis.com/$discovery/rest')
CLIENT_SECRETS_PATH = 'Downloads/client_secret.json'  # Path to client_secrets.json file.
VIEW_ID = 'Your View ID'  # VIEW_ID  is  profile id GA account which information to be collected


def initialize_analyticsreporting():
  """Initializes the analyticsreporting service object.

  Returns:
    analytics an authorized analyticsreporting service object.
  """
# Parse command-line arguments.
  parser = argparse.ArgumentParser(
      formatter_class=argparse.RawDescriptionHelpFormatter,
      parents=[tools.argparser])
  flags = parser.parse_args([])

#  Set up a Flow object to be used if we need to authenticate.

  flow = client.flow_from_clientsecrets(
      CLIENT_SECRETS_PATH, scope=SCOPES,
      message=tools.message_if_missing(CLIENT_SECRETS_PATH))

  """
  Prepare credentials, and authorize HTTP object with them.
  If the credentials don't exist or are invalid run through the native client
  flow. The Storage object will ensure that if successful the good
  credentials will get written back to a file. 
  """

  storage = file.Storage('analyticsreporting.dat')
  credentials = storage.get()
  if credentials is None or credentials.invalid:
    credentials = tools.run_flow(flow, storage, flags)
  http = credentials.authorize(http=httplib2.Http())

# Build the service object.
  analytics = build('analytics', 'v4', http=http, discoveryServiceUrl=DISCOVERY_URI)

  return analytics

def get_report(analytics):

    #  Use the Analytics Service Object to query the Analytics Reporting API V4.

  return analytics.reports().batchGet(
      body={
        'reportRequests': [
        {
          'viewId': VIEW_ID,
          'dateRanges': [{'startDate': 'yesterday', 'endDate': 'yesterday'}], # date range for data
            'dimensions': [{'name': 'ga:date'}], # Dimension of table or table index
          'metrics': [     # Variables / Columns
              {'expression': 'ga:Users'},
              {'expression': 'ga:NewUsers'},
              {'expression': 'ga:Sessions'},
              {'expression': 'ga:Pageviews'},
              {'expression': 'ga:sessionsPerUser'},
              {'expression': 'ga:AvgSessionDuration'},
              {'expression': 'ga:bouncerate'}
            ]
        }]
      }
  ).execute()


def get_response(response):
  """Parses and prints the Analytics Reporting API V4 response"""

  for report in response.get('reports', []):
    rows = report.get('data', {}).get('rows', [])
    ga_data = []
    for row in rows:
      dateRangeValues = row.get('metrics', [])

      for values in dateRangeValues:
          ga_data.append(values.get('values', []))
       # store data in google sheets
      gc = pygsheets.authorize()

      wks = gc.open('your google sheet name')[0]
      wks.insert_rows(row =1, number =1)
      wks.update_values('B2', ga_data)
      wks.update_values('A2', [[date]])
  　return ga_data


def main():

  analytics = initialize_analyticsreporting()
  response = get_report(analytics)
  get_response(response)

if __name__ == '__main__':
  main()

