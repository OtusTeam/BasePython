-- joinedload(Post.user)

SELECT posts.id          AS posts_id
     , posts.title       AS posts_title
     , posts.text        AS posts_text
     , posts.user_id     AS posts_user_id
     , users_1.id        AS users_1_id
     , users_1.username  AS users_1_username
     , users_1.email     AS users_1_email
     , users_1.full_name AS users_1_full_name
FROM posts
         LEFT OUTER JOIN users AS users_1
                         ON users_1.id = posts.user_id;

-- selectinload(User.posts)

SELECT users.id
     , users.username
     , users.email
     , users.full_name
FROM users
ORDER BY users.id;

SELECT posts.user_id AS posts_user_id
     , posts.id      AS posts_id
     , posts.title   AS posts_title
     , posts.text    AS posts_text
FROM posts
WHERE posts.user_id IN (1, 2, 3, 4, 5);


--
SELECT users.id
     , users.username
     , users.email
     , users.full_name
FROM users
ORDER BY users.id;

SELECT posts.user_id AS posts_user_id
     , posts.id      AS posts_id
     , posts.title   AS posts_title
     , posts.text    AS posts_text
FROM posts
WHERE posts.user_id IN (1, 2, 3, 4, 5);

SELECT posts_1.id      AS posts_1_id
     , tags.name       AS tags_name
     , tags.created_at AS tags_created_at
FROM posts AS posts_1
         JOIN post_tag_association AS post_tag_association_1 ON posts_1.id = post_tag_association_1.post_id
         JOIN tags ON tags.name = post_tag_association_1.tag_name
WHERE posts_1.id IN (1, 2, 3, 4, 5, 6);

---


create or replace function update_updated_at()
returns trigger as $$
begin
	NEW.updated_at = now();
	return NEW;
end;
$$ language plpgsql;


create trigger trg_update_products_updated_at
before update
on posts
for each row
execute function update_updated_at();
