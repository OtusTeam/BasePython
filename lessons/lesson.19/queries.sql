CREATE TABLE users
(
    id       SERIAL      NOT NULL,
    username VARCHAR(32) NOT NULL,
    email    VARCHAR,
    PRIMARY KEY (id),
    UNIQUE (username),
    UNIQUE (email)
);

-- CREATE TABLE posts
-- (
--     id           SERIAL                  NOT NULL,
--     title        VARCHAR(100) DEFAULT '' NOT NULL,
--     published_at TIMESTAMP WITHOUT TIME ZONE DEFAULT now() NOT NULL,
--     PRIMARY KEY (id)
-- );

CREATE TABLE posts
(
    id           SERIAL                                    NOT NULL,
    title        VARCHAR(100)                DEFAULT ''    NOT NULL,
    published_at TIMESTAMP WITHOUT TIME ZONE DEFAULT now() NOT NULL,
    user_id      INTEGER                                   NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (user_id) REFERENCES users (id)
);


--

SELECT users.username
     , users.email
     , users.id
FROM users
WHERE users.username = 'john'::VARCHAR
-- user username john User(id=1, username='john', email=None)
SELECT users.username
     , users.email
     , users.id
FROM users
WHERE users.username = 'sam'::VARCHAR
-- user username sam User(id=2, username='sam', email='sam@example.com')

INSERT
INTO posts (title, published_at, user_id)
SELECT p0::VARCHAR, p1::TIMESTAMP WITHOUT TIME ZONE, p2::INTEGER
FROM (VALUES ( 'MySQL Lesson':: VARCHAR
--   , %(published_at__0) s:: TIMESTAMP WITHOUT TIME ZONE
             , 1:: INTEGER
             , 0),
             ('MS SQL Intro'::
                 2)) AS imp_sen(p0, p1, p2, sen_counter)

ORDER BY sen_counter
RETURNING posts.id, posts.id AS id__1
SELECT posts.title        AS posts_title
     , posts.published_at AS posts_published_at
     , posts.user_id      AS posts_user_id
     , posts.id           AS posts_id
FROM posts
WHERE posts.id = 1::INTEGER
-- Post(id=1, title='MySQL Lesson', published_at=2024-01-30 17:52:00.242932, user_id=1)
SELECT posts.title        AS posts_title
     , posts.published_at AS posts_published_at
     , posts.user_id      AS posts_user_id
     , posts.id           AS posts_id
FROM posts
WHERE posts.id = 2::INTEGER
-- Post(id=2, title='MS SQL Intro', published_at=2024-01-30 17:52:00.242935, user_id=1)
SELECT posts.title        AS posts_title
     , posts.published_at AS posts_published_at
     , posts.user_id      AS posts_user_id
     , posts.id           AS posts_id
FROM posts
WHERE posts.id = 3::INTEGER
-- Post(id=3, title='Postgres update review', published_at=2024-01-30 17:52:00.242935, user_id=1)

-- [Post(id=1, title='MySQL Lesson', published_at=2024-01-30 17:52:00.242932, user_id=1), Post(id=2, title='MS SQL Intro', published_at=2024-01-30 17:52:00.242935, user_id=1), Post(id=3, title='Postgres update review', published_at=2024-01-30 17:52:00.242935, user_id=1)]

SELECT users.username AS users_username, users.email AS users_email, users.id AS users_id
FROM users
WHERE users.id = 2::INTEGER
-- 2024-01-30 20:52:00,255 INFO sqlalchemy.engine.Engine [cached since 0.03871s ago] {'pk_1': 2}
-- 2024-01-30 20:52:00,256 INFO sqlalchemy.engine.Engine INSERT INTO posts (title, published_at, user_id) SELECT p0::VARCHAR, p1::TIMESTAMP WITHOUT TIME ZONE, p2::INTEGER FROM (VALUES (%(title__0)s::VARCHAR, %(published_at__0)s::TIMESTAMP WITHOUT TIME ZONE, %(user_id__0)s::INTEGER, 0), (%(title__1)s::VARCHAR, %(published_at__1)s::TIMESTAMP WITHOUT TIME ZONE, %(user_id__1)s::INTEGER, 1)) AS imp_sen(p0, p1, p2, sen_counter) ORDER BY sen_counter RETURNING posts.id, posts.id AS id__1
-- 2024-01-30 20:52:00,256 INFO sqlalchemy.engine.Engine [cached since 0.01364s ago (insertmanyvalues) 1/1 (ordered)] {'title__0': 'PyCharm recent release details', 'published_at__0': datetime.datetime(2024, 1, 30, 17, 52, 0, 256526), 'user_id__0': 2, 'title__1': 'VS Code tips and tricks', 'published_at__1': datetime.datetime(2024, 1, 30, 17, 52, 0, 256529), 'user_id__1': 2}
-- 2024-01-30 20:52:00,258 INFO sqlalchemy.engine.Engine COMMIT
-- 2024-01-30 20:52:00,261 INFO sqlalchemy.engine.Engine BEGIN (implicit)
-- 2024-01-30 20:52:00,261 INFO sqlalchemy.engine.Engine SELECT posts.title AS posts_title, posts.published_at AS posts_published_at, posts.user_id AS posts_user_id, posts.id AS posts_id
-- FROM posts
-- WHERE posts.id = %(pk_1)s::INTEGER
-- 2024-01-30 20:52:00,261 INFO sqlalchemy.engine.Engine [cached since 0.01206s ago] {'pk_1': 4}
-- Post(id=4, title='PyCharm recent release details', published_at=2024-01-30 17:52:00.256526, user_id=2)
-- 2024-01-30 20:52:00,263 INFO sqlalchemy.engine.Engine SELECT posts.title AS posts_title, posts.published_at AS posts_published_at, posts.user_id AS posts_user_id, posts.id AS posts_id
-- FROM posts
-- WHERE posts.id = %(pk_1)s::INTEGER
-- 2024-01-30 20:52:00,263 INFO sqlalchemy.engine.Engine [cached since 0.01448s ago] {'pk_1': 5}
-- Post(id=5, title='VS Code tips and tricks', published_at=2024-01-30 17:52:00.256529, user_id=2)
-- [Post(id=4, title='PyCharm recent release details', published_at=2024-01-30 17:52:00.256526, user_id=2), Post(id=5, title='VS Code tips and tricks', published_at=2024-01-30 17:52:00.256529, user_id=2)]
-- 2024-01-30 20:52:00,264 INFO sqlalchemy.engine.Engine ROLLBACK


SELECT posts.title
     , posts.published_at
     , posts.user_id
     , posts.id
FROM posts
ORDER BY posts.id;

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
WHERE users.id IN (1, 2, 3);

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
WHERE posts.user_id IN (1, 2, 3, 4, 5, 6);


SELECT users.username
     , users.email
     , users.id
     , count(posts.id) AS posts_count
FROM users
         LEFT OUTER JOIN posts ON users.id = posts.user_id
GROUP BY users.id
ORDER BY users.id;

SELECT users.username
     , users.email
     , users.id
FROM users
         JOIN posts ON users.id = posts.user_id
WHERE posts.title ILIKE '%intro%'::VARCHAR
ORDER BY users.id;

SELECT users.username
     , users.email
     , users.id
FROM users
     JOIN posts ON users.id = posts.user_id
GROUP BY users.id
HAVING count(posts.id) > 1::INTEGER
ORDER BY users.id;
