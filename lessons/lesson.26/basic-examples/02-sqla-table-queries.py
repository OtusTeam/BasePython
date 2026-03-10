from sqlalchemy import (
    create_engine,
    Table,
    MetaData,
    Column,
    Integer,
    String,
    insert,
    select,
    desc,
)

import config


engine = create_engine(
    url=config.DB_URL,
    echo=config.DB_ECHO,
)

metadata = MetaData()


users_table = Table(
    "users",
    metadata,
    Column(
        "id",
        Integer,
        primary_key=True,
        # autoincrement=True,
        nullable=False,
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
        nullable=True,
        default="",
        server_default="",
    ),
)


# не нужно это сюда копировать!
# этот код я скопировал только для демонстрации и отладки.
sql = """
CREATE TABLE users (
	id INTEGER NOT NULL, 
	username VARCHAR(32) NOT NULL, 
	email VARCHAR(150), 
	full_name VARCHAR(100) DEFAULT '', 
	PRIMARY KEY (id), 
	UNIQUE (username), 
	UNIQUE (email)
)
"""


def create_table() -> None:
    # print({"users": users_table})
    # print(metadata.tables)
    metadata.drop_all(bind=engine)
    metadata.create_all(bind=engine)


def insert_values() -> None:
    new_users_data = [
        {
            users_table.c.username: "bob",
            users_table.c.email: "bob@example.com",
            users_table.c.full_name: "Bob White",
        },
        {
            users_table.c.username: "john",
            users_table.c.email: "john@example.com",
            users_table.c.full_name: "Johnathan",
        },
        {
            users_table.c.username: "alice",
            users_table.c.email: None,
            users_table.c.full_name: "",
        },
    ]
    statement = insert(users_table).values(new_users_data)
    print(statement)
    print(repr(statement))

    with engine.connect() as conn:
        conn.execute(statement)
        conn.commit()


def fetch_values() -> None:
    """
    Example queries
    """
    # пример сформированного запроса
    """
    SELECT users.id
         , users.username
         , users.email
         , users.full_name 
    FROM users 
    WHERE users.email IS NOT NULL
    ORDER BY users.username DESC
    """
    statement = (
        select(users_table)
        .where(
            users_table.c.email.isnot(None),
        )
        .order_by(desc(users_table.c.username))
    )
    print(statement)
    print(repr(statement))
    with engine.connect() as conn:
        result = conn.execute(statement)

    for row in result:
        # print(row)
        print(row.id, row.username, row.email, row.full_name)


def main() -> None:
    # create_table()
    # insert_values()
    fetch_values()


if __name__ == "__main__":
    main()
