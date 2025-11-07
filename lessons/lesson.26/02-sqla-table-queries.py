from sqlalchemy import (
    create_engine,
    insert,
    select,
    Table,
    MetaData,
    Column,
    Integer,
    String,
)

import config

engine = create_engine(
    "sqlite:///blog-app.db",
    echo=config.SQLA_DB_ECHO,
)

metadata = MetaData()
users_table = Table(
    "users",
    metadata,
    Column(
        "id",
        Integer,
        primary_key=True,
    ),
    Column(
        "username",
        String(32),
        nullable=False,
        unique=True,
    ),
    Column(
        "email",
        String(100),
        nullable=True,
        unique=True,
    ),
    Column(
        "full_name",
        String(150),
        nullable=False,
        server_default="",
    ),
)

# только для изучения и демонстрации
# копирую сюда тот SQL,
# что был сгенерирован алхимией
SQL = """
CREATE TABLE users (
	id INTEGER NOT NULL, 
	username VARCHAR(32) NOT NULL, 
	email VARCHAR(100), 
	full_name VARCHAR(150) DEFAULT '' NOT NULL, 
	PRIMARY KEY (id), 
	UNIQUE (username), 
	UNIQUE (email)
);
"""
# нам обычно никуда не нужно вставлять этот код.
# это просто служебная информация


def create() -> None:
    # print(metadata.tables)
    metadata.drop_all(bind=engine)
    metadata.create_all(bind=engine)


def insert_values() -> None:
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
                users_table.c.full_name: "Alice White",
            },
            {
                users_table.c.username: "nick",
                users_table.c.email: None,
                users_table.c.full_name: "",
            },
        ]
    )
    print(statement)
    print(repr(statement))
    with engine.connect() as conn:
        conn.execute(statement)
        conn.commit()


def fetch_values() -> None:
    statement = select(users_table).order_by(users_table.c.id)
    with engine.connect() as conn:
        result = conn.execute(statement)

    for row in result:
        print(row)
        print(row.id, row.username, row.email, row.full_name)
        # print(row[0], row[1], row[2], row[3])


def main() -> None:
    create()
    insert_values()
    fetch_values()


if __name__ == "__main__":
    main()
