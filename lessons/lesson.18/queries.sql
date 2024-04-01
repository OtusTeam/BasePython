SELECT 1;
SELECT 1 + 2;


SELECT 1 as "one";
SELECT 1 + 2 "one and two";

SELECT 1 "one", 2 as "two", 1 + 2 "1+2";


SELECT gen_random_uuid();

SELECT 'abc'::VARCHAR(3);
SELECT 'щяь'::VARCHAR(3);


CREATE TABLE authors
(
    id SERIAL PRIMARY KEY,
    username VARCHAR UNIQUE NOT NULL
);

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

ALTER TABLE authors
ADD COLUMN email VARCHAR UNIQUE;

--

SELECT id
FROM authors;

SELECT id, username
FROM authors;

SELECT *
FROM authors;

SELECT username, id
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

SELECT *
FROM authors
ORDER BY username;

SELECT *
FROM authors
ORDER BY username DESC;

-- ascending
-- descending

INSERT INTO authors (username)
VALUES ('kate');


INSERT INTO authors (username)
VALUES ('bob'),
        ('alice');

INSERT INTO authors (username, email)
VALUES ('kyle', 'kyle@example.com'),
       ('andrew', NULL);


UPDATE authors
SET email = 'admin@example.com'
WHERE username = 'admin';

SELECT *
FROM authors
WHERE email IS NULL;

SELECT *
FROM authors
WHERE email IS NOT NULL;

UPDATE authors
SET email = NULL
WHERE email = '';

SELECT id, username, length(username)
FROM authors
ORDER BY length(username), username;


SELECT id, username, concat(username, '@ya.ru')
FROM authors;


UPDATE authors
SET email = concat(username, '@ya.ru')
WHERE email IS NULL and length(username) > 4;

UPDATE authors
SET email = concat(username, '@bk.ru')
WHERE email IS NULL;

SELECT *
FROM authors
WHERE email ilike '%@bk.%'
ORDER BY id;

SELECT *
FROM authors
WHERE email ilike '%@bk.ru'
ORDER BY id;


--

SELECT *
FROM posts;


INSERT INTO posts (title, author_id)
VALUES
    ('SQL Lesson', 4);


INSERT INTO posts (title, author_id)
VALUES
    ('Postgres Lesson', 3),
    ('MariaDB Lesson', 5);


INSERT INTO posts (title, author_id)
VALUES
    ('Databases Lesson', 5);



SELECT id, title, author_id
FROM posts;

SELECT p.id, p.title, a.username
FROM posts p
JOIN authors a
    ON p.author_id = a.id;


SELECT a.id, a.username, count(p.id) "posts-count"
FROM authors a
JOIN posts p on a.id = p.author_id
GROUP BY a.id
ORDER BY a.id;


SELECT a.id, a.username, count(p.id) "posts-count"
FROM authors a
LEFT JOIN posts p on a.id = p.author_id
GROUP BY a.id
ORDER BY a.id;

SELECT a.id, a.username, p.title
FROM authors a
LEFT JOIN posts p on a.id = p.author_id
ORDER BY a.id;
