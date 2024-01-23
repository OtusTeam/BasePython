SELECT 1;
SELECT 2;
SELECT 1 + 2;

SELECT 1 as "one";
SELECT 2 "two";

SELECT 1 + 2 "1+2";

SELECT 1 "one", 2 "two", 1 + 2 "one plus two";
SELECT 1, 2, 1 + 2 "one plus two";

CREATE TABLE authors
(
    id SERIAL PRIMARY KEY,
    username VARCHAR UNIQUE NOT NULL
);

ALTER TABLE authors
ADD COLUMN email VARCHAR UNIQUE;

SELECT nextval('authors_id_seq');

CREATE TABLE posts
(
    id SERIAL PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    body TEXT NOT NULL DEFAULT '',
    author_id BIGINT NOT NULL,

    CONSTRAINT fk_author
        FOREIGN KEY (author_id)
            REFERENCES authors (id)
);

--

SELECT *
FROM authors;

SELECT *
FROM authors
-- ORDER BY id ASC;
ORDER BY id;

SELECT *
FROM authors
ORDER BY id DESC;

SELECT *
FROM authors
ORDER BY username;

SELECT *
FROM authors
ORDER BY username DESC;

SELECT id, username
FROM authors
ORDER BY username DESC;

SELECT username, id
FROM authors
ORDER BY username DESC;

SELECT id
FROM authors
ORDER BY username DESC;

SELECT id
FROM authors
ORDER BY username;

INSERT INTO authors (username)
VALUES ('kate');

INSERT INTO authors (username, email)
VALUES ('kyle', 'kyle@example.com'),
       ('bob', NULL);

--

INSERT INTO posts (title, author_id)
VALUES ('SQL Lesson', 11);

INSERT INTO posts (title, author_id)
VALUES ('Postgres Lesson', 4),
       ('Database Into', 12);


INSERT INTO posts (title, author_id)
VALUES ('MariaDB Lesson', 4);


SELECT id, title, author_id
FROM posts
WHERE author_id = 4;

SELECT p.id "post_id", p.title, a.username, a.email
FROM posts p
JOIN authors a on a.id = p.author_id;

SELECT p.id "post_id"
     , p.title
     , a.id
     , a.username
     , a.email
     , p.body
FROM posts p
JOIN authors a on a.id = p.author_id;


SELECT *
FROM authors
ORDER BY id;

SELECT *
FROM authors
WHERE authors.email IS NULL;

SELECT *
FROM authors
WHERE authors.email IS NOT NULL;


SELECT *
FROM authors
WHERE
    authors.email IS NULL
 AND
    length(authors.username) > 3;


UPDATE authors
SET email = 'bob@ya.ru'
WHERE username = 'bob';

UPDATE authors
SET email = concat(username, '@bk.ru')
WHERE
    email IS NULL AND length(username) > 3;


SELECT a.id, a.username, p.id, p.title
FROM authors a
JOIN posts p on a.id = p.author_id;


SELECT a.id, a.username, p.id, p.title
FROM authors a
INNEr JOIN posts p on a.id = p.author_id;

SELECT a.id, a.username, p.id, p.title
FROM authors a
LEFT JOIN posts p on a.id = p.author_id;



SELECT DISTINCT (a.id), a.username
FROM authors a
JOIN posts p on a.id = p.author_id
ORDER BY a.id;

SELECT a.id, a.username
FROM authors a
WHERE a.id IN (
    SELECT p.author_id
    FROM posts p
)
ORDER BY a.id;



SELECT p.id, p.title, p.author_id
FROM posts p
WHERE p.title ilike '%lesson%';

SELECT a.id, a.username
FROM authors a
WHERE a.id in (
    SELECT p.author_id
    FROM posts p
    WHERE p.title ilike '%lesson%'
);

SELECT count(a.id)
FROM authors a;

SELECT count(p.id)
FROM posts p;

SELECT count(*)
FROM posts p;


SELECT count(a.id)
     , length(a.username)
     , array_agg(a.id)
     , array_agg(a.username)
FROM authors a
GROUP BY length(a.username);


SELECT a.id
     , a.username
     , count(p.id) "posts count"
     , array_agg(p.title) "posts titles"
FROM authors a
LEFT OUTER JOIN posts p on a.id = p.author_id
GROUP BY a.id;
