SELECT blog_posts.id         AS blog_posts_id,
       blog_posts.created_at AS blog_posts_created_at,
       blog_posts.title      AS blog_posts_title,
       blog_posts.body       AS blog_posts_body,
       blog_posts.status     AS blog_posts_status,
       blog_posts.author_id  AS blog_posts_author_id,
       blog_tags_1.id        AS blog_tags_1_id,
       blog_tags_1.name      AS blog_tags_1_name
FROM blog_posts
         LEFT JOIN (
    posts_tags_association AS posts_tags_association_1
        JOIN blog_tags AS blog_tags_1 ON blog_tags_1.id = posts_tags_association_1.tag_id
    )
                   ON blog_posts.id = posts_tags_association_1.post_id;

SELECT blog_posts.id         AS blog_posts_id,
       blog_posts.created_at AS blog_posts_created_at,
       blog_posts.title      AS blog_posts_title,
       blog_posts.body       AS blog_posts_body,
       blog_posts.status     AS blog_posts_status,
       blog_posts.author_id  AS blog_posts_author_id,
       blog_tags_1.id        AS blog_tags_1_id,
       blog_tags_1.name      AS blog_tags_1_name
FROM blog_posts
         RIGHT JOIN (
    posts_tags_association AS posts_tags_association_1
        JOIN blog_tags AS blog_tags_1 ON blog_tags_1.id = posts_tags_association_1.tag_id
    )
                    ON blog_posts.id = posts_tags_association_1.post_id;



SELECT *
FROM blog_users;

SELECT *
FROM blog_authors;


SELECT *
FROM blog_users
         JOIN blog_authors ba on blog_users.id = ba.user_id;


SELECT *
FROM blog_users
         INNER JOIN blog_authors ba on blog_users.id = ba.user_id;

SELECT *
FROM blog_users
         LEFT OUTER JOIN blog_authors ba on blog_users.id = ba.user_id;

SELECT *
FROM blog_users
         LEFT JOIN blog_authors ba on blog_users.id = ba.user_id;

-- INNER JOIN == JOIN
-- LEFT OUTER JOIN == LEFT JOIN

SELECT *
FROM blog_authors
         JOIN blog_users bu on blog_authors.user_id = bu.id;

SELECT *
FROM blog_authors
         RIGHT JOIN blog_users bu on blog_authors.user_id = bu.id;


SELECT blog_posts.id             AS blog_posts_id,
       blog_posts.created_at     AS blog_posts_created_at,
       blog_posts.title          AS blog_posts_title,
       blog_posts.body           AS blog_posts_body,
       blog_posts.status         AS blog_posts_status,
       blog_posts.author_id      AS blog_posts_author_id,
       blog_users_1.id           AS blog_users_1_id,
       blog_users_1.created_at   AS blog_users_1_created_at,
       blog_users_1.username     AS blog_users_1_username,
       blog_users_1.is_staff     AS blog_users_1_is_staff,
       blog_authors_1.id         AS blog_authors_1_id,
       blog_authors_1.created_at AS blog_authors_1_created_at,
       blog_authors_1.name       AS blog_authors_1_name,
       blog_authors_1.user_id    AS blog_authors_1_user_id,
       blog_tags_1.id            AS blog_tags_1_id,
       blog_tags_1.name          AS blog_tags_1_name
FROM blog_posts
         LEFT OUTER JOIN blog_authors AS blog_authors_1 ON blog_authors_1.id = blog_posts.author_id
         LEFT OUTER JOIN blog_users AS blog_users_1 ON blog_users_1.id = blog_authors_1.user_id
         LEFT OUTER JOIN (
    posts_tags_association AS posts_tags_association_1
        JOIN blog_tags AS blog_tags_1
        ON blog_tags_1.id = posts_tags_association_1.tag_id
    )
                         ON blog_posts.id = posts_tags_association_1.post_id;


SELECT bp.*, bt.*
FROM posts_tags_association
         JOIN blog_tags bt on posts_tags_association.tag_id = bt.id
         JOIN blog_posts bp on bp.id = posts_tags_association.post_id;


SELECT blog_posts.id             AS blog_posts_id,
       blog_posts.created_at     AS blog_posts_created_at,
       blog_posts.title          AS blog_posts_title,
       blog_posts.body           AS blog_posts_body,
       blog_posts.status         AS blog_posts_status,
       blog_posts.author_id      AS blog_posts_author_id,
       blog_users_1.id           AS blog_users_1_id,
       blog_users_1.created_at   AS blog_users_1_created_at,
       blog_users_1.username     AS blog_users_1_username,
       blog_users_1.is_staff     AS blog_users_1_is_staff,
       blog_authors_1.id         AS blog_authors_1_id,
       blog_authors_1.created_at AS blog_authors_1_created_at,
       blog_authors_1.name       AS blog_authors_1_name,
       blog_authors_1.user_id    AS blog_authors_1_user_id,
       blog_tags_1.id            AS blog_tags_1_id,
       blog_tags_1.name          AS blog_tags_1_name
FROM blog_posts
         JOIN posts_tags_association AS posts_tags_association_1 ON blog_posts.id = posts_tags_association_1.post_id
         JOIN blog_tags ON blog_tags.id = posts_tags_association_1.tag_id
         LEFT OUTER JOIN blog_authors AS blog_authors_1 ON blog_authors_1.id = blog_posts.author_id
         LEFT OUTER JOIN blog_users AS blog_users_1 ON blog_users_1.id = blog_authors_1.user_id
         LEFT OUTER JOIN (posts_tags_association AS posts_tags_association_2 JOIN blog_tags AS blog_tags_1 ON blog_tags_1.id = posts_tags_association_2.tag_id)
                         ON blog_posts.id = posts_tags_association_2.post_id
WHERE blog_tags.name IN ('news', 'flask');



SELECT bp.*, bt.*
FROM posts_tags_association
         FULL JOIN blog_posts bp on bp.id = posts_tags_association.post_id
         FULL JOIN blog_tags bt on bt.id = posts_tags_association.tag_id;


CREATE TABLE meals
(
    id   SERIAL PRIMARY KEY,
    name VARCHAR
);

CREATE TABLE drinks
(
    id   SERIAL PRIMARY KEY,
    name VARCHAR
);

SELECT m.name, d.name
FROM meals m
         CROSS JOIN drinks d;

SELECT id, name as name, 'meal' as cat
FROM meals
UNION
SELECT id, name as name, 'drink' as cat
FROM drinks
ORDER BY name;


SELECT blog_posts.id             AS blog_posts_id,
       blog_posts.created_at     AS blog_posts_created_at,
       blog_posts.title          AS blog_posts_title,
       blog_posts.body           AS blog_posts_body,
       blog_posts.status         AS blog_posts_status,
       blog_posts.author_id      AS blog_posts_author_id,
       blog_users_1.id           AS blog_users_1_id,
       blog_users_1.created_at   AS blog_users_1_created_at,
       blog_users_1.username     AS blog_users_1_username,
       blog_users_1.is_staff     AS blog_users_1_is_staff,
       blog_authors_1.id         AS blog_authors_1_id,
       blog_authors_1.created_at AS blog_authors_1_created_at,
       blog_authors_1.name       AS blog_authors_1_name,
       blog_authors_1.user_id    AS blog_authors_1_user_id,
       blog_tags_1.id            AS blog_tags_1_id,
       blog_tags_1.name          AS blog_tags_1_name
FROM blog_posts
         JOIN posts_tags_association AS posts_tags_association_1 ON blog_posts.id = posts_tags_association_1.post_id
         JOIN blog_tags ON blog_tags.id = posts_tags_association_1.tag_id
         LEFT OUTER JOIN blog_authors AS blog_authors_1 ON blog_authors_1.id = blog_posts.author_id
         LEFT OUTER JOIN blog_users AS blog_users_1 ON blog_users_1.id = blog_authors_1.user_id
         LEFT OUTER JOIN (posts_tags_association AS posts_tags_association_2 JOIN blog_tags AS blog_tags_1 ON blog_tags_1.id = posts_tags_association_2.tag_id)
                         ON blog_posts.id = posts_tags_association_2.post_id
WHERE blog_tags.name = 'news'
  AND blog_tags.name = 'python';


--

SELECT blog_posts.id             AS blog_posts_id,
       blog_posts.created_at     AS blog_posts_created_at,
       blog_posts.title          AS blog_posts_title,
       blog_posts.body           AS blog_posts_body,
       blog_posts.status         AS blog_posts_status,
       blog_posts.author_id      AS blog_posts_author_id,
       blog_users_1.id           AS blog_users_1_id,
       blog_users_1.created_at   AS blog_users_1_created_at,
       blog_users_1.username     AS blog_users_1_username,
       blog_users_1.is_staff     AS blog_users_1_is_staff,
       blog_authors_1.id         AS blog_authors_1_id,
       blog_authors_1.created_at AS blog_authors_1_created_at,
       blog_authors_1.name       AS blog_authors_1_name,
       blog_authors_1.user_id    AS blog_authors_1_user_id,
       blog_tags_1.id            AS blog_tags_1_id,
       blog_tags_1.name          AS blog_tags_1_name
FROM blog_posts
         JOIN posts_tags_association AS posts_tags_association_1 ON blog_posts.id = posts_tags_association_1.post_id
         JOIN blog_tags ON blog_tags.id = posts_tags_association_1.tag_id
         LEFT OUTER JOIN blog_authors AS blog_authors_1 ON blog_authors_1.id = blog_posts.author_id
         LEFT OUTER JOIN blog_users AS blog_users_1 ON blog_users_1.id = blog_authors_1.user_id
         LEFT OUTER JOIN (
    posts_tags_association AS posts_tags_association_2 JOIN blog_tags AS blog_tags_1 ON blog_tags_1.id = posts_tags_association_2.tag_id
    )
                         ON blog_posts.id = posts_tags_association_2.post_id
;


-- only these tags
SELECT *
FROM blog_tags bt
WHERE bt.name IN ('news', 'python');

-- check associations
SELECT *
FROM posts_tags_association
         JOIN blog_tags bt on bt.id = posts_tags_association.tag_id
WHERE bt.name IN ('news', 'python');

-- filter
SELECT bp.*, bt1.name, bt2.name
FROM blog_posts bp
         JOIN posts_tags_association pta1 on bp.id = pta1.post_id
         JOIN posts_tags_association pta2 on bp.id = pta2.post_id
         JOIN blog_tags bt1 on bt1.id = pta1.tag_id
         JOIN blog_tags bt2 on bt2.id = pta2.tag_id
WHERE bt1.name = 'news'
  AND bt2.name = 'python';

-- with outer joins:
SELECT blog_posts.id             AS blog_posts_id,
       blog_posts.created_at     AS blog_posts_created_at,
       blog_posts.title          AS blog_posts_title,
       blog_posts.body           AS blog_posts_body,
       blog_posts.status         AS blog_posts_status,
       blog_posts.author_id      AS blog_posts_author_id,
       blog_users_1.id           AS blog_users_1_id,
       blog_users_1.created_at   AS blog_users_1_created_at,
       blog_users_1.username     AS blog_users_1_username,
       blog_users_1.is_staff     AS blog_users_1_is_staff,
       blog_authors_1.id         AS blog_authors_1_id,
       blog_authors_1.created_at AS blog_authors_1_created_at,
       blog_authors_1.name       AS blog_authors_1_name,
       blog_authors_1.user_id    AS blog_authors_1_user_id,
       blog_tags_1.id            AS blog_tags_1_id,
       blog_tags_1.name          AS blog_tags_1_name
FROM blog_posts
         JOIN posts_tags_association AS posts_tags_association_1 ON blog_posts.id = posts_tags_association_1.post_id
         JOIN blog_tags AS tbl_tags_1 ON tbl_tags_1.id = posts_tags_association_1.tag_id
         JOIN posts_tags_association AS posts_tags_association_2 ON blog_posts.id = posts_tags_association_2.post_id
         JOIN blog_tags AS tbl_tags_2 ON tbl_tags_2.id = posts_tags_association_2.tag_id
         LEFT OUTER JOIN blog_authors AS blog_authors_1 ON blog_authors_1.id = blog_posts.author_id
         LEFT OUTER JOIN blog_users AS blog_users_1 ON blog_users_1.id = blog_authors_1.user_id
         LEFT OUTER JOIN (posts_tags_association AS posts_tags_association_3 JOIN blog_tags AS blog_tags_1 ON blog_tags_1.id = posts_tags_association_3.tag_id)
                         ON blog_posts.id = posts_tags_association_3.post_id
WHERE tbl_tags_1.name = 'news'
  AND tbl_tags_2.name = 'python';


-- and again

SELECT blog_posts.id             AS blog_posts_id,
       blog_posts.created_at     AS blog_posts_created_at,
       blog_posts.title          AS blog_posts_title,
       blog_posts.body           AS blog_posts_body,
       blog_posts.status         AS blog_posts_status,
       blog_posts.author_id      AS blog_posts_author_id,
       blog_users_1.id           AS blog_users_1_id,
       blog_users_1.created_at   AS blog_users_1_created_at,
       blog_users_1.username     AS blog_users_1_username,
       blog_users_1.is_staff     AS blog_users_1_is_staff,
       blog_authors_1.id         AS blog_authors_1_id,
       blog_authors_1.created_at AS blog_authors_1_created_at,
       blog_authors_1.name       AS blog_authors_1_name,
       blog_authors_1.user_id    AS blog_authors_1_user_id,
       blog_tags_1.id            AS blog_tags_1_id,
       blog_tags_1.name          AS blog_tags_1_name
FROM blog_posts
         JOIN posts_tags_association AS posts_tags_association_1 ON blog_posts.id = posts_tags_association_1.post_id
         JOIN blog_tags AS tbl_tags_0 ON tbl_tags_0.id = posts_tags_association_1.tag_id
         JOIN posts_tags_association AS posts_tags_association_2 ON blog_posts.id = posts_tags_association_2.post_id
         JOIN blog_tags AS tbl_tags_1 ON tbl_tags_1.id = posts_tags_association_2.tag_id
         LEFT OUTER JOIN blog_authors AS blog_authors_1 ON blog_authors_1.id = blog_posts.author_id
         LEFT OUTER JOIN blog_users AS blog_users_1 ON blog_users_1.id = blog_authors_1.user_id
         LEFT OUTER JOIN (posts_tags_association AS posts_tags_association_3 JOIN blog_tags AS blog_tags_1 ON blog_tags_1.id = posts_tags_association_3.tag_id)
                         ON blog_posts.id = posts_tags_association_3.post_id
WHERE tbl_tags_0.name = 'django'
  AND tbl_tags_1.name = 'python';
