UPDATE users
SET token=gen_random_uuid()
WHERE users.token IS NULL;

ALTER TABLE users
    ALTER COLUMN token SET NOT NULL;

UPDATE alembic_version
SET version_num='ce8e6b03a61b'
WHERE alembic_version.version_num = '6dc8719d3457';

COMMIT;


