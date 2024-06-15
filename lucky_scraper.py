from bs4 import BeautifulSoup
import requests

import json
from pathlib import Path
import re


def main():
    url = 'http://rssblog.ameba.jp/luckyexchangeltd/rss20.xml'
    source = requests.get(url).text

    soup = BeautifulSoup(source, 'xml')

    exchange_rates: Path = Path.cwd() / 'exchange_rates.json'

    rates: list[dict] = []
    if saved_data := get_saved_json(exchange_rates):
        rates.extend(saved_data)

    # get dict of all items into a list and extend the rates list
    rates.extend([get_item(i.text) for i in soup.find_all('item')])

    # save all rates data to file
    write_json(rates, exchange_rates)


def get_item(item_text: str) -> dict[str: any]:
    # Scrape date to text since datetime objects will not serialize to JSON
    exchange = {}
    d = re.compile(r'(\d{4})年(\d{1,2})月(\d{1,2})')
    if matches := d.search(item_text):
        year, month, day = (int(matches.group(1)),
                            int(matches.group(2)),
                            int(matches.group(3)))

        item_date = f'{year}-{month:02}-{day:02}'
        exchange['date'] = item_date

    rate = re.compile(r'(\(Our Change.*\))[<>/\w]+(\D{3}＝)(\d{3}\.\d{2})[<>/\w]+')
    if matches := rate.search(item_text):
        # message = f'{matches.group(1)} {matches.group(2)} {matches.group(3)}'
        exchange_rate = float(matches.group(3))
        exchange['exchange rate'] = exchange_rate

    return exchange


def get_saved_json(file: Path) -> list[dict] | None:
    if file.exists():
        data: str = file.read_text()
        return json.loads(data)


def write_json(data: list[dict], file: Path) -> None:
    json_payload = json.dumps(data, indent=4)
    file.write_text(json_payload)


if __name__ == '__main__':
    main()
