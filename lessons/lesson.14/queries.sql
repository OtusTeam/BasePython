CREATE TABLE authors (
    id SERIAL PRIMARY KEY,
    nickname VARCHAR UNIQUE NOT NULL
);

CREATE TABLE articles (
    id SERIAL PRIMARY KEY,
    title VARCHAR NOT NULL,
    body TEXT NOT NULL,
    raw_data jsonb,
    author_id INT NOT NULL,

  CONSTRAINT fk_author
    FOREIGN KEY (author_id)
      REFERENCES authors(id)
);

-- QUERIES

SELECT *
FROM authors;

SELECT id, nickname
FROM authors;

SELECT id, username, email
FROM users;


SELECT id, username, email
FROM users
WHERE username IS NULL;


SELECT id, username, email
FROM users
WHERE username IS NOT NULL;


SELECT id, username, email
FROM users
WHERE username LIKE 'jo%';


SELECT id, username, email
FROM users
WHERE users.email LIKE '%@example.com'
ORDER BY id;

SELECT id, username, email
FROM users
WHERE username = 'sam';

SELECT id, username, email
FROM users
WHERE users.email LIKE '%@example.com'
ORDER BY id DESC
LIMIT 2
;


INSERT INTO users (username, email)
VALUES ('nick', 'nick@gmail.com');


INSERT INTO users (email)
VALUES ('gorge@gmail.com');

UPDATE users
SET username = 'gorge'
WHERE email = 'gorge@gmail.com';

--

SELECT id, nickname
FROM authors
WHERE id = 1;


SELECT *
FROM articles
WHERE author_id = 1;


SELECT id, nickname
FROM authors
WHERE nickname = 'Sam Smith';


SELECT au.id, au.nickname, ar.id, ar.title, ar.body
FROM authors au
JOIN articles ar on au.id = ar.author_id
WHERE au.nickname = 'Sam Smith';

SELECT au.id, au.nickname, ar.id, ar.title, ar.body
FROM authors au
LEFT OUTER JOIN articles ar on au.id = ar.author_id
WHERE au.nickname = 'Ann White';

SELECT au.id, au.nickname, ar.id, ar.title, ar.body
FROM authors au
LEFT OUTER JOIN articles ar on au.id = ar.author_id
WHERE au.nickname = 'John Black';


SELECT au.id, au.nickname, ar.id, ar.title, ar.body
FROM authors au
LEFT OUTER JOIN articles ar on au.id = ar.author_id;


SELECT au.id, au.nickname, ar.id, ar.title, ar.body
FROM authors au
LEFT OUTER JOIN articles ar on au.id = ar.author_id
WHERE title ILIKE '%lesson%';


SELECT au.id, au.nickname, ar.id, ar.title, ar.body
FROM authors au
LEFT OUTER JOIN articles ar on au.id = ar.author_id
WHERE title ILIKE '%lesson%'
ORDER BY au.id DESC;



SELECT * FROM (
    SELECT au.id, au.nickname, ar.id, ar.title, ar.body
    FROM authors au
    LEFT OUTER JOIN articles ar on au.id = ar.author_id
    WHERE title ILIKE '%lesson%'
) as aa
WHERE aa.nickname LIKE '%Smith';


SELECT * FROM articles
WHERE articles.raw_data ->> 'spam' = 'eggs';


SELECT * FROM articles
WHERE NOT (articles.raw_data ? 'spam');


SELECT * FROM articles
WHERE articles.raw_data is NULL OR NOT (articles.raw_data ? 'spam');


SELECT *
     , raw_data -> 'foo' AS foo_value
     , raw_data -> 'foo' -> 'bar' AS foo_bar_value
     , raw_data -> 'foo' ->> 'bar' AS foo_bar_str_value
FROM articles
WHERE (raw_data -> 'foo' ->> 'bar') = 'baz';

SELECT * FROM users
WHERE id < 5;
