CREATE TABLE users
(
    id        SERIAL          NOT NULL,
    username  TEXT            NOT NULL,
    email     TEXT,
    full_name TEXT DEFAULT '' NOT NULL,
    PRIMARY KEY (id),
    CHECK (length(username) <= 32),
    CHECK (length(email) <= 200),
    CHECK (length(full_name) <= 100),
    UNIQUE (username),
    UNIQUE (email)
);

CREATE TABLE users
(
    id        INTEGER GENERATED ALWAYS AS IDENTITY,
    username  TEXT            NOT NULL,
    email     TEXT,
    full_name TEXT DEFAULT '' NOT NULL,
    PRIMARY KEY (id),
    CHECK (length(username) <= 32),
    CHECK (length(email) <= 200),
    CHECK (length(full_name) <= 100),
    UNIQUE (username),
    UNIQUE (email)
);

CREATE TABLE posts
(
    id      INTEGER GENERATED ALWAYS AS IDENTITY,
    title   TEXT    NOT NULL,
    body    TEXT    NOT NULL,
    user_id INTEGER NOT NULL,
    PRIMARY KEY (id),
    CHECK (length(title) <= 80),
    FOREIGN KEY (user_id) REFERENCES users (id)
);


CREATE TABLE posts
(
    title   TEXT    NOT NULL,
    body    TEXT    NOT NULL,
    user_id INTEGER NOT NULL,
    id      INTEGER GENERATED ALWAYS AS IDENTITY,
    PRIMARY KEY (id),
    CHECK (length(title) <= 80),
    FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE CASCADE
);

SELECT users.username
     , users.email
     , users.full_name
     , users.id
FROM users
ORDER BY users.id;

SELECT posts.user_id AS posts_user_id
     , posts.title   AS posts_title
     , posts.body    AS posts_body
     , posts.id      AS posts_id
FROM posts
WHERE posts.user_id IN (1, 2, 3);

SELECT posts.title
     , posts.body
     , posts.user_id
     , posts.id
     , users_1.username
     , users_1.email
     , users_1.full_name
     , users_1.id AS id_1
FROM posts
         LEFT OUTER JOIN users AS users_1
                         ON users_1.id = posts.user_id
ORDER BY posts.id;

SELECT posts.title
     , posts.body
     , posts.user_id
     , posts.id
     , users_1.username
     , users_1.email
     , users_1.full_name
     , users_1.id AS id_1
FROM posts
         JOIN users AS users_1 ON users_1.id = posts.user_id
ORDER BY posts.id;

--

SELECT posts.title
     , users.username
FROM posts,
     users;

SELECT posts.title
     , users.username
FROM posts
         JOIN users ON users.id = posts.user_id;


SELECT posts.title
     , posts.body
     , posts.user_id
     , posts.id
     , users_1.username
     , users_1.email
     , users_1.full_name
     , users_1.id AS id_1
FROM posts
         JOIN users ON users.id = posts.user_id
         JOIN users AS users_1 ON users_1.id = posts.user_id
WHERE users.email IS NOT NULL
ORDER BY posts.id;


--

SELECT posts.title
     , posts.body
     , posts.user_id
     , posts.id
     , posts.created_at
FROM posts
WHERE posts.title ILIKE '%lesson%'
   OR posts.title ILIKE '%intro%';

SELECT posts_1.id        AS posts_1_id
     , tags.name         AS tags_name
     , tags.display_name AS tags_display_name
     , tags.created_at   AS tags_created_at
FROM posts AS posts_1
         JOIN posts_tags_association_table AS posts_tags_association_table_1
              ON posts_1.id = posts_tags_association_table_1.post_id
         JOIN tags ON tags.name = posts_tags_association_table_1.tag_name
WHERE posts_1.id IN (5, 6, 7, 8, 9, 10);


SELECT posts.title
     , posts.body
     , posts.user_id
     , posts.id
     , posts.created_at
     , users_1.username
     , users_1.email
     , users_1.full_name
     , users_1.id         AS id_1
     , users_1.created_at AS created_at_1
FROM posts
         JOIN users AS users_1 ON users_1.id = posts.user_id;


--
--
--

SELECT users.username
     , users.email
     , users.full_name
     , users.id
     , users.created_at
FROM users;

SELECT posts.user_id    AS posts_user_id
     , posts.title      AS posts_title
     , posts.body       AS posts_body
     , posts.id         AS posts_id
     , posts.created_at AS posts_created_at
FROM posts
WHERE posts.user_id IN (2, 3, 4);

SELECT posts_1.id        AS posts_1_id
     , tags.name         AS tags_name
     , tags.display_name AS tags_display_name
     , tags.created_at   AS tags_created_at
FROM posts AS posts_1
         JOIN posts_tags_association_table AS posts_tags_association_table_1
              ON posts_1.id = posts_tags_association_table_1.post_id
         JOIN tags ON tags.name = posts_tags_association_table_1.tag_name
WHERE posts_1.id IN (1, 2, 3, 5, 6, 7, 8, 9, 10, 11);

--


SELECT users.username
     , users.email
     , users.full_name
     , users.id
     , users.created_at
FROM users
WHERE length(users.username) > 3;

SELECT posts.title      AS posts_title
     , posts.body       AS posts_body
     , posts.user_id    AS posts_user_id
     , posts.id         AS posts_id
     , posts.created_at AS posts_created_at
     , anon_1.users_id  AS anon_1_users_id
FROM (SELECT users.id AS users_id
      FROM users
      WHERE length(users.username) > 3) AS anon_1
         JOIN posts ON anon_1.users_id = posts.user_id;

SELECT tags.name         AS tags_name
     , tags.display_name AS tags_display_name
     , tags.created_at   AS tags_created_at
     , posts_1.id        AS posts_1_id
FROM (SELECT users.id AS users_id
      FROM users
      WHERE length(users.username) > 3) AS anon_1
         JOIN posts AS posts_1 ON anon_1.users_id = posts_1.user_id
         JOIN posts_tags_association_table AS posts_tags_association_table_1
              ON posts_1.id = posts_tags_association_table_1.post_id
         JOIN tags ON tags.name = posts_tags_association_table_1.tag_name
