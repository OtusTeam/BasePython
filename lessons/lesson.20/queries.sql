SELECT 1;

SELECT 2;

SELECT 1 + 2;

SELECT 2 + 3, 5 * 4;

SELECT 1 as "one";

SELECT 1 as one;

SELECT 2 two;

SELECT 1 + 2 "one and two";

SELECT now();

SELECT gen_random_uuid();


CREATE TABLE authors
(
    id SERIAL PRIMARY KEY,
    username VARCHAR UNIQUE NOT NULL
);

ALTER TABLE authors
    ADD COLUMN email VARCHAR(250) UNIQUE;


CREATE TABLE posts
(
    id SERIAL PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    body TEXT NOT NULL DEFAULT '',
    author_id INTEGER NOT NULL,

    CONSTRAINT fk_author
        FOREIGN KEY (author_id)
            REFERENCES authors (id)
);

CREATE TABLE example_table (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    column1 TEXT,
    column2 INTEGER
);


--


SELECT id
FROM authors;

SELECT id, username
FROM authors;

SELECT *
FROM authors;

SELECT username, id
FROM authors;

SELECT id, username
FROM authors
-- ORDER BY id ASC;
ORDER BY id;

SELECT id, username
FROM authors
ORDER BY id DESC;

SELECT id, username
FROM authors
ORDER BY username;

INSERT INTO authors (username)
VALUES ('kate');

INSERT INTO authors (username, email)
    VALUES ('kyle', 'kyle@ya.ru'),
           ('andrew', NULL);


SELECT *
FROM authors
WHERE email IS NOT NULL;

SELECT *
FROM authors
WHERE username = 'bob';

SELECT *
FROM authors
WHERE username = 'qwerty';

UPDATE authors
SET email = 'admin@admin.com'
WHERE username = 'admin';


SELECT id, username, authors.email
FROM authors
ORDER BY id;


SELECT id
     , username
     , concat(username, '@domain.com')
     , length(username)
FROM authors
WHERE email IS NULL
ORDER BY length(username), username, id;


UPDATE authors
SET email = concat(username, '@ya.ru')
WHERE length(username) = 3 AND email IS NULL;

UPDATE authors
SET email = concat(username, '@vk.com')
WHERE length(username) = 4 AND email IS NULL;

SELECT *
FROM authors
WHERE email ilike '%@ya.ru'
ORDER BY id;

SELECT *
FROM authors
WHERE NOT (email ilike '%@vk.com')
ORDER BY id;

SELECT *
FROM authors
WHERE NOT (email ilike '%@vk.com') OR email IS NULL
ORDER BY id;


INSERT INTO posts (title, author_id)
VALUES
    ('PostgreSQL Lesson', 4),
    ('MariaDB Lesson', 9);


INSERT INTO posts (title, author_id)
VALUES
    ('Databases Lesson', 9);


SELECT id
     , title
     , author_id
FROM posts
ORDER BY id;

SELECT p.id
     , title
     , a.username
     , a.email
     , a.id
FROM posts p
JOIN authors a on a.id = p.author_id
ORDER BY p.id;

SELECT a.id
     , a.username
     , a.email
     , count(p.id) "posts count"
FROM authors a
JOIN posts p on a.id = p.author_id
GROUP BY a.id
ORDER BY a.id;

SELECT *
FROM authors a
JOIN posts p on a.id = p.author_id;

SELECT a.id
     , a.username
     , a.email
     , array_agg(p.title)
FROM authors a
JOIN posts p on a.id = p.author_id
GROUP BY a.id
ORDER BY a.id;

SELECT *
FROM posts
WHERE author_id IN (4, 9)
ORDER BY id;
