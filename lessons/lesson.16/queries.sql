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
