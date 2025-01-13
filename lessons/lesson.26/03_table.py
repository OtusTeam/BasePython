from sqlalchemy import Table
from sqlalchemy import Column
from sqlalchemy import MetaData
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import insert

from common import engine


metadata = MetaData()

users_table = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String(40), nullable=False),
    Column(
        "email",
        String(255),
        nullable=True,
        unique=True,
    ),
)

BECOMES_SQL = """\
CREATE TABLE users
(
    id    INTEGER     NOT NULL,
    name  VARCHAR(40) NOT NULL,
    email VARCHAR(255),
    PRIMARY KEY (id)
)
"""


def main():
    print(users_table)
    print(repr(users_table))
    print(metadata.tables)

    metadata.create_all(bind=engine)

    stmt1 = insert(users_table).values(
        {
            users_table.c.name: "Nick",
            # users_table.c.email: "nick@ya.ru",
        }
    )

    stmt2 = insert(users_table).values(
        [
            {
                users_table.c.name: "Bob",
                users_table.c.email: "bob@ya.ru",
            },
            {
                users_table.c.name: "Alice",
                users_table.c.email: None,
            },
        ]
    )

    with engine.connect() as conn:
        conn.execute(stmt1)
        conn.execute(stmt2)

        conn.commit()


if __name__ == "__main__":
    main()
