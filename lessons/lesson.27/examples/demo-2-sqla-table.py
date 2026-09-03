from sqlalchemy import (
    create_engine,
    text,
    select,
    func,
    Table,
    MetaData,
    Column,
    String,
    Integer,
    insert,
)

engine = create_engine(
    "sqlite:///./blog.db",
    echo=True,  # debug flag!
)

metadata = MetaData()

users_table = Table(
    "users",
    metadata,
    Column(
        "id",
        Integer,
        primary_key=True,
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
        String(200),
        nullable=True,
        unique=True,
    ),
    Column(
        "full_name",
        String(100),
        nullable=False,
        unique=False,
        server_default="",
    ),
)


def create_tables():
    print(users_table)
    print(repr(users_table))
    print(metadata.tables)
    # никогда в проде!
    # только через миграции
    metadata.create_all(bind=engine)


# это я сюда скопировал ПРОСТО ДЛЯ ДЕМОНСТРАЦИИ
# в реальный код мы это НЕ КОПИРУЕМ
# это debug лог для нашего исследования.
got_sql = """\
CREATE TABLE users (
	id INTEGER NOT NULL, 
	username VARCHAR(32) NOT NULL, 
	email VARCHAR(200), 
	full_name VARCHAR(100) DEFAULT '' NOT NULL, 
	PRIMARY KEY (id), 
	UNIQUE (username), 
	UNIQUE (email)
)
"""


def insert_values():
    stmt = insert(users_table).values(
        [
            {
                users_table.c.username: "bob",
                users_table.c.email: "bob@example.com",
                users_table.c.full_name: "",
            },
            {
                users_table.c.username: "alice",
                users_table.c.email: None,
                users_table.c.full_name: "Alice White",
            },
        ],
    )

    print("statement:")
    print(stmt)

    with engine.connect() as conn:
        conn.execute(stmt)

        conn.commit()


def fetch_values():
    stmt = select(users_table).where(
        users_table.c.email.is_not(None),
        (func.length(users_table.c.username) > 3),
    )
    print(stmt)
    with engine.connect() as conn:
        res = conn.execute(stmt)

        for row in res.all():
            print(row)


def main():
    create_tables()
    # insert_values()
    fetch_values()

    engine.dispose()


if __name__ == "__main__":
    main()
