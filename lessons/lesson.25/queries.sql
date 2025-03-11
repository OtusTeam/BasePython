SELECT 1;
SELECT 2;

SELECT 1 + 2;

SELECT 1 + 2 as "sum";
SELECT 1 + 2 as three;

SELECT 2 * 2, 3 * 3;

SELECT 2 * 2 four, 3 * 3 nine;

SELECT CURRENT_TIMESTAMP;

--

PRAGMA foreign_keys = ON;

--


CREATE TABLE authors
(
    id       INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    username VARCHAR(32) UNIQUE                NOT NULL,
    bio      VARCHAR(200)                      NOT NULL DEFAULT '',
    email    VARCHAR(120) UNIQUE
);

CREATE TABLE publications
(
    id           INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    author_id    INTEGER                           NOT NULL,
    title        VARCHAR(120)                      NOT NULL,
    body         TEXT                              NOT NULL DEFAULT '',
    published_at DATETIME,
    FOREIGN KEY (author_id)
        REFERENCES authors (id)
        ON DELETE CASCADE
);

--


SELECT *
FROM authors;

INSERT INTO authors (username)
VALUES ('bob');


INSERT INTO authors (username, bio, email)
VALUES ('alice', 'Nice day', 'alice@example.com'),
       ('john', '', NULL);


ALTER TABLE authors
    ADD COLUMN full_name VARCHAR(100) NOT NULL DEFAULT '';


SELECT id, username, email
FROM authors;

SELECT id, username, email
FROM authors
ORDER BY username;

SELECT id, username, email
FROM authors
WHERE email IS NOT NULL;

SELECT id, username, email
FROM authors
WHERE email IS NULL;


SELECT id, username, email
FROM authors
ORDER BY username
LIMIT 3 OFFSET 2;


SELECT id, username, email
FROM authors
WHERE username = 'bob';


SELECT id, username, email
FROM authors
WHERE username = 'jack';


--

-- Insert publication by Author 1
INSERT INTO publications (author_id, title, body, published_at)
VALUES (2, 'The Future of Technology',
        'In this article, we explore the advancements in technology that are shaping our future. From AI to quantum computing, the possibilities are endless.',
        '2023-10-01 10:00:00');

-- Insert publication by Author 2
INSERT INTO publications (author_id, title, body, published_at)
VALUES (2, 'Healthy Living: Tips and Tricks',
        'This publication provides practical tips for maintaining a healthy lifestyle, including diet, exercise, and mental well-being.',
        NULL);

-- Insert publication by Author 3
INSERT INTO publications (author_id, title, body, published_at)
VALUES (3, 'Traveling the World: A Guide',
        'A comprehensive guide to traveling the world, covering the best destinations, travel tips, and cultural experiences.',
        '2023-10-03 09:15:00');


-- fails!!
INSERT INTO publications(author_id, title)
VALUES (0, 'abc');

--
SELECT p.id, p.title
FROM publications p;

SELECT p.id, p.title, a.id, a.username, a.email
FROM publications p
    JOIN authors a ON a.id = p.author_id
;

SELECT a.id, a.username, p.title
FROM authors a
    JOIN publications p ON a.id = p.author_id;

SELECT a.id, a.username, p.title
FROM authors a
    LEFT JOIN publications p ON a.id = p.author_id;


SELECT p.id, p.title, a.id, a.username, a.email
FROM publications p
    JOIN authors a ON a.id = p.author_id
WHERE a.email IS NOT NULL;


SELECT p.id, p.title, a.id, a.username, a.email
FROM publications p
    JOIN authors a ON a.id = p.author_id
WHERE p.published_at < CURRENT_TIMESTAMP;

--
