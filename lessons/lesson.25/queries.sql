-- sqlite examples

SELECT * FROM demo;

select * from demo where hint like '%new%';

select * from demo where name like '%port%';

select * from demo where name = 'Import';


-- postgres examples

select version();

select 'hello';

select 1 as "one";


select 2 two, 3 "three (3)";


select 'one' "one (один)", 2 two, 3 "three (3)", '4' "four (string)";


create table if not exists authors (
  id serial primary key,
  username text unique not null
);

CREATE TABLE posts (
    id SERIAL PRIMARY KEY,
    title text NOT NULL,
    body TEXT NOT NULL default '',
    author_id INTEGER NOT NULL,
    CONSTRAINT fk_author
        FOREIGN KEY (author_id)
        REFERENCES authors(id)
        ON DELETE CASCADE
);



select * from authors;


select * from posts;


select id, title, author_id from posts;


select p.id, p.title, a.username, p.author_id
from posts p
join authors a on a.id = p.author_id;


select * from authors
order by username;

select * from authors
order by username asc;


select * from authors
order by username desc;


-- select * from authors
-- order by username desc, first_name asc;



select * from authors
where length(username) = 4
order by username desc;


select * from authors
where
length(username) = 4
and
id > 2
order by username desc;



insert into authors (username)
values ('john');


insert into authors (username)
values ('sam');

select gen_random_uuid();



insert into authors (username)
values ('kate'),
	   ('ann');


insert into posts (title, author_id)
values ('Python lesson', 1),
       ('Postgres lesson', 3);


insert into posts (title, author_id)
values ('Python lesson', 1),
       ('Postgres lesson', 555);
