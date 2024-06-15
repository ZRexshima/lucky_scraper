import json
from pathlib import Path
from lucky_scraper import get_saved_json
from lucky_scraper import write_json
from lucky_scraper import get_item


def test_get_saved_json():
    """Tests retrieval of json from test.json after creating the file"""
    data: list[dict] = [{'date': '2024-06-15', 'rate': 153.3}]
    test_file: Path = Path.cwd() / 'test.json'
    json_payload = json.dumps(data, indent=4)
    test_file.write_text(json_payload)

    test_list: list[dict] = get_saved_json(test_file)
    assert test_list[0] == {'date': '2024-06-15', 'rate': 153.3}


def test_write_json():
    """Tests saving json to file"""
    data: list[dict] = [{'date': '2024-06-15', 'rate': 153.3}]
    test_file: Path = Path.cwd() / 'test.json'
    # json_payload = json.dumps(data, indent=4)
    # test_file.write_text(json_payload)
    write_json(data, test_file)

    file_data = test_file.read_text()
    raw_data = json.loads(file_data)
    assert raw_data == data


def test_get_item():
    ...

