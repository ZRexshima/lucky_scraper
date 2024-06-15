import json
from pathlib import Path
from json_reader import get_saved_json


def test_get_saved_json():
    """Tests retrieval of json from test.json after creating the file"""
    data: list[dict] = [{'date': '2024-06-15', 'rate': 153.3}]
    test_file: Path = Path.cwd() / 'test.json'
    json_payload = json.dumps(data, indent=4)
    test_file.write_text(json_payload)

    test_list: list[dict] = get_saved_json(test_file)
    assert test_list[0] == {'date': '2024-06-15', 'rate': 153.3}
