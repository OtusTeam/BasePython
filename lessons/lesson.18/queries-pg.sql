CREATE TABLE users
(
    id         SERIAL                                    NOT NULL,
    username   VARCHAR(32)                               NOT NULL,
    email      VARCHAR(100),
    is_staff   BOOLEAN                     DEFAULT false NOT NULL,
    created_at TIMESTAMP WITHOUT TIME ZONE DEFAULT now() NOT NULL,
    PRIMARY KEY (id),
    UNIQUE (username),
    UNIQUE (email)
);


CREATE TABLE posts
(
    id           SERIAL                                    NOT NULL,
    title        VARCHAR(100)                              NOT NULL,
    body         TEXT                        DEFAULT ''    NOT NULL,
    published_at TIMESTAMP WITHOUT TIME ZONE DEFAULT now() NOT NULL,
    user_id      INTEGER                                   NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (user_id) REFERENCES users (id)
);

SELECT *
FROM users;

SELECT *
FROM posts;

INSERT INTO posts (title, user_id)
VALUES ('Some title', 1);

INSERT INTO posts (title, user_id)
VALUES ('Another title', 2);

INSERT INTO posts (title, user_id)
VALUES ('New title', 2);


INSERT INTO posts (title, user_id)
VALUES ('Post by John', 1)
RETURNING posts.id;


--
SELECT users.id         AS users_id,
       users.username   AS users_username,
       users.email      AS users_email,
       users.is_staff   AS users_is_staff,
       users.created_at AS users_created_at
FROM users
WHERE users.id = 2;

-- ************* user sam

SELECT posts.id           AS posts_id,
       posts.title        AS posts_title,
       posts.body         AS posts_body,
       posts.published_at AS posts_published_at,
       posts.user_id      AS posts_user_id
FROM posts
WHERE posts.user_id = 2;
--     post 3 Post by Sam
--     post 4 PyCharm lesson
--     post 5 VS Code lesson


-- all

-- N + 1 problem

SELECT users.id         AS users_id,
       users.username   AS users_username,
       users.email      AS users_email,
       users.is_staff   AS users_is_staff,
       users.created_at AS users_created_at
FROM users
ORDER BY users.id;

-- ************* user john
SELECT posts.id           AS posts_id,
       posts.title        AS posts_title,
       posts.body         AS posts_body,
       posts.published_at AS posts_published_at,
       posts.user_id      AS posts_user_id
FROM posts
WHERE posts.user_id = 1;


-- ************* user sam
SELECT posts.id           AS posts_id,
       posts.title        AS posts_title,
       posts.body         AS posts_body,
       posts.published_at AS posts_published_at,
       posts.user_id      AS posts_user_id
FROM posts
WHERE posts.user_id = 2;


-- joined

SELECT users.id             AS users_id,
       users.username       AS users_username,
       users.email          AS users_email,
       users.is_staff       AS users_is_staff,
       users.created_at     AS users_created_at,
       posts_1.id           AS posts_1_id,
       posts_1.title        AS posts_1_title,
       posts_1.body         AS posts_1_body,
       posts_1.published_at AS posts_1_published_at,
       posts_1.user_id      AS posts_1_user_id
FROM users
         LEFT OUTER JOIN posts AS posts_1
                         ON users.id = posts_1.user_id
ORDER BY users.id;


SELECT users.id             AS users_id,
       users.username       AS users_username,
       users.email          AS users_email,
       users.is_staff       AS users_is_staff,
       users.created_at     AS users_created_at,
       posts_1.id           AS posts_1_id,
       posts_1.title        AS posts_1_title,
       posts_1.body         AS posts_1_body,
       posts_1.published_at AS posts_1_published_at,
       posts_1.user_id      AS posts_1_user_id
FROM users
         JOIN posts AS posts_1 ON users.id = posts_1.user_id
ORDER BY users.id;

SELECT posts.id           AS posts_id,
       posts.title        AS posts_title,
       posts.body         AS posts_body,
       posts.published_at AS posts_published_at,
       posts.user_id      AS posts_user_id,
       users_1.id         AS users_1_id,
       users_1.username   AS users_1_username,
       users_1.email      AS users_1_email,
       users_1.is_staff   AS users_1_is_staff,
       users_1.created_at AS users_1_created_at
FROM posts
         JOIN users AS users_1 ON users_1.id = posts.user_id
ORDER BY posts.id;

-- len

SELECT posts.id           AS posts_id,
       posts.title        AS posts_title,
       posts.body         AS posts_body,
       posts.published_at AS posts_published_at,
       posts.user_id      AS posts_user_id
FROM posts
WHERE length(posts.title) <= 11
ORDER BY posts.id;


-- join

SELECT posts.id           AS posts_id,
       posts.title        AS posts_title,
       posts.body         AS posts_body,
       posts.published_at AS posts_published_at,
       posts.user_id      AS posts_user_id
FROM posts
         JOIN users ON posts.user_id = users.id
WHERE users.email ILIKE '%@yahoo.com';


SELECT posts.id           AS posts_id,
       posts.title        AS posts_title,
       posts.body         AS posts_body,
       posts.published_at AS posts_published_at,
       posts.user_id      AS posts_user_id,
       users_1.id         AS users_1_id,
       users_1.username   AS users_1_username,
       users_1.email      AS users_1_email,
       users_1.is_staff   AS users_1_is_staff,
       users_1.created_at AS users_1_created_at
FROM posts
         JOIN users ON users.id = posts.user_id
         LEFT OUTER JOIN users AS users_1 ON users_1.id = posts.user_id
WHERE users.email ILIKE '%@example.com'
ORDER BY posts.id