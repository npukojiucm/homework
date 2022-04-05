create table if not exists Genre (
	Id serial primary key,
	Name text not null
);

create table if not exists Performers (
	Id serial primary key,
	Name text not null,
	Id_Genre integer references Genre(Id)
);

create table if not exists Albums (
	Id serial primary key,
	Name text not null,
	Year_issue date not null,
	Id_Genre integer references Performers(Id)
);

create table if not exists Tracks (
	Id serial primary key,
	Name text not null,
	Duration time not null,
	Id_Genre integer references Albums(Id)
);
