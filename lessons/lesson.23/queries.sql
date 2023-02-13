--
SELECT blog_authors.id,
       blog_authors.created_at,
       blog_authors.name,
       blog_authors.user_id,
       blog_users_1.id AS id_1,
       blog_users_1.username,
       blog_users_1.is_staff
FROM blog_authors
         LEFT OUTER JOIN blog_users AS blog_users_1
                         ON blog_users_1.id = blog_authors.user_id
ORDER BY blog_authors.id;

--

SELECT blog_posts.author_id  AS blog_posts_author_id,
       blog_posts.id         AS blog_posts_id,
       blog_posts.created_at AS blog_posts_created_at,
       blog_posts.title      AS blog_posts_title,
       blog_posts.body       AS blog_posts_body
FROM blog_posts
WHERE blog_posts.author_id IN (1, 2, 3);

--
SELECT blog_posts_1.id      AS blog_posts_1_id,
       blog_tags.id         AS blog_tags_id,
       blog_tags.created_at AS blog_tags_created_at,
       blog_tags.name       AS blog_tags_name
FROM blog_posts AS blog_posts_1
         JOIN posts_tags_association AS posts_tags_association_1 ON blog_posts_1.id = posts_tags_association_1.post_id
         JOIN blog_tags ON blog_tags.id = posts_tags_association_1.tag_id
WHERE blog_posts_1.id IN (1, 2, 3, 4);

SELECT blog_tags.id, blog_tags.created_at, blog_tags.name
FROM blog_tags;

INSERT INTO posts_tags_association (post_id, tag_id)
VALUES (3, 1),
       (3, 6),
       (3, 8),
       (2, 4),
       (2, 6),
       (4, 1),
       (4, 6),
       (4, 9),
       (1, 3),
       (1, 6)
;
COMMIT
