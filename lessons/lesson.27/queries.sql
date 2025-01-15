CREATE TABLE authors
(
    id    INTEGER         NOT NULL,
    name  VARCHAR(200)    NOT NULL,
    email VARCHAR(250),
    bio   TEXT DEFAULT '' NOT NULL,
    PRIMARY KEY (id),
    UNIQUE (email)
)


CREATE TABLE publication
(
    title      VARCHAR                              NOT NULL,
    body       TEXT     DEFAULT ''                  NOT NULL,
    created_at DATETIME DEFAULT (CURRENT_TIMESTAMP) NOT NULL,
    id         INTEGER                              NOT NULL,
    PRIMARY KEY (id)
)


CREATE TABLE publication
(
    id         INTEGER                              NOT NULL,
    title      VARCHAR                              NOT NULL,
    body       TEXT     DEFAULT ''                  NOT NULL,
    author_id  INTEGER                              NOT NULL,
    created_at DATETIME DEFAULT (CURRENT_TIMESTAMP) NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (author_id) REFERENCES author (id)
)


SELECT publication.title
     , publication.body
     , publication.author_id
     , publication.created_at
     , publication.id
     , author_1.name
     , author_1.email
     , author_1.bio
     , author_1.id AS id_1
FROM publication
         LEFT OUTER JOIN author AS author_1
             ON author_1.id = publication.author_id
ORDER BY publication.title;


--         select(Author)
--         .options(
--             selectinload(Author.publications),
--         )
--         .order_by(Author.id)
