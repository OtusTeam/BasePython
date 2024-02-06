BEGIN;

-- INFO  [alembic.runtime.migration] Running upgrade 4bfe591983da -> 0a665288abf8, add email col to users table
-- Running upgrade 4bfe591983da -> 0a665288abf8

ALTER TABLE users
    ADD COLUMN email VARCHAR;

ALTER TABLE users
    ADD CONSTRAINT ix_unique_email UNIQUE (email);

UPDATE alembic_version
SET version_num='0a665288abf8'
WHERE alembic_version.version_num = '4bfe591983da';

COMMIT;

--

BEGIN;

-- INFO  [alembic.runtime.migration] Running upgrade 25f86d432e94 -> 4bfe591983da, create table posts
-- Running upgrade 25f86d432e94 -> 4bfe591983da

CREATE TABLE posts
(
    id           SERIAL                                    NOT NULL,
    title        VARCHAR(100)                DEFAULT ''    NOT NULL,
    published_at TIMESTAMP WITHOUT TIME ZONE DEFAULT now() NOT NULL,
    user_id      INTEGER                                   NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (user_id) REFERENCES users (id)
);

UPDATE alembic_version
SET version_num='4bfe591983da'
WHERE alembic_version.version_num = '25f86d432e94';

-- INFO  [alembic.runtime.migration] Running upgrade 4bfe591983da -> 0a665288abf8, add email col to users table
-- Running upgrade 4bfe591983da -> 0a665288abf8

ALTER TABLE users
    ADD COLUMN email VARCHAR;

ALTER TABLE users
    ADD CONSTRAINT ix_unique_email UNIQUE (email);

UPDATE alembic_version
SET version_num='0a665288abf8'
WHERE alembic_version.version_num = '4bfe591983da';

COMMIT;

--

BEGIN;

-- INFO  [alembic.runtime.migration] Running upgrade 25f86d432e94 -> 4bfe591983da, create table posts
-- Running upgrade 25f86d432e94 -> 4bfe591983da

CREATE TABLE posts
(
    id           SERIAL                                    NOT NULL,
    title        VARCHAR(100)                DEFAULT ''    NOT NULL,
    published_at TIMESTAMP WITHOUT TIME ZONE DEFAULT now() NOT NULL,
    user_id      INTEGER                                   NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (user_id) REFERENCES users (id)
);

UPDATE alembic_version
SET version_num='4bfe591983da'
WHERE alembic_version.version_num = '25f86d432e94';

-- INFO  [alembic.runtime.migration] Running upgrade 4bfe591983da -> 0a665288abf8, add email col to users table
-- Running upgrade 4bfe591983da -> 0a665288abf8

ALTER TABLE users
    ADD COLUMN email VARCHAR;

ALTER TABLE users
    ADD CONSTRAINT ix_unique_email UNIQUE (email);

UPDATE alembic_version
SET version_num='0a665288abf8'
WHERE alembic_version.version_num = '4bfe591983da';

COMMIT;

