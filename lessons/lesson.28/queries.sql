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
ORDER BY posts.id