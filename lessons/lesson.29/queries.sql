SELECT users.username
     , users.email
     , users.full_name
     , users.id
FROM users
ORDER BY users.username;


SELECT posts.user_id AS posts_user_id
     , posts.title   AS posts_title
     , posts.content AS posts_content
     , posts.id      AS posts_id
FROM posts
WHERE posts.user_id IN (3, 2, 1);


SELECT posts_1.id        AS posts_1_id
     , tags.slug         AS tags_slug
     , tags.display_name AS tags_display_name
     , tags.id           AS tags_id
FROM posts AS posts_1
         JOIN posts_tags_association AS posts_tags_association_1 ON posts_1.id = posts_tags_association_1.post_id
         JOIN tags ON tags.id = posts_tags_association_1.tag_id;


SELECT users.username
     , users.email
     , users.full_name
     , users.id
FROM users
WHERE length(users.username) > 3
ORDER BY users.username;

SELECT users.username
     -- , users.email
     -- , users.full_name
     , users.id
     , posts.title
FROM users
     JOIN posts ON users.id = posts.user_id
WHERE length(users.username) > 3
  AND posts.title ILIKE '%news%'
ORDER BY users.username