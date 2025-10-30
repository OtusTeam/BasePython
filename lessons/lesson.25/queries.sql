SELECT 1;

SELECT version();

SELECT 1 + 2;

SELECT 2 + 3 as "two-and-three";
SELECT 2 + 3 "two-and-three";

select 3 + 4 num;


select gen_random_uuid();


SELECT 2 + 3, 5 + 6;

select now(), gen_random_uuid();

select *
from pg_timezone_names;

select "name", abbrev, utc_offset
from pg_timezone_names;

select name, abbrev, utc_offset
from pg_timezone_names
order by name;

select name, abbrev, utc_offset
from pg_timezone_names
where name ilike '%moscow%'
order by name;

select name, abbrev, utc_offset
from pg_timezone_names
where abbrev = 'MSK'
order by name;

select name, abbrev, utc_offset
from pg_timezone_names
where name = 'Europe/Moscow'
order by name;

select name, abbrev, utc_offset
from pg_timezone_names
where name ilike '%peter%'
order by name;

-----


create table users (
    id bigserial primary key,
    username varchar(32) unique not null,
    email varchar(150) unique,
    full_name varchar not null default ''
);

select users.id user_id
     , email
from users;

select *
from users
where email = 'foobar@example.com';

insert into users (username, email)
values ('bob', 'bob@example.com');

insert into users (username)
values ('sam');

insert into users (username)
values ('kate'),
       ('john');

insert into users (username, email)
values ('nick', 'n@example.com'),
       ('nans', 'n@example.com');

insert into users (username, email)
values ('nick', 'nick@example.com'),
       ('nans', 'nans@example.com');


select *
from users
where email is null;

select *
from users
where email is not null;


insert into users (username, email)
values ('jack', 'jack@example.com'),
       ('alice', NULL);


select *
from users
order by id;
