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
    username VARCHAR(32) UNIQUE NOT NULL,
    bio      VARCHAR(200)       NOT NULL DEFAULT '',
    email    VARCHAR(120) UNIQUE
);

CREATE TABLE publications
(
    id           INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    author_id    INTEGER      NOT NULL,
    title        VARCHAR(120) NOT NULL,
    body         TEXT         NOT NULL DEFAULT '',
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


--

SELECT users.username
     , users.full_name
     , users.email
     , users.created_at
     , users.id
FROM users
WHERE users.username = 'alice'


--


BEGIN;

-- INFO  [alembic.runtime.migration] Running upgrade b39bb783280d -> e770c0edaaa8, add col full_name to users
-- Running upgrade b39bb783280d -> e770c0edaaa8

ALTER TABLE users
    ADD COLUMN full_name VARCHAR(100) DEFAULT '' NOT NULL;

UPDATE alembic_version
SET version_num='e770c0edaaa8'
WHERE alembic_version.version_num = 'b39bb783280d';

-- INFO  [alembic.runtime.migration] Running upgrade e770c0edaaa8 -> f8a06c1f7697, add col body to articles
-- Running upgrade e770c0edaaa8 -> f8a06c1f7697

ALTER TABLE articles
    ADD COLUMN body TEXT DEFAULT '' NOT NULL;

UPDATE alembic_version
SET version_num='f8a06c1f7697'
WHERE alembic_version.version_num = 'e770c0edaaa8';

COMMIT;

---

SELECT sources.name
     , sources.url
     , sources.id
FROM sources
ORDER BY sources.id;

SELECT sources_1.id          AS sources_1_id
     , articles.title        AS articles_title
     , articles.body         AS articles_body
     , articles.published_at AS articles_published_at
     , articles.author_id    AS articles_author_id
     , articles.id           AS articles_id
FROM sources AS sources_1
         JOIN article_source_association_table AS article_source_association_table_1
              ON sources_1.id = article_source_association_table_1.source_id
         JOIN articles ON articles.id = article_source_association_table_1.article_id
WHERE sources_1.id IN (1, 2, 3, 4, 5)


ALTER TABLE article_source_association_table
    ADD COLUMN id INTEGER GENERATED ALWAYS AS IDENTITY;

