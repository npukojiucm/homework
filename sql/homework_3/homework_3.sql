create table if not exists performers (
	id serial,
	name text not null primary key
);

create table if not exists genre (
	id serial,
	name text not null primary key
);

create table if not exists performgenre (
	perform_name text not null references performers(name),
	genre_name text not null references genre(name),
	constraint perfom_genre primary key (perform_name, genre_name)
);

create table if not exists albums (
	id serial,
	name text not null primary key,
	year_issue integer not null
);

create table if not exists performalbums (
	perform_name text not null references performers(name),
	album_name text not null references albums(name),
	constraint perform_albums primary key (perform_name, album_name)
);

create table if not exists tracks (
	id serial,
	name text not null primary key,
	duration integer not null,
	album_name text references albums(name)
);

create table if not exists collections (
	id serial,
	name text not null primary key,
	year_issue integer not null
);

create table if not exists collecttracks (
	collect_name text not null references collections(name),
	tracks_name text not null references tracks(name),
	constraint collect_tracks primary key (collect_name, tracks_name)
);