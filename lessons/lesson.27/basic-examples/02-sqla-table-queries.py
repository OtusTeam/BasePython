from sqlalchemy import (
    create_engine,
    Table,
    MetaData,
    Column,
    Integer,
    String,
    insert,
    select,
)
from sqlalchemy.engine import row
from sqlalchemy.sql.functions import user

import config

engine = create_engine(
    url=config.SQLA_DB_URL,
    echo=config.SQLA_DB_ECHO,
)

metadata = MetaData()

users_table_name = "users"
users_table = Table(
    users_table_name,
    metadata,
    Column(
        "id",
        Integer,
        primary_key=True,
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
    ),
    Column(
        "full_name",
        String(100),
        nullable=False,
        server_default="",
    ),
)


def create_tables() -> None:
    # print(metadata.tables)
    # методы drop_all / create_all только для быстрой проверки, для быстрого создания.
    metadata.drop_all(engine)
    metadata.create_all(engine)


def insert_values() -> None:
    new_users_values = [
        {
            users_table.c.username: "bob",
            users_table.c.email: "bob@example.com",
            users_table.c.full_name: "Bob White",
        },
        {
            users_table.c.username: "alice",
            users_table.c.email: None,
            users_table.c.full_name: "Alice White",
        },
        {
            users_table.c.username: "john",
            users_table.c.email: None,
            users_table.c.full_name: "",
        },
    ]
    statement = insert(users_table).values(new_users_values)
    print(statement)
    print(repr(statement))

    with engine.connect() as conn:
        conn.execute(statement)
        conn.commit()


def fetch_values() -> None:
    # statement = select(users_table).order_by(users_table.c.id)
    match_email_domain = "example.com"
    filter_value = f"%@{match_email_domain}"
    statement = (
        select(users_table)
        .where(
            # users_table.c.username == "bob",
            # users_table.c.email == filter_value,
            users_table.c.email.like(filter_value),
        )
        .order_by(users_table.c.id)
    )

    with engine.connect() as conn:
        result = conn.execute(statement)

    for row in result:
        print(row)
        print(row.id, row.username, row.email, row.full_name)
        # print(row[0], row[1], row[2], row[3])


def main() -> None:
    # create_tables()
    # insert_values()
    # fetch_values()
    print(metadata)
    print(metadata.tables)
    print(repr(metadata.tables[users_table_name]))
    print(repr(users_table))


# чисто для информации!
# мы в реальности не копируем это сюда в код!
# это только для демо - что было АВТОМАТИЧЕСКИ сгенерировано из нашего кода.

SQL = """\
CREATE TABLE users (
	id INTEGER NOT NULL, 
	username VARCHAR(32) NOT NULL, 
	email VARCHAR(150), 
	full_name VARCHAR(100) DEFAULT '' NOT NULL, 
	PRIMARY KEY (id), 
	UNIQUE (username), 
	UNIQUE (email)
);
"""

if __name__ == "__main__":
    main()
