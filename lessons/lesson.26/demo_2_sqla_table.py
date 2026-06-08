from sqlalchemy import (
    create_engine,
    MetaData,
    Table,
    Column,
    Integer,
    String,
    insert,
    select,
)

import config

engine = create_engine(
    url=config.DB_URL,
    echo=config.DB_ECHO,
)

metadata = MetaData()

authors_table = Table(
    "authors",
    metadata,
    Column(
        "id",
        Integer,
        primary_key=True,
        nullable=False,
        # autoincrement=
    ),
    Column(
        "username",
        String(32),
        unique=True,
        nullable=False,
    ),
    Column(
        "email",
        String(150),
        unique=True,
        nullable=True,
    ),
    Column(
        "full_name",
        String(100),
        nullable=False,
        # default="",
        server_default="",
    ),
)

# примерно такое будет сгенерировано
# руками писать это не нужно
# и копировать сюда из терминала тоже не нужно
some_name = """
CREATE TABLE authors (
	id INTEGER NOT NULL, 
	username VARCHAR(32) NOT NULL, 
	email VARCHAR(150), 
	full_name VARCHAR(100) DEFAULT '' NOT NULL, 
	PRIMARY KEY (id), 
	UNIQUE (username), 
	UNIQUE (email)
);
"""


def create_tables():
    print({"authors": authors_table})
    print(metadata.tables)
    metadata.drop_all(engine)  # удалит всё! безвозвратно
    metadata.create_all(engine)


def insert_authors():
    new_authors_data = [
        {
            authors_table.c.username: "john",
            authors_table.c.email: "john@example.com",
            authors_table.c.full_name: "",
        },
        {
            authors_table.c.username: "bob",
            authors_table.c.email: "bob@example.com",
            authors_table.c.full_name: "Bob Black",
        },
        {
            authors_table.c.username: "alice",
            authors_table.c.email: None,
            authors_table.c.full_name: "Alice",
        },
    ]
    statement = insert(authors_table).values(new_authors_data)
    print(statement)
    print(repr(statement))

    with engine.connect() as conn:
        conn.execute(statement)
        conn.commit()


def fetch_values():
    statement = (
        select(authors_table)
        .where(
            authors_table.c.email.isnot(None),
        )
        .order_by(
            authors_table.c.username.desc(),
        )
    )
    print(statement)
    print(repr(statement))

    with engine.connect() as conn:
        result = conn.execute(statement)

    for row in result:
        print(row.id, row.username, row.email, row.full_name)


def main():
    # create_tables()
    # insert_authors()
    fetch_values()


if __name__ == "__main__":
    main()
