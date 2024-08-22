BEGIN;

-- INFO  [alembic.runtime.migration] Running upgrade 1b73fc0146b7 -> 73b181dd7485, Make not null username col on owners table
-- Running upgrade 1b73fc0146b7 -> 73b181dd7485

UPDATE owners
SET username=SUBSTRING(md5(CAST(owners.id AS VARCHAR)) FROM 1 FOR 6)
WHERE owners.username IS NULL;

ALTER TABLE owners
    ALTER COLUMN username SET NOT NULL;

UPDATE alembic_version
SET version_num='73b181dd7485'
WHERE alembic_version.version_num = '1b73fc0146b7';

COMMIT;
