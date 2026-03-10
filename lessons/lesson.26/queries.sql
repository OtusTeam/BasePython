SELECT 1;


select 1;

select version();

select uuidv7();

select now();


select 1 as one;
select 1  + 2 as "three";
select 1  + 2 as "1 + 2";
select 1  + 2 "1 + 2 =";


create table if not exists notes (
    id serial primary key not null,
    title text not null unique,
    note text not null default '',
    created_at timestamptz not null default now()
);

drop table notes;

insert into notes (title, note)
values ('SQL Intro', 'My thoughts on the SQL intro.');


insert into notes (title, note)
values
    ('Python Intro', 'Some Python tricks'),
    ('JS Intro', 'Frontend most used language.');


select *
from notes;



select *
from notes
order by id desc;

select *
from notes
order by note;

select *
from notes
where note like '%.';


select *
from notes
where title ilike '%js%';

select
      'user_' || idx || '@example.com'
    , 'User Name ' || idx
    , idx % 3 != 0
    , now() - (random() * interval '365 days')
from generate_series(1, 100000) as idx;
