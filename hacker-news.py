#!/opt/homebrew/anaconda3/bin/python

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title Hacker News
# @raycast.mode compact

# Optional parameters:
# @raycast.icon 📰
# @raycast.argument1 { "type": "text", "placeholder": "Date (e.g., 0604)", "optional": true }

# Documentation:
# @raycast.description Open top 30 links in the front page of Hacker News
# @raycast.author wenkaiyn
# @raycast.authorURL https://raycast.com/wenkaiyn

import sys
import webbrowser
from datetime import datetime, timedelta, timezone
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup

if len(sys.argv) == 1 or not sys.argv[1]:
    date = (datetime.now(timezone.utc) - timedelta(days=1.5)).strftime('%Y-%m-%d')
else:
    date = str(datetime.now(timezone.utc).year) + '-' + sys.argv[1][:2] + '-' + sys.argv[1][2:]
url = f'https://news.ycombinator.com/front?day={date}'

response = requests.get(url)
response.raise_for_status()

soup = BeautifulSoup(response.text, 'html.parser')
links = [span.find('a')['href'] for span in soup.find_all('span', class_='titleline')]

for link in [url] + links:
    if link.startswith('item?id='):
        link = urljoin('https://news.ycombinator.com', link)

    print('Opening:', link)
    webbrowser.open_new_tab(link)
