import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd

# Connect to Google
# Scope: Enable access to specific links
scope = ['https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive"]

credentials = ServiceAccountCredentials.from_json_keyfile_name("gs_credentials.json", scope)
client = gspread.authorize(credentials)

# Create a blank spreadsheet (Note: We're using a service account, so this spreadsheet is visible only to this account)
sheet = client.create("NewDatabase")

# To access newly created spreadsheet from Google Sheets with your own Google account you must share it with your email
# Sharing a Spreadsheet
sheet.share('your_email_goes_here', perm_type='user', role='writer')

# Open the spreadsheet
sheet = client.open("NewDatabase").sheet1
# read csv with pandas
df = pd.read_csv('football_news.csv')
# export df to a sheet
sheet.update([df.columns.values.tolist()] + df.values.tolist())
