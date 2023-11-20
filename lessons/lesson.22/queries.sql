-- INFO  [alembic.runtime.migration] Running upgrade bf6af59287fe -> d43c2b46e4e1, add unique index to posts table
-- Running upgrade bf6af59287fe -> d43c2b46e4e1

ALTER TABLE posts
    ADD UNIQUE (title, published_at);

UPDATE alembic_version
SET version_num='d43c2b46e4e1'
WHERE alembic_version.version_num = 'bf6af59287fe';

COMMIT;

