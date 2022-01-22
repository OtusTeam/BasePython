
CREATE TABLE authors (
    id SERIAL PRIMARY KEY,
    username VARCHAR UNIQUE NOT NULL
);


ALTER TABLE authors
ADD COLUMN email VARCHAR;

ALTER TABLE authors
ADD CONSTRAINT authors_email_unique UNIQUE (email);


CREATE TABLE articles (
    id SERIAL PRIMARY KEY,
    title VARCHAR NOT NULL,
    body TEXT NOT NULL DEFAULT '',
    raw_data jsonb,
    author_id INT NOT NULL,

    CONSTRAINT fk_author
     FOREIGN KEY (author_id)
      REFERENCES authors(id)
);

-- QUERIES

-- authors

SELECT *
FROM authors;

SELECT id
FROM authors;

SELECT username
FROM authors;

SELECT id, username
FROM authors;

SELECT id, username
FROM authors
ORDER BY id;

SELECT id, username
FROM authors
ORDER BY username;


SELECT *
FROM authors
WHERE authors.email IS NOT NULL;


SELECT *
FROM authors
WHERE authors.email IS NULL;


SELECT *
FROM authors
WHERE authors.email ILIKE '%@example.com';

SELECT *
FROM authors
WHERE authors.email ILIKE '%@google.com';

SELECT *
FROM authors
WHERE authors.email ILIKE '%.ru';


SELECT *
FROM authors
ORDER BY id
LIMIT 5;


SELECT *
FROM authors
ORDER BY id
OFFSET 3
LIMIT 5;

SELECT *
FROM authors
ORDER BY id DESC
OFFSET 3
LIMIT 5;


INSERT INTO authors (username)
VALUES ('ann');

INSERT INTO authors (username, email)
VALUES ('kate', 'kate@example.com');


UPDATE authors
SET email = 'ann@google.com'
WHERE username = 'ann';

SELECT *
FROM authors
WHERE id > 3;

SELECT *
FROM authors
WHERE id < 3;

SELECT *
FROM authors
WHERE id = 10;

SELECT *
FROM authors
WHERE id = 20;

--

INSERT INTO articles
    (title, raw_data, author_id)
VALUES (
    'SQL Lesson',
    '{"spam": "eggs", "foo": "bar"}',
    10
    );


SELECT *
FROM articles;

SELECT *
FROM articles
WHERE author_id = 10;

SELECT *
FROM articles
WHERE author_id = 11;

SELECT *
FROM articles
WHERE author_id = 12;

SELECT ar.id, ar.title, ar.raw_data, a.username, a.email
FROM articles ar
JOIN authors a on a.id = ar.author_id;

SELECT ar.id,
       ar.title,
       ar.raw_data,
       a.username,
       a.email,
       ar.raw_data,
       a.username,
       a.email,
       ar.raw_data,
       a.username,
       a.email,
       ar.raw_data,
       a.username,
       a.email,
       a.username
FROM articles ar
         JOIN authors a on a.id = ar.author_id;


SELECT ar.id, ar.title, ar.raw_data, a.username, a.email
FROM articles ar
JOIN authors a on a.id = ar.author_id
WHERE a.username = 'ann';

SELECT ar.id, ar.title, ar.raw_data, a.username, a.email
FROM articles ar
JOIN authors a on a.id = ar.author_id
WHERE a.username = 'john';



SELECT DISTINCT author_id
FROM articles;

SELECT *
FROM authors a
WHERE id IN (
    SELECT DISTINCT author_id
    FROM articles
);


SELECT *
FROM articles
WHERE articles.raw_data ->> 'foo' = 'bar';


SELECT *
FROM articles
WHERE articles.raw_data ->> 'spam' = 'eggs';


SELECT *
FROM articles
WHERE articles.raw_data ? 'foo';


SELECT *
FROM articles
WHERE NOT (articles.raw_data ? 'foo');


SELECT *
FROM articles
WHERE (
    NOT (articles.raw_data ? 'foo')
    OR articles.raw_data IS NULL
);


SELECT id
     , title
     , raw_data
     , raw_data -> 'foo' AS foo_value
     , raw_data ->> 'foo' AS foo_value_2
     , raw_data ->> 'a' AS a_value_json
     , raw_data -> 'a' ->> 'b' AS a_b_value_json
     , raw_data -> 'a' -> 'b' ->> 'c' AS a_b_c_value_json
FROM articles;
