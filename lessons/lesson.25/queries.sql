SELECT version();

SELECT gen_random_uuid();

SELECT now();

select 1;

select 1, 2;

select 1 as "one", 2 as "two";


select 1 one, 2 "two", 1 + 2 three;


select 1 one, 2 "two", 1 + 2 "one and two";

select *
from pg_catalog.pg_timezone_names;

select "name", abbrev
from pg_timezone_names;

select "name", abbrev
from pg_timezone_names
order by "name" desc;

select "name", abbrev, utc_offset
from pg_timezone_names
where abbrev = 'MSK'
order by "name";

select "name", abbrev, utc_offset
from pg_timezone_names
where "name" ilike '%moscow%'
order by "name";

select "name", abbrev, utc_offset
from pg_timezone_names
where abbrev ilike 'msk'
order by "name";


create table if not exists notes (
    id smallserial primary key not null,
    note_text text not null default ''
);

insert into notes (note_text)
values ('hello pglite');

insert into notes (note_text)
values ('hello postgres'),
       ('hello again');

select *
from notes;

update notes
set id = 10
where id = 1;


create table if not exists better_notes (
    id bigint generated always as identity primary key,
    title text not null default '',
    "text" text not null default ''
);

drop table better_notes;

insert into better_notes (title, "text")
values ('PG Intro', 'some text'),
       ('SQL Intro', 'Structured query language'),
       ('Python Lesson', 'print("hello py")');

select *
from better_notes;

select *
from better_notes
where title ilike '%intro%';
