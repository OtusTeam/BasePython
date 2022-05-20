SELECT posts.id          AS posts_id,
       posts.created_at  AS posts_created_at,
       posts.title       AS posts_title,
       posts.body        AS posts_body,
       posts.author_id   AS posts_author_id,
       tags_1.id         AS tags_1_id,
       tags_1.created_at AS tags_1_created_at,
       tags_1.name       AS tags_1_name
FROM posts
         LEFT OUTER JOIN (
    posts_tags_association AS posts_tags_association_1
        JOIN tags AS tags_1
    ON tags_1.id = posts_tags_association_1.tag_id
    ) ON posts.id = posts_tags_association_1.post_id;


SELECT *
FROM posts_tags_association AS posts_tags_association_1
         JOIN tags AS tags_1
              ON tags_1.id = posts_tags_association_1.tag_id;


--

SELECT posts.id         AS posts_id,
       posts.created_at AS posts_created_at,
       posts.title      AS posts_title,
       posts.body       AS posts_body,
       posts.author_id  AS posts_author_id
FROM posts;


SELECT posts_1.id      AS posts_1_id
     , tags.id         AS tags_id
     , tags.created_at AS tags_created_at
     , tags.name       AS tags_name
FROM posts AS posts_1
         JOIN posts_tags_association AS posts_tags_association_1
              ON posts_1.id = posts_tags_association_1.post_id
         JOIN tags ON tags.id = posts_tags_association_1.tag_id
WHERE posts_1.id IN (1, 2, 5, 6, 7);


--

SELECT tags.id            AS tags_id,
       tags.created_at    AS tags_created_at,
       tags.name          AS tags_name,
       posts_1.id         AS posts_1_id,
       posts_1.created_at AS posts_1_created_at,
       posts_1.title      AS posts_1_title,
       posts_1.body       AS posts_1_body,
       posts_1.author_id  AS posts_1_author_id
FROM tags
         LEFT OUTER JOIN (
    posts_tags_association AS posts_tags_association_1 JOIN posts AS posts_1
    ON posts_1.id = posts_tags_association_1.post_id)
                         ON tags.id = posts_tags_association_1.tag_id;

--

SELECT users.id             AS users_id,
       users.created_at     AS users_created_at,
       users.username       AS users_username,
       users.is_staff       AS users_is_staff,
       tags_1.id            AS tags_1_id,
       tags_1.created_at    AS tags_1_created_at,
       tags_1.name          AS tags_1_name,
       posts_1.id           AS posts_1_id,
       posts_1.created_at   AS posts_1_created_at,
       posts_1.title        AS posts_1_title,
       posts_1.body         AS posts_1_body,
       posts_1.author_id    AS posts_1_author_id,
       authors_1.id         AS authors_1_id,
       authors_1.created_at AS authors_1_created_at,
       authors_1.name       AS authors_1_name,
       authors_1.user_id    AS authors_1_user_id
FROM users
         JOIN authors ON users.id = authors.user_id
         JOIN posts ON authors.id = posts.author_id
         JOIN posts_tags_association AS posts_tags_association_1 ON posts.id = posts_tags_association_1.post_id
         JOIN tags ON tags.id = posts_tags_association_1.tag_id
         LEFT OUTER JOIN authors AS authors_1 ON users.id = authors_1.user_id
         LEFT OUTER JOIN posts AS posts_1 ON authors_1.id = posts_1.author_id
         LEFT OUTER JOIN (posts_tags_association AS posts_tags_association_2 JOIN tags AS tags_1
                          ON tags_1.id = posts_tags_association_2.tag_id)
                         ON posts_1.id = posts_tags_association_2.post_id
WHERE tags.name = 'news';
