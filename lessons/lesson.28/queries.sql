INSERT INTO users (username, email, full_name)
VALUES ('john', 'john@example.com', 'John Smith')

SELECT users.id        AS users_id
     , users.username  AS users_username
     , users.email     AS users_email
     , users.full_name AS users_full_name
FROM users
WHERE users.id = 1;


SELECT 7;

SELECT id
FROM users;

SELECT users.id
     , users.username
     , users.email
     , users.full_name
FROM users
WHERE users.email IS NOT NULL
  AND length(users.username) > 3
ORDER BY users.id;


CREATE TABLE posts
(
    id      INTEGER                 NOT NULL,
    title   VARCHAR(100) DEFAULT '' NOT NULL,
    text    TEXT         DEFAULT '' NOT NULL,
    user_id INTEGER                 NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (user_id) REFERENCES users (id)
);



SELECT posts.id
     , posts.title
     , posts.text
     , posts.user_id
     , users_1.id AS id_1
     , users_1.username
     , users_1.email
     , users_1.full_name
FROM posts
     LEFT OUTER JOIN users AS users_1
         ON users_1.id = posts.user_id
ORDER BY posts.id;
