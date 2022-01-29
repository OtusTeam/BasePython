-- CREATE TABLE blog_users
-- (
--     id       INTEGER NOT NULL,
--     username VARCHAR(32),
--     is_staff BOOLEAN,
--     PRIMARY KEY (id),
--     UNIQUE (username)
-- );

CREATE TABLE blog_users
(
    id         INTEGER NOT NULL,
    created_at DATETIME DEFAULT (CURRENT_TIMESTAMP) NOT NULL,
    username   VARCHAR(32),
    is_staff   BOOLEAN,
    PRIMARY KEY (id),
    UNIQUE (username)
);

SELECT CURRENT_TIMESTAMP;

SELECT 1, 2, 3;

SELECT 1 + 2 AS sum;

INSERT INTO blog_users (created_at, username, is_staff)
VALUES ('2022-01-29 08:44:42.137146', 'sam', 0);


CREATE TABLE blog_authors
(
    id         INTEGER NOT NULL,
    created_at DATETIME    DEFAULT (CURRENT_TIMESTAMP) NOT NULL,
    name       VARCHAR(64) DEFAULT '' NOT NULL,
    user_id    INTEGER NOT NULL,
    PRIMARY KEY (id),
    UNIQUE (user_id),
    FOREIGN KEY (user_id) REFERENCES blog_users (id)
);

SELECT blog_users.id         AS blog_users_id,
       blog_users.created_at AS blog_users_created_at,
       blog_users.username   AS blog_users_username,
       blog_users.is_staff   AS blog_users_is_staff
FROM blog_users
WHERE blog_users.username = 'sam';

INSERT INTO blog_authors (created_at, name, user_id)
VALUES ('2022-01-29 08:58:16.416214', 'Samuel White', 3);

SELECT blog_authors.id         AS blog_authors_id,
       blog_authors.created_at AS blog_authors_created_at,
       blog_authors.name       AS blog_authors_name,
       blog_authors.user_id    AS blog_authors_user_id
FROM blog_authors
WHERE blog_authors.id = 1;

SELECT blog_users.id         AS blog_users_id,
       blog_users.created_at AS blog_users_created_at,
       blog_users.username   AS blog_users_username,
       blog_users.is_staff   AS blog_users_is_staff
FROM blog_users
WHERE blog_users.id = 3;


SELECT blog_authors.id         AS blog_authors_id,
       blog_authors.created_at AS blog_authors_created_at,
       blog_authors.name       AS blog_authors_name,
       blog_authors.user_id    AS blog_authors_user_id
FROM blog_authors
WHERE 3 = blog_authors.user_id;


CREATE TABLE blog_posts
(
    id         INTEGER NOT NULL,
    created_at DATETIME     DEFAULT (CURRENT_TIMESTAMP) NOT NULL,
    title      VARCHAR(200) DEFAULT '' NOT NULL,
    body       TEXT         DEFAULT '' NOT NULL,
    status     VARCHAR(10)  DEFAULT 'draft' NOT NULL,
    author_id  INTEGER NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (author_id) REFERENCES blog_authors (id)
);

SELECT blog_authors.id         AS blog_authors_id,
       blog_authors.created_at AS blog_authors_created_at,
       blog_authors.name       AS blog_authors_name,
       blog_authors.user_id    AS blog_authors_user_id
FROM blog_authors
         JOIN blog_users ON blog_users.id = blog_authors.user_id
WHERE blog_users.username = 'john';


INSERT INTO blog_posts (created_at, title, body, status, author_id)
VALUES ('2022-01-29 09:17:02.816578',
        'Lesson Django',
        '',
        'draft',
        2);

INSERT INTO blog_posts (created_at, title, body, status, author_id)
VALUES ('2022-01-29 09:17:02.816920',
        'Lesson Flask',
        '',
        'draft',
        2);


SELECT blog_posts.id             AS blog_posts_id,
       blog_posts.created_at     AS blog_posts_created_at,
       blog_posts.title          AS blog_posts_title,
       blog_posts.body           AS blog_posts_body,
       blog_posts.status         AS blog_posts_status,
       blog_posts.author_id      AS blog_posts_author_id,
       blog_users_1.id           AS blog_users_1_id,
       blog_users_1.created_at   AS blog_users_1_created_at,
       blog_users_1.username     AS blog_users_1_username,
       blog_users_1.is_staff     AS blog_users_1_is_staff,
       blog_authors_1.id         AS blog_authors_1_id,
       blog_authors_1.created_at AS blog_authors_1_created_at,
       blog_authors_1.name       AS blog_authors_1_name,
       blog_authors_1.user_id    AS blog_authors_1_user_id
FROM blog_posts
         LEFT OUTER JOIN blog_authors AS blog_authors_1 ON blog_authors_1.id = blog_posts.author_id
         LEFT OUTER JOIN blog_users AS blog_users_1 ON blog_users_1.id = blog_authors_1.user_id


SELECT blog_authors.id         AS blog_authors_id,
       blog_authors.created_at AS blog_authors_created_at,
       blog_authors.name       AS blog_authors_name,
       blog_authors.user_id    AS blog_authors_user_id,
       blog_users_1.id         AS blog_users_1_id,
       blog_users_1.created_at AS blog_users_1_created_at,
       blog_users_1.username   AS blog_users_1_username,
       blog_users_1.is_staff   AS blog_users_1_is_staff,
       blog_posts_1.id         AS blog_posts_1_id,
       blog_posts_1.created_at AS blog_posts_1_created_at,
       blog_posts_1.title      AS blog_posts_1_title,
       blog_posts_1.body       AS blog_posts_1_body,
       blog_posts_1.status     AS blog_posts_1_status,
       blog_posts_1.author_id  AS blog_posts_1_author_id
FROM blog_authors
         JOIN blog_posts ON blog_posts.author_id = blog_authors.id
         LEFT OUTER JOIN blog_users AS blog_users_1 ON blog_users_1.id = blog_authors.user_id
         LEFT OUTER JOIN blog_posts AS blog_posts_1 ON blog_authors.id = blog_posts_1.author_id
WHERE lower(blog_posts.title) LIKE lower('lesson%');
