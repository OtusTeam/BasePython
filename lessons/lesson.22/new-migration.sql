-- COMMAND: alembic downgrade --sql 3a8585:4fb7 > new-migration.sql


BEGIN;

-- Running downgrade 3a8585c93e66 -> e9dbb556d516

ALTER TABLE blog_users DROP COLUMN created_at;

UPDATE alembic_version SET version_num='e9dbb556d516' WHERE alembic_version.version_num = '3a8585c93e66';

-- Running downgrade e9dbb556d516 -> 4fb730957be6

ALTER TABLE blog_users DROP COLUMN archived;

UPDATE alembic_version SET version_num='4fb730957be6' WHERE alembic_version.version_num = 'e9dbb556d516';

COMMIT;

