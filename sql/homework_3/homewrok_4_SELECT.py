from pprint import pprint

import sqlalchemy
import psycopg2

db = 'postgresql://npuko:1234@localhost:5432/homework'
engine = sqlalchemy.create_engine(db)
connection = engine.connect()

pprint(connection.execute(f"""
    SELECT genre_name , COUNT(*) FROM performgenre
    GROUP BY genre_name
    ORDER BY COUNT(*) DESC;
""").fetchall())

pprint(connection.execute(f"""
    SELECT COUNT(album_name) FROM albums a
    JOIN tracks t ON a.name = t.album_name
    WHERE year_issue BETWEEN 2019 AND 2020;
""").fetchall())

pprint(connection.execute(f"""
    SELECT a.name, ROUND(AVG(t.duration), 2) FROM albums a
    JOIN tracks t ON a.name = t.album_name
    GROUP BY a.name
    ORDER BY AVG(t.duration);
""").fetchall())

pprint(connection.execute(f"""
    SELECT name FROM performers
    WHERE name != (
        SELECT perform_name FROM performalbums pa
        JOIN albums a ON pa.album_name = a.name
        WHERE year_issue = 2020);
""").fetchall())

pprint(connection.execute(f"""
    SELECT cl.name FROM performers p
    JOIN performalbums pa ON p.name = pa.perform_name
    JOIN albums a ON pa.album_name = a.name
    JOIN tracks t ON a.name = t.album_name
    JOIN collecttracks ct ON t.name = ct.tracks_name
    JOIN collections cl ON ct.collect_name = cl.name
    WHERE p.name = 'Billie Eilish'
    GROUP BY cl.name;
""").fetchall())

pprint(connection.execute(f"""
    SELECT pa.album_name FROM performalbums pa
    JOIN performers p ON pa.perform_name = p.name
    JOIN performgenre pg ON p.name = pg.perform_name
    GROUP BY pa.album_name
    HAVING COUNT(genre_name) > 1;
""").fetchall())

pprint(connection.execute(f"""
    SELECT t.name, COUNT(collect_name) FROM tracks t
    JOIN collecttracks ct ON t.name = ct.tracks_name
    GROUP BY t.name
    HAVING COUNT(collect_name) = 0;
""").fetchall())

pprint(connection.execute(f"""
    SELECT p.name FROM performers p
    JOIN performalbums pa ON p.name = pa.perform_name
    JOIN albums a ON pa.album_name = a.name
    JOIN tracks t ON a.name = t.album_name
    WHERE duration = (
        SELECT MIN(duration) FROM tracks);
""").fetchall())

pprint(connection.execute(f"""
    SELECT a.name FROM albums a
    JOIN tracks t ON a.name = t.album_name
    GROUP BY a.name
    HAVING COUNT(t.name) = (
        SELECT COUNT(t.name) FROM tracks t
        GROUP BY album_name
        ORDER BY COUNT(t.name)
        LIMIT 1);
""").fetchall())