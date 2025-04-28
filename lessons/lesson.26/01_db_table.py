"""

Example:

>>> class MyMeta:
...     def __init__(self):
...         self.tables = {}
...
...     def register_table(self, table_name, table):
...         if table_name in self.tables:
...             raise Exception("Table {} already exists".format(table_name))
...         self.tables[table_name] = table
>>>
>>>
>>> class MyTable:
...     def __init__(
...         self,
...         table_name: str,
...         meta: MyMeta,
...         *cols: Column,
...     ):
...         meta.register_table(table_name, self)
>>>
>>>
>>> my_meta = MyMeta()
>>> MyTable("users", my_meta)
"""

from pathlib import Path

from sqlalchemy import (
    create_engine,
    Table,
    Column,
    Integer,
    String,
    MetaData,
    insert,
    select,
)

# from sqlalchemy.dialects.sqlite import dialect


BASE_DIR = Path(__file__).parent
SQLITE_DB_FILE = BASE_DIR / "blog.db"

# enable for debug
ECHO = True
# ECHO = False
engine = create_engine(
    # url="sqlite:///:memory:",
    url=f"sqlite:///{SQLITE_DB_FILE}",
    echo=ECHO,
)

EXAMPLE_SQLITE_CREATE = """
CREATE TABLE users (
	id INTEGER NOT NULL, 
	username VARCHAR(32) NOT NULL, 
	email VARCHAR(150), 
	full_name VARCHAR DEFAULT '' NOT NULL, 
	PRIMARY KEY (id), 
	UNIQUE (username), 
	UNIQUE (email)
)
"""

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
        String,
        nullable=False,
        default="",
        server_default="",
    ),
)


def create_users() -> None:

    insert_bob_statement = insert(users_table).values(
        {
            users_table.c.username: "bob",
            users_table.c.email: "bob@example.com",
        },
    )
    # print("statement:")
    # print(insert_bob_statement)
    # print(repr(insert_bob_statement))
    # print(
    #     insert_bob_statement.compile(
    #         # dialect=dialect(),
    #         compile_kwargs={"literal_binds": True},
    #     )
    # )

    with engine.connect() as conn:
        conn.execute(insert_bob_statement)
        conn.commit()

    insert_users_statement = insert(users_table).values(
        [
            {
                users_table.c.username: "alice",
                users_table.c.email: "alice@example.com",
            },
            {
                users_table.c.username: "jack",
                users_table.c.email: None,
            },
        ],
    )
    with engine.connect() as conn:
        conn.execute(insert_users_statement)
        conn.commit()


def main() -> None:
    print(metadata.tables)
    metadata.create_all(engine)

    # DROP TABLE users
    # metadata.drop_all(engine)
    # with engine.connect() as conn:
    #     pass

    # create_users()

    select_statement = select(users_table)
    with engine.connect() as conn:
        result = conn.execute(select_statement)

    for row in result.all():
        print(row)
        # print(row[1])
        print(row.username, row.email)


if __name__ == "__main__":
    main()
