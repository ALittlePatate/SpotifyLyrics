import os
import csv
import re
import requests
import webbrowser
from bs4 import BeautifulSoup

os.system('tasklist /v /fi "IMAGENAME eq Spotify.exe" /fo List > list.csv')

with open('list.csv', encoding='latin1', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)

title = str(data[9])
title = re.split(':', title)
title = str(title[1])
title = title[:-2]
title = title[1:]
print(title)

USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0"
headers = {"user-agent": USER_AGENT}
URL = "https://google.com/search?q="+title+" rap genius"
resp = requests.get(URL, headers=headers)
soup = BeautifulSoup(resp.content, "html.parser")
results = []
for g in soup.find_all('div', class_='r'):
    anchors = g.find_all('a')
    if anchors:
        link = anchors[0]['href']
        item = {
            link
            }
        results.append(item)
        results = str(results[0])
        break

results = results[:-2]
results = results[2:]
webbrowser.open(results)
os.system('del list.csv')

