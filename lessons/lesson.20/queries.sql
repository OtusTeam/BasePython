
INSERT INTO blog_users (created_at, username, is_staff) VALUES (%s, %s, %s) RETURNING blog_users.id
(datetime.datetime(2021, 8, 14, 8, 47, 21, 481564), 'john', False)
INSERT INTO blog_users (created_at, username, is_staff) VALUES (%s, %s, %s) RETURNING blog_users.id
(datetime.datetime(2021, 8, 14, 8, 47, 21, 512937), 'sam', False)
INSERT INTO blog_authors (created_at, name, bio, user_id) VALUES (%s, %s, %s, %s) RETURNING blog_authors.id
(datetime.datetime(2021, 8, 14, 8, 47, 21, 526852), 'John Smith', 'I like Python', 2)
INSERT INTO blog_authors (created_at, name, bio, user_id) VALUES (%s, %s, %s, %s) RETURNING blog_authors.id
(datetime.datetime(2021, 8, 14, 8, 47, 21, 536211), 'Sam White', 'I like docker', 3)


SELECT blog_users.created_at,
       blog_users.id,
       blog_users.username,
       blog_users.is_staff,
       blog_authors_1.created_at AS created_at_1,
       blog_authors_1.id         AS id_1,
       blog_authors_1.name,
       blog_authors_1.bio,
       blog_authors_1.user_id
FROM blog_users
 LEFT OUTER JOIN blog_authors AS blog_authors_1 ON blog_users.id = blog_authors_1.user_id



SELECT blog_authors.created_at,
       blog_authors.id,
       blog_authors.name,
       blog_authors.bio,
       blog_authors.user_id,
       blog_users_1.created_at AS created_at_1,
       blog_users_1.id         AS id_1,
       blog_users_1.username,
       blog_users_1.is_staff
FROM blog_authors
         LEFT OUTER JOIN blog_users AS blog_users_1 ON blog_users_1.id = blog_authors.user_id

--


SELECT blog_authors.created_at,
       blog_authors.id,
       blog_authors.name,
       blog_authors.bio,
       blog_authors.user_id,
       blog_users_1.created_at AS created_at_1,
       blog_users_1.id         AS id_1,
       blog_users_1.username,
       blog_users_1.is_staff
FROM blog_authors
         LEFT OUTER JOIN blog_users AS blog_users_1 ON blog_users_1.id = blog_authors.user_id;

SELECT blog_articles.author_id  AS blog_articles_author_id,
       blog_articles.created_at AS blog_articles_created_at,
       blog_articles.id         AS blog_articles_id,
       blog_articles.title      AS blog_articles_title,
       blog_articles.body       AS blog_articles_body,
       blog_articles.status     AS blog_articles_status
FROM blog_articles
WHERE blog_articles.author_id IN (1, 2);


SELECT blog_articles_1.id   AS blog_articles_1_id,
       blog_tags.created_at AS blog_tags_created_at,
       blog_tags.id         AS blog_tags_id,
       blog_tags.name       AS blog_tags_name
FROM blog_articles AS blog_articles_1
     JOIN blog_articles_tags_association_table AS blog_articles_tags_association_table_1
          ON blog_articles_1.id = blog_articles_tags_association_table_1.article_id
     JOIN blog_tags ON blog_tags.id = blog_articles_tags_association_table_1.tag_id
WHERE blog_articles_1.id IN (4, 5, 6);
