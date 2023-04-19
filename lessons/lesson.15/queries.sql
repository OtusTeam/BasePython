SELECT 1;

SELECT 1, 2;

SELECT 1, 2, 2 + 3;

SELECT 1 as "one";
SELECT 1 as "one", 2 as "two";
SELECT 1 "one", 2 "two", 1 + 2 "sum";


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

-- SELECT nextval('authors_id_seq');

-- SELECT *
-- SELECT username, id
SELECT id, username
FROM authors;


SELECT id, username
FROM authors
WHERE username = 'sam';

SELECT id, username
FROM authors
WHERE id < 3;


INSERT INTO authors (username)
VALUES ('kate');


INSERT INTO authors (username)
VALUES ('jake'),
       ('nick'),
       ('bob'),
       ('kile');

INSERT INTO authors (username)
VALUES ('alice'),
       ('glen'),
       ('mike'),
       ('pam');

UPDATE authors
SET username = 'kyle'
-- WHERE id = 9
WHERE username = 'kile';


SELECT id, username
FROM authors
ORDER BY id;

SELECT id, username
FROM authors
ORDER BY username;


UPDATE authors
SET email = 'kyle@google.com'
-- WHERE id = 9
WHERE username = 'kyle';


-- UPDATE

SELECT *
FROM authors
WHERE username LIKE '%a%';

UPDATE authors
SET email = concat(username, '@yahoo.com')
WHERE username LIKE '%a%';


SELECT *
FROM authors
WHERE email IS NOT NULL;

SELECT *
FROM authors
WHERE email IS NULL;

SELECT *
FROM authors
WHERE email like '%@yahoo.com';

SELECT *
FROM authors
WHERE NOT (email like '%@yahoo.com');

SELECT *
FROM authors
WHERE NOT (email like '%@yahoo.com')
   OR email IS NULL;


SELECT id, username, email
FROM authors
-- ORDER BY username
ORDER BY id
LIMIT 5 OFFSET 10;


-- posts

INSERT INTO posts (title, raw_data, author_id)
VALUES ('SQL Lesson',
        '{}',
        9),
       ('Postgres Tutorial',
        '{
          "foo": "bar",
          "spam": "eggs"
        }',
        7),
       ('PyCharm Update',
        '{
          "foo": "baz",
          "fizz": "buzz"
        }',
        5)
;


INSERT INTO posts (title, author_id)
VALUES ('Nullable fields', 13);


SELECT id, title, raw_data, author_id
FROM posts;

SELECT p.id, title, raw_data, author_id, a.username, a.email
FROM posts p
         JOIN authors a on a.id = p.author_id;

SELECT p.id
     , title
     , raw_data
--      , author_id
     , a.username
     , a.email
FROM posts p
         JOIN authors a on a.id = p.author_id;



SELECT p.id
     , title
     , raw_data
--      , author_id
     , a.username
     , a.email
FROM posts p
         JOIN authors a on a.id = p.author_id
-- WHERE email IS NOT NULL
WHERE email ilike '%@yahoo.com'
-- WHERE lower(email) like lower('%yahoo.com');
;


INSERT INTO posts (title, raw_data, author_id)
VALUES ('Nested objects', '{
  "foo": {
    "ids": [
      1,
      2,
      3
    ]
  }
}', 7);


-- EXPLAIN ANALYSE
SELECT p.id
     , title
     , raw_data
     , raw_data ? 'foo' as "foo present"
     , raw_data -> 'foo'   "foo value"
     , raw_data ->> 'foo'   "foo string value"
     , raw_data -> 'foo' -> 'ids' "foo -> ids"
--      , author_id
FROM posts p
-- WHERE raw_data ? 'foo'
-- WHERE raw_data -> 'foo' = '"bar"'::jsonb
WHERE raw_data ->> 'foo' = 'bar'
;

-- insensitive -- ilike
-- case sensitive -- like
