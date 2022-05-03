from datetime import datetime
import bs4
import requests
import re

url_timeline = 'https://habr.com/ru/all/'
url_basic = 'https://habr.com'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

KEYWORDS = ['дизайн', 'фото', 'web', 'python']
#
responce = requests.get(url=url_timeline, headers=headers)
text = responce.text

soup = bs4.BeautifulSoup(text, features='html.parser')
articles = soup.findAll(class_='tm-article-snippet__title tm-article-snippet__title_h2')

for article in articles:
    href = article.find(class_='tm-article-snippet__title-link').attrs['href']
    responce = requests.get(url=f'{url_basic}{href}', headers=headers)
    text = responce.text
    soup = bs4.BeautifulSoup(text, features='html.parser')
    tittle = soup.find(class_='tm-article-snippet__title tm-article-snippet__title_h1').text
    hubs = soup.find_all(class_='tm-article-snippet__hubs-item')
    hubs = [hub.text.lower() for hub in hubs]
    body = soup.find(id='post-content-body').text
    date = soup.find(class_='tm-article-snippet__datetime-published').find('time').attrs['title'][0:10]
    for key in KEYWORDS:
        search = re.findall(rf'\b{key}\b', tittle.lower() + ''.join(hubs) + body.lower())
        if key in search:
            print(key)
            print(datetime.strptime(date, "%Y-%m-%d").date(), tittle, url_basic + href)
            break