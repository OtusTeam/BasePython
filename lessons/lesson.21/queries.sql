-- CREATE TABLE blog_users
-- (
--     id       SERIAL      NOT NULL,
--     username VARCHAR(20) NOT NULL,
--     is_staff BOOLEAN,
--     PRIMARY KEY (id),
--     UNIQUE (username)
-- );

CREATE TABLE blog_users
(
    id         SERIAL                                    NOT NULL,
    created_at TIMESTAMP WITHOUT TIME ZONE DEFAULT now() NOT NULL,
    username   VARCHAR(20)                               NOT NULL,
    is_staff   BOOLEAN                                   NOT NULL,
    PRIMARY KEY (id),
    UNIQUE (username)
);

CREATE TABLE blog_authors
(
    id         SERIAL                                    NOT NULL,
    created_at TIMESTAMP WITHOUT TIME ZONE DEFAULT now() NOT NULL,
    name       VARCHAR(80)                 DEFAULT ''    NOT NULL,
    user_id    INTEGER                                   NOT NULL,
    PRIMARY KEY (id),
    UNIQUE (user_id),
    FOREIGN KEY (user_id) REFERENCES blog_users (id)
);

CREATE TABLE blog_posts
(
    id         SERIAL                                    NOT NULL,
    created_at TIMESTAMP WITHOUT TIME ZONE DEFAULT now() NOT NULL,
    title      VARCHAR(100)                DEFAULT ''    NOT NULL,
    body       TEXT                        DEFAULT ''    NOT NULL,
    author_id  INTEGER                                   NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (author_id) REFERENCES blog_authors (id)
);


-- Demo join author
SELECT blog_users.id          users_id,
       blog_users.username    users_username,
       blog_authors_1.id      authors_1_id,
       blog_authors_1.name    authors_1_name,
       blog_authors_1.user_id authors_1_user_id
FROM blog_users
         LEFT OUTER JOIN blog_authors AS blog_authors_1
                         ON blog_authors_1.user_id = blog_users.id;


-- Demo join user
SELECT blog_authors.id         AS blog_authors_id,
       blog_authors.created_at AS blog_authors_created_at,
       blog_authors.name       AS blog_authors_name,
       blog_authors.user_id    AS blog_authors_user_id,
       blog_users_1.id         AS blog_users_1_id,
       blog_users_1.created_at AS blog_users_1_created_at,
       blog_users_1.username   AS blog_users_1_username,
       blog_users_1.is_staff   AS blog_users_1_is_staff
FROM blog_authors
         LEFT OUTER JOIN blog_users AS blog_users_1
                         ON blog_users_1.id = blog_authors.user_id;


SELECT blog_authors.id         AS blog_authors_id,
       blog_authors.created_at AS blog_authors_created_at,
       blog_authors.name       AS blog_authors_name,
       blog_authors.user_id    AS blog_authors_user_id,
       blog_users_1.id         AS blog_users_1_id,
       blog_users_1.created_at AS blog_users_1_created_at,
       blog_users_1.username   AS blog_users_1_username,
       blog_users_1.is_staff   AS blog_users_1_is_staff
FROM blog_authors
         JOIN blog_users ON blog_users.id = blog_authors.user_id
         LEFT OUTER JOIN blog_users AS blog_users_1
                         ON blog_users_1.id = blog_authors.user_id
WHERE blog_users.username = 'john';


SELECT blog_posts.id         AS blog_posts_id,
       blog_posts.title      AS blog_posts_title,
       blog_authors_1.name   AS blog_authors_1_name,
       blog_users_1.username AS blog_users_1_username
FROM blog_posts
         LEFT OUTER JOIN blog_authors AS blog_authors_1
                         ON blog_authors_1.id = blog_posts.author_id
         LEFT OUTER JOIN blog_users AS blog_users_1
                         ON blog_users_1.id = blog_authors_1.user_id;


--
SELECT blog_posts.id             AS blog_posts_id,
       blog_posts.created_at     AS blog_posts_created_at,
       blog_posts.title          AS blog_posts_title,
       blog_posts.body           AS blog_posts_body,
       blog_posts.author_id      AS blog_posts_author_id,
       blog_users_1.id           AS blog_users_1_id,
       blog_users_1.username     AS blog_users_1_username,
       blog_users_1.is_staff     AS blog_users_1_is_staff,
       blog_authors_1.id         AS blog_authors_1_id,
       blog_authors_1.created_at AS blog_authors_1_created_at,
       blog_authors_1.name       AS blog_authors_1_name,
       blog_authors_1.user_id    AS blog_authors_1_user_id
FROM blog_posts
         JOIN blog_authors ON blog_authors.id = blog_posts.author_id
         JOIN blog_users ON blog_users.id = blog_authors.user_id
         LEFT OUTER JOIN blog_authors AS blog_authors_1
                         ON blog_authors_1.id = blog_posts.author_id
         LEFT OUTER JOIN blog_users AS blog_users_1
                         ON blog_users_1.id = blog_authors_1.user_id
WHERE blog_users.username = 'bob';
-----

--

SELECT blog_posts.id         AS blog_posts_id,
       blog_posts.created_at AS blog_posts_created_at,
       blog_posts.title      AS blog_posts_title,
       blog_posts.body       AS blog_posts_body,
       blog_posts.author_id  AS blog_posts_author_id
FROM blog_posts;

SELECT blog_posts_1.id      AS blog_posts_1_id,
       blog_tags.id         AS blog_tags_id,
       blog_tags.created_at AS blog_tags_created_at,
       blog_tags.name       AS blog_tags_name
FROM blog_posts AS blog_posts_1
         JOIN posts_tags_association AS posts_tags_association_1
              ON blog_posts_1.id = posts_tags_association_1.post_id
         JOIN blog_tags
              ON blog_tags.id = posts_tags_association_1.tag_id
WHERE blog_posts_1.id IN (1, 2, 3, 4);

INSERT INTO posts_tags_association (post_id, tag_id)
VALUES (2, 8),
       (2, 12),
       (3, 10),
       (3, 13),
       (1, 9),
       (1, 12),
       (4, 11),
       (4, 13);


SELECT blog_users.id       AS blog_users_id,
       blog_users.username AS blog_users_username,
       blog_users.is_staff AS blog_users_is_staff
FROM blog_users
         JOIN blog_authors ON
    blog_users.id = blog_authors.user_id
         JOIN blog_posts ON
    blog_authors.id = blog_posts.author_id
         JOIN posts_tags_association AS posts_tags_association_1 ON
    blog_posts.id = posts_tags_association_1.post_id
         JOIN blog_tags ON
    blog_tags.id = posts_tags_association_1.tag_id
WHERE lower(blog_tags.name) = 'sql';


SELECT blog_posts.id             AS blog_posts_id,
       blog_posts.created_at     AS blog_posts_created_at,
       blog_posts.title          AS blog_posts_title,
       blog_posts.body           AS blog_posts_body,
       blog_posts.author_id      AS blog_posts_author_id,
       blog_authors_1.id         AS blog_authors_1_id,
       blog_authors_1.created_at AS blog_authors_1_created_at,
       blog_authors_1.name       AS blog_authors_1_name,
       blog_authors_1.user_id    AS blog_authors_1_user_id,
       blog_tags_1.id            AS blog_tags_1_id,
       blog_tags_1.created_at    AS blog_tags_1_created_at,
       blog_tags_1.name          AS blog_tags_1_name
FROM blog_posts
         JOIN posts_tags_association AS posts_tags_association_1 ON
    blog_posts.id = posts_tags_association_1.post_id
         JOIN blog_tags ON
    blog_tags.id = posts_tags_association_1.tag_id
         LEFT OUTER JOIN blog_authors AS blog_authors_1 ON
    blog_authors_1.id = blog_posts.author_id
         LEFT OUTER JOIN (
    posts_tags_association AS posts_tags_association_2 JOIN blog_tags AS blog_tags_1
    ON
        blog_tags_1.id = posts_tags_association_2.tag_id)
                         ON
                             blog_posts.id = posts_tags_association_2.post_id
WHERE lower(blog_tags.name) IN ('sql', 'python', 'news');


--
SELECT blog_posts.id             AS blog_posts_id,
       blog_posts.created_at     AS blog_posts_created_at,
       blog_posts.title          AS blog_posts_title,
       blog_posts.body           AS blog_posts_body,
       blog_posts.author_id      AS blog_posts_author_id,
       blog_authors_1.id         AS blog_authors_1_id,
       blog_authors_1.created_at AS blog_authors_1_created_at,
       blog_authors_1.name       AS blog_authors_1_name,
       blog_authors_1.user_id    AS blog_authors_1_user_id,
       blog_tags_1.id            AS blog_tags_1_id,
       blog_tags_1.created_at    AS blog_tags_1_created_at,
       blog_tags_1.name          AS blog_tags_1_name,
       table_tags_1.name,
       table_tags_2.name
FROM blog_posts
         JOIN posts_tags_association AS posts_tags_association_1
              ON blog_posts.id = posts_tags_association_1.post_id
         JOIN blog_tags AS table_tags_1
              ON table_tags_1.id = posts_tags_association_1.tag_id
         JOIN posts_tags_association AS posts_tags_association_2
              ON blog_posts.id = posts_tags_association_2.post_id
         JOIN blog_tags AS table_tags_2
              ON table_tags_2.id = posts_tags_association_2.tag_id
         LEFT OUTER JOIN blog_authors AS blog_authors_1
                         ON blog_authors_1.id = blog_posts.author_id
         LEFT OUTER JOIN (posts_tags_association AS posts_tags_association_3 JOIN blog_tags AS blog_tags_1
                          ON blog_tags_1.id = posts_tags_association_3.tag_id)
                         ON blog_posts.id = posts_tags_association_3.post_id
WHERE lower(table_tags_1.name) = 'python'
  AND lower(table_tags_2.name) = 'lesson';


SELECT blog_posts.id             AS blog_posts_id,
       blog_posts.created_at     AS blog_posts_created_at,
       blog_posts.title          AS blog_posts_title,
       blog_posts.body           AS blog_posts_body,
       blog_posts.author_id      AS blog_posts_author_id,
       blog_authors_1.id         AS blog_authors_1_id,
       blog_authors_1.created_at AS blog_authors_1_created_at,
       blog_authors_1.name       AS blog_authors_1_name,
       blog_authors_1.user_id    AS blog_authors_1_user_id,
       blog_tags_1.id            AS blog_tags_1_id,
       blog_tags_1.created_at    AS blog_tags_1_created_at
       , blog_tags_1.name          AS blog_tags_1_name
       , table_tags_search_flask.name
       , table_tags_search_python.name
       , table_tags_search_lesson.name
FROM blog_posts
     JOIN posts_tags_association AS posts_tags_association_1 ON blog_posts.id = posts_tags_association_1.post_id
     JOIN blog_tags AS table_tags_search_flask ON table_tags_search_flask.id = posts_tags_association_1.tag_id
     JOIN posts_tags_association AS posts_tags_association_2 ON blog_posts.id = posts_tags_association_2.post_id
     JOIN blog_tags AS table_tags_search_python ON table_tags_search_python.id = posts_tags_association_2.tag_id
     JOIN posts_tags_association AS posts_tags_association_3 ON blog_posts.id = posts_tags_association_3.post_id
     JOIN blog_tags AS table_tags_search_lesson ON table_tags_search_lesson.id = posts_tags_association_3.tag_id
     LEFT OUTER JOIN blog_authors AS blog_authors_1 ON blog_authors_1.id = blog_posts.author_id
     LEFT OUTER JOIN (posts_tags_association AS posts_tags_association_4 JOIN blog_tags AS blog_tags_1
                      ON blog_tags_1.id = posts_tags_association_4.tag_id)
                     ON blog_posts.id = posts_tags_association_4.post_id
WHERE lower(table_tags_search_flask.name) = 'flask'
  AND lower(table_tags_search_python.name) = 'python'
  AND lower(table_tags_search_lesson.name) = 'lesson'
;

SELECT id, username
FROM blog_users;

SELECT now();