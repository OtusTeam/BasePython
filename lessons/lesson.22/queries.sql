-- UPGRADE

-- ➜ alembic upgrade --sql 4fb7:3a8585
BEGIN;

-- INFO  [alembic.runtime.migration] Running upgrade 4fb730957be6 -> e9dbb556d516, upgrade users: add archived column
-- Running upgrade 4fb730957be6 -> e9dbb556d516

ALTER TABLE blog_users
    ADD COLUMN archived BOOLEAN DEFAULT false NOT NULL;

UPDATE alembic_version
SET version_num='e9dbb556d516'
WHERE alembic_version.version_num = '4fb730957be6';

-- INFO  [alembic.runtime.migration] Running upgrade e9dbb556d516 -> 3a8585c93e66, upgrade users: add created_at column
-- Running upgrade e9dbb556d516 -> 3a8585c93e66

ALTER TABLE blog_users
    ADD COLUMN created_at TIMESTAMP WITHOUT TIME ZONE DEFAULT now() NOT NULL;

UPDATE alembic_version
SET version_num='3a8585c93e66'
WHERE alembic_version.version_num = 'e9dbb556d516';

COMMIT;


-- DOWNGRADE


-- ➜ alembic downgrade --sql 3a8585:4fb7
BEGIN;

-- INFO  [alembic.runtime.migration] Running downgrade 3a8585c93e66 -> e9dbb556d516, upgrade users: add created_at column
-- Running downgrade 3a8585c93e66 -> e9dbb556d516

ALTER TABLE blog_users DROP COLUMN created_at;

UPDATE alembic_version
SET version_num='e9dbb556d516'
WHERE alembic_version.version_num = '3a8585c93e66';

-- INFO  [alembic.runtime.migration] Running downgrade e9dbb556d516 -> 4fb730957be6, upgrade users: add archived column
-- Running downgrade e9dbb556d516 -> 4fb730957be6

ALTER TABLE blog_users DROP COLUMN archived;

UPDATE alembic_version
SET version_num='4fb730957be6'
WHERE alembic_version.version_num = 'e9dbb556d516';

COMMIT;


-- update

BEGIN;

-- Running upgrade c0856bbe4253 -> c25b4a0ef56d

ALTER TABLE blog_authors
    ADD COLUMN bio VARCHAR DEFAULT '' NOT NULL;

UPDATE blog_authors
SET bio=blog_users.bio FROM blog_users
WHERE blog_authors.user_id = blog_users.id;

UPDATE alembic_version
SET version_num='c25b4a0ef56d'
WHERE alembic_version.version_num = 'c0856bbe4253';

COMMIT;


--


SELECT blog_posts.created_at     AS blog_posts_created_at,
       blog_posts.title          AS blog_posts_title,
       blog_posts.body           AS blog_posts_body,
       blog_posts.author_id      AS blog_posts_author_id,
       blog_posts.id             AS blog_posts_id,
       blog_authors_1.created_at AS blog_authors_1_created_at,
       blog_authors_1.name       AS blog_authors_1_name,
       blog_authors_1.bio        AS blog_authors_1_bio,
       blog_authors_1.user_id    AS blog_authors_1_user_id,
       blog_authors_1.id         AS blog_authors_1_id
FROM blog_posts
         JOIN blog_posts_tags_association AS blog_posts_tags_association_1
              ON blog_posts.id = blog_posts_tags_association_1.post_id
         JOIN blog_tags ON blog_tags.id = blog_posts_tags_association_1.tag_id
         LEFT OUTER JOIN blog_authors AS blog_authors_1 ON blog_authors_1.id = blog_posts.author_id
WHERE lower(blog_tags.name) IN ('pycharm', 'mysql')
ORDER BY blog_posts.title;

SELECT blog_posts_1.id      AS blog_posts_1_id,
       blog_tags.created_at AS blog_tags_created_at,
       blog_tags.name       AS blog_tags_name,
       blog_tags.id         AS blog_tags_id
FROM blog_posts AS blog_posts_1
         JOIN blog_posts_tags_association AS blog_posts_tags_association_1
              ON blog_posts_1.id = blog_posts_tags_association_1.post_id
         JOIN blog_tags ON blog_tags.id = blog_posts_tags_association_1.tag_id
WHERE blog_posts_1.id IN 4, 1);


--
SELECT blog_posts.created_at AS blog_posts_created_at,
       blog_posts.title      AS blog_posts_title,
       blog_posts.body       AS blog_posts_body,
       blog_posts.author_id  AS blog_posts_author_id,
       blog_posts.id         AS blog_posts_id
FROM blog_posts
WHERE (lower(blog_posts.title) LIKE '%mysql%')
   OR (lower(blog_posts.title) LIKE '%postgres%')
ORDER BY blog_posts.id


--

SELECT blog_posts.created_at AS blog_posts_created_at,
       blog_posts.title      AS blog_posts_title,
       blog_posts.body       AS blog_posts_body,
       blog_posts.author_id  AS blog_posts_author_id,
       blog_posts.id         AS blog_posts_id
FROM blog_posts
         JOIN blog_posts_tags_association AS blog_posts_tags_association_1
              ON blog_posts.id = blog_posts_tags_association_1.post_id
         JOIN blog_tags AS table_tags_database ON table_tags_database.id = blog_posts_tags_association_1.tag_id
         JOIN blog_posts_tags_association AS blog_posts_tags_association_2
              ON blog_posts.id = blog_posts_tags_association_2.post_id
         JOIN blog_tags AS table_tags_tutorial ON table_tags_tutorial.id = blog_posts_tags_association_2.tag_id
         JOIN blog_posts_tags_association AS blog_posts_tags_association_3
              ON blog_posts.id = blog_posts_tags_association_3.post_id
         JOIN blog_tags AS table_tags_mysql ON table_tags_mysql.id = blog_posts_tags_association_3.tag_id
WHERE lower(table_tags_database.name) = 'database'
  AND lower(table_tags_tutorial.name) = 'tutorial'
  AND lower(table_tags_mysql.name) = 'mysql'
ORDER BY blog_posts.id;


SELECT blog_posts_1.id      AS blog_posts_1_id,
       blog_tags.created_at AS blog_tags_created_at,
       blog_tags.name       AS blog_tags_name,
       blog_tags.id         AS blog_tags_id
FROM blog_posts AS blog_posts_1
         JOIN blog_posts_tags_association AS blog_posts_tags_association_1
              ON blog_posts_1.id = blog_posts_tags_association_1.post_id
         JOIN blog_tags ON blog_tags.id = blog_posts_tags_association_1.tag_id
WHERE blog_posts_1.id IN (4)

--

SELECT blog_posts.created_at,
       blog_posts.title,
       blog_posts.body,
       blog_posts.author_id,
       blog_posts.id,
       blog_authors_1.created_at AS created_at_1,
       blog_authors_1.name,
       blog_authors_1.bio,
       blog_authors_1.user_id,
       blog_authors_1.id         AS id_1
FROM blog_posts
         JOIN blog_posts_tags_association AS blog_posts_tags_association_1
              ON blog_posts.id = blog_posts_tags_association_1.post_id
         JOIN blog_tags ON blog_tags.id = blog_posts_tags_association_1.tag_id
         LEFT OUTER JOIN blog_authors AS blog_authors_1 ON blog_authors_1.id = blog_posts.author_id
WHERE lower(blog_tags.name) IN ('tutorial', 'mysql', 'database', 'python');

SELECT blog_posts_1.id      AS blog_posts_1_id,
       blog_tags.created_at AS blog_tags_created_at,
       blog_tags.name       AS blog_tags_name,
       blog_tags.id         AS blog_tags_id
FROM blog_posts AS blog_posts_1
         JOIN blog_posts_tags_association AS blog_posts_tags_association_1
              ON blog_posts_1.id = blog_posts_tags_association_1.post_id
         JOIN blog_tags ON blog_tags.id = blog_posts_tags_association_1.tag_id
WHERE blog_posts_1.id IN (4, 5, 3, 2);

--
SELECT DISTINCT blog_posts.created_at,
                blog_posts.title,
                blog_posts.body,
                blog_posts.author_id,
                blog_posts.id,
                blog_authors_1.created_at AS created_at_1,
                blog_authors_1.name,
                blog_authors_1.bio,
                blog_authors_1.user_id,
                blog_authors_1.id         AS id_1
FROM blog_posts
         JOIN blog_posts_tags_association AS blog_posts_tags_association_1
              ON blog_posts.id = blog_posts_tags_association_1.post_id
         JOIN blog_tags ON blog_tags.id = blog_posts_tags_association_1.tag_id
         LEFT OUTER JOIN blog_authors AS blog_authors_1 ON blog_authors_1.id = blog_posts.author_id
WHERE lower(blog_tags.name) IN ('tutorial', 'mysql', 'database');