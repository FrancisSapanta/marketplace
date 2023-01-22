import gspread
from oauth2client.service_account import ServiceAccountCredentials


def get_sheet(user_request):

    scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

    creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)

    client = gspread.authorize(creds)

    sheet = client.open("MarketAPI").sheet1 
    data = sheet.get_values()  

    data = sheet.findall(user_request)

    for x in range(len(data)):
        row = sheet.row_values(data[x].row)
        print(row)

# get_sheet()