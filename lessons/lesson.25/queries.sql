SELECT 1;

SELECT 1 + 2;

SELECT 1 as "one";
SELECT 2 as two;
SELECT 3 three;

SELECT 3 + 4 sum;


SELECT now();


---
-- users

CREATE TABLE users
(
    id BIGSERIAL PRIMARY KEY,
    username VARCHAR(32) UNIQUE NOT NULL,
    email VARCHAR(150) UNIQUE,
    full_name VARCHAR NOT NULL DEFAULT ''
);


SELECT *
FROM users;

UPDATE users
SET email = 'bob@example.com'
WHERE username = 'bob';

SELECT *
FROM users
ORDER BY id;

SELECT *
FROM users
ORDER BY username;

SELECT *
FROM users
ORDER BY email, username;

INSERT INTO users (username, email)
VALUES ('jack', 'a.jack@abc.com');

INSERT INTO users (username, email)
VALUES ('kate', 'kate@example.com'),
       ('sam', NULL);



SELECT id, username, length(username)
FROM users
ORDER BY length(username) DESC, username;
