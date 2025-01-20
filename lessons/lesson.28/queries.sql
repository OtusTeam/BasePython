-- INFO  [alembic.runtime.migration] Running upgrade 53356bff487f -> 9b2929a6afb3, add email col to author table
-- Running upgrade 53356bff487f -> 9b2929a6afb3
BEGIN;

ALTER TABLE author
    ADD COLUMN email VARCHAR(250);

SELECT COUNT(*)
FROM author;

ALTER TABLE author
    ADD CONSTRAINT uq_author_email UNIQUE (email);

UPDATE alembic_version
SET version_num='9b2929a6afb3'
WHERE alembic_version.version_num = '53356bff487f';

COMMIT;


--

BEGIN;

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

