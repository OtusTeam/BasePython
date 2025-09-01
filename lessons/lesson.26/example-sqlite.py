import sqlite3

from collections import namedtuple


def namedtuple_factory(cursor, row):
    fields = [column[0] for column in cursor.description]
    cls = namedtuple("Row", fields)
    return cls._make(row)


def init():
    con = sqlite3.connect("blog.db")

    cur = con.cursor()

    res = cur.execute("SELECT 1, 2, 3;")
    print(res.fetchone())

    res = cur.execute("SELECT 2 + 3;")
    print(res.fetchone()[0])

    cur.execute(
        """
    CREATE TABLE users
    (
        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        username VARCHAR(32) UNIQUE NOT NULL,
        email VARCHAR(150) UNIQUE,
        full_name VARCHAR(200) NOT NULL DEFAULT ''
    );
    """
    )
    con.commit()


def insert_values():
    con = sqlite3.connect("blog.db")

    users = [
        # username, email, full_name
        ("bob", "bob@example.com", "Bob Smith"),
        ("John", None, "John Black"),
        ("Kate", None, ""),
    ]
    con.executemany(
        """INSERT INTO users (username, email, full_name) VALUES (?, ?, ?)""",
        users,
    )
    con.commit()


def main() -> None:
    # init()

    con = sqlite3.connect("blog.db")
    cur = con.cursor()

    # cur.row_factory = sqlite3.Row
    cur.row_factory = namedtuple_factory
    res = cur.execute("SELECT * FROM users;")

    for row in res:
        print(row)
        # print(row["username"], row["email"], row["full_name"])
        print(row[1], row[2], row[3])
        print(row.username, row.email, row.full_name)


if __name__ == "__main__":
    main()
