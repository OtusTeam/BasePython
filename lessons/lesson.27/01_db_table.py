# from datetime import datetime, timezone

from sqlalchemy import (
    MetaData,
    Table,
    Column,
    Integer,
    String,
    DateTime,
    func,
    create_engine,
    insert,
    select,
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
        "full_name",
        String(100),
        nullable=False,
        default="",
        server_default="",
    ),
    Column(
        "email",
        String(100),
        unique=True,
        nullable=True,
    ),
    Column(
        "created_at",
        DateTime(timezone=False),
        nullable=False,
        # default=lambda: datetime.now(timezone.utc),
        server_default=func.now(),
    ),
)

# это просто для демонстрации
# что алхимия сгененрирует по таблице выше
# из питон кода будет создан такой запрос на создание таблицы
BECOMES_SQL = """
CREATE TABLE users (
	id INTEGER NOT NULL, 
	username VARCHAR(32) NOT NULL, 
	full_name VARCHAR(100) DEFAULT '' NOT NULL, 
	email VARCHAR(100), 
	created_at DATETIME DEFAULT (CURRENT_TIMESTAMP) NOT NULL, 
	PRIMARY KEY (id), 
	UNIQUE (username), 
	UNIQUE (email)
)
"""


def insert_users(engine):

    insert_bob_stmt = insert(users_table).values(
        {
            users_table.c.username: "bob",
            users_table.c.email: "bob@example.com",
        },
    )
    with engine.connect() as conn:
        conn.execute(insert_bob_stmt)
        conn.commit()

    insert_users_stmt = insert(users_table).values(
        [
            {
                users_table.c.username: "alice",
                users_table.c.email: "alice@example.com",
            },
            {
                users_table.c.username: "jack",
                users_table.c.email: None,
            },
        ]
    )
    with engine.connect() as conn:
        conn.execute(insert_users_stmt)
        conn.commit()


def main():
    engine = create_engine(
        # "sqlite:///:memory:",
        "sqlite:///users.db",
        echo=True,
    )
    print(metadata.tables)
    # metadata.drop_all(engine)
    metadata.create_all(engine)
    # insert_users(engine)
    stmt = select(users_table)
    with engine.connect() as conn:
        result = conn.execute(stmt)
    for row in result.fetchall():
        print(row)
        print(row[1], row.email)
        # print(row.username)
        # print(row.email)
    # insert_users(engine)


if __name__ == "__main__":
    main()
