import pytest
from Tests_Task2.main import create_directory
import requests

fixtures = [
    ('Directory1'),
    ('Directory2'),
    ('Directory3'),
    ('Directory4')
]


@pytest.mark.parametrize('name_directory', fixtures)
def test_one_create_directory(name_directory):
    status_code = create_directory(name_directory).status_code
    assert status_code == 201


@pytest.mark.parametrize('name_directory', fixtures)
def test_info_dir(name_directory):
    url = 'https://cloud-api.yandex.net/v1/disk/resources'
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Authorization': 'OAuth AQAAAAAQzmQWAADLW9XBkawjzkmls2tgCa4g0eM'
    }
    param = {
        'path': name_directory,
        'limit': '0'
    }
    response = requests.get(url=url, params=param, headers=headers)
    assert response.status_code == 200


@pytest.mark.parametrize('name_directory', fixtures)
def test_del_create_directory(name_directory):
    url = 'https://cloud-api.yandex.net/v1/disk/resources'
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Authorization': 'OAuth AQAAAAAQzmQWAADLW9XBkawjzkmls2tgCa4g0eM'
    }
    param = {
        'path': name_directory,
        'permanently': 'true'
    }
    response = requests.delete(url=url, params=param, headers=headers)
    assert response.status_code == 204
