CREATE TABLE users
(
    id         SERIAL NOT NULL,
    username   VARCHAR(20),
    archived   BOOLEAN,
    created_at TIMESTAMP WITHOUT TIME ZONE,
    PRIMARY KEY (id),
    UNIQUE (username)
);


CREATE TABLE users
(
    left_id    INTEGER NOT NULL,
    right_id   INTEGER NOT NULL,
    username   VARCHAR(20),
    archived   BOOLEAN,
    created_at TIMESTAMP WITHOUT TIME ZONE,
    PRIMARY KEY (left_id, right_id),
    UNIQUE (username)
);

CREATE TABLE users
(
    id         VARCHAR NOT NULL,
    username   VARCHAR(20),
    archived   BOOLEAN,
    created_at TIMESTAMP WITHOUT TIME ZONE,
    PRIMARY KEY (id),
    UNIQUE (username)
);

CREATE TABLE users
(
    id         INTEGER NOT NULL,
    username   VARCHAR(20),
    archived   BOOLEAN,
    created_at TIMESTAMP WITHOUT TIME ZONE,
    PRIMARY KEY (id),
    UNIQUE (username)
);

CREATE TABLE users
(
    id         SERIAL                NOT NULL,
    username   VARCHAR(20),
    archived   BOOLEAN DEFAULT FALSE NOT NULL,
    created_at TIMESTAMP WITHOUT TIME ZONE DEFAULT now() NOT NULL,
    PRIMARY KEY (id),
    UNIQUE (username)
);


INSERT INTO users (username, archived)
VALUES ('john', FALSE) RETURNING users.id


SELECT users.id         AS users_id,
       users.username   AS users_username,
       users.archived   AS users_archived,
       users.created_at AS users_created_at
FROM users
WHERE users.id = 1;


SELECT users.id         AS users_id,
       users.username   AS users_username,
       users.archived   AS users_archived,
       users.created_at AS users_created_at
FROM users
WHERE users.id IN (0, 1, 2, 3);

SELECT users.id         AS users_id,
       users.username   AS users_username,
       users.archived   AS users_archived,
       users.created_at AS users_created_at
FROM users
WHERE users.username ILIKE '%n%';


UPDATE users
SET archived = TRUE
WHERE users.id = 3;
