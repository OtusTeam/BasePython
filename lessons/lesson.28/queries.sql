SELECT post.title,
       post.body,
       post.user_id,
       post.id,
       user_1.username,
       user_1.email,
       user_1.full_name,
       user_1.id AS id_1
FROM post
         LEFT OUTER JOIN
     "user" AS user_1
     ON user_1.id = post.user_id
ORDER BY post.id;

--
--

SELECT "user".username
     , "user".email
     , "user".full_name
     , "user".id
FROM "user"
ORDER BY "user".id;


SELECT post.user_id AS post_user_id
     , post.title   AS post_title
     , post.body    AS post_body
     , post.id      AS post_id
FROM post
WHERE post.user_id IN (1, 2, 3);

