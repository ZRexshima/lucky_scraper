from bs4 import BeautifulSoup
import requests

from datetime import date
import re


def main():
    url = 'http://rssblog.ameba.jp/luckyexchangeltd/rss20.xml'
    source = requests.get(url).text

    soup = BeautifulSoup(source, 'xml')

    # get a single item
    item_text = soup.find('item').get_text()

    items = []
    item = {}
    if new_data := get_item(item_text):
        item = new_data
        items.append(item)
    print(item)
    print(items)


def get_item(item_text: str) -> dict[str: any]:
    # Scrape and convert date to datetime.date object
    exchange = {}
    d = re.compile(r'(\w{3})\.(\d{1,2})\.{2}(\d{4})\b')
    if matches := d.search(item_text):
        m, day, year = (matches.group(1), int(matches.group(2)),
                        int(matches.group(3)))
        months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                  'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        if m in months:
            month = months.index(m) + 1
        else:
            raise ValueError('Invalid month value')

        item_date = date(year, month, day)
        exchange['date'] = item_date

    rate = re.compile(r'(\(Our Change.*\))[<>/\w]+(\D{3}＝)(\d{3}\.\d{2})[<>/\w]+')
    if matches := rate.search(item_text):
        message = f'{matches.group(1)} {matches.group(2)} {matches.group(3)}'
        exchange_rate = float(matches.group(3))
        exchange['exchange rate'] = exchange_rate

    return exchange


if __name__ == '__main__':
    main()
