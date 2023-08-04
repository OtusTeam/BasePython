-- INFO  [alembic.runtime.migration] Context impl PostgresqlImpl.
-- INFO  [alembic.runtime.migration] Generating static SQL
-- INFO  [alembic.runtime.migration] Will assume transactional DDL.
BEGIN;

CREATE TABLE alembic_version
(
    version_num VARCHAR(32) NOT NULL,
    CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num)
);

-- INFO  [alembic.runtime.migration] Running upgrade  -> b817b17bd18d, create table users
-- Running upgrade  -> b817b17bd18d

CREATE TABLE users
(
    id         SERIAL                                    NOT NULL,
    username   VARCHAR(32)                               NOT NULL,
    created_at TIMESTAMP WITHOUT TIME ZONE DEFAULT now() NOT NULL,
    PRIMARY KEY (id),
    UNIQUE (username)
);

INSERT INTO alembic_version (version_num)
VALUES ('b817b17bd18d')
RETURNING alembic_version.version_num;

-- INFO  [alembic.runtime.migration] Running upgrade b817b17bd18d -> abd9048193a4, create table posts
-- Running upgrade b817b17bd18d -> abd9048193a4

CREATE TABLE posts
(
    id           SERIAL                                    NOT NULL,
    title        VARCHAR(100)                              NOT NULL,
    body         TEXT                        DEFAULT ''    NOT NULL,
    published_at TIMESTAMP WITHOUT TIME ZONE DEFAULT now() NOT NULL,
    user_id      INTEGER                                   NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (user_id) REFERENCES users (id)
);

UPDATE alembic_version
SET version_num='abd9048193a4'
WHERE alembic_version.version_num = 'b817b17bd18d';

-- INFO  [alembic.runtime.migration] Running upgrade abd9048193a4 -> 6d5b046467a8, add email to users table
-- Running upgrade abd9048193a4 -> 6d5b046467a8

ALTER TABLE users
    ADD COLUMN email VARCHAR(100);

ALTER TABLE users
    ADD CONSTRAINT users_unique_email UNIQUE (email);

UPDATE alembic_version
SET version_num='6d5b046467a8'
WHERE alembic_version.version_num = 'abd9048193a4';

-- INFO  [alembic.runtime.migration] Running upgrade 6d5b046467a8 -> 8cb72ea7e203, add is_staff col to users table
-- Running upgrade 6d5b046467a8 -> 8cb72ea7e203

ALTER TABLE users
    ADD COLUMN is_staff BOOLEAN DEFAULT false NOT NULL;

UPDATE alembic_version
SET version_num='8cb72ea7e203'
WHERE alembic_version.version_num = '6d5b046467a8';

COMMIT;

