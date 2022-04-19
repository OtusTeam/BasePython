-- SQL
-- Structured Query Language

SELECT 1;

SELECT 1 + 2;

SELECT 1 + 2 AS "one plus two";


-- Create table Authors
CREATE TABLE authors (
    id SERIAL PRIMARY KEY,
    username VARCHAR UNIQUE NOT NULL
);

ALTER TABLE authors
ADD COLUMN email VARCHAR;


CREATE TABLE articles (
    id SERIAL PRIMARY KEY,
    title VARCHAR NOT NULL,
    body TEXT NOT NULL DEFAULT '',
    raw_data JSONB,
    author_id INT NOT NULL,

    CONSTRAINT fk_author
      FOREIGN KEY (author_id)
        REFERENCES authors(id)
);


-- queries
-- authors

SELECT *
FROM authors;

SELECT id
FROM authors;

SELECT username
FROM authors;

SELECT id, username
FROM authors;

SELECT username, id
FROM authors;


SELECT id, username
FROM authors
ORDER BY username;


SELECT id, username
FROM authors
-- ORDER BY username ASC ;
ORDER BY username DESC;

INSERT INTO
    authors (username)
    VALUES
           ('clark'),
--            ('jack'),
           ('jack'),
           ('ann');


INSERT INTO
    authors (username, email)
    VALUES ('kate', 'kate@example.com');


UPDATE authors
SET email = 'john@example.com'
WHERE username = 'john';


UPDATE authors
SET email = 'clark@google.com'
WHERE username = 'clark';

UPDATE authors
SET email = 'ann@google.com'
WHERE username = 'ann';


--

SELECT *
FROM authors
WHERE email IS NULL;

-- SELECT *
-- FROM authors;

SELECT *
FROM authors
WHERE email IS NOT NULL;

SELECT *
FROM authors
WHERE email IS NOT NULL
ORDER BY id;


SELECT *
FROM authors
WHERE email ILIKE '%@google.com'
ORDER BY id;

SELECT *
FROM authors
WHERE NOT (email ILIKE '%@google.com')
ORDER BY id;

SELECT *
FROM authors
WHERE NOT (email ILIKE '%@google.com') OR email IS NULL
ORDER BY id;

--  LIMIT / OFFSET

SELECT *
FROM authors
ORDER BY id;


SELECT *
FROM authors
ORDER BY id
LIMIT 5;

SELECT *
FROM authors
ORDER BY id
LIMIT 10;

SELECT *
FROM authors
ORDER BY id
LIMIT 3
OFFSET 2;


SELECT *
FROM authors
ORDER BY id
LIMIT 3
OFFSET 5;

SELECT *
FROM authors
ORDER BY id DESC
LIMIT 3
OFFSET 5;


-- Fetch articles

SELECT *
FROM articles;

SELECT ar.id, ar.title
FROM articles ar;

SELECT ar.id, ar.title, a.username, a.email
-- FROM articles AS ar
FROM articles ar
-- JOIN authors a on a.id = ar.author_id;
-- LEFT JOIN authors AS a on a.id = ar.author_id;
LEFT JOIN authors a on a.id = ar.author_id;


INSERT INTO articles
    (title, raw_data, author_id)
    VALUES (
            'SQL JSONB',
            '{"spam": "eggs", "foo": "bar"}',
            7
           );

SELECT *
FROM articles a
WHERE a.raw_data ->> 'spam' = 'eggs';

SELECT *
FROM articles a
WHERE a.raw_data ->> 'foo' = 'bar';

SELECT *
FROM articles a
WHERE a.raw_data ? 'foo';

SELECT a.id
     , a.title
     , a.raw_data ->> 'spam' AS "spam value"
     , a.raw_data ->> 'foo' AS "foo value"
FROM articles a;
