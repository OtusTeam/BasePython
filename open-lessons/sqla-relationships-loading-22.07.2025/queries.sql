CREATE TABLE datacenters
(
    name        VARCHAR(80)                               NOT NULL,
    description VARCHAR                     DEFAULT ''    NOT NULL,
    created_at  TIMESTAMP WITHOUT TIME ZONE DEFAULT now() NOT NULL,
    PRIMARY KEY (name)
);

CREATE TABLE users
(
    username   VARCHAR(32)                               NOT NULL,
    datacenter VARCHAR(80)                               NOT NULL,
    id         SERIAL                                    NOT NULL,
    created_at TIMESTAMP WITHOUT TIME ZONE DEFAULT now() NOT NULL,
    PRIMARY KEY (id),
    UNIQUE (username),
    FOREIGN KEY (datacenter) REFERENCES datacenters (name)
);

CREATE TABLE articles
(
    title      VARCHAR(100)                              NOT NULL,
    text       TEXT                        DEFAULT ''    NOT NULL,
    user_id    INTEGER                                   NOT NULL,
    id         SERIAL                                    NOT NULL,
    created_at TIMESTAMP WITHOUT TIME ZONE DEFAULT now() NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (user_id) REFERENCES users (id)
);

CREATE INDEX ix_articles_title ON articles (title);

CREATE TABLE profiles
(
    about      VARCHAR                     DEFAULT ''    NOT NULL,
    site       VARCHAR(4096)               DEFAULT ''    NOT NULL,
    user_id    INTEGER                                   NOT NULL,
    id         SERIAL                                    NOT NULL,
    created_at TIMESTAMP WITHOUT TIME ZONE DEFAULT now() NOT NULL,
    PRIMARY KEY (id),
    UNIQUE (user_id),
    FOREIGN KEY (user_id) REFERENCES users (id)
);

--

SELECT users.username
     , users.datacenter
     , users.id
     , users.created_at
     , profiles_1.about
     , profiles_1.site
     , profiles_1.user_id
     , profiles_1.id         AS id_1
     , profiles_1.created_at AS created_at_1
FROM users
         LEFT OUTER JOIN profiles AS profiles_1
                         ON users.id = profiles_1.user_id
ORDER BY users.id;

--

SELECT users.username
     , users.datacenter
     , users.id
     , users.created_at
     , profiles_1.about
     , profiles_1.site
     , profiles_1.user_id
     , profiles_1.id         AS id_1
     , profiles_1.created_at AS created_at_1
FROM users
         LEFT OUTER JOIN profiles AS profiles_1 ON users.id = profiles_1.user_id
ORDER BY users.id;

SELECT articles.user_id    AS articles_user_id
     , articles.title      AS articles_title
     , articles.text       AS articles_text
     , articles.id         AS articles_id
     , articles.created_at AS articles_created_at
FROM articles
WHERE articles.user_id IN (1, 2, 3, 4, 5, 6, 7);

--

SELECT users.username
     , users.datacenter
     , users.id
     , users.created_at
     , profiles_1.about
     , profiles_1.site
     , profiles_1.user_id
     , profiles_1.id         AS id_1
     , profiles_1.created_at AS created_at_1
FROM users
         LEFT OUTER JOIN profiles AS profiles_1 ON users.id = profiles_1.user_id
ORDER BY users.id;

SELECT articles.title      AS articles_title
     , articles.text       AS articles_text
     , articles.user_id    AS articles_user_id
     , articles.id         AS articles_id
     , articles.created_at AS articles_created_at
     , anon_1.users_id     AS anon_1_users_id
FROM (SELECT users.id AS users_id
      FROM users) AS anon_1
         JOIN articles ON anon_1.users_id = articles.user_id

--

SELECT users.username
     , users.datacenter
     , users.id
     , users.created_at
     , articles_1.title
     , articles_1.text
     , articles_1.user_id
     , articles_1.id         AS id_1
     , articles_1.created_at AS created_at_1
     , profiles_1.about
     , profiles_1.site
     , profiles_1.user_id    AS user_id_1
     , profiles_1.id         AS id_2
     , profiles_1.created_at AS created_at_2
FROM users
         LEFT OUTER JOIN articles AS articles_1
                         ON users.id = articles_1.user_id
         LEFT OUTER JOIN profiles AS profiles_1
                         ON users.id = profiles_1.user_id
ORDER BY users.id;

--

SELECT articles.title
     , articles.text
     , articles.user_id
     , articles.id
     , articles.created_at
     , users_1.username
     , users_1.datacenter
     , users_1.id         AS id_1
     , users_1.created_at AS created_at_1
FROM articles
         LEFT OUTER JOIN users AS users_1
                         ON users_1.id = articles.user_id
ORDER BY articles.user_id, articles.title;

--

SELECT articles.title
     , articles.text
     , articles.user_id
     , articles.id
     , articles.created_at
     , profiles_1.about
     , profiles_1.site
     , profiles_1.user_id    AS user_id_1
     , profiles_1.id         AS id_1
     , profiles_1.created_at AS created_at_1
     , users_1.username
     , users_1.datacenter
     , users_1.id            AS id_2
     , users_1.created_at    AS created_at_2
FROM articles
         LEFT OUTER JOIN users AS users_1 ON users_1.id = articles.user_id
         LEFT OUTER JOIN profiles AS profiles_1 ON users_1.id = profiles_1.user_id
ORDER BY articles.user_id, articles.title;

---

SELECT users.username
     , users.datacenter
     , users.id
     , users.created_at
     , datacenters_1.name
     , datacenters_1.description
     , datacenters_1.created_at AS created_at_1
     , profiles_1.about
     , profiles_1.site
     , profiles_1.user_id
     , profiles_1.id            AS id_1
     , profiles_1.created_at    AS created_at_2
FROM users
         LEFT OUTER JOIN datacenters AS datacenters_1 ON datacenters_1.name = users.datacenter
         LEFT OUTER JOIN profiles AS profiles_1 ON users.id = profiles_1.user_id
ORDER BY users.id;


SELECT articles.user_id    AS articles_user_id
     , articles.title      AS articles_title
     , articles.text       AS articles_text
     , articles.id         AS articles_id
     , articles.created_at AS articles_created_at
FROM articles
WHERE articles.user_id IN (1, 2, 3, 4, 5, 6, 7);

--
SELECT users.username
     , users.datacenter
     , users.id
     , users.created_at
     , profiles_1.about
     , profiles_1.site
     , profiles_1.user_id
     , profiles_1.id         AS id_1
     , profiles_1.created_at AS created_at_1
FROM users
         LEFT OUTER JOIN profiles AS profiles_1 ON users.id = profiles_1.user_id
ORDER BY users.id;

SELECT articles.user_id    AS articles_user_id
     , articles.title      AS articles_title
     , articles.text       AS articles_text
     , articles.id         AS articles_id
     , articles.created_at AS articles_created_at
FROM articles
WHERE articles.user_id IN (1, 2, 3, 4, 5, 6, 7);

SELECT datacenters.name        AS datacenters_name
     , datacenters.description AS datacenters_description
     , datacenters.created_at  AS datacenters_created_at
FROM datacenters
WHERE datacenters.name IN ('dc1', 'dc2')
