SELECT posts.title
     , posts.published_at
     , posts.created_at
     , posts.user_id
     , posts.id
FROM posts
ORDER BY posts.id;

SELECT posts_1.id      AS posts_1_id
     , tags.name       AS tags_name
     , tags.created_at AS tags_created_at
     , tags.id         AS tags_id
FROM posts AS posts_1
         JOIN posts_tags_association AS posts_tags_association_1
              ON posts_1.id = posts_tags_association_1.post_id
         JOIN tags
              ON tags.id = posts_tags_association_1.tag_id
WHERE posts_1.id IN (1, 2, 3, 4, 5);

--
SELECT posts.title
     , posts.user_id
     , posts.id
     , tags.name
FROM posts
         JOIN posts_tags_association AS posts_tags_association_1
              ON posts.id = posts_tags_association_1.post_id
         JOIN tags
              ON tags.id = posts_tags_association_1.tag_id
WHERE tags.name = 'news'::VARCHAR;

--
SELECT users.username
     , users.email
     , users.full_name
     , users.id
FROM users
         JOIN posts
              ON users.id = posts.user_id
         JOIN posts_tags_association AS posts_tags_association_1
              ON posts.id = posts_tags_association_1.post_id
         JOIN tags
              ON tags.id = posts_tags_association_1.tag_id
WHERE tags.name = 'news';


SELECT users.username
     , users.email
     , users.full_name
     , users.id
FROM users
         JOIN posts
              ON users.id = posts.user_id
         JOIN posts_tags_association AS posts_tags_association_1
              ON posts.id = posts_tags_association_1.post_id
         JOIN tags
              ON tags.id = posts_tags_association_1.tag_id
WHERE tags.name = 'news'::VARCHAR
GROUP BY users.username
       , users.email
       , users.full_name
       , users.id;
