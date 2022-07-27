-- SQL
-- Structured Query Language

SELECT 1;
SELECT 7;
SELECT 1 + 2;

SELECT 2 + 3 AS result;

-- create table authors
CREATE TABLE authors
(
    id       SERIAL PRIMARY KEY,
    username VARCHAR UNIQUE NOT NULL
);

ALTER TABLE authors
    ADD COLUMN email VARCHAR UNIQUE;


CREATE TABLE posts
(
    id        SERIAL PRIMARY KEY,
    title     VARCHAR(100) NOT NULL,
    body      TEXT         NOT NULL DEFAULT '',
    raw_data  jsonb,
    author_id INT          NOT NULL,

    CONSTRAINT fk_author
        FOREIGN KEY (author_id)
            REFERENCES authors (id)
);


SELECT *
FROM authors;

INSERT INTO authors (username)
VALUES ('sam');


INSERT INTO authors (username)
VALUES ('kate'),
       ('nick'),
       ('bob'),
       ('alice');


INSERT INTO authors (id, username)
VALUES (DEFAULT, 'ann'),
       (DEFAULT, 'george');


SELECT *
FROM authors
WHERE username = 'bob';


SELECT *
FROM authors
WHERE username like 'a%';

SELECT *
FROM authors
WHERE username like '%a%';

SELECT *
FROM authors
WHERE username like '%a%e';

SELECT *
FROM authors
ORDER BY username;

SELECT *
FROM authors
ORDER BY id;

SELECT *
FROM authors
ORDER BY id DESC;

SELECT *
FROM authors
ORDER BY id ASC;

SELECT *
FROM authors
WHERE email IS NOT NULL;

SELECT *
FROM authors
WHERE email like '%@example.com';

UPDATE authors
SET email = 'kate@gmail.com'
WHERE username = 'kate';


SELECT id, username, email
FROM authors
-- ORDER BY id DESC
ORDER BY username
LIMIT 5 OFFSET 3;

-- posts

INSERT INTO posts (title, raw_data, author_id)
VALUES ('SQL Lesson',
        '{}',
        9),
       (
        'Postgres Tutorial',
        '{"foo": "bar", "spam": "eggs"}',
        7
       ),
       (
        'Pycharm Update',
        '{"foo": "baz", "fizz": "buzz"}',
        7
       );


SELECT *
FROM posts;

SELECT p.id, p.title, a.username, a.email
FROM posts p
JOIN authors a on a.id = p.author_id;

SELECT a.id, a.email, a.username, p.title
FROM authors a
JOIN posts p on a.id = p.author_id;

SELECT a.id, a.email, a.username, p.title
FROM authors a
LEFT JOIN posts p on a.id = p.author_id;


SELECT p.id
     , p.title
     , p.raw_data
     , p.raw_data -> 'foo' as foo_value
     , p.raw_data -> 'spam' spam_value
     , p.raw_data ? 'foo' foo_key_exists
FROM posts p;


SELECT p.id
     , p.title
     , p.raw_data
     , p.raw_data -> 'foo'
     , p.raw_data ->> 'foo'
FROM posts p
WHERE p.raw_data ->> 'foo' = 'bar';

SELECT p.id
     , p.title
     , p.raw_data
     , p.raw_data ? 'foo'
     , p.raw_data -> 'foo'
     , p.raw_data ->> 'foo'
FROM posts p
WHERE p.raw_data ? 'foo';

-- 34322
-- totally randomly generated
