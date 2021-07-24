CREATE TABLE blog_users (
        created_at DATETIME DEFAULT (CURRENT_TIMESTAMP) NOT NULL,
        id INTEGER NOT NULL,
        username VARCHAR(32),
        is_staff BOOLEAN NOT NULL,
        PRIMARY KEY (id),
        UNIQUE (username)
);


CREATE TABLE blog_authors (
        created_at DATETIME DEFAULT (CURRENT_TIMESTAMP) NOT NULL,
        id INTEGER NOT NULL,
        name VARCHAR(64) DEFAULT '' NOT NULL,
        user_id INTEGER NOT NULL,
        PRIMARY KEY (id),
        UNIQUE (user_id),
        FOREIGN KEY(user_id) REFERENCES blog_users (id)
);

CREATE TABLE blog_articles (
        created_at DATETIME DEFAULT (CURRENT_TIMESTAMP) NOT NULL,
        id INTEGER NOT NULL,
        title VARCHAR(120) DEFAULT '' NOT NULL,
        body TEXT DEFAULT '' NOT NULL,
        status VARCHAR(10) DEFAULT 'draft' NOT NULL,
        author_id INTEGER NOT NULL,
        PRIMARY KEY (id),
        FOREIGN KEY(author_id) REFERENCES blog_authors (id)
);


SELECT blog_users.created_at     AS blog_users_created_at,
       blog_users.id             AS blog_users_id,
       blog_users.username       AS blog_users_username,
       blog_users.is_staff       AS blog_users_is_staff,
       blog_authors_1.created_at AS blog_authors_1_created_at,
       blog_authors_1.id         AS blog_authors_1_id,
       blog_authors_1.name       AS blog_authors_1_name,
       blog_authors_1.user_id    AS blog_authors_1_user_id
FROM blog_users
         LEFT OUTER JOIN blog_authors AS blog_authors_1 ON blog_users.id = blog_authors_1.user_id;


SELECT blog_authors.created_at AS blog_authors_created_at,
       blog_authors.id         AS blog_authors_id,
       blog_authors.name       AS blog_authors_name,
       blog_authors.user_id    AS blog_authors_user_id,
       blog_users_1.created_at AS blog_users_1_created_at,
       blog_users_1.id         AS blog_users_1_id,
       blog_users_1.username   AS blog_users_1_username,
       blog_users_1.is_staff   AS blog_users_1_is_staff
FROM blog_authors
         LEFT OUTER JOIN blog_users AS blog_users_1 ON blog_users_1.id = blog_authors.user_id
WHERE blog_authors.id = 2;


SELECT blog_authors.created_at    AS blog_authors_created_at,
       blog_authors.id            AS blog_authors_id,
       blog_authors.name          AS blog_authors_name,
       blog_authors.user_id       AS blog_authors_user_id,
       blog_articles_1.created_at AS blog_articles_1_created_at,
       blog_articles_1.id         AS blog_articles_1_id,
       blog_articles_1.title      AS blog_articles_1_title,
       blog_articles_1.body       AS blog_articles_1_body,
       blog_articles_1.status     AS blog_articles_1_status,
       blog_articles_1.author_id  AS blog_articles_1_author_id
FROM blog_authors
         LEFT OUTER JOIN blog_articles AS blog_articles_1 ON blog_authors.id = blog_articles_1.author_id;



SELECT blog_users.created_at      AS blog_users_created_at,
       blog_users.id              AS blog_users_id,
       blog_users.username        AS blog_users_username,
       blog_users.is_staff        AS blog_users_is_staff,
       blog_articles_1.created_at AS blog_articles_1_created_at,
       blog_articles_1.id         AS blog_articles_1_id,
       blog_articles_1.title      AS blog_articles_1_title,
       blog_articles_1.body       AS blog_articles_1_body,
       blog_articles_1.status     AS blog_articles_1_status,
       blog_articles_1.author_id  AS blog_articles_1_author_id,
       blog_authors_1.created_at  AS blog_authors_1_created_at,
       blog_authors_1.id          AS blog_authors_1_id,
       blog_authors_1.name        AS blog_authors_1_name,
       blog_authors_1.user_id     AS blog_authors_1_user_id
FROM blog_users
         LEFT OUTER JOIN blog_authors AS blog_authors_1 ON blog_users.id = blog_authors_1.user_id
         LEFT OUTER JOIN blog_articles AS blog_articles_1 ON blog_authors_1.id = blog_articles_1.author_id;



SELECT blog_articles.created_at AS blog_articles_created_at,
       blog_articles.id         AS blog_articles_id,
       blog_articles.title      AS blog_articles_title,
       blog_articles.body       AS blog_articles_body,
       blog_articles.status     AS blog_articles_status,
       blog_articles.author_id  AS blog_articles_author_id
FROM blog_articles
         JOIN blog_authors ON blog_authors.id = blog_articles.author_id
WHERE lower(blog_authors.name) LIKE lower('john%');


SELECT blog_users.created_at AS blog_users_created_at,
       blog_users.id         AS blog_users_id,
       blog_users.username   AS blog_users_username,
       blog_users.is_staff   AS blog_users_is_staff
FROM blog_users
         JOIN blog_authors ON blog_authors.user_id = blog_users.id
         JOIN blog_articles ON blog_articles.author_id = blog_authors.id
WHERE lower(blog_articles.title) LIKE lower('%flask%');



-- INSERT INTO blog_users (created_at, username, is_staff) VALUES (?, ?, ?)
-- INSERT INTO blog_authors (created_at, name, user_id) VALUES (?, ?, ?)
-- INSERT INTO blog_articles (created_at, title, body, status, author_id) VALUES (?, ?, ?, ?, ?)
-- INSERT INTO blog_articles (created_at, title, body, status, author_id) VALUES (?, ?, ?, ?, ?)
-- ('2021-07-24 09:29:35.279910', 'docker-compose intro', 'Hello again..', 'draft', 4)


-- SELECT blog_users.created_at AS blog_users_created_at, blog_users.id AS blog_users_id, blog_users.username AS blog_users_username, blog_users.is_staff AS blog_users_is_staff
-- FROM blog_users
-- WHERE blog_users.id = ?

SELECT blog_authors.created_at AS blog_authors_created_at,
       blog_authors.id         AS blog_authors_id,
       blog_authors.name       AS blog_authors_name,
       blog_authors.user_id    AS blog_authors_user_id
FROM blog_authors
WHERE blog_authors.id = 4;

-- Author(id=4, name='Nick Gray', user_id=5, created_at=2021-07-24 09:29:35.279034)
SELECT blog_articles.created_at AS blog_articles_created_at,
       blog_articles.id         AS blog_articles_id,
       blog_articles.title      AS blog_articles_title,
       blog_articles.body       AS blog_articles_body,
       blog_articles.status     AS blog_articles_status,
       blog_articles.author_id  AS blog_articles_author_id
FROM blog_articles
WHERE 4 = blog_articles.author_id;

-- INSERT INTO blog_articles (created_at, title, body, status, author_id)
-- VALUES (?, ?, ?, ?, ?) ('2021-07-24 09:29:35.285599', 'PyCharm intro', 'lalala..', 'draft', 4)

SELECT blog_authors.created_at AS blog_authors_created_at,
       blog_authors.id         AS blog_authors_id,
       blog_authors.name       AS blog_authors_name,
       blog_authors.user_id    AS blog_authors_user_id
FROM blog_authors
WHERE blog_authors.id = 4;

SELECT blog_articles.created_at AS blog_articles_created_at,
       blog_articles.id         AS blog_articles_id,
       blog_articles.title      AS blog_articles_title,
       blog_articles.body       AS blog_articles_body,
       blog_articles.status     AS blog_articles_status,
       blog_articles.author_id  AS blog_articles_author_id
FROM blog_articles
WHERE 4 = blog_articles.author_id;
