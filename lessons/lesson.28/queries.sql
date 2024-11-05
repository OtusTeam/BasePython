--
BEGIN;

SELECT tag.name, tag.created_at, tag.id
FROM tag
ORDER BY tag.id;

SELECT author.name
     , author.username
     , author.email
     , author.promocode
     , author.joined_at
     , author.id
FROM author
WHERE author.username = 'bob';


-- fetched author by username 'bob': Author(id=1, name='Bob', username='bob', email='bob@example.com')

INSERT INTO publication (title, body, author_id)
VALUES ('Spam And Eggs HowTo', '', 1)
RETURNING publication.id
    COMMIT;


BEGIN;
SELECT publication.title     AS publication_title
     , publication.body      AS publication_body
     , publication.author_id AS publication_author_id
     , publication.id        AS publication_id
FROM publication
WHERE publication.id = 7;

-- created publication
-- Publication(id=7, title='Spam And Eggs HowTo', author_id=1)

SELECT tag.name       AS tag_name
     , tag.created_at AS tag_created_at
     , tag.id         AS tag_id
FROM tag,
     publication_tag_association
WHERE 7 = publication_tag_association.publication_id
  AND tag.id = publication_tag_association.tag_id
-- publication's tags: []

-- SELECT tag.name AS tag_name, tag.created_at AS tag_created_at, tag.id AS tag_id
-- FROM tag
-- WHERE tag.id = %(pk_1)s::INTEGER
-- [generated in 0.00008s] {'pk_1': 1}
-- SELECT tag.name AS tag_name, tag.created_at AS tag_created_at, tag.id AS tag_id
-- FROM tag
-- WHERE tag.id = %(pk_1)s::INTEGER
-- [cached since 0.0009039s ago] {'pk_1': 2}
-- SELECT tag.name AS tag_name, tag.created_at AS tag_created_at, tag.id AS tag_id
-- FROM tag
-- WHERE tag.id = %(pk_1)s::INTEGER
-- [cached since 0.001658s ago] {'pk_1': 3}
INSERT INTO publication_tag_association (publication_id, tag_id)
VALUES (% s, % s)
-- [generated in 0.00004s] [{'publication_id': 7, 'tag_id': 1}, {'publication_id': 7, 'tag_id': 2}, {'publication_id': 7, 'tag_id': 3}]
-- SELECT tag.name AS tag_name, tag.created_at AS tag_created_at, tag.id AS tag_id
-- FROM tag
-- WHERE tag.id = %(pk_1)s::INTEGER
-- [cached since 0.004071s ago] {'pk_1': 1}
-- [Tag(name='foo', created_at=datetime.datetime(2024, 11, 5, 17, 21, 24, 933134)), Tag(name='spam', created_at=datetime.datetime(2024, 11, 5, 17, 23, 38, 955614)), Tag(name='eggs', created_at=datetime.datetime(2024, 11, 5, 17, 23, 38, 960591))]
COMMIT;
BEGIN;

SELECT publication.title     AS publication_title
     , publication.body      AS publication_body
     , publication.author_id AS publication_author_id
     , publication.id        AS publication_id
FROM publication
WHERE publication.id = 7;

SELECT tag.name       AS tag_name
     , tag.created_at AS tag_created_at
     , tag.id         AS tag_id
FROM tag,
     publication_tag_association
WHERE 7 = publication_tag_association.publication_id
  AND tag.id = publication_tag_association.tag_id;

-- publication's tags after commit: [Tag(name='foo', created_at=datetime.datetime(2024, 11, 5, 17, 21, 24, 933134)), Tag(name='spam', created_at=datetime.datetime(2024, 11, 5, 17, 23, 38, 955614)), Tag(name='eggs', created_at=datetime.datetime(2024, 11, 5, 17, 23, 38, 960591))]
ROLLBACK


--

SELECT publication.title
     , publication.body
     , publication.author_id
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
         JOIN tag
              ON tag.id = publication_tag_association_1.tag_id
WHERE publication_1.id IN (1,
                           2,
                           3,
                           4,
                           5,
                           6,
                           7);

--

DELETE FROM publication_tag_association
WHERE publication_tag_association.publication_id = 7 AND publication_tag_association.tag_id = 2
-- WHERE publication_tag_association.publication_id = 5 AND publication_tag_association.tag_id = 2

