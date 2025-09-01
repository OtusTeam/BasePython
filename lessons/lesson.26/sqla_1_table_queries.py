from sqlalchemy import (
    text,
    select,
    insert,
    Table,
    MetaData,
    Column,
    Integer,
    String,
)
from sqlalchemy import create_engine

engine = create_engine(
    "sqlite:///blog.db",
    echo=True,
)

metadata = MetaData()


users_table = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("username", String(32), nullable=False),
    Column("email", String(150), unique=True),
    Column(
        "full_name",
        String(100),
        nullable=False,
        server_default="",
    ),
)

# просто для удобства вставляю сюда то,
# что было сгенерировано и выполнено.
# не требуется делать это на своём проекте.
# это только демонстрация.
SQL_GENERATED = """
CREATE TABLE users (
	id INTEGER NOT NULL, 
	username VARCHAR(32) NOT NULL, 
	email VARCHAR(150), 
	full_name VARCHAR(100) DEFAULT '' NOT NULL, 
	PRIMARY KEY (id), 
	UNIQUE (email)
)
"""
# этот SQL запрос был сгенерирован алхимией.


def insert_users() -> None:

    statement = insert(users_table).values(
        [
            {
                users_table.c.username: "bob",
                users_table.c.email: "bob@example.com",
                users_table.c.full_name: "Bob White",
            },
            {
                users_table.c.username: "alice",
                users_table.c.email: None,
                users_table.c.full_name: "Alice Black",
            },
            {
                users_table.c.username: "john",
                users_table.c.email: None,
                users_table.c.full_name: "",
            },
        ]
    )
    # print(statement)
    with engine.connect() as conn:
        conn.execute(statement)
        conn.commit()


def main() -> None:
    print(repr(users_table))
    print(metadata.tables)
    metadata.create_all(engine)

    statement = select(users_table).order_by(users_table.c.id)
    with engine.connect() as conn:
        result = conn.execute(statement)

    for row in result:
        print(row)
        print(row.id, row.username, row.email, row.full_name)
        print(row[0], row[1], row[2])


if __name__ == "__main__":
    main()
