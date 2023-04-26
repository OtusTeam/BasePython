SELECT blog_users.username   AS blog_users_username,
       blog_users.email      AS blog_users_email,
       blog_users.archived   AS blog_users_archived,
       blog_users.created_at AS blog_users_created_at,
       blog_users.id         AS blog_users_id
FROM blog_users;

SELECT blog_authors.name    AS blog_authors_name,
       blog_authors.user_id AS blog_authors_user_id,
       blog_authors.id      AS blog_authors_id
FROM blog_authors
WHERE blog_authors.user_id = 4;

--
SELECT blog_users.username    AS blog_users_username,
       blog_users.email       AS blog_users_email,
       blog_users.archived    AS blog_users_archived,
       blog_users.created_at  AS blog_users_created_at,
       blog_users.id          AS blog_users_id,
       blog_authors_1.name    AS blog_authors_1_name,
       blog_authors_1.user_id AS blog_authors_1_user_id,
       blog_authors_1.id      AS blog_authors_1_id
FROM blog_users
         LEFT OUTER JOIN blog_authors AS blog_authors_1
                         ON blog_users.id = blog_authors_1.user_id;

--
SELECT blog_authors.name       AS blog_authors_name,
       blog_authors.user_id    AS blog_authors_user_id,
       blog_authors.id         AS blog_authors_id,
       blog_users_1.username   AS blog_users_1_username,
       blog_users_1.email      AS blog_users_1_email,
       blog_users_1.archived   AS blog_users_1_archived,
       blog_users_1.created_at AS blog_users_1_created_at,
       blog_users_1.id         AS blog_users_1_id
FROM blog_authors
         LEFT OUTER JOIN blog_users AS blog_users_1
                         ON blog_users_1.id = blog_authors.user_id;

--

SELECT blog_users.username    AS blog_users_username,
       blog_users.email       AS blog_users_email,
       blog_users.archived    AS blog_users_archived,
       blog_users.created_at  AS blog_users_created_at,
       blog_users.id          AS blog_users_id,
       blog_authors_1.name    AS blog_authors_1_name,
       blog_authors_1.user_id AS blog_authors_1_user_id,
       blog_authors_1.id      AS blog_authors_1_id
FROM blog_users
         JOIN blog_authors
              ON blog_users.id = blog_authors.user_id
         LEFT OUTER JOIN blog_authors AS blog_authors_1
                         ON blog_users.id = blog_authors_1.user_id
WHERE blog_authors.user_id IS NOT NULL;

SELECT blog_users.username    AS blog_users_username,
       blog_users.email       AS blog_users_email,
       blog_users.archived    AS blog_users_archived,
       blog_users.created_at  AS blog_users_created_at,
       blog_users.id          AS blog_users_id,
       blog_authors_1.name    AS blog_authors_1_name,
       blog_authors_1.user_id AS blog_authors_1_user_id,
       blog_authors_1.id      AS blog_authors_1_id
FROM blog_users
         JOIN blog_authors AS blog_authors_1
              ON blog_users.id = blog_authors_1.user_id;


SELECT blog_users.username    AS blog_users_username,
       blog_users.email       AS blog_users_email,
       blog_users.archived    AS blog_users_archived,
       blog_users.created_at  AS blog_users_created_at,
       blog_users.id          AS blog_users_id,
       blog_authors_1.name    AS blog_authors_1_name,
       blog_authors_1.user_id AS blog_authors_1_user_id,
       blog_authors_1.id      AS blog_authors_1_id
FROM blog_users
         JOIN blog_authors AS blog_authors_1
              ON blog_users.id = blog_authors_1.user_id;


SELECT id
     , username
     , length(username)
     , length(username) = 4
     , concat(username, '@google.com') as email
     , username || '@yahoo.com'
FROM blog_users;

SELECT blog_authors.name       AS blog_authors_name,
       blog_authors.user_id    AS blog_authors_user_id,
       blog_authors.id         AS blog_authors_id,
       blog_users_1.username   AS blog_users_1_username,
       blog_users_1.email      AS blog_users_1_email,
       blog_users_1.archived   AS blog_users_1_archived,
       blog_users_1.created_at AS blog_users_1_created_at,
       blog_users_1.id         AS blog_users_1_id
FROM blog_authors
         JOIN blog_users
              ON blog_users.id = blog_authors.user_id
         LEFT OUTER JOIN blog_users AS blog_users_1
                         ON blog_users_1.id = blog_authors.user_id
WHERE blog_users.email LIKE '%@google.com';

--
SELECT blog_users.username    AS blog_users_username,
       blog_users.email       AS blog_users_email,
       blog_users.archived    AS blog_users_archived,
       blog_users.created_at  AS blog_users_created_at,
       blog_users.id          AS blog_users_id,
       blog_posts_1.title     AS blog_posts_1_title,
       blog_posts_1.body      AS blog_posts_1_body,
       blog_posts_1.author_id AS blog_posts_1_author_id,
       blog_posts_1.id        AS blog_posts_1_id,
       blog_authors_1.name    AS blog_authors_1_name,
       blog_authors_1.user_id AS blog_authors_1_user_id,
       blog_authors_1.id      AS blog_authors_1_id
FROM blog_users
         LEFT OUTER JOIN blog_authors AS blog_authors_1 ON blog_users.id = blog_authors_1.user_id
         LEFT OUTER JOIN blog_posts AS blog_posts_1 ON blog_authors_1.id = blog_posts_1.author_id
ORDER BY blog_users.id;

--

SELECT blog_users.username    AS blog_users_username,
       blog_users.email       AS blog_users_email,
       blog_users.archived    AS blog_users_archived,
       blog_users.created_at  AS blog_users_created_at,
       blog_users.id          AS blog_users_id,
       blog_authors_1.name    AS blog_authors_1_name,
       blog_authors_1.user_id AS blog_authors_1_user_id,
       blog_authors_1.id      AS blog_authors_1_id
FROM blog_users
         LEFT OUTER JOIN blog_authors AS blog_authors_1 ON blog_users.id = blog_authors_1.user_id
ORDER BY blog_users.id;

SELECT blog_posts.author_id AS blog_posts_author_id,
       blog_posts.title     AS blog_posts_title,
       blog_posts.body      AS blog_posts_body,
       blog_posts.id        AS blog_posts_id
FROM blog_posts
WHERE blog_posts.author_id IN (1, 2);


--

SELECT blog_authors.name       AS blog_authors_name,
       blog_authors.user_id    AS blog_authors_user_id,
       blog_authors.id         AS blog_authors_id,
       blog_users_1.username   AS blog_users_1_username,
       blog_users_1.email      AS blog_users_1_email,
       blog_users_1.archived   AS blog_users_1_archived,
       blog_users_1.created_at AS blog_users_1_created_at,
       blog_users_1.id         AS blog_users_1_id
FROM blog_authors
         LEFT OUTER JOIN blog_users
             AS blog_users_1 ON blog_users_1.id = blog_authors.user_id
ORDER BY blog_authors.id;

SELECT blog_posts.author_id AS blog_posts_author_id,
       blog_posts.title     AS blog_posts_title,
       blog_posts.body      AS blog_posts_body,
       blog_posts.id        AS blog_posts_id
FROM blog_posts
WHERE blog_posts.author_id IN (1, 2);

