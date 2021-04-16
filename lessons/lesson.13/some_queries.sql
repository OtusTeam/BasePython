CREATE TABLE users
(
    id       INTEGER NOT NULL,
    username VARCHAR(32),
    is_staff BOOLEAN NOT NULL,
    PRIMARY KEY (id),
    UNIQUE (username),
    CHECK (is_staff IN (0, 1))
);

CREATE TABLE users
(
    id         INTEGER                              NOT NULL,
    username   VARCHAR(32),
    is_staff   BOOLEAN  DEFAULT '0'                 NOT NULL,
    created_at DATETIME DEFAULT (CURRENT_TIMESTAMP) NOT NULL,
    PRIMARY KEY (id),
    UNIQUE (username),
    CHECK (is_staff IN (0, 1))
);


CREATE TABLE posts
(
    id      INTEGER                NOT NULL,
    title   VARCHAR(64) DEFAULT '' NOT NULL,
    user_id INTEGER                NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (user_id) REFERENCES users (id)
);


SELECT *
FROM users;

SELECT *
FROM posts;

SELECT *
FROM posts
         JOIN users u on u.id = posts.user_id;

SELECT users.id         AS users_id,
       users.username   AS users_username,
       users.is_staff   AS users_is_staff,
       users.created_at AS users_created_at,
       posts_1.id       AS posts_1_id,
       posts_1.title    AS posts_1_title,
       posts_1.user_id  AS posts_1_user_id
FROM users
         LEFT OUTER JOIN posts AS posts_1 ON users.id = posts_1.user_id
WHERE users.username = 'admin';


--
SELECT users.id         AS users_id,
       users.username   AS users_username,
       users.is_staff   AS users_is_staff,
       users.created_at AS users_created_at,
       posts_1.id       AS posts_1_id,
       posts_1.title    AS posts_1_title,
       posts_1.user_id  AS posts_1_user_id
FROM users
         JOIN posts ON users.id = posts.user_id
         LEFT OUTER JOIN posts AS posts_1 ON users.id = posts_1.user_id
WHERE lower(posts.title) LIKE lower('%fastapi%')

SELECT users.id         AS users_id,
       users.username   AS users_username,
       users.is_staff   AS users_is_staff,
       users.created_at AS users_created_at
FROM users
         JOIN posts ON users.id = posts.user_id
WHERE lower(posts.title) LIKE lower('%django%')
   OR lower(posts.title) LIKE lower('%flask%')
