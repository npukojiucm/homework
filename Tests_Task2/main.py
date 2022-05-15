from pprint import pprint

import requests


def create_directory(name_directory):
    url = 'https://cloud-api.yandex.net/v1/disk/resources'
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Authorization': 'OAuth AQAAAAAQzmQWAADLW9XBkawjzkmls2tgCa4g0eM'
    }
    param = {'path': name_directory}

    response = requests.put(url=url, params=param, headers=headers)
    return response

# pprint(create_directory('Test_dir').json())