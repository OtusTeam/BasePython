BEGIN;

-- INFO  [alembic.runtime.migration] Running upgrade 02efe881123b -> 03dff9349f46, make email column not null
-- Running upgrade 02efe881123b -> 03dff9349f46

UPDATE users
SET email=(users.username || '@invalid.mail')
WHERE users.email IS NULL;

ALTER TABLE users
    ALTER COLUMN email
        SET NOT NULL;

UPDATE alembic_version
SET version_num='03dff9349f46'
WHERE alembic_version.version_num = '02efe881123b';

COMMIT;

---

BEGIN;

-- INFO  [alembic.runtime.migration] Running downgrade 03dff9349f46 -> 02efe881123b, make email column not null
-- Running downgrade 03dff9349f46 -> 02efe881123b

ALTER TABLE users
    ALTER COLUMN email DROP NOT NULL;

UPDATE alembic_version
SET version_num='02efe881123b'
WHERE alembic_version.version_num = '03dff9349f46';

COMMIT;

--

INSERT INTO posts (title, body, user_id)
VALUES ('Post by user #1 (python | sqlalchemy | tutorial)', '')
-- {'body__0': '', 'title__0': 'Post by user #1 (python | sqlalchemy | tutorial)', 'user_id__0': 1, 'body__1': '', 'title__1': 'Post by user #3 (python | web | tutorial)', 'user_id__1': 3, 'body__2': '', 'title__2': 'Post by user #4 (web | ops | data | python)', 'user_id__2': 4, 'body__3': '', 'title__3': 'Post by user #1 (sqlalchemy | data | python)', 'user_id__3': 1, 'body__4': '', 'title__4': 'Post by user #3 (ops | web | tutorial)', 'user_id__4': 3, 'body__5': '', 'title__5': 'Post by user #4 (data | python | sqlalchemy)', 'user_id__5': 4, 'body__6': '', 'title__6': 'Post by user #1 (web | tutorial | ops)', 'user_id__6': 1}

INSERT INTO posts_tags_association
    (post_id, tag_name)
VALUES (16, 'web'),
       (16, 'tutorial');
-- [{'post_id': 16, 'tag_name': 'web'}, {'post_id': 16, 'tag_name': 'tutorial'}, {'post_id': 16, 'tag_name': 'ops'}, {'post_id': 10, 'tag_name': 'python'}, {'post_id': 10, 'tag_name': 'sqlalchemy'}, {'post_id': 10, 'tag_name': 'tutorial'}, {'post_id': 14, 'tag_name': 'ops'}, {'post_id': 14, 'tag_name': 'web'}  ... displaying 10 of 22 total bound parameter sets ...  {'post_id': 13, 'tag_name': 'data'}, {'post_id': 13, 'tag_name': 'python'}]


--

SELECT posts.title
     , posts.body
     , posts.user_id
     , posts.id
     , posts.created_at
FROM posts
ORDER BY posts.id;


SELECT posts_1.id       AS posts_1_id
     , tags.name        AS tags_name
     , tags.description AS tags_description
FROM posts AS posts_1
         JOIN posts_tags_association AS posts_tags_association_1
              ON posts_1.id = posts_tags_association_1.post_id
         JOIN tags
              ON tags.name = posts_tags_association_1.tag_name
WHERE posts_1.id IN (1, 2, 3, 11, 12, 13);


--

SELECT tags.name        AS tags_name
     , tags.description AS tags_description
     , anon_1.posts_id  AS anon_1_posts_id
FROM (SELECT posts.id AS posts_id
      FROM posts
      where posts.id IN (1, 2, 3, 11, 12, 13)) AS anon_1
         JOIN posts_tags_association AS posts_tags_association_1
              ON anon_1.posts_id = posts_tags_association_1.post_id
         JOIN tags
              ON tags.name = posts_tags_association_1.tag_name


--

SELECT users.username
     , users.email
     , users.full_name
     , users.id
FROM users
     JOIN posts ON users.id = posts.user_id
     JOIN posts_tags_association AS posts_tags_association_1 ON posts.id = posts_tags_association_1.post_id
     JOIN tags ON tags.name = posts_tags_association_1.tag_name
WHERE tags.name = 'python'
ORDER BY users.id;


SELECT posts.user_id    AS posts_user_id
     , posts.title      AS posts_title
     , posts.body       AS posts_body
     , posts.id         AS posts_id
     , posts.created_at AS posts_created_at
FROM posts,
     posts_tags_association AS posts_tags_association_1,
     tags
WHERE posts.user_id IN (1, 3, 4)
  AND posts.id = posts_tags_association_1.post_id
  AND tags.name = posts_tags_association_1.tag_name
  AND tags.name = 'python';

SELECT posts_1.id       AS posts_1_id
     , tags.name        AS tags_name
     , tags.description AS tags_description
FROM posts AS posts_1
         JOIN posts_tags_association AS posts_tags_association_1 ON posts_1.id = posts_tags_association_1.post_id
         JOIN tags ON tags.name = posts_tags_association_1.tag_name
WHERE posts_1.id IN (46, 50, 48, 47, 45)
