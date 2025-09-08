


BEGIN;

-- INFO  [alembic.runtime.migration] Running upgrade 02efe881123b -> 03dff9349f46, make email column not null
-- Running upgrade 02efe881123b -> 03dff9349f46

UPDATE users
SET email=(users.username || '@invalid.mail')
WHERE users.email IS NULL;

ALTER TABLE users
ALTER COLUMN email
SET NOT NULL;

UPDATE alembic_version SET version_num='03dff9349f46'
           WHERE alembic_version.version_num = '02efe881123b';

COMMIT;

---

BEGIN;

-- INFO  [alembic.runtime.migration] Running downgrade 03dff9349f46 -> 02efe881123b, make email column not null
-- Running downgrade 03dff9349f46 -> 02efe881123b

ALTER TABLE users ALTER COLUMN email DROP NOT NULL;

UPDATE alembic_version SET version_num='02efe881123b'
           WHERE alembic_version.version_num = '03dff9349f46';

COMMIT;
