
```sql
BEGIN;

-- Running upgrade 15b552bb6f57 -> 4f33531e2e61

UPDATE post
SET slug=regexp_replace(regexp_replace(lower(post.title), '[^a-z0-9]+', '-', 'g'), '-', '-')
WHERE post.slug IS NULL;

ALTER TABLE post
    ALTER COLUMN slug SET NOT NULL;

UPDATE alembic_version
SET version_num='4f33531e2e61'
WHERE alembic_version.version_num = '15b552bb6f57';

COMMIT;

```
