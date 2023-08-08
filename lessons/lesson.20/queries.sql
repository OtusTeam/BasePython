SELECT posts.id           AS posts_id,
       posts.created_at   AS posts_created_at,
       posts.title        AS posts_title,
       posts.body         AS posts_body,
       posts.published_at AS posts_published_at,
       posts.user_id      AS posts_user_id
FROM posts
ORDER BY posts.id;


SELECT posts_1.id      AS posts_1_id
     , tags.id         AS tags_id
     , tags.created_at AS tags_created_at
     , tags.name       AS tags_name
FROM posts AS posts_1
         JOIN posts_tags_association AS posts_tags_association_1
              ON posts_1.id = posts_tags_association_1.post_id
         JOIN tags
              ON tags.id = posts_tags_association_1.tag_id
WHERE posts_1.id IN (1, 2, 3, 4, 5);

--
SELECT posts.id           AS posts_id,
       posts.created_at   AS posts_created_at,
       posts.title        AS posts_title,
       posts.body         AS posts_body,
       posts.published_at AS posts_published_at,
       posts.user_id      AS posts_user_id
FROM posts
ORDER BY posts.id;

SELECT posts_1.id      AS posts_1_id
     , tags.id         AS tags_id
     , tags.created_at AS tags_created_at
     , tags.name       AS tags_name
FROM posts AS posts_1
         JOIN posts_tags_association AS posts_tags_association_1
              ON posts_1.id = posts_tags_association_1.post_id
         JOIN tags
              ON tags.id = posts_tags_association_1.tag_id
WHERE posts_1.id IN (1, 2, 3, 4, 5);

SELECT tags.id         AS tags_id
     , tags.created_at AS tags_created_at
     , tags.name       AS tags_name
FROM tags
ORDER BY tags.id;

INSERT INTO posts_tags_association (post_id, tag_id)
VALUES (4, 1),
       (4, 4),
       (2, 1),
       (2, 2),
       (5, 5),
       (3, 1),
       (3, 3),
       (1, 6);

-- COMMIT;
-- BEGIN
SELECT posts.id           AS posts_id,
       posts.created_at   AS posts_created_at,
       posts.title        AS posts_title,
       posts.body         AS posts_body,
       posts.published_at AS posts_published_at,
       posts.user_id      AS posts_user_id
FROM posts
ORDER BY posts.id;

SELECT posts_1.id      AS posts_1_id
     , tags.id         AS tags_id
     , tags.created_at AS tags_created_at
     , tags.name       AS tags_name
FROM posts AS posts_1
         JOIN posts_tags_association AS posts_tags_association_1
              ON posts_1.id = posts_tags_association_1.post_id
         JOIN tags
              ON tags.id = posts_tags_association_1.tag_id
WHERE posts_1.id IN (1, 2, 3, 4, 5);


--

SELECT users.id       AS users_id
--      , users.created_at AS users_created_at
     , users.username AS users_username
--      , users.email      AS users_email
--      , users.is_staff   AS users_is_staff
--      , users.bio        AS users_bio
     , tags.id        AS tag_id
     , tags.name      AS tag_name
     , posts.id       AS post_id
FROM users
         JOIN posts
              ON users.id = posts.user_id
         JOIN posts_tags_association AS posts_tags_association_1
              ON posts.id = posts_tags_association_1.post_id
         JOIN tags
              ON tags.id = posts_tags_association_1.tag_id
WHERE lower(tags.name) IN ('python', 'js');

--

SELECT users.id             AS users_id
     , users.created_at     AS users_created_at
     , users.username       AS users_username
     , users.email          AS users_email
     , users.is_staff       AS users_is_staff
     , users.bio            AS users_bio
     , posts_1.id           AS posts_1_id
     , posts_1.created_at   AS posts_1_created_at
     , posts_1.title        AS posts_1_title
     , posts_1.body         AS posts_1_body
     , posts_1.published_at AS posts_1_published_at
     , posts_1.user_id      AS posts_1_user_id
FROM users
         JOIN posts
              ON users.id = posts.user_id
         JOIN posts_tags_association AS posts_tags_association_1
              ON posts.id = posts_tags_association_1.post_id
         JOIN tags
              ON tags.id = posts_tags_association_1.tag_id
         LEFT OUTER JOIN posts AS posts_1
                         ON users.id = posts_1.user_id
WHERE lower(tags.name) IN ('python', 'js')
ORDER BY users.id;

--

SELECT posts_1.id      AS posts_1_id
     , tags.id         AS tags_id
     , tags.created_at AS tags_created_at
     , tags.name       AS tags_name
FROM posts AS posts_1
         JOIN posts_tags_association AS posts_tags_association_1
              ON posts_1.id = posts_tags_association_1.post_id
         JOIN tags
              ON tags.id = posts_tags_association_1.tag_id
WHERE posts_1.id IN (2, 3, 4, 5)
----