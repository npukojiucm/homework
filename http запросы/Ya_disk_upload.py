import os.path

import requests


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        """Метод загружает файлы по списку file_list на яндекс диск"""
        name_file = os.path.basename(file_path)
        url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        head = {'Accept': 'application/json', 'Authorization': 'OAuth {}'.format(self.token)}
        param = {'path': '{}'.format(name_file), 'overwrite': 'True'}
        resp_get = requests.get(url=url, headers=head, params=param).json().get('href')
        x = requests.put(url=resp_get, headers=head, data=open(file_path))
        if x.status_code == 201:
            print('Загрузка прошла успешно!!!')


if __name__ == '__main__':
    path_to_file = ''
    token = ''
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)
