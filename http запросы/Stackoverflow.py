from pprint import pprint

import requests

import datetime

date1 = datetime.date.today() - datetime.timedelta(days=2)
date2 = datetime.date.today() - datetime.timedelta(days=1)

url = 'https://api.stackexchange.com/2.3/questions'
param = {'fromdate': date1, 'todate': date2, 'tagged': 'Python', 'site': 'stackoverflow'}
x = requests.get(url=url, params=param)
pprint(x.json())