SELECT 1;

SELECT 1 + 2;

SELECT 1 + 2 as sum;
SELECT 1 + 2 as "total sum";

SELECT 1 "one", 2 two;

SELECT 2 * 3;

SELECT now();

SELECT CURRENT_TIMESTAMP;

---
-- Таблица пользователей

CREATE TABLE users
(
    id        BIGSERIAL PRIMARY KEY,
    username  VARCHAR(32) UNIQUE NOT NULL,
    email     VARCHAR(150) UNIQUE,
    full_name VARCHAR            NOT NULL DEFAULT ''
);


-- ALTER TABLE users
-- DROP COLUMN full_name;

ALTER TABLE users
    ADD COLUMN full_name VARCHAR NOT NULL DEFAULT '';

DROP TABLE users;

-- таблица постов

CREATE TABLE posts
(
    id      BIGSERIAL PRIMARY KEY,
    title   VARCHAR(150) NOT NULL DEFAULT '',
    body    TEXT         NOT NULL DEFAULT '',
    user_id BIGINT       NOT NULL,
    FOREIGN KEY (user_id)
        REFERENCES users (id)
        ON DELETE CASCADE
);

---


SELECT *
FROM users;

SELECT id, username
FROM users;

INSERT INTO users (username, email)
VALUES ('john', 'john@example.com');

INSERT INTO users (username, email)
VALUES ('sam', 'sam@example.com'),
       ('alice', NULL);


INSERT INTO users (username)
VALUES ('bob');

INSERT INTO users (username, email, full_name)
VALUES ('kyle', 'kyle@example.com', 'Kyle Grey');


UPDATE users
SET full_name = 'Kyle Grey'
WHERE username = 'kyle';


UPDATE users
SET full_name = 'Bob White'
WHERE username = 'bob';


SELECT *
FROM users
WHERE email IS NOT NULL;

SELECT *
FROM users
WHERE email IS NULL;

SELECT id, username, length(username)
FROM users;

SELECT *
FROM users
WHERE length(username) > 3;

UPDATE users
SET email = username || '@yahoo.com'
WHERE email IS NULL;


SELECT *
FROM users
ORDER BY id;

SELECT *
FROM users


ORDER BY username;


SELECT *
FROM users
ORDER BY full_name, username DESC;


---

INSERT INTO posts (title, body, user_id)
VALUES ('The Enchanted Forest: A Journey Through Myth and Magic',
        'Explore the depths of the Enchanted Forest, where ancient trees whisper secrets and mythical creatures roam. Discover the legends that have shaped this magical realm and the adventures that await those brave enough to enter.',
        2),

       ('The Art of Potion Making: A Beginner’s Guide',
        'Unlock the secrets of potion making with this comprehensive guide. From healing elixirs to love potions, learn the essential ingredients and techniques to create your own magical brews.',
        4),

       ('Dragons: Guardians of the Skies',
        'Delve into the fascinating world of dragons, the majestic creatures that soar through the skies. This article explores their history, symbolism, and the role they play in various cultures around the globe.',
        5),

       ('The Lost City of Atlantis: Fact or Fiction?',
        'Join us as we investigate the mysteries surrounding the legendary lost city of Atlantis. Was it a real place, or merely a figment of imagination? Discover the theories and evidence that continue to captivate historians and adventurers alike.',
        2),

       ('Magical Creatures of the Night: A Closer Look',
        'From the elusive unicorn to the mischievous pixie, the night is alive with magical creatures. This article takes you on a journey to uncover the myths and stories behind these enchanting beings.',
        4),

       ('Wizards and Wands: The Science Behind Magic',
        'What if magic was more than just fantasy? Explore the scientific principles that could explain the wonders of wizardry and the art of wand crafting in this thought-provoking article.',
        5),

       ('The Chronicles of Time Travel: Adventures Beyond the Present',
        'Time travel has fascinated humanity for centuries. Join us as we explore the theories, stories, and potential realities of traveling through time, and what it could mean for our understanding of history.',
        2);


SELECT p.title, u.username, u.full_name
FROM posts p
         JOIN users u ON u.id = p.user_id
ORDER BY u.id

--

SELECT posts.title
     , posts.body
     , posts.user_id
     , posts.created_at
     , posts.id
     , users_1.username
     , users_1.email
     , users_1.full_name
     , users_1.created_at AS created_at_1
     , users_1.id         AS id_1
FROM posts
         LEFT OUTER JOIN users AS users_1
                         ON users_1.id = posts.user_id
ORDER BY posts.id


--

SELECT users.username
     , users.email
     , users.full_name
     , users.created_at
     , users.id
     , posts_1.title
     , posts_1.body
     , posts_1.user_id
     , posts_1.created_at AS created_at_1
     , posts_1.id         AS id_1
FROM users
         JOIN posts AS posts_1 ON users.id = posts_1.user_id
ORDER BY users.id
--

SELECT users.username
     , users.email
     , users.full_name
     , users.created_at
     , users.id
FROM users
ORDER BY users.id;

SELECT posts.user_id    AS posts_user_id
     , posts.title      AS posts_title
     , posts.body       AS posts_body
     , posts.created_at AS posts_created_at
     , posts.id         AS posts_id
FROM posts
WHERE posts.user_id IN (1, 2, 3)

--

SELECT users.username
     , users.email
     , users.full_name
     , users.created_at
     , users.id
FROM users
         JOIN posts ON users.id = posts.user_id
ORDER BY users.id

SELECT posts.user_id    AS posts_user_id
     , posts.title      AS posts_title
     , posts.body       AS posts_body
     , posts.created_at AS posts_created_at
     , posts.id         AS posts_id
FROM posts
WHERE posts.user_id IN (1, 3)


--
--
--

-- (.venv) suren@MacBookPro db-blog-application % alembic upgrade --sql 09ed:8764
-- INFO  [alembic.runtime.migration] Context impl PostgresqlImpl.
-- INFO  [alembic.runtime.migration] Generating static SQL
-- INFO  [alembic.runtime.migration] Will assume transactional DDL.
-- BEGIN;
--
-- INFO  [alembic.runtime.migration] Running upgrade 09ed8ada8abe -> 8764cd527aee, create table user_status
-- Running upgrade 09ed8ada8abe -> 8764cd527aee

CREATE TABLE user_status
(
    id          SERIAL                                    NOT NULL,
    name        VARCHAR(10)                               NOT NULL,
    description VARCHAR(255)                DEFAULT ''    NOT NULL,
    created_at  TIMESTAMP WITHOUT TIME ZONE DEFAULT now() NOT NULL,
    CONSTRAINT pk_user_status PRIMARY KEY (id),
    CONSTRAINT uq_user_status_name UNIQUE (name)
);

UPDATE alembic_version
SET version_num='8764cd527aee'
WHERE alembic_version.version_num = '09ed8ada8abe';

COMMIT;


--
--
--

BEGIN;

-- Running upgrade 8764cd527aee -> bae3a0f6bee1

ALTER TABLE users
    ADD COLUMN status VARCHAR(10);

ALTER TABLE users
    ADD CONSTRAINT fk_users_status_user_status FOREIGN KEY (status) REFERENCES user_status (name);

UPDATE alembic_version
SET version_num='bae3a0f6bee1'
WHERE alembic_version.version_num = '8764cd527aee';

-- Running upgrade bae3a0f6bee1 -> 8c1ceb690e3d

ALTER TABLE user_status
    ALTER COLUMN name TYPE VARCHAR(20);

ALTER TABLE users
    ALTER COLUMN status TYPE VARCHAR(20);

UPDATE alembic_version
SET version_num='8c1ceb690e3d'
WHERE alembic_version.version_num = 'bae3a0f6bee1';

COMMIT;


--

-- Running upgrade 8c1ceb690e3d -> bf721fe535f4

UPDATE users
SET friend_code=SUBSTRING(md5(CAST(random() AS VARCHAR)) FROM 1 FOR 6)
WHERE users.friend_code IS NULL;

ALTER TABLE users
    ALTER COLUMN friend_code SET NOT NULL;

UPDATE alembic_version
SET version_num='bf721fe535f4'
WHERE alembic_version.version_num = '8c1ceb690e3d';

COMMIT;


--
--
--
--

SELECT posts.title
     , posts.body
     , posts.user_id
     , posts.created_at
     , posts.id
FROM posts
ORDER BY posts.id

SELECT posts_1.id      AS posts_1_id
     , tags.name       AS tags_name
     , tags.created_at AS tags_created_at
     , tags.id         AS tags_id
FROM posts AS posts_1
     JOIN posts_tags_association AS posts_tags_association_1
         ON posts_1.id = posts_tags_association_1.post_id
     JOIN tags
         ON tags.id = posts_tags_association_1.tag_id
WHERE posts_1.id IN (1, 2, 3, 4, 12, 13, 14, 15, 16, 17, 18)