create table if not exists Performers (
	Id serial primary key,
	Name text not null
);

create table if not exists Genre (
	Id serial primary key,
	Name text not null
);

create table if not exists PerformGenre (
	perform_id integer not null references Performers(Id),
	genre_id integer not null references Genre(Id),
	constraint perfom_genre primary key (perform_id, genre_id)
);

create table if not exists Albums (
	Id serial primary key,
	Name text not null,
	Year_issue date not null
);

create table if not exists PerformAlbums (
	perform_id integer not null references Performers(Id),
	album_id integer not null references Albums(Id),
	constraint perform_albums primary key (perform_id, album_id)
);

create table if not exists Tracks (
	Id serial primary key,
	Name text not null,
	Duration time not null,
	Id_Genre integer references Albums(Id)
);

create table if not exists Collections (
	Id serial primary key,
	Name text not null,
	Year_issue date not null
);

create table if not exists CollectTracks (
	collect_id integer not null references Collections(Id),
	tracks_id integer not null references Tracks(Id),
	constraint collect_tracks primary key (collect_id, tracks_id)
);