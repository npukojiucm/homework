from datetime import datetime
import requests
import sqlalchemy
import psycopg2
from tqdm import tqdm


class LastFM:
    url = 'http://ws.audioscrobbler.com/2.0/'
    params = {
        'api_key': 'db277c645d0f72fc182f4d5720404680',
        'format': 'json'
    }

    def chart_gettopartists(self, limit):
        """
        Получение артистов из топ чарта
        """
        chart_gettopartists_params = {
            'method': 'chart.gettopartists',
            'limit': limit
        }
        response = requests.get(url=self.url, params={**self.params, **chart_gettopartists_params}).json()
        top_artist = [name['name'] for name in response['artists']['artist']]
        return top_artist

    def artist_gettoptags(self, artist):
        """
        Получение тэгов(жанров) из топ чарта
        """
        artist_gettoptags_params = {
            'method': 'artist.gettoptags',
            'artist': artist
        }
        response = requests.get(url=self.url, params={**self.params, **artist_gettoptags_params}).json()
        return response

    def artist_gettopalbums(self, artist, limit):
        """"
        Получение топ альбомов артиста
        """
        artist_gettopalbums_params = {
            'method': 'artist.gettopalbums',
            'artist': artist,
            'limit': limit
        }
        response = requests.get(url=self.url, params={**self.params, **artist_gettopalbums_params}).json()
        album = [album['name'].replace("'", "`") for album in
                 response['topalbums']['album']]
        return album

    def album_getinfo(self, artist, album):
        """
        Получение информации о альбоме
        """
        album_getinfo_params = {
            'method': 'album.getinfo',
            'artist': artist,
            'album': album
        }
        response = requests.get(url=self.url, params={**self.params, **album_getinfo_params}).json()
        return response


db = 'postgresql://@localhost:5432/'
engine = sqlalchemy.create_engine(db)
connection = engine.connect()


fm = LastFM()

artist = fm.chart_gettopartists('8')

for artist_ in artist:
    connection.execute(f"""
    INSERT INTO performers(name)
    VALUES('{artist_}');
    """)

genre = set()
for artist_ in tqdm(artist):
    for genre_ in fm.artist_gettoptags(artist_)['toptags']['tag'][0:5]:
        genre.add(genre_['name'])
for genre_ in tqdm(genre):
    connection.execute(f"""
    INSERT INTO genre(name)
    VALUES('{genre_}');
    """)

for artist_ in tqdm(artist):
    for genre_ in fm.artist_gettoptags(artist_)['toptags']['tag'][0:5]:
        connection.execute(f"""
        INSERT INTO performgenre(perform_name, genre_name)
        VALUES('{artist_}', '{genre_['name']}');
        """)

tracks = set()
for artist_ in tqdm(artist):
    album = fm.artist_gettopalbums(artist_, '4')
    for album_ in album[0:2]:
        if 'wiki' in fm.album_getinfo(artist_, album_)['album'].keys():
            if 'published' in fm.album_getinfo(artist_, album_)['album']['wiki']:
                            date = fm.album_getinfo(artist_, album_)['album']['wiki']['published']
                            date_format = '%d %b %Y, %H:%M'
                            year = int(str(datetime.strptime(date, date_format))[0:4])
        else:
            year = 0000

        connection.execute(f"""
                INSERT INTO albums(name, year_issue)
                VALUES('{album_}', {year});
                """)

        connection.execute(f"""
                        INSERT INTO performalbums(perform_name, album_name)
                        VALUES('{artist_}', '{album_}');
                        """)

        collections = album[album.index(album_) + 2]
        connection.execute(f"""
                                INSERT INTO collections(name, year_issue)
                                VALUES('{collections}', '{year}');
                                """)


        for info in fm.album_getinfo(artist_, album_):
            if 'album' not in fm.album_getinfo(artist_, album_).keys():
                continue
            if 'tracks' not in fm.album_getinfo(artist_, album_)['album'].keys():
                continue
            for track in fm.album_getinfo(artist_, album_)['album']['tracks']['track']:
                if track['duration'] is None:
                    continue
                if track['name'].replace("'", "`") not in tracks:
                    tracks.add(track['name'].replace("'", "`"))
                    connection.execute(f"""
                                    INSERT INTO tracks(name, duration, album_name)
                                    VALUES('{track['name'].replace("'", "`")}', {track['duration']}, '{album_}');
                                """)
                else:
                    continue
                connection.execute(f"""
                                INSERT INTO collecttracks(collect_name, tracks_name)
                                VALUES('{collections}', '{track['name'].replace("'", "`")}');
                            """)

