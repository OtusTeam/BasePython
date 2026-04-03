SELECT post.title
     , post.content
     , post.user_id
     , post.id
FROM post
ORDER BY post.title;

SELECT post_1.id AS post_1_id
     , tag.name  AS tag_name
     , tag.id    AS tag_id
FROM post AS post_1
         JOIN posts_tags_association AS posts_tags_association_1 ON post_1.id = posts_tags_association_1.post_id
         JOIN tag ON tag.id = posts_tags_association_1.tag_id
WHERE post_1.id IN (1, 2, 4, 5, 6)


--

SELECT tag.name
     , tag.description
FROM tag;

SELECT post.title
     , post.content
     , post.user_id
     , post.id
FROM post;

SELECT post_1.id       AS post_1_id
     , tag.name        AS tag_name
     , tag.description AS tag_description
FROM post AS post_1
         JOIN posts_tags_association AS posts_tags_association_1
              ON post_1.id = posts_tags_association_1.post_id
         JOIN tag
              ON tag.name = posts_tags_association_1.tag_name;


INSERT INTO posts_tags_association (post_id, tag_name)
VALUES ((10::int, 'JS'::citext),
        (10::int, 'Intro'::citext),
        (13::int, 'Python'::citext),
        (13::int, 'news'::citext),
        (7::int, 'Python'::citext),
        (7::int, 'Intro'::citext));

---


insert into "user" (username, email, full_name)
select
      'user_' || rnd || '_' || idx
    , 'user_' || rnd || '_' || idx || '@example.com'
    , 'User Name ' || rnd || ' ' || idx
from generate_series(1, 1000) as idx, floor(random() * 100) as rnd;
