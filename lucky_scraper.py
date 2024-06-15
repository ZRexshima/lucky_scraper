from bs4 import BeautifulSoup
import requests

from datetime import date
import re


url = 'http://rssblog.ameba.jp/luckyexchangeltd/rss20.xml'
source = requests.get(url).text

soup = BeautifulSoup(source, 'xml')

# get a single item
item_text = soup.find('item').get_text()

exchange = {}
# Scrape and convert date to datetime.date object
d = re.compile(r'(\w{3})\.(\d{1,2})\.{2}(\d{4})\b')
if matches := d.search(item_text):
    m = matches.group(1)
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
              'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    if m in months:
        month = months.index(m) + 1
    else:
        raise ValueError('Invalid month value')

    day = int(matches.group(2))
    year = int(matches.group(3))
    item_date = date(year, month, day)
    exchange['date'] = item_date

rate = re.compile(r'(\(Our Change.*\))[<>/\w]+(\D{3}＝)(\d{3}\.\d{2})[<>/\w]+')
if matches := rate.search(item_text):
    message = f'{matches.group(1)} {matches.group(2)} {matches.group(3)}'
    exchange_rate = float(matches.group(3))
    exchange['exchange rate'] = exchange_rate


print(exchange)
