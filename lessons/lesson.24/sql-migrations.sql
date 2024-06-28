
-- INFO  [alembic.runtime.migration] Context impl PostgresqlImpl.
-- INFO  [alembic.runtime.migration] Generating static SQL
-- INFO  [alembic.runtime.migration] Will assume transactional DDL.
BEGIN;

CREATE TABLE alembic_version (
    version_num VARCHAR(32) NOT NULL,
    CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num)
);

-- INFO  [alembic.runtime.migration] Running upgrade  -> 4e9f42ca9f65, create users table
-- -- Running upgrade  -> 4e9f42ca9f65
--
-- CREATE TABLE users (
--     id SERIAL NOT NULL,
--     username VARCHAR(32) NOT NULL,
--     email VARCHAR,
--     CONSTRAINT pk_users PRIMARY KEY (id),
--     CONSTRAINT uq_users_email UNIQUE (email),
--     CONSTRAINT uq_users_username UNIQUE (username)
-- );
--
-- INSERT INTO alembic_version (version_num) VALUES ('4e9f42ca9f65') RETURNING alembic_version.version_num;

-- INFO  [alembic.runtime.migration] Running upgrade 4e9f42ca9f65 -> 515a0d758e1b, create posts table
-- Running upgrade 4e9f42ca9f65 -> 515a0d758e1b

CREATE TABLE posts (
    id SERIAL NOT NULL,
    title VARCHAR(100) NOT NULL,
    published_at TIMESTAMP WITHOUT TIME ZONE,
    user_id INTEGER NOT NULL,
    CONSTRAINT pk_posts PRIMARY KEY (id),
    CONSTRAINT fk_posts_user_id_users FOREIGN KEY(user_id) REFERENCES users (id)
);

UPDATE alembic_version SET version_num='515a0d758e1b' WHERE alembic_version.version_num = '4e9f42ca9f65';

COMMIT;


--


-- INFO  [alembic.runtime.migration] Running upgrade 0bee249a8c0e -> 1d0e0468114b, not null ref code on users table
-- Running upgrade 0bee249a8c0e -> 1d0e0468114b

UPDATE users SET ref_code=SUBSTRING(md5(users.username) FROM 1 FOR 6) WHERE users.ref_code IS NULL;

ALTER TABLE users ALTER COLUMN ref_code SET NOT NULL;

UPDATE alembic_version SET version_num='1d0e0468114b' WHERE alembic_version.version_num = '0bee249a8c0e';

COMMIT;

