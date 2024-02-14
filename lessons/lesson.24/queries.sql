SELECT users.username
     , users.email
     , users.full_name
     , users.token
     , users.created_at
     , users.id
FROM users
-- WHERE length(username) > 3
ORDER BY users.id;


SELECT users.username
     , users.email
     , users.full_name
     , users.token
     , users.created_at
     , users.id
FROM users
WHERE length(username) > 3
ORDER BY users.id
OFFSET 2 LIMIT 5;


SELECT count(*) AS count_1
FROM (SELECT users.username
           , users.email
           , users.full_name
           , users.token
           , users.created_at
           , users.id
      FROM users
      WHERE length(username) > 3) AS anon_1


--

SELECT posts.title
--      , posts.published_at
--      , posts.created_at
     , tags.name
     , posts.id
FROM posts
         JOIN posts_tags_association AS posts_tags_association_1
              ON posts.id = posts_tags_association_1.post_id
         JOIN tags
              ON tags.id = posts_tags_association_1.tag_id
-- WHERE lower(tags.name) = 'code-editors'::VARCHAR
--   AND lower(tags.name) = 'news'::VARCHAR
ORDER BY posts.id;

SELECT posts.title
--      , posts.published_at
--      , posts.created_at
--      , posts.user_id
     , table_tags_1.name
     , table_tags_2.name
     , posts.id
FROM posts
         JOIN posts_tags_association AS posts_tags_association_1
              ON posts.id = posts_tags_association_1.post_id
         JOIN tags AS table_tags_1
              ON table_tags_1.id = posts_tags_association_1.tag_id
         JOIN posts_tags_association AS posts_tags_association_2
              ON posts.id = posts_tags_association_2.post_id
         JOIN tags AS table_tags_2
              ON table_tags_2.id = posts_tags_association_2.tag_id
WHERE lower(table_tags_1.name) = 'code-editors'::VARCHAR
  AND lower(table_tags_2.name) = 'news'::VARCHAR
ORDER BY posts.id;


SELECT posts.title
     , posts.published_at
     , posts.created_at
     , posts.user_id
     , posts.id
FROM posts
         JOIN posts_tags_association AS posts_tags_association_1
              ON posts.id = posts_tags_association_1.post_id
         JOIN tags AS tags_news
              ON tags_news.id = posts_tags_association_1.tag_id
         JOIN posts_tags_association AS posts_tags_association_2
              ON posts.id = posts_tags_association_2.post_id
         JOIN tags AS "tags_ms sql"
              ON "tags_ms sql".id = posts_tags_association_2.tag_id
         JOIN posts_tags_association AS posts_tags_association_3
              ON posts.id = posts_tags_association_3.post_id
         JOIN tags AS tags_postgres
              ON tags_postgres.id = posts_tags_association_3.tag_id
WHERE lower(tags_news.name) = 'news'::VARCHAR
  AND lower("tags_ms sql".name) = 'ms sql'::VARCHAR
  AND lower(tags_postgres.name) = 'postgres'::VARCHAR
ORDER BY posts.id
