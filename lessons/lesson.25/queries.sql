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