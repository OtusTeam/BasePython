SELECT 1;
SELECT 1 + 2;
SELECT 1, 2, 1 + 2;

SELECT 1 as "one";
SELECT 1, 'one';
SELECT 1 as "one", 'one' as "one str";
SELECT 1 + 2 as "1 + 2";
SELECT 1, 2, 1 + 2;

SELECT 1 "one";
SELECT 1 "one_num", 'one' "one";

--
--

CREATE TABLE authors
(
    id SERIAL PRIMARY KEY,
    username VARCHAR UNIQUE NOT NULL
);


ALTER TABLE authors
ADD COLUMN email VARCHAR UNIQUE;

CREATE TABLE posts
(
    id SERIAL PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    body TEXT NOT NULL DEFAULT '',
    author_id INT NOT NULL,

    CONSTRAINT fk_author
        FOREIGN KEY (author_id)
            REFERENCES authors (id)
);

--

SELECT *
FROM authors;


SELECT *
FROM authors
ORDER BY id DESC;


SELECT id, username
FROM authors;


SELECT username, id
FROM authors;


SELECT username
FROM authors;


SELECT username
FROM authors
ORDER BY username;


INSERT INTO authors (username)
VALUES ('kate');

INSERT INTO authors (username, email)
VALUES
    ('kyle', 'kyle@example.com'),
    ('bob', 'bob@example.com');


SELECT id, email, username
FROM authors
WHERE length(username) = 4;

SELECT id, email, username
FROM authors
WHERE username = 'admin';

SELECT id, email, username
FROM authors
WHERE username = 'ad';


SELECT id, email, username
FROM authors
WHERE
    length(username) = 4
    AND email IS NULL
;


UPDATE authors
SET username = 'sam'
WHERE username = 'samuel';


UPDATE authors
SET email = concat(username, '@ya.ru')
WHERE
    length(username) = 4
    AND email IS NULL
;

SELECT id, username, email
FROM authors
-- WHERE id > 3
WHERE username > 'john'
-- ORDER BY id
ORDER BY username
LIMIT 2;
-- OFFSET 2;

SELECT *
FROM authors
WHERE email LIKE '%@ya.ru';

SELECT *
FROM authors
WHERE email NOT LIKE '%@ya.ru';

SELECT *
FROM authors
WHERE email NOT LIKE '%@ya.ru' OR email IS NULL;


INSERT INTO posts (title, author_id)
VALUES ('SQL Lesson', 3);

INSERT INTO posts (title, author_id)
VALUES ('PG Lesson', 3),
        ('MariaDB Lesson', 4)
       ;

SELECT *
FROM posts;

SELECT *
FROM posts
WHERE author_id = 4;

SELECT *
FROM posts p
JOIN authors a on a.id = p.author_id;

SELECT *
FROM posts p
JOIN authors a on a.id = p.author_id
WHERE a.username = 'john';

SELECT p.id, p.title
FROM posts p
JOIN authors a on a.id = p.author_id
WHERE a.username = 'john';


SELECT a.id, a.username, p.id, p.title
FROM authors a
JOIN posts p on a.id = p.author_id
WHERE p.title ilike '%pg%';


SELECT a.id, a.username, p.id, p.title
FROM authors a
JOIN posts p on a.id = p.author_id
WHERE p.title ilike '%pg%' OR p.title ilike '%maria%';

SELECT a.id, a.username, p.id, p.title
FROM authors a
LEFT OUTER JOIN posts p on a.id = p.author_id;

SELECT *
FROM authors;

SELECT id, username, length(username) username_len
FROM authors;

SELECT authors.email, count(id)
FROM authors
GROUP BY email;
