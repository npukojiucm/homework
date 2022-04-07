create table if not exists Department (
	id serial primary key,
	name varchar(40) not null
);

create table if not exists Employee (
	id serial,
	name text not null,
	department_id integer not null references Department(id),
	constraint employee_pk primary key (id, name)
);

create table if not exists Manager (
	id integer primary key,
	name text not null,
	foreign key (id, name) references Employee (id, name)
);

alter table Employee add column manager integer references Manager(id);
