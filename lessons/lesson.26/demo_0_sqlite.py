import sqlite3

DB_FILENAME = "blog.db"

SQL_CREATE_TABLE_AUTHORS = """\
CREATE TABLE if not exists authors (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username VARCHAR(32) UNIQUE NOT NULL,
    email VARCHAR(150) UNIQUE,
    full_name VARCHAR(100) NOT NULL DEFAULT ''
);
"""

conn = sqlite3.connect(DB_FILENAME)
conn.row_factory = sqlite3.Row
cur = conn.cursor()


def demo_select():
    # conn = sqlite3.connect(DB_FILENAME)
    # cur = conn.cursor()

    cur.execute("SELECT 1;")
    print("one result:", cur.fetchone())

    cur.execute("SELECT 1, 2, 3;")
    print("new one result:", cur.fetchone())
    print("again one result:", cur.fetchone())

    cur.execute("SELECT 2 + 3, LOWER('Hello World!');")
    print("res:", cur.fetchone())

    # conn.close()


def create_table_authors():
    # conn = sqlite3.connect(DB_FILENAME)
    # cur = conn.cursor()

    cur.execute(SQL_CREATE_TABLE_AUTHORS)
    # conn.close()


def insert_values():
    # conn = sqlite3.connect(DB_FILENAME)
    # cur = conn.cursor()

    user_john_data = ("john", "john@example.com")
    cur.execute(
        "INSERT INTO authors (username, email) VALUES (?, ?)",
        user_john_data,
    )

    users_data = [
        ("bob", "bob@example.com", "Bob Black"),
        ("alice", "alice@example.com", "Alice White"),
    ]
    cur.executemany(
        "INSERT INTO authors (username, email, full_name) VALUES (?, ?, ?)",
        users_data,
    )

    conn.commit()

    # conn.close()


def show_values():
    # conn = sqlite3.connect(DB_FILENAME)
    # conn.row_factory = sqlite3.Row
    # cur = conn.cursor()

    cur.execute("SELECT * FROM authors ORDER BY id;")
    for row in cur.fetchall():
        # print(row)
        print(row[0], row[1], row[2], row[3])
        print(row["id"], row["username"], row["email"], row["full_name"])

    # conn.close()


def main():
    demo_select()
    create_table_authors()
    insert_values()
    show_values()


if __name__ == "__main__":
    main()
