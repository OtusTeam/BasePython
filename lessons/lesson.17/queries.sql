SELECT 1;
SELECT now();

CREATE TABLE authors
(
    id       SERIAL PRIMARY KEY,
    username VARCHAR UNIQUE NOT NULL,
    email    VARCHAR UNIQUE
);

CREATE TABLE posts
(
    id        SERIAL PRIMARY KEY,
    title     VARCHAR(100) NOT NULL,
    body      TEXT         NOT NULL DEFAULT '',
    raw_meta  jsonb        NOT NULL DEFAULT '{}',

    author_id INTEGER      NOT NULL
        CONSTRAINT posts_authors_fk
            REFERENCES authors (id)
);

DROP TABLE posts;

--
--

INSERT INTO authors (username, email)
VALUES ('john', 'john@example.com'),
       ('kate', 'kate@yahoo.com'),
       ('nick', NULL);


INSERT INTO posts (title, author_id)
VALUES ('Django Lesson', 1),
       ('Flask Lesson', 1),
       ('SQL Lesson', 2);


UPDATE posts
SET raw_meta = '{
  "spam": "eggs",
  "foo": "bar",
  "data": {
    "fizz": "buzz"
  },
  "movies": [
    "A",
    "B",
    "C"
  ]
}'
WHERE title = 'Django Lesson';



UPDATE posts
SET raw_meta = '{
  "foo": "baz"
}'
WHERE title = 'Flask Lesson';

--

SELECT *
FROM posts
ORDER BY id;

SELECT id, title, raw_meta
FROM posts
ORDER BY id;

SELECT id, title, raw_meta
FROM posts
WHERE raw_meta ? 'foo'
ORDER BY id;

SELECT id, title, raw_meta
FROM posts
WHERE raw_meta ->> 'foo' = 'bar'
-- AND raw_meta -> 'foo' = '"bar"'::jsonb
ORDER BY id;

SELECT id
     , title
     , raw_meta ->> 'foo'         as "text"
     , raw_meta -> 'foo'          as "json"
     , raw_meta -> 'movies'       as "movies json array"
     , raw_meta -> 'movies' -> 0  as "first movie json str"
     , raw_meta -> 'movies' ->> 0 as "first movie text"
     , raw_meta
     , 'bar'                      as "text bar"
     , '"bar"'::jsonb             as "json bar"
FROM posts
ORDER BY id;


-- sqla queries

INSERT INTO users (username, email, is_staff, created_at)
VALUES ('john', NULL, FALSE, '...')
RETURNING users.id;

SELECT users.id         AS users_id,
       users.username   AS users_username,
       users.email      AS users_email,
       users.is_staff   AS users_is_staff,
       users.created_at AS users_created_at
FROM users
WHERE users.id = 1;

