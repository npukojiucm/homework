import sqlalchemy
import psycopg2

db = 'postgresql://npuko:1234@localhost:5432/homework'
engine = sqlalchemy.create_engine(db)
connection = engine.connect()

print(connection.execute(f"""
    SELECT name, year_issue FROM albums
    WHERE year_issue = 2018;
    """).fetchall())

print(connection.execute(f"""
    SELECT name, duration FROM tracks
    ORDER BY duration DESC;
    """).fetchone())

print(connection.execute(f"""
    SELECT name FROM tracks
    WHERE duration >= 210;
    """).fetchall())

print(connection.execute(f"""
    SELECT name FROM collections
    WHERE year_issue BETWEEN 2018 and 2020;
    """).fetchall())

print(connection.execute(f"""
    SELECT name FROM performers
    WHERE name NOT ILIKE '%% %%';
    """).fetchall())

print(connection.execute(f"""
    SELECT name FROM tracks
    WHERE name ILIKE '%% my %%' or name ILIKE '%% мой %%';
    """).fetchall())
