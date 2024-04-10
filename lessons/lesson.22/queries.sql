BEGIN;

-- INFO  [alembic.runtime.migration] Running upgrade d7c62b9242fd -> c8f3228ed335, title on posts now 80
-- Running upgrade d7c62b9242fd -> c8f3228ed335

ALTER TABLE posts ALTER COLUMN title TYPE VARCHAR(80);

UPDATE alembic_version
SET version_num='c8f3228ed335'
WHERE alembic_version.version_num = 'd7c62b9242fd';

COMMIT;


BEGIN;

-- INFO  [alembic.runtime.migration] Running upgrade a3435736b6a7 -> d7c62b9242fd, add bio to users
-- Running upgrade a3435736b6a7 -> d7c62b9242fd

ALTER TABLE users
    ADD COLUMN bio VARCHAR(200);

UPDATE alembic_version
SET version_num='d7c62b9242fd'
WHERE alembic_version.version_num = 'a3435736b6a7';

-- INFO  [alembic.runtime.migration] Running upgrade d7c62b9242fd -> c8f3228ed335, title on posts now 80
-- Running upgrade d7c62b9242fd -> c8f3228ed335

ALTER TABLE posts ALTER COLUMN title TYPE VARCHAR(80);

UPDATE alembic_version
SET version_num='c8f3228ed335'
WHERE alembic_version.version_num = 'd7c62b9242fd';

COMMIT;


--

BEGIN;

-- INFO  [alembic.runtime.migration] Running upgrade d7c62b9242fd -> c8f3228ed335, title on posts now 80
-- Running upgrade d7c62b9242fd -> c8f3228ed335

UPDATE posts
SET title=SUBSTRING(posts.title FROM 0 FOR 81)
WHERE length(posts.title) > 80;

ALTER TABLE posts ALTER COLUMN title TYPE VARCHAR(80);

UPDATE alembic_version
SET version_num='c8f3228ed335'
WHERE alembic_version.version_num = 'd7c62b9242fd';

COMMIT;


BEGIN;

-- INFO  [alembic.runtime.migration] Running upgrade c8f3228ed335 -> 0ff6b81dd0ac, add ref_code to users table
-- Running upgrade c8f3228ed335 -> 0ff6b81dd0ac

ALTER TABLE users ADD COLUMN ref_code VARCHAR(10);

ALTER TABLE users ADD CONSTRAINT unique_ix_ref_code UNIQUE (ref_code);

UPDATE alembic_version SET version_num='0ff6b81dd0ac' WHERE alembic_version.version_num = 'c8f3228ed335';

COMMIT;

BEGIN;

-- INFO  [alembic.runtime.migration] Running downgrade 0ff6b81dd0ac -> c8f3228ed335, add ref_code to users table
-- Running downgrade 0ff6b81dd0ac -> c8f3228ed335

ALTER TABLE users DROP CONSTRAINT unique_ix_ref_code;

ALTER TABLE users DROP COLUMN ref_code;

UPDATE alembic_version SET version_num='c8f3228ed335' WHERE alembic_version.version_num = '0ff6b81dd0ac';

COMMIT;



