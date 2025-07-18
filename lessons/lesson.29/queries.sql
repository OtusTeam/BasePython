SELECT posts.title,
       posts.body,
       posts.user_id,
       posts.created_at,
       posts.id,
       users_1.name,
       users_1.username,
       users_1.email,
       users_1.created_at AS created_at_1,
       users_1.id         AS id_1
FROM posts
         LEFT OUTER JOIN users AS users_1 ON users_1.id = posts.user_id
ORDER BY posts.title;

--

SELECT users.name
     , users.username
     , users.email
     , users.created_at
     , users.id
FROM users
ORDER BY users.id;

SELECT posts.user_id    AS posts_user_id,
       posts.title      AS posts_title,
       posts.body       AS posts_body,
       posts.created_at AS posts_created_at,
       posts.id         AS posts_id
FROM posts
WHERE posts.user_id IN (1, 2, 3, 4, 5, 6)


--

SELECT users.name
     , users.username
     , users.email
     , users.created_at
     , users.id
     , posts.id
FROM users
         JOIN posts ON users.id = posts.user_id
WHERE posts.title ILIKE '%intro%'
ORDER BY users.id;



SELECT users.name
     , users.username
     , users.email
     , users.created_at
     , users.id
FROM users
WHERE EXISTS (SELECT 1
              FROM posts
              WHERE posts.user_id = users.id
                AND posts.title ILIKE '%intro%')
ORDER BY users.id;


--

SELECT users.name
     , users.username
     , users.email
     , users.created_at
     , users.id
FROM users
WHERE EXISTS (SELECT 1
              FROM posts
              WHERE posts.user_id = users.id
                AND posts.title ILIKE '%intro%')
ORDER BY users.id


UPDATE users
SET email = username || 'email.com'
WHERE email IS NULL

--

SELECT posts.title
     , posts.body
     , posts.user_id
     , posts.created_at
     , posts.id
     , users_1.name
     , users_1.username
     , users_1.email
     , users_1.created_at AS created_at_1
     , users_1.id         AS id_1
FROM posts
         LEFT OUTER JOIN users AS users_1 ON users_1.id = posts.user_id
ORDER BY posts.title;


SELECT posts_1.id      AS posts_1_id
     , tags.name       AS tags_name
     , tags.created_at AS tags_created_at
     , tags.id         AS tags_id
FROM posts AS posts_1
         JOIN posts_tags_association AS posts_tags_association_1
              ON posts_1.id = posts_tags_association_1.post_id
         JOIN tags
              ON tags.id = posts_tags_association_1.tag_id;


---
SELECT posts.title
     , posts.body
     , posts.user_id
     , posts.created_at
     , posts.id
FROM posts
         JOIN posts_tags_association AS posts_tags_association_1 ON posts.id = posts_tags_association_1.post_id
         JOIN tags ON tags.id = posts_tags_association_1.tag_id
WHERE lower(tags.name) = 'intro'::VARCHAR
ORDER BY posts.title;

SELECT posts_1.id      AS posts_1_id
     , tags.name       AS tags_name
     , tags.created_at AS tags_created_at
     , tags.id         AS tags_id
FROM posts AS posts_1
         JOIN posts_tags_association AS posts_tags_association_1 ON posts_1.id = posts_tags_association_1.post_id
         JOIN tags ON tags.id = posts_tags_association_1.tag_id
WHERE posts_1.id IN (5, 4, 6, 1, 2);

--

SELECT posts.title
     , posts.body
     , posts.user_id
     , posts.created_at
     , posts.id
FROM posts
         JOIN posts_tags_association AS posts_tags_association_1 ON posts.id = posts_tags_association_1.post_id
         JOIN tags ON tags.id = posts_tags_association_1.tag_id
WHERE lower(tags.name) = 'intro'
ORDER BY posts.title;


SELECT tags.name       AS tags_name
     , tags.created_at AS tags_created_at
     , tags.id         AS tags_id
     , anon_1.posts_id AS anon_1_posts_id
FROM (SELECT posts.id AS posts_id
      FROM posts
               JOIN posts_tags_association AS posts_tags_association_1 ON posts.id = posts_tags_association_1.post_id
               JOIN tags ON tags.id = posts_tags_association_1.tag_id
      WHERE lower(tags.name) = 'intro') AS anon_1
         JOIN posts_tags_association AS posts_tags_association_2 ON anon_1.posts_id = posts_tags_association_2.post_id
         JOIN tags ON tags.id = posts_tags_association_2.tag_id;
