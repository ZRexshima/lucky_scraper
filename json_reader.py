import json
from pathlib import Path


def main():
    exchanges = []
    test_file: Path = Path.cwd() / 'test.json'
    if read_json := get_saved_json(test_file):
        exchanges += read_json
    exchange = {'date': '2024-06-16', 'rate': 153.1}
    exchanges.append(exchange)
    print(exchanges)


def get_saved_json(file: Path) -> list[dict] | None:
    if file.exists():
        data: str = file.read_text()
        return json.loads(data)


def write_json(data: str, file: Path) -> None:
    json_payload = json.dumps(data, indent=4)
    file.write_text(json_payload)


if __name__ == '__main__':
    main()
