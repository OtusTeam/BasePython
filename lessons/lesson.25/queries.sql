SELECT 1;
select 2;
SELECT 1 + 2;

SELECT 1 + 2 as "1 + 2";

SELECT 1 as "one";
SELECT 2 two;

SELECT now();

SELECT gen_random_uuid();

CREATE TABLE authors
(
    id SERIAL PRIMARY KEY,
    username VARCHAR UNIQUE NOT NULL
);

ALTER TABLE authors
    ADD COLUMN email VARCHAR(250) UNIQUE;

--

SELECT nextval('authors_id_seq');

SELECT *
FROM authors;

SELECT *
FROM authors
ORDER BY id;

SELECT *
FROM authors
ORDER BY username;

SELECT *
FROM authors
ORDER BY id DESC;

SELECT id, username
FROM authors
ORDER BY id;

SELECT username, id
FROM authors
ORDER BY id;

INSERT INTO authors (username)
VALUES ('kate');

SELECT *
FROM authors
WHERE email IS NOT NULL;

INSERT INTO authors (username, email)
VALUES ('kyle', 'kyle@yahoo.ru'),
       ('clark', NULL);


UPDATE authors
SET email = username || '@example.com'
WHERE email IS NULL;
