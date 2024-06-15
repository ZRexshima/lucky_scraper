import json
from pathlib import Path

exchanges = []
test_file: Path = Path.cwd() / 'test.json'
if test_file.exists():
    data = test_file.read_text()
    read_json = json.loads(data)
    exchanges.extend(read_json)


exchange: dict[str, str] = {'date': '2024-06-15', 'rate': 153.30}

exchanges.append(exchange)

json_payload: str = json.dumps(exchanges)
print(exchanges)
print()
print(json_payload)


test_file.write_text(json_payload)

