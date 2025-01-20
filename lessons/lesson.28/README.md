Инструкция для админа базы:

Раскатить миграцию:

```sql
BEGIN;
-- Running upgrade 14bc8e509acf -> a5390146783a

UPDATE author SET ref_code=SUBSTRING(md5(CAST(random() AS VARCHAR)) FROM 1 FOR 6) WHERE author.ref_code IS NULL;

ALTER TABLE author ALTER COLUMN ref_code SET NOT NULL;

UPDATE alembic_version SET version_num='a5390146783a' WHERE alembic_version.version_num = '14bc8e509acf';

COMMIT;
```

или

вот две миграции, они в рамках одной транзакции

```sql
-- первая: [описание]

BEGIN;

-- INFO  [alembic.runtime.migration] Running upgrade faa4416c842b -> 14bc8e509acf, add ref_code to author table
-- Running upgrade faa4416c842b -> 14bc8e509acf

ALTER TABLE author
    ADD COLUMN ref_code VARCHAR;

ALTER TABLE author
    ADD CONSTRAINT uq_author_ref_code UNIQUE (ref_code);

UPDATE alembic_version
SET version_num='14bc8e509acf'
WHERE alembic_version.version_num = 'faa4416c842b';

-- INFO  [alembic.runtime.migration] Running upgrade 14bc8e509acf -> a5390146783a, make author.ref_code not null
-- Running upgrade 14bc8e509acf -> a5390146783a

UPDATE author
SET ref_code=SUBSTRING(md5(CAST(random() AS VARCHAR)) FROM 1 FOR 6)
WHERE author.ref_code IS NULL;

ALTER TABLE author
    ALTER COLUMN ref_code SET NOT NULL;

UPDATE alembic_version
SET version_num='a5390146783a'
WHERE alembic_version.version_num = '14bc8e509acf';

COMMIT;
```

Если будем откатывать релиз, то вот откат миграций:

```sql
BEGIN;

-- INFO  [alembic.runtime.migration] Running downgrade a5390146783a -> 14bc8e509acf, make author.ref_code not null
-- Running downgrade a5390146783a -> 14bc8e509acf

ALTER TABLE author
    ALTER COLUMN ref_code DROP NOT NULL;

UPDATE alembic_version
SET version_num='14bc8e509acf'
WHERE alembic_version.version_num = 'a5390146783a';

-- INFO  [alembic.runtime.migration] Running downgrade 14bc8e509acf -> faa4416c842b, add ref_code to author table
-- Running downgrade 14bc8e509acf -> faa4416c842b

ALTER TABLE author
    DROP CONSTRAINT uq_author_ref_code;

ALTER TABLE author
    DROP COLUMN ref_code;

UPDATE alembic_version
SET version_num='faa4416c842b'
WHERE alembic_version.version_num = '14bc8e509acf';

COMMIT;

```