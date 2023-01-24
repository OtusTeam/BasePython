SELECT 1;

SELECT 1 + 2;

SELECT 'hello world!';

SELECT 1 AS "num";
SELECT 1 + 2 AS num_sum;

SELECT 1, 2;

SELECT 1 + 2 AS sum12, 2 + 3 AS sum23;
SELECT 1 + 2 sum12, 2 + 3 sum23;


SELECT *
FROM pg_config;

SELECT setting
FROM pg_config;

SELECT setting, name
FROM pg_config;

SELECT setting, name
FROM pg_config
WHERE name = 'VERSION';


CREATE TABLE authos
(
    id SERIAL PRIMARY KEY
);

DROP TABLE authos;


CREATE TABLE authors
(
    id       SERIAL PRIMARY KEY,
    username VARCHAR UNIQUE NOT NULL
);

ALTER TABLE authors
    ADD COLUMN email VARCHAR UNIQUE;

ALTER TABLE authors
    ADD COLUMN qwerty VARCHAR NOT NULL DEFAULT '';

ALTER TABLE authors
    DROP COLUMN qwerty;

CREATE TABLE posts
(
    id         SERIAL PRIMARY KEY,
    title      VARCHAR(100) NOT NULL,
    body       TEXT         NOT NULL DEFAULT '',
    extra_data JSONB,
    quotes     varchar[],

    author_id  INTEGER      NOT NULL,

    CONSTRAINT fk_author
        FOREIGN KEY (author_id)
            REFERENCES authors (id)
);


SELECT *
FROM authors;


SELECT *
FROM authors
ORDER BY id;

SELECT *
FROM authors
ORDER BY id ASC;

SELECT *
FROM authors
ORDER BY id DESC;

SELECT username
FROM authors;

SELECT authors.email
FROM authors;

SELECT authors.email
FROM authors
WHERE authors.email IS NOT NULL;

SELECT username
FROM authors
WHERE email IS NOT NULL;

INSERT INTO authors (username, email)
VALUES ('george', 'george@me.com');

INSERT INTO authors (username, email)
VALUES ('jim', NULL),
       ('kate', 'kate@me.com');

SELECT *
FROM authors
WHERE username = 'admin';
-- WHERE username IS NOT NULL;

SELECT *
FROM authors
WHERE email like '%@me.com';


SELECT *
FROM authors
WHERE username <> 'admin';

SELECT now();
SELECT now() + interval '3 hours';

SELECT now()::date;
SELECT now()::time;
SELECT date_part('hour', now());
SELECT date_part('month', now());
SELECT date_part('year', now());



SELECT *
FROM authors
-- ORDER BY id DESC
ORDER BY username
LIMIT 5
OFFSET 6
;


EXPLAIN ANALYSE
SELECT *
FROM authors
ORDER BY id
LIMIT 3
OFFSET 5
;

EXPLAIN ANALYSE
SELECT *
FROM authors
WHERE id > 5
ORDER BY id
-- ORDER BY username
LIMIT 3
;

EXPLAIN ANALYSE
SELECT *
FROM authors
WHERE username > 'john'
ORDER BY username
LIMIT 3
;

SELECT 'a' > 'b';
SELECT 'a' = 'b';
SELECT 'a' < 'b';
SELECT 'a' = 'a';
SELECT 'a' < 'aa';
SELECT 'bob' < 'bob1';


-- POSTS


INSERT INTO posts (title, extra_data, quotes, author_id)
VALUES ('SQL Lesson',
        '{}',
        ARRAY ['to be..', 'qwerty'],
        2);


INSERT INTO posts (title, extra_data, author_id)
VALUES ('PG Lesson',
        '{
          "key": "value",
          "spam": "eggs"
        }',
        3),
       ('MYSQL Lesson',
        '{
          "fizz": "buzz",
          "spam": "eggs"
        }',
        4)
;


SELECT *
FROM posts;


--
create table authors
(
    id       serial
        primary key,
    username varchar not null
        unique,
    email    varchar
        unique
);

alter table authors
    owner to otus;

create table posts
(
    id         serial
        primary key,
    title      varchar(100)          not null,
    body       text default ''::text not null,
    extra_data jsonb,
    quotes     character varying[],
    author_id  integer               not null
        constraint fk_author
            references authors
);

alter table posts
    owner to otus;


SELECT *
FROM posts;

SELECT *
FROM posts
WHERE extra_data IS NULL;

SELECT *
FROM posts
WHERE extra_data = 'null';

SELECT p.id
     , p.title
     , p.extra_data
     , a.username
     , a.email
     , p.extra_data -> 'foo' foo_value_json
     , p.extra_data ->> 'foo' foo_value
     , p.extra_data -> 'foo' -> 'abc' foo_abc_value_json
     , p.extra_data -> 'foo' ->> 'abc' foo_abc_value
     , p.extra_data -> 'spam' spam_value_json
     , p.extra_data ->> 'spam' spam_value
     , p.extra_data ? 'spam' spam_present
FROM posts p
JOIN authors a on a.id = p.author_id;
