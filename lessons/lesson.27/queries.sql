SELECT 1;


select 1;

select version();

select uuidv7();

select now();


select 1 as one;
select 1 + 2 as "three";
select 1 + 2 as "1 + 2";
select 1 + 2 "1 + 2 =";


create table if not exists notes
(
    id         serial primary key not null,
    title      text               not null unique,
    note       text               not null default '',
    created_at timestamptz        not null default now()
);

drop table notes;

insert into notes (title, note)
values ('SQL Intro', 'My thoughts on the SQL intro.');


insert into notes (title, note)
values ('Python Intro', 'Some Python tricks'),
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

select 'user_' || idx || '@example.com'
     , 'User Name ' || idx
     , idx % 3 != 0
     , now() - (random() * interval '365 days')
from generate_series(1, 100000) as idx;



---
---
---
---


SELECT post.title
     , post.content
     , post.user_id
     , post.id
FROM post
ORDER BY post.title

--

SELECT post.title
     , post.content
     , post.user_id
     , post.id
     , user_1.username
     , user_1.email
     , user_1.full_name
     , user_1.id AS id_1
FROM post
         LEFT OUTER JOIN user AS user_1
                         ON user_1.id = post.user_id
ORDER BY post.title, post.id ASC;


---

SELECT user.username
     , user.email
     , user.full_name
     , user.id
FROM user
WHERE user.email IS NOT NULL
ORDER BY user.username;

--

SELECT post.user_id AS post_user_id
     , post.title   AS post_title
     , post.content AS post_content
     , post.id      AS post_id
FROM post
WHERE post.user_id IN (2, 1, 4);

--

SELECT post.title, post.content, post.user_id, post.id
FROM post
ORDER BY post.title, post.id ASC

SELECT user.username       AS user_username
     , user.email          AS user_email
     , user.full_name      AS user_full_name
     , user.id             AS user_id
     , anon_1.post_user_id AS anon_1_post_user_id
FROM (SELECT DISTINCT post.user_id AS post_user_id
      FROM post) AS anon_1
         JOIN user ON user.id = anon_1.post_user_id


--

SELECT user.username
     , user.email
     , user.full_name
     , user.id
     , post.id
     , post.title
FROM user
     JOIN post
         ON user.id = post.user_id
WHERE post.title LIKE '%-2'
ORDER BY user.username;

SELECT post.user_id AS post_user_id
     , post.title   AS post_title
     , post.content AS post_content
     , post.id      AS post_id
FROM post
WHERE post.user_id IN (3, 2);
