import requests


class SuperHero:
    def __init__(self, token: str):
        self.token = token

    def _id_hero(self, name_hero: list):
        id_ = {}
        for name in name_hero:
            url = f'https://superheroapi.com/api/{self.token}/search/{name}'
            res = requests.get(url=url)
            id_[name] = res.json().get('results')[0]['id']
        return id_

    def intell_hero(self, name_hero: list):
        hero = {}
        for name, id in self._id_hero(name_hero).items():
            url = f'https://superheroapi.com/api/{self.token}/{id}/powerstats'
            res = requests.get(url=url).json().get('intelligence')
            hero[name] = int(res)
        for name, id in hero.items():
            if id == sorted(hero.values(), reverse=True)[0]:
                print(f'Самый умный {name} - {id}')
        print(hero)


TOKEN = SuperHero('2619421814940190')
super_hero = ['Hulk', 'Captain America', 'Thanos']

TOKEN.intell_hero(super_hero)
