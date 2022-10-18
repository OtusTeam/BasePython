SELECT 1;

SELECT 1 + 2;

SELECT 'hello world';

SELECT 1 AS num;
SELECT 1 + 2 "nums sum";

--

SELECT *
FROM pg_config;

SELECT setting
FROM pg_config
WHERE name = 'VERSION';

--
CREATE SEQUENCE my_first_seq;

SELECT nextval('my_first_seq');


--

-- CREATE TABLE authors
-- (
--     id SERIAL PRIMARY KEY
-- );

DROP TABLE authors;


CREATE TABLE authors
(
    id       SERIAL PRIMARY KEY,
    username VARCHAR UNIQUE NOT NULL
);

ALTER TABLE authors
    ADD COLUMN email varchar unique;


CREATE TABLE posts
(
    id         SERIAL PRIMARY KEY,
    title      VARCHAR(100) NOT NULL,
    body       TEXT         NOT NULL DEFAULT '',
    extra_data JSONB,
    author_id  INTEGER      NOT NULL,

    CONSTRAINT fk_author
        FOREIGN KEY (author_id)
            REFERENCES authors (id)

);


--

INSERT INTO authors (username)
VALUES ('sam');

SELECT *
FROM authors;


INSERT INTO authors (username)
VALUES ('john'),
       ('bob'),
       ('alice'),
       ('kate'),
       ('nick');

INSERT INTO authors (id, username)
VALUES (DEFAULT, 'george'),
       (DEFAULT, 'steeve');


SELECT *
FROM authors
WHERE authors.username = 'bob';



SELECT *
FROM authors a
WHERE a.username = 'bob';

SELECT *
FROM authors a
WHERE a.username <> 'bob';


SELECT *
FROM authors a
WHERE a.username = 'bob'
   OR a.username = 'sam';


SELECT *
FROM authors a
WHERE a.username like 'a%';


SELECT *
FROM authors a
WHERE a.username like '%a%';

SELECT *
FROM authors a
WHERE a.username like '%t%';

SELECT *
FROM authors a
WHERE a.username ilike '%T%';

INSERT INTO authors (username)
VALUES ('Tom');


-- i = case insensitive
SELECT *
FROM authors a
WHERE a.username ilike '%t%';

--
SELECT *
FROM authors
ORDER BY id;

SELECT *
FROM authors
ORDER BY username;

-- ASC - ascending
-- DESC - descending
SELECT *
FROM authors
ORDER BY username DESC;


UPDATE authors
SET email = 'sam@example.com'
WHERE username = 'sam';

SELECT now();
SELECT CAST(now() AS date);

--
SELECT *
FROM authors
ORDER BY id
LIMIT 3
;

SELECT *
FROM authors
ORDER BY id
OFFSET 5
;

SELECT *
FROM authors
ORDER BY id
OFFSET 5 LIMIT 3
;

-- keyset == offset by key (id)
SELECT *
FROM authors
WHERE id > 5
ORDER BY id
LIMIT 3
;

-- posts

INSERT INTO posts (title, extra_data, author_id)
VALUES ('SQL Lesson',
        '{}',
        2),
       ('Postgres Tutorial',
        '{
          "foo": "bar",
          "spam": "eggs"
        }',
        4),
       ('Pycharm News',
        '{
          "foo": "baz",
          "fizz": "buzz"
        }',
        4)
;

SELECT p.id, p.title, p.extra_data
FROM posts p;

SELECT p.id
     , p.title
     , p.extra_data
     , p.body
FROM posts p;

SELECT p.id
     , p.title
     , p.extra_data
     , p.extra_data -> 'foo' foo_json_str
     , p.extra_data ->> 'foo' foo_str
     , p.extra_data ->> 'spam' spam_str
     , p.extra_data ? 'foo' foo_present
     , p.extra_data ->> 'foo' = 'bar' foo_str_eq_bar
FROM posts p;

SELECT p.id
     , p.title
     , p.extra_data
FROM posts p
WHERE p.extra_data ->> 'foo' = 'bar';
