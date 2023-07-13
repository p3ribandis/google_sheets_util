import pygsheets
import random


class pygsheetsExt:

    gc = pygsheets.authorize(service_account_file="google_sheets_util/mypython_secret_id.json")
    sh = gc.open('anekdoty')

    def getData(sheetName):
        wks = pygsheetsExt.sh.worksheet_by_title(sheetName)
        col = wks.get_col(1, returnas='matrix', include_tailing_empty=False)
        r = random.randint(0, len(col)-1)
        res = col[r]
        return res

    def set_new_worksheet(name, content):
        wks = pygsheetsExt.sh.add_worksheet(name)
        wks.update_col(1, content)
        print('ready')
