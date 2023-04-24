CREATE TABLE users
(
    id         SERIAL                                    NOT NULL,
    username   VARCHAR(30)                               NOT NULL,
    email      VARCHAR(180),
    archived   BOOLEAN                     DEFAULT false NOT NULL,
    created_at TIMESTAMP WITHOUT TIME ZONE DEFAULT now() NOT NULL,
    PRIMARY KEY (id),
    UNIQUE (username),
    UNIQUE (email)
);

--
INSERT INTO users (username, email, archived)
VALUES ('john', 'john@example.com', FALSE)
RETURNING users.id;
-- COMMIT
SELECT users.id         AS users_id,
       users.username   AS users_username,
       users.email      AS users_email,
       users.archived   AS users_archived,
       users.created_at AS users_created_at
FROM users
WHERE users.id = 1;

SELECT users.id         AS users_id,
       users.username   AS users_username,
       users.email      AS users_email,
       users.archived   AS users_archived,
       users.created_at AS users_created_at
FROM users
WHERE users.id = 4;