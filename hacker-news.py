#!/opt/homebrew/Caskroom/miniconda/base/bin/python

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
from html.parser import HTMLParser
from urllib.parse import urljoin
from urllib.request import Request, urlopen


class TitleLinkParser(HTMLParser):
    """Collects the first <a href> inside each <span class="titleline">."""

    def __init__(self):
        super().__init__()
        self.links = []
        self._in_titleline = False

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'span' and attrs.get('class') == 'titleline':
            self._in_titleline = True
        elif tag == 'a' and self._in_titleline and 'href' in attrs:
            self.links.append(attrs['href'])
            self._in_titleline = False


if len(sys.argv) == 1 or not sys.argv[1]:
    date = (datetime.now(timezone.utc) - timedelta(days=1.5)).strftime('%Y-%m-%d')
else:
    date = str(datetime.now(timezone.utc).year) + '-' + sys.argv[1][:2] + '-' + sys.argv[1][2:]
url = f'https://news.ycombinator.com/front?day={date}'

with urlopen(Request(url, headers={'User-Agent': 'Mozilla/5.0'})) as response:
    html = response.read().decode('utf-8')

parser = TitleLinkParser()
parser.feed(html)
links = parser.links

for link in [url] + links:
    if link.startswith('item?id='):
        link = urljoin('https://news.ycombinator.com', link)

    print('Opening:', link)
    webbrowser.open_new_tab(link)
