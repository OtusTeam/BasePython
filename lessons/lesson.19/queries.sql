-- UPGRADE

-- ➜ alembic upgrade --sql 4fb7:3a8585
BEGIN;

-- INFO  [alembic.runtime.migration] Running upgrade 4fb730957be6 -> e9dbb556d516, upgrade users: add archived column
-- Running upgrade 4fb730957be6 -> e9dbb556d516

ALTER TABLE blog_users ADD COLUMN archived BOOLEAN DEFAULT false NOT NULL;

UPDATE alembic_version SET version_num='e9dbb556d516' WHERE alembic_version.version_num = '4fb730957be6';

-- INFO  [alembic.runtime.migration] Running upgrade e9dbb556d516 -> 3a8585c93e66, upgrade users: add created_at column
-- Running upgrade e9dbb556d516 -> 3a8585c93e66

ALTER TABLE blog_users ADD COLUMN created_at TIMESTAMP WITHOUT TIME ZONE DEFAULT now() NOT NULL;

UPDATE alembic_version SET version_num='3a8585c93e66' WHERE alembic_version.version_num = 'e9dbb556d516';

COMMIT;


-- DOWNGRADE


-- ➜ alembic downgrade --sql 3a8585:4fb7
BEGIN;

-- INFO  [alembic.runtime.migration] Running downgrade 3a8585c93e66 -> e9dbb556d516, upgrade users: add created_at column
-- Running downgrade 3a8585c93e66 -> e9dbb556d516

ALTER TABLE blog_users DROP COLUMN created_at;

UPDATE alembic_version SET version_num='e9dbb556d516' WHERE alembic_version.version_num = '3a8585c93e66';

-- INFO  [alembic.runtime.migration] Running downgrade e9dbb556d516 -> 4fb730957be6, upgrade users: add archived column
-- Running downgrade e9dbb556d516 -> 4fb730957be6

ALTER TABLE blog_users DROP COLUMN archived;

UPDATE alembic_version SET version_num='4fb730957be6' WHERE alembic_version.version_num = 'e9dbb556d516';

COMMIT;


-- update

BEGIN;

-- Running upgrade c0856bbe4253 -> c25b4a0ef56d

ALTER TABLE blog_authors ADD COLUMN bio VARCHAR DEFAULT '' NOT NULL;

UPDATE blog_authors SET bio=blog_users.bio
            FROM blog_users WHERE blog_authors.user_id = blog_users.id;

UPDATE alembic_version SET version_num='c25b4a0ef56d' WHERE alembic_version.version_num = 'c0856bbe4253';

COMMIT;



