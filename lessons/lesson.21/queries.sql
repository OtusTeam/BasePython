CREATE TABLE users
(
    username VARCHAR(32) NOT NULL,
    email    VARCHAR,
    id       SERIAL      NOT NULL,
    PRIMARY KEY (id),
    UNIQUE (username),
    UNIQUE (email)
);


CREATE TABLE posts
(
    title        VARCHAR(100)                DEFAULT ''    NOT NULL,
    published_at TIMESTAMP WITHOUT TIME ZONE DEFAULT now() NOT NULL,
    user_id      INTEGER                                   NOT NULL,
    id           SERIAL                                    NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (user_id)
        REFERENCES users (id)
);



INSERT INTO users (username, email)
VALUES ('john'::VARCHAR, NULL)
RETURNING users.id;

SELECT users.username AS users_username, users.email AS users_email, users.id AS users_id
FROM users
WHERE users.id = 1::INTEGER;
-- User(id=1, username='john', email=None)
INSERT INTO users (username, email)
VALUES ('sam', NULL)
RETURNING users.id;

SELECT users.username AS users_username, users.email AS users_email, users.id AS users_id
FROM users
WHERE users.id = 2;
-- User(id=2, username='sam', email=None)

INSERT INTO posts (title, user_id)
VALUES ('Intro Lesson'::VARCHAR, 1)
RETURNING posts.id;

INSERT INTO posts
    (title, user_id)
VALUES ('1', 2),
       ('2', 2),
       ('3', 2);


SELECT posts.title
     , posts.published_at
     , posts.user_id
     , posts.id
FROM posts
WHERE posts.user_id = 10
ORDER BY posts.id;


SELECT users.username
     , users.id
     , posts_1.id AS post_id
     , posts_1.title
     , posts_1.published_at
     , posts_1.user_id
FROM users
         LEFT OUTER JOIN posts AS posts_1
                         ON users.id = posts_1.user_id
ORDER BY users.id;


SELECT users.username
     , users.email
     , users.id
     , posts_1.title
     , posts_1.published_at
     , posts_1.user_id
     , posts_1.id AS id_1
FROM users
--      JOIN posts
         INNER JOIN posts
                    ON users.id = posts.user_id
         LEFT OUTER JOIN posts AS posts_1
                         ON users.id = posts_1.user_id
ORDER BY users.id;


SELECT posts.title
     , posts.published_at
     , posts.user_id
     , posts.id
     , users_1.username
     , users_1.email
     , users_1.id AS id_1
FROM posts
         LEFT OUTER JOIN users AS users_1
                         ON users_1.id = posts.user_id
ORDER BY posts.id;

-- 1: fetch users
SELECT users.username
     , users.email
     , users.id
FROM users
ORDER BY users.id;

-- 2: fetch pots __for fetched users__
SELECT posts.user_id      AS posts_user_id
     , posts.title        AS posts_title
     , posts.published_at AS posts_published_at
     , posts.id           AS posts_id
FROM posts
WHERE posts.user_id IN (1, 2, 3);


--


-- 1: fetch all posts
SELECT posts.title
     , posts.published_at
     , posts.user_id
     , posts.id
FROM posts
ORDER BY posts.id;

-- 2: fetch authors __for all fetched posts__
SELECT users.id       AS users_id
     , users.username AS users_username
     , users.email    AS users_email
FROM users
WHERE users.id IN (1, 2);
