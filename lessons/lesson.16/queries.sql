CREATE TABLE users
(
    id         SERIAL                                    NOT NULL,
    created_at TIMESTAMP WITHOUT TIME ZONE DEFAULT now() NOT NULL,
    username   VARCHAR(20),
    is_staff   BOOLEAN                     DEFAULT 'FALSE',
    PRIMARY KEY (id),
    UNIQUE (username)
);


INSERT INTO users (created_at, username, is_staff)
VALUES (% s, % s, % s)
RETURNING users.id
    (datetime.datetime(2022, 4, 26, 17, 30, 49, 927774), 'john', False);


CREATE TABLE authors
(
    id         SERIAL                                    NOT NULL,
    created_at TIMESTAMP WITHOUT TIME ZONE DEFAULT now() NOT NULL,
    name       VARCHAR                     DEFAULT ''    NOT NULL,
    user_id    INTEGER                                   NOT NULL,
    PRIMARY KEY (id),
    UNIQUE (user_id),
    FOREIGN KEY (user_id) REFERENCES users (id)
);


INSERT INTO authors (created_at, name, user_id)
VALUES (% s, % s, % s)
RETURNING authors.id
    (datetime.datetime(2022, 4, 26, 17, 46, 8, 385205), 'Samuel', 5);

SELECT authors.id         AS authors_id,
       authors.created_at AS authors_created_at,
       authors.name       AS authors_name,
       authors.user_id    AS authors_user_id
FROM authors
WHERE authors.id = 1;

SELECT users.id         AS users_id,
       users.created_at AS users_created_at,
       users.username   AS users_username,
       users.is_staff   AS users_is_staff
FROM users
WHERE users.id = 5;

--
--

SELECT authors.id         AS authors_id,
       authors.created_at AS authors_created_at,
       authors.name       AS authors_name,
       authors.user_id    AS authors_user_id
FROM authors
WHERE authors.id = 1;

SELECT users.id         AS users_id,
       users.created_at AS users_created_at,
       users.username   AS users_username,
       users.is_staff   AS users_is_staff
FROM users
WHERE users.id = 5;


--

SELECT authors.id         AS authors_id,
       authors.created_at AS authors_created_at,
       authors.name       AS authors_name,
       authors.user_id    AS authors_user_id,
       users_1.id         AS users_1_id,
       users_1.created_at AS users_1_created_at,
       users_1.username   AS users_1_username,
       users_1.is_staff   AS users_1_is_staff
FROM authors
         LEFT OUTER JOIN users AS users_1 ON users_1.id = authors.user_id
WHERE authors.id = 1;

--
SELECT users.id             AS users_id,
       users.created_at     AS users_created_at,
       users.username       AS users_username,
       users.is_staff       AS users_is_staff,
       authors_1.id         AS authors_1_id,
       authors_1.created_at AS authors_1_created_at,
       authors_1.name       AS authors_1_name,
       authors_1.user_id    AS authors_1_user_id
FROM users
         LEFT JOIN authors AS authors_1 ON users.id = authors_1.user_id
-- WHERE users.username = 'sam';
-- WHERE users.username = 'john';


SELECT users.id         AS users_id,
       users.created_at AS users_created_at,
       users.username   AS users_username,
       users.is_staff   AS users_is_staff
FROM users
         JOIN authors ON users.id = authors.user_id
WHERE authors.name = 'Samuel'
LIMIT 1;


SELECT users.id             AS users_id,
       users.created_at     AS users_created_at,
       users.username       AS users_username,
       users.is_staff       AS users_is_staff,
       authors_1.id         AS authors_1_id,
       authors_1.created_at AS authors_1_created_at,
       authors_1.name       AS authors_1_name,
       authors_1.user_id    AS authors_1_user_id
FROM users
         JOIN authors ON users.id = authors.user_id
         LEFT OUTER JOIN authors AS authors_1 ON users.id = authors_1.user_id
WHERE authors.name = 'Samuel'
LIMIT 1;


CREATE TABLE posts
(
    id         SERIAL                                    NOT NULL,
    created_at TIMESTAMP WITHOUT TIME ZONE DEFAULT now() NOT NULL,
    title      VARCHAR(200)                              NOT NULL,
    body       TEXT                        DEFAULT ''    NOT NULL,
    author_id  INTEGER                                   NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (author_id) REFERENCES authors (id)
);

INSERT INTO posts (created_at, title, body, author_id)
VALUES (% s, % s, % s, % s)
RETURNING posts.id
    (datetime.datetime(2022, 4, 26, 18, 27, 34, 496207), 'Django Intro', '', 1);
INSERT INTO posts (created_at, title, body, author_id)
VALUES (% s, % s, % s, % s)
RETURNING posts.id
    (datetime.datetime(2022, 4, 26, 18, 27, 34, 500741), 'Flask Lesson', '', 1);


--

SELECT users.id             AS users_id,
       users.created_at     AS users_created_at,
       users.username       AS users_username,
       users.is_staff       AS users_is_staff,
       posts_1.id           AS posts_1_id,
       posts_1.created_at   AS posts_1_created_at,
       posts_1.title        AS posts_1_title,
       posts_1.body         AS posts_1_body,
       posts_1.author_id    AS posts_1_author_id,
       authors_1.id         AS authors_1_id,
       authors_1.created_at AS authors_1_created_at,
       authors_1.name       AS authors_1_name,
       authors_1.user_id    AS authors_1_user_id
FROM users
         LEFT OUTER JOIN authors AS authors_1 ON users.id = authors_1.user_id
         LEFT OUTER JOIN posts AS posts_1 ON authors_1.id = posts_1.author_id
WHERE users.username = 'sam';