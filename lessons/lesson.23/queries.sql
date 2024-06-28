CREATE TABLE users
(
    id       SERIAL      NOT NULL,
    username VARCHAR(32) NOT NULL,
    email    VARCHAR,
    PRIMARY KEY (id),
    UNIQUE (username),
    UNIQUE (email)
);


CREATE TABLE posts
(
    id           SERIAL       NOT NULL,
    title        VARCHAR(100) NOT NULL,
    published_at TIMESTAMP WITHOUT TIME ZONE,
    user_id      INTEGER      NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (user_id) REFERENCES users (id)
);


SELECT users.username AS users_username
     , users.email    AS users_email
     , users.id       AS users_id
FROM users;

INSERT INTO posts (title, user_id)
VALUES ('PostgreSQL news'::VARCHAR, 2::INTEGER)
RETURNING posts.id;

SELECT users.id
     , users.username
     , users.email
FROM users
ORDER BY users.username DESC;

SELECT posts.id
     , posts.title
     , posts.published_at
     , posts.user_id
FROM posts
ORDER BY posts.id;


SELECT posts.title        AS posts_title
     , posts.published_at AS posts_published_at
     , posts.user_id      AS posts_user_id
     , posts.id           AS posts_id
FROM posts
WHERE 3::INTEGER = posts.user_id;

SELECT users.username AS users_username
     , users.email    AS users_email
     , users.id       AS users_id
FROM users
WHERE users.id = 3::INTEGER;


SELECT users.username
     , users.email
     , users.id
     , posts_1.title
     , posts_1.published_at
     , posts_1.user_id
     , posts_1.id AS id_1
FROM users
         LEFT OUTER JOIN posts AS posts_1
                         ON users.id = posts_1.user_id
ORDER BY users.id;

--

SELECT users.username
     , users.email
     , users.id
FROM users
ORDER BY users.id;

SELECT posts.user_id      AS posts_user_id
     , posts.title        AS posts_title
     , posts.published_at AS posts_published_at
     , posts.id           AS posts_id
FROM posts
WHERE posts.user_id IN (1, 2, 3);


SELECT posts.title,
       posts.user_id,
       users_1.username,
       users_1.id AS id_1
FROM posts
         LEFT OUTER JOIN users AS users_1
                         ON users_1.id = posts.user_id
ORDER BY posts.id;

SELECT posts.title, posts.published_at, posts.user_id, posts.id
FROM posts
         JOIN users ON users.id = posts.user_id
WHERE length(users.username) > 1::INTEGER
ORDER BY posts.id;

SELECT posts.title
     , posts.published_at
     , posts.user_id
     , posts.id
     , users_1.username
     , users_1.email
     , users_1.id AS id_1
FROM posts
         JOIN users ON users.id = posts.user_id
         LEFT OUTER JOIN users AS users_1 ON users_1.id = posts.user_id
WHERE length(users.username) > 3::INTEGER
ORDER BY posts.id;


SELECT posts.title
     , posts.published_at
     , posts.user_id
     , posts.id
FROM posts
         JOIN users ON users.id = posts.user_id
WHERE length(users.username) > 3::INTEGER
ORDER BY posts.id;

SELECT users.id       AS users_id
     , users.username AS users_username
     , users.email    AS users_email
FROM users
WHERE users.id IN (2);


SELECT users.username
     , users.id
     , count(posts.id) AS posts_count
FROM users
         LEFT OUTER JOIN posts ON users.id = posts.user_id
GROUP BY users.id
ORDER BY count(posts.id) DESC, users.username;

