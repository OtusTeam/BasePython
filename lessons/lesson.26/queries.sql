SELECT version();

select 1;

select 1, 2;
select 1 + 2;
select 1 + 2, 3 + 4;


select 1 + 2 as sum, 3 + 4;
select 1 + 2 as sum, 3 + 4 total;

select 1 + 2 as "sum 1 + 2", 3 + 4 total;

select 'hello' hi;

select generate_series(1, 10);

select 'hello ' || 'world!' hi;

select 'hello ' || 'world!' || coalesce(null, '');

select 'hello' || 1;


--

create table users (
    id bigint generated always as identity primary key,
    username text check ( length(username) <= 32 ) unique
);



alter table users
    alter column username set not null;


alter table users
add column email text check ( length(email) <= 120 )unique;


select *
from users;


select *
from users
order by id;


select *
from users
order by username;

select *
from users
order by username desc;

insert into users (username)
values ('alice');

insert into users (username)
values ('Alice');

delete from users
where username = 'Alice';

update users
set email = username || '@example.com'
where username not like '%-%';

select *
from users
where username not like '%-%'
order by id;

select *
from users
where length(username) > 3
order by id;


insert into users (username, email)
values ('john', NULL),
       ('clark', 'clark@yahoo.com');


select *
from users
order by id;


select *
from users
where email like '%@example.com'
order by id;


select 1 = 1, 2 = 3, null = null, null is null;
