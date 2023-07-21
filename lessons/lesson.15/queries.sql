-- selects

SELECT 1;

SELECT 1, 2;

SELECT 1, 2, 2 + 3;

SELECT 1 as "one";
SELECT 1 as "one", 2 as "two";

SELECT 1 "one";
SELECT 1 "one", 2 "two";
SELECT 1 "one", 2 "two", 2 + 3 "sum";


-- tables

-- create authors table
CREATE TABLE authors
(
    id SERIAL PRIMARY KEY,
    username VARCHAR UNIQUE NOT NULL
);

-- DROP TABLE authors;

ALTER TABLE authors
    ADD COLUMN email VARCHAR UNIQUE;

-- queries

-- query authors
SELECT id, username
FROM authors;

SELECT username, id
FROM authors;

SELECT username, id
FROM authors
WHERE username = 'sam';

SELECT username, id
FROM authors
WHERE id > 1;


-- create authors

INSERT INTO authors (username)
VALUES ('kate');

INSERT INTO authors (username)
VALUES ('jake'),
       ('nick'),
       ('bob');


SELECT id, username, email
FROM authors
ORDER BY id;

SELECT *
FROM authors
ORDER BY id;


INSERT INTO authors (username, email)
VALUES ('alice', 'alice@example.com'),
       ('mike', NULL),
       ('kyle', 'kyle@yahoo.com');


SELECT *
FROM authors
WHERE email IS NULL;

SELECT *
FROM authors
WHERE email IS NOT NULL;

SELECT *
FROM authors
WHERE email IS NOT NULL
ORDER BY id;


SELECT *
FROM authors
WHERE email LIKE '%@yahoo.com'
ORDER BY id;

SELECT *
FROM authors
WHERE NOT (email LIKE '%@yahoo.com')
ORDER BY id;

SELECT *
FROM authors
WHERE NOT (email LIKE '%@yahoo.com')
ORDER BY id;

SELECT *
FROM authors
WHERE NOT (email LIKE '%@yahoo.com') OR email IS NULL
ORDER BY id;


UPDATE authors
SET email = 'mike@example.com'
WHERE username = 'mike';


UPDATE authors
SET email = concat(username, '@ya.ru')
WHERE email is NULL;
