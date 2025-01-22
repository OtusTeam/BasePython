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


--
BEGIN;

SELECT tag.name
     , tag.created_at
     , tag.id
FROM tag
ORDER BY tag.name;


SELECT publication.title
     , publication.body
     , publication.author_id
     , publication.created_at
     , publication.id
FROM publication
ORDER BY publication.id;


SELECT publication_1.id AS publication_1_id
     , tag.name         AS tag_name
     , tag.created_at   AS tag_created_at
     , tag.id           AS tag_id
FROM publication AS publication_1
         JOIN publication_tag_association AS publication_tag_association_1
              ON publication_1.id = publication_tag_association_1.publication_id
         JOIN tag ON tag.id = publication_tag_association_1.tag_id
WHERE publication_1.id IN (1, 2, 3, 4, 5);

INSERT INTO publication_tag_association (publication_id, tag_id)
VALUES (2, 3),
       (2, 4),
       (3, 1),
       (3, 2),
       (4, 2),
       (4, 4),
       (5, 5),
       (5, 6),
       (1, 1),
       (1, 3);

COMMIT;


--
--
--


SELECT publication.title
     , publication.body
     , publication.author_id
     , publication.created_at
     , publication.id
FROM publication
WHERE (publication.title LIKE '%%' || 'Go' || '%%')
LIMIT 1;

SELECT tag.name, tag.created_at, tag.id
FROM tag
WHERE tag.name = 'python';

SELECT tag.name       AS tag_name
     , tag.created_at AS tag_created_at
     , tag.id         AS tag_id
FROM tag,
     publication_tag_association
WHERE 5 = publication_tag_association.publication_id
  AND tag.id = publication_tag_association.tag_id;

INSERT INTO publication_tag_association (publication_id, tag_id)
VALUES (5, 2);

COMMIT;
-- saved association


BEGIN
SELECT publication.title      AS publication_title
     , publication.body       AS publication_body
     , publication.author_id  AS publication_author_id
     , publication.created_at AS publication_created_at
     , publication.id         AS publication_id
FROM publication
WHERE publication.id = 5;

SELECT tag.name AS tag_name, tag.created_at AS tag_created_at, tag.id AS tag_id
FROM tag,
     publication_tag_association
WHERE 5 = publication_tag_association.publication_id
  AND tag.id = publication_tag_association.tag_id;


DELETE
FROM publication_tag_association
WHERE publication_tag_association.publication_id = 5
  AND publication_tag_association.tag_id = 2;

COMMIT;
-- removed association


--

DELETE FROM publication_tag_association
       WHERE publication_tag_association.publication_id = 5
         AND publication_tag_association.tag_id = 2;
