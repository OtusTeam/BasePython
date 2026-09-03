import sqlite3
from enum import nonmember

con = sqlite3.connect("blog.db")
con.row_factory = sqlite3.Row


SQL_CREATE_TABLE_USERS = """\
create table if not exists users (
    id integer primary key not null,
    username varchar(32) unique not null,
    email varchar(200) unique,
    full_name varchar(100) not null default ''
);
"""


def create_table():
    cur = con.cursor()
    cur.execute(SQL_CREATE_TABLE_USERS)


def insert_values():
    cur = con.cursor()

    username = "john"
    cur.execute(
        """insert into users (username, email, full_name)
        values (?, ?, ?);
        """,
        (username, None, "John"),
    )

    cur.executemany(
        """insert into users (username, email)
           values (?, ?);
        """,
        [
            ("bob", "bob@example.com"),
            ("alice", None),
        ],
    )

    cur.executemany(
        """insert into users (username, email)
           values (:username, :email);
        """,
        [
            {
                "username": "kate",
                "email": "kate@ya.ru",
            },
            {
                "username": "kyle",
                "email": None,
            },
        ],
    )

    con.commit()


def show_values():
    cur = con.cursor()
    cur.execute("select * from users order by id;")

    # print("one:", cur.fetchone())
    # print("two:", cur.fetchone())
    # print("all:")
    for row in cur.fetchall():
        # print(row[0], row[1], row[2])
        print(row["id"], row["username"], row["email"])

    cur.execute(
        """
        select id, username, email, full_name
        from users where username = ?;
        """,
        ("john",),
    )
    print()
    row = cur.fetchone()
    if row is None:
        print("no row")
        return
    print("full name:", row["full_name"])
    print("email:", row["email"])
    print("email:", row[2])


def main():
    create_table()
    # insert_values()
    show_values()

    con.close()


if __name__ == "__main__":
    main()
