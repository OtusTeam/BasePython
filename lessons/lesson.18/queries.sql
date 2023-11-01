SELECT users.id,
       users.username,
       users.email
FROM users
WHERE users.username ILIKE '%o%';
-- [User(id=1, username='john', email=None), User(id=3, username='bob', email=None)]


UPDATE users
SET email=concat(users.username, '@ya.ru')
WHERE users.username ILIKE '%o%'
RETURNING users.id;

--
CREATE TABLE posts
(
    title        VARCHAR(100)                DEFAULT ''    NOT NULL,
    published_at TIMESTAMP WITHOUT TIME ZONE DEFAULT now() NOT NULL,
    user_id      INTEGER                                   NOT NULL,
    id           SERIAL                                    NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (user_id) REFERENCES users (id)
);

--

SELECT posts.title
     , posts.published_at
     , posts.user_id
     , posts.id
FROM posts
ORDER BY posts.id;

--
SELECT posts.title, posts.published_at, posts.user_id, posts.id
FROM posts
ORDER BY posts.id;

--
SELECT posts.title, posts.published_at, posts.user_id, posts.id
FROM posts
ORDER BY posts.id;

--
SELECT posts.title
     , posts.user_id
     , posts.id
     , users_1.username
     , users_1.id AS id_1
FROM posts
         LEFT OUTER JOIN users AS users_1
                         ON users_1.id = posts.user_id
ORDER BY posts.id;


--
SELECT posts.title
     , posts.published_at
     , posts.user_id
     , posts.id
FROM posts
ORDER BY posts.id;

SELECT users.id       AS users_id
     , users.username AS users_username
     , users.email    AS users_email
FROM users
WHERE users.id IN (1, 2);


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

--
SELECT users.username
     , users.email
     , users.id
FROM users
         JOIN posts ON users.id = posts.user_id
WHERE posts.title ILIKE 'Post%'
ORDER BY users.id;

SELECT posts.user_id      AS posts_user_id
     , posts.title        AS posts_title
     , posts.published_at AS posts_published_at
     , posts.id           AS posts_id
FROM posts
WHERE posts.user_id IN (1);

--

SELECT users.username
     , users.email
     , users.id
     , posts_1.title
     , posts_1.published_at
     , posts_1.user_id
     , posts_1.id AS id_1
FROM users
         JOIN posts ON users.id = posts.user_id
         LEFT OUTER JOIN posts AS posts_1 ON users.id = posts_1.user_id
WHERE posts.title ILIKE 'Another%'
ORDER BY users.id;

SELECT count(*)
FROM posts;

SELECT u.id
     , u.username
     , p.id
     , p.title
FROM users u
         JOIN posts p ON u.id = p.user_id
ORDER BY u.id;

SELECT u.id
     , u.username
     , count(p.id) "posts count"
FROM users u
         JOIN posts p ON u.id = p.user_id
--      LEFT OUTER JOIN posts p ON u.id = p.user_id
GROUP BY u.id
ORDER BY u.id;

SELECT u.id
     , u.username
     , count(p.id) "posts count"
FROM users u
         JOIN posts p ON u.id = p.user_id
--      LEFT OUTER JOIN posts p ON u.id = p.user_id
GROUP BY u.id
HAVING count(p.id) >= 2
ORDER BY u.id;

--

SELECT users.username, users.email, users.id
FROM users
         JOIN posts ON users.id = posts.user_id
GROUP BY users.id
-- HAVING count(posts.id) >= 2
ORDER BY users.id;

SELECT posts.user_id      AS posts_user_id
     , posts.title        AS posts_title
     , posts.published_at AS posts_published_at
     , posts.id           AS posts_id
FROM posts
WHERE posts.user_id IN (1)
