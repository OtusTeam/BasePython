-- get tags w/ posts
SELECT tags.name
     , tags.id
FROM tags
ORDER BY tags.id;

SELECT tags_1.id          AS tags_1_id
     , posts.title        AS posts_title
     , posts.published_at AS posts_published_at
     , posts.user_id      AS posts_user_id
     , posts.id           AS posts_id
FROM tags AS tags_1
         JOIN posts_tags_association AS posts_tags_association_1 ON tags_1.id = posts_tags_association_1.tag_id
         JOIN posts ON posts.id = posts_tags_association_1.post_id
WHERE tags_1.id IN (1, 2, 4, 5, 6, 7, 8, 9);

-- get posts w/ tags

SELECT posts.title
     , posts.published_at
     , posts.user_id
     , posts.id
FROM posts
ORDER BY posts.id;

SELECT posts_1.id AS posts_1_id
     , tags.name  AS tags_name
     , tags.id    AS tags_id
FROM posts AS posts_1
         JOIN posts_tags_association AS posts_tags_association_1 ON posts_1.id = posts_tags_association_1.post_id
         JOIN tags ON tags.id = posts_tags_association_1.tag_id
WHERE posts_1.id IN (1, 2, 3, 4, 5, 6);

-- update: associate tags w/ posts

INSERT
INTO posts_tags_association (post_id, tag_id)
VALUES (4, 5),
       (4, 6),
       (4, 8),
       (5, 6);


--
SELECT users.username
     , posts.title
     , tags.name
FROM users
         JOIN posts
              ON users.id = posts.user_id
         JOIN posts_tags_association AS posts_tags_association_1
              ON posts.id = posts_tags_association_1.post_id
         JOIN tags
              ON tags.id = posts_tags_association_1.tag_id
WHERE lower(tags.name) = 'sql'::VARCHAR
ORDER BY users.id;


SELECT posts.title
     , posts.id
     , posts.user_id
     , tags.name
FROM posts
         JOIN posts_tags_association AS posts_tags_association_1
              ON posts.id = posts_tags_association_1.post_id
         JOIN tags
              ON tags.id = posts_tags_association_1.tag_id
WHERE lower(tags.name) = 'sql'::VARCHAR
ORDER BY posts.id;



SELECT DISTINCT posts.user_id
FROM posts
         JOIN posts_tags_association AS posts_tags_association_1
              ON posts.id = posts_tags_association_1.post_id
         JOIN tags
              ON tags.id = posts_tags_association_1.tag_id
WHERE lower(tags.name) = 'sql'::VARCHAR;


SELECT users.id
     , users.username

FROM users
WHERE users.id IN (SELECT DISTINCT posts.user_id
                   FROM posts
                            JOIN posts_tags_association AS posts_tags_association_1
                                 ON posts.id = posts_tags_association_1.post_id
                            JOIN tags
                                 ON tags.id = posts_tags_association_1.tag_id
                   WHERE lower(tags.name) = 'sql'::VARCHAR);


--
SELECT users.username
     , users.id
FROM users
WHERE users.id IN (SELECT anon_2.anon_1
                   FROM (SELECT DISTINCT posts.user_id AS anon_1
                         FROM posts
                                  JOIN posts_tags_association AS posts_tags_association_1
                                       ON posts.id = posts_tags_association_1.post_id
                                  JOIN tags
                                       ON tags.id = posts_tags_association_1.tag_id
                         WHERE lower(tags.name) = 'sql'::VARCHAR) AS anon_2)
ORDER BY users.id;


--
SELECT posts.title
     , posts.published_at
     , posts.user_id
     , posts.id
     , t.name t1
     , t.name t2
FROM posts
         JOIN posts_tags_association AS posts_tags_association_1 ON posts.id = posts_tags_association_1.post_id
         JOIN tags t ON t.id = posts_tags_association_1.tag_id
         JOIN tags t2 ON t.id = posts_tags_association_1.tag_id
WHERE lower(t.name) IN ('mysql', 'sql', 'news')
-- WHERE lower(tags.name) = 'mysql'
--   OR lower(tags.name) = 'sql'
ORDER BY posts.id;


SELECT posts_1.id AS posts_1_id
     , tags.name  AS tags_name
     , tags.id    AS tags_id
FROM posts AS posts_1
         JOIN posts_tags_association AS posts_tags_association_1 ON posts_1.id = posts_tags_association_1.post_id
         JOIN tags ON tags.id = posts_tags_association_1.tag_id
WHERE posts_1.id IN (2, 3, 4, 5, 6);


SELECT posts.title
     , posts.published_at
     , posts.user_id
     , posts.id
     , table_tags1.name as t1
     , table_tags2.name as t2
FROM posts
         JOIN posts_tags_association AS posts_tags_association_1 ON posts.id = posts_tags_association_1.post_id
         JOIN tags AS table_tags1 ON table_tags1.id = posts_tags_association_1.tag_id
         JOIN posts_tags_association AS posts_tags_association_2 ON posts.id = posts_tags_association_2.post_id
         JOIN tags AS table_tags2 ON table_tags2.id = posts_tags_association_2.tag_id
WHERE lower(table_tags1.name) = 'sql'::VARCHAR
  AND lower(table_tags2.name) = 'mysql'::VARCHAR
ORDER BY posts.id
