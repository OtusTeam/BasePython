import sqlite3

DB_FILENAME = "blog.db"


create_table_users = """\
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username VARCHAR(32) UNIQUE NOT NULL,
    email VARCHAR(150) UNIQUE,
    full_name VARCHAR(100) NOT NULL DEFAULT ''
);
"""


def init_db() -> None:
    conn = sqlite3.connect(DB_FILENAME)
    cur = conn.cursor()

    cur.execute("SELECT 1, 2, 3;")
    print("fetch one (1)", cur.fetchone())
    print("fetch one (2)", cur.fetchone())

    cur.execute("SELECT 2 + 3;")
    # print(result.fetchone())
    print(cur.fetchone()[0])

    conn.execute(create_table_users)
    conn.close()


def insert_values() -> None:
    conn = sqlite3.connect(DB_FILENAME)
    users = [
        # username, email, full_name
        ("bob", "bob@example.com", "Bob White"),
        ("alice", "alice@example.com", "Alice"),
        ("john", None, ""),
    ]
    conn.executemany(
        "INSERT INTO users (username, email, full_name) VALUES (?, ?, ?)",
        users,
    )
    # conn.execute("INSERT INTO users (username, email, full_name) VALUES (?, ?, ?)",)
    conn.commit()

    conn.close()
    print("Inserted values")


def show_values() -> None:
    conn = sqlite3.connect(DB_FILENAME)

    cur = conn.cursor()
    # cur.execute("SELECT * FROM users;")
    # for row in cur:
    #     print(row)

    res = cur.execute("SELECT * FROM users;")
    for row in res:
        # print(row)
        print(row[0], row[1], row[2], row[3])

    conn.close()


def main() -> None:
    # init_db()
    # insert_values()
    show_values()


if __name__ == "__main__":
    main()
