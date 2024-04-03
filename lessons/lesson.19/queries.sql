INSERT INTO authors (username, email)
VALUES ('john'::VARCHAR, NULL)
RETURNING authors.id;

CREATE TABLE users
(
    id       SERIAL      NOT NULL,
    username VARCHAR(32) NOT NULL,
    email    VARCHAR,
    PRIMARY KEY (id),
    UNIQUE (username),
    UNIQUE (email)
);

SELECT users.id       AS users_id
     , users.username AS users_username
     , users.email    AS users_email
FROM users
WHERE users.id = 1::INTEGER;


INSERT INTO users (username, email)
SELECT p0::VARCHAR, p1::VARCHAR
FROM (VALUES ('a'::VARCHAR, NULL, 0),
             ('b'::VARCHAR, NULL, 1),
             ('c', NULL, 2)) AS imp_sen(p0, p1, sen_counter)
ORDER BY sen_counter
RETURNING users.id, users.id AS id__1;


UPDATE users
SET email=concat(lower(users.username), '@example.com'::VARCHAR)
WHERE users.email IS NULL
  AND length(users.username) > 1::INTEGER
RETURNING users.id;
