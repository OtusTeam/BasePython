INSERT INTO posts_tags_association (post_id, tag_id)
VALUES (3, 4),
       (3, 5),
       (2, 8),
       (2, 10);


--

SELECT posts_1.id AS posts_1_id
     , tags.name  AS tags_name
     , tags.id    AS tags_id
FROM posts AS posts_1
         JOIN posts_tags_association AS posts_tags_association_1 ON posts_1.id = posts_tags_association_1.post_id
         JOIN tags ON tags.id = posts_tags_association_1.tag_id
WHERE posts_1.id IN (1,
                     2,
                     3,
                     4,
                     5,
                     6);

--

SELECT posts.title
     , posts.published_at
     , posts.user_id
     , posts.id
FROM posts
         JOIN posts_tags_association AS posts_tags_association_1 ON posts.id = posts_tags_association_1.post_id
         JOIN tags ON tags.id = posts_tags_association_1.tag_id
WHERE lower(tags.name) = 'sql'::VARCHAR
ORDER BY posts.id;

SELECT posts_1.id AS posts_1_id
     , tags.name  AS tags_name
     , tags.id    AS tags_id
FROM posts AS posts_1
         JOIN posts_tags_association AS posts_tags_association_1 ON posts_1.id = posts_tags_association_1.post_id
         JOIN tags ON tags.id = posts_tags_association_1.tag_id
WHERE posts_1.id IN (1, 2, 3);


--
SELECT users.username
     , users.email
     , users.full_name
     , users.ref_code
     , users.id
FROM users
         JOIN posts
              ON users.id = posts.user_id
         JOIN posts_tags_association AS posts_tags_association_1
              ON posts.id = posts_tags_association_1.post_id
         JOIN tags
              ON tags.id = posts_tags_association_1.tag_id
-- WHERE lower(tags.name) = 'sql'::VARCHAR
ORDER BY users.id;


SELECT DISTINCT posts.user_id
FROM posts
         JOIN posts_tags_association AS posts_tags_association_1
              ON posts.id = posts_tags_association_1.post_id
         JOIN tags
              ON tags.id = posts_tags_association_1.tag_id
WHERE lower(tags.name) = 'sql'::VARCHAR;


--

SELECT users.username
     , users.email
     , users.full_name
     , users.ref_code
     , users.id
FROM users
WHERE users.id IN (SELECT anon_2.anon_1
                   FROM (SELECT DISTINCT posts.user_id AS anon_1
                         FROM posts
                                  JOIN posts_tags_association AS posts_tags_association_1
                                       ON posts.id = posts_tags_association_1.post_id
                                  JOIN tags ON tags.id = posts_tags_association_1.tag_id
                         WHERE lower(tags.name) = 'sql'::VARCHAR) AS anon_2)
ORDER BY users.id


--

SELECT posts.title
     , posts.published_at
     , posts.user_id
     , posts.id
     , tags.name
FROM posts
         JOIN posts_tags_association AS posts_tags_association_1 ON posts.id = posts_tags_association_1.post_id
         JOIN tags ON tags.id = posts_tags_association_1.tag_id
WHERE lower(tags.name) IN ('lesson'::VARCHAR, 'python'::VARCHAR)
ORDER BY posts.id;


SELECT posts_1.id AS posts_1_id
     , tags.name  AS tags_name
     , tags.id    AS tags_id
FROM posts AS posts_1
         JOIN posts_tags_association AS posts_tags_association_1 ON posts_1.id = posts_tags_association_1.post_id
         JOIN tags ON tags.id = posts_tags_association_1.tag_id
WHERE posts_1.id IN (1, 2, 3, 4, 5, 6)
ORDER BY tags.id;


SELECT posts.title
     , posts.published_at
     , posts.user_id
     , posts.id
     , table_tags1.id
     , table_tags1.name
     , table_tags2.id
     , table_tags2.name
FROM posts
         JOIN posts_tags_association AS posts_tags_association_1 ON posts.id = posts_tags_association_1.post_id
         JOIN tags AS table_tags1 ON table_tags1.id = posts_tags_association_1.tag_id
         JOIN posts_tags_association AS posts_tags_association_2 ON posts.id = posts_tags_association_2.post_id
         JOIN tags AS table_tags2 ON table_tags2.id = posts_tags_association_2.tag_id
WHERE lower(table_tags1.name) = 'lesson'::VARCHAR
  AND lower(table_tags2.name) = 'python'::VARCHAR
ORDER BY posts.id;

SELECT posts.title
     , posts.published_at
     , posts.user_id
     , posts.id
     , table_tags_for_sql.name
     , table_tags_for_postgres.name
     , table_tags_for_news.name
FROM posts
         JOIN posts_tags_association AS posts_tags_association_1
              ON posts.id = posts_tags_association_1.post_id
         JOIN tags AS table_tags_for_sql
              ON table_tags_for_sql.id = posts_tags_association_1.tag_id
         JOIN posts_tags_association AS posts_tags_association_2
              ON posts.id = posts_tags_association_2.post_id
         JOIN tags AS table_tags_for_postgres
              ON table_tags_for_postgres.id = posts_tags_association_2.tag_id
         JOIN posts_tags_association AS posts_tags_association_3
              ON posts.id = posts_tags_association_3.post_id
         JOIN tags AS table_tags_for_news
              ON table_tags_for_news.id = posts_tags_association_3.tag_id
WHERE lower(table_tags_for_sql.name) = 'sql'
  AND lower(table_tags_for_postgres.name) = 'postgres'
  AND lower(table_tags_for_news.name) = 'news'
ORDER BY posts.id
