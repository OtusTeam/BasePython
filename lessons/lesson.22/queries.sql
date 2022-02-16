2022-02-12 11:34:29,496 INFO sqlalchemy.engine.Engine
CREATE TABLE blog_users
(
    id         SERIAL                                      NOT NULL,
    created_at TIMESTAMP WITHOUT TIME ZONE DEFAULT now()   NOT NULL,
    username   VARCHAR(32),
    is_staff   BOOLEAN                     DEFAULT 'FALSE' NOT NULL,
    PRIMARY KEY (id),
    UNIQUE (username)
) 2022-02-12 11:34:29,496 INFO sqlalchemy.engine.Engine [no key 0.00008s] ()
2022-02-12 11:34:29,521 INFO sqlalchemy.engine.Engine
CREATE TABLE blog_tags
(
    id   SERIAL      NOT NULL,
    name VARCHAR(32) NOT NULL,
    PRIMARY KEY (id),
    UNIQUE (name)
) 2022-02-12 11:34:29,521 INFO sqlalchemy.engine.Engine [no key 0.00008s] ()
2022-02-12 11:34:29,548 INFO sqlalchemy.engine.Engine
CREATE TABLE blog_authors
(
    id         SERIAL                                    NOT NULL,
    created_at TIMESTAMP WITHOUT TIME ZONE DEFAULT now() NOT NULL,
    name       VARCHAR(64)                 DEFAULT ''    NOT NULL,
    user_id    INTEGER                                   NOT NULL,
    PRIMARY KEY (id),
    UNIQUE (user_id),
    FOREIGN KEY (user_id) REFERENCES blog_users (id)
) 2022-02-12 11:34:29,548 INFO sqlalchemy.engine.Engine [no key 0.00009s] ()
2022-02-12 11:34:29,580 INFO sqlalchemy.engine.Engine
CREATE TABLE blog_posts
(
    id         SERIAL                                      NOT NULL,
    created_at TIMESTAMP WITHOUT TIME ZONE DEFAULT now()   NOT NULL,
    title      VARCHAR(200)                DEFAULT ''      NOT NULL,
    body       TEXT                        DEFAULT ''      NOT NULL,
    status     VARCHAR(10)                 DEFAULT 'draft' NOT NULL,
    author_id  INTEGER                                     NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (author_id) REFERENCES blog_authors (id)
) 2022-02-12 11:34:29,580 INFO sqlalchemy.engine.Engine [no key 0.00037s] ()
2022-02-12 11:34:29,595 INFO sqlalchemy.engine.Engine
CREATE INDEX ix_blog_posts_author_id ON blog_posts (author_id) 2022-02-12 11:34:29,595 INFO sqlalchemy.engine.Engine [no key 0.00012s] ()
2022-02-12 11:34:29,604 INFO sqlalchemy.engine.Engine
CREATE TABLE posts_tags_association
(
    post_id INTEGER NOT NULL,
    tag_id  INTEGER NOT NULL,
    PRIMARY KEY (post_id, tag_id),
    FOREIGN KEY (post_id) REFERENCES blog_posts (id),
    FOREIGN KEY (tag_id) REFERENCES blog_tags (id)
) 2022-02-12 11:34:29,604 INFO sqlalchemy.engine.Engine [no key 0.00009s] ()
2022-02-12 11:34:29,615 INFO sqlalchemy.engine.Engine
COMMIT


--

SELECT blog_authors.id
     , blog_authors.created_at
     , blog_authors.name
     , blog_authors.user_id
FROM blog_authors
         JOIN blog_users ON blog_users.id = blog_authors.user_id
WHERE blog_users.username = 'john';


--
SELECT blog_posts.id,
       blog_posts.created_at,
       blog_posts.title,
       blog_posts.body,
       blog_posts.status,
       blog_posts.author_id,
       blog_users_1.id           AS id_1,
       blog_users_1.created_at   AS created_at_1,
       blog_users_1.username,
       blog_users_1.is_staff,
       blog_authors_1.id         AS id_2,
       blog_authors_1.created_at AS created_at_2,
       blog_authors_1.name,
       blog_authors_1.user_id
FROM blog_posts
         LEFT OUTER JOIN blog_authors AS blog_authors_1 ON blog_authors_1.id = blog_posts.author_id
         LEFT OUTER JOIN blog_users AS blog_users_1 ON blog_users_1.id = blog_authors_1.user_id;


--
SELECT blog_posts.id,
       blog_posts.created_at,
       blog_posts.title,
       blog_posts.body,
       blog_posts.status,
       blog_posts.author_id,
       blog_users_1.id           AS id_1,
       blog_users_1.created_at   AS created_at_1,
       blog_users_1.username,
       blog_users_1.is_staff,
       blog_authors_1.id         AS id_2,
       blog_authors_1.created_at AS created_at_2,
       blog_authors_1.name,
       blog_authors_1.user_id,
       blog_tags_1.id            AS id_3,
       blog_tags_1.name          AS name_1
FROM blog_posts
         LEFT OUTER JOIN blog_authors AS blog_authors_1 ON blog_authors_1.id = blog_posts.author_id
         LEFT OUTER JOIN blog_users AS blog_users_1 ON blog_users_1.id = blog_authors_1.user_id
         LEFT OUTER JOIN (posts_tags_association AS posts_tags_association_1 JOIN blog_tags AS blog_tags_1 ON blog_tags_1.id = posts_tags_association_1.tag_id)
                         ON blog_posts.id = posts_tags_association_1.post_id;


--

SELECT blog_posts_1.id AS blog_posts_1_id, blog_tags.id AS blog_tags_id, blog_tags.name AS blog_tags_name
FROM blog_posts AS blog_posts_1
         JOIN posts_tags_association AS posts_tags_association_1 ON blog_posts_1.id = posts_tags_association_1.post_id
         JOIN blog_tags ON blog_tags.id = posts_tags_association_1.tag_id
WHERE blog_posts_1.id IN (5, 6, 7, 8)
