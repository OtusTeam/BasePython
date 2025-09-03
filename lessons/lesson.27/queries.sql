SELECT posts.title,
       posts.body,
       posts.user_id,
       posts.id,
       posts.created_at,
       users_1.username,
       users_1.email,
       users_1.full_name,
       users_1.id AS id_1
FROM posts
         LEFT OUTER JOIN users AS users_1
                         ON users_1.id = posts.user_id
ORDER BY posts.id;

--

SELECT users.username, users.email, users.full_name, users.id
FROM users
ORDER BY users.id;

SELECT posts.user_id    AS posts_user_id,
       posts.title      AS posts_title,
       posts.body       AS posts_body,
       posts.id         AS posts_id,
       posts.created_at AS posts_created_at
FROM posts
WHERE posts.user_id IN (1, 2, 3, 4, 5)


--

SELECT users.username
     , users.email
     , users.full_name
     , users.id
FROM users
         JOIN posts ON users.id = posts.user_id
WHERE lower(posts.title) LIKE lower('%#3%')
ORDER BY users.id

--

SELECT users.username, users.email, users.full_name, users.id
FROM users
         JOIN posts ON users.id = posts.user_id
WHERE lower(posts.title) LIKE lower('%#3%')
ORDER BY users.id;

SELECT posts.user_id    AS posts_user_id,
       posts.title      AS posts_title,
       posts.body       AS posts_body,
       posts.id         AS posts_id,
       posts.created_at AS posts_created_at
FROM posts
WHERE posts.user_id IN (1, 3)
  AND lower(posts.title) LIKE lower('%#3%')
