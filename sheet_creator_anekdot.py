import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
from sheets import pygsheetsExt as pyg

URL_TEMPLATE = "https://baneks.ru/top"
r = requests.get(URL_TEMPLATE)
r.encoding = 'utf8'

soup = bs(r.text, "html.parser")
sheet_content = soup.find_all('a')
sheet_name = soup.find('h1') 
content_text = []
for i in range(1, len(sheet_content)):
    content_text.append(sheet_content[i].text)

pyg.set_new_worksheet(sheet_name.text, content_text)
