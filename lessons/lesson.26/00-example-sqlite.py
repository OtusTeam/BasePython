import sqlite3


def init() -> None:
    conn = sqlite3.connect("blog.db")

    cur = conn.cursor()

    res = cur.execute("SELECT 1, 2, 3;")
    print(res.fetchone())

    res = cur.execute("SELECT 2 + 3;")
    # print(res.fetchall())
    print(res.fetchone()[0])

    create_users_sql = """
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username VARCHAR(32) UNIQUE NOT NULL,
        email VARCHAR(100) UNIQUE,
        full_name VARCHAR(150) NOT NULL DEFAULT ''
    )
    """
    conn.execute(create_users_sql)
    conn.commit()


def insert_values() -> None:
    conn = sqlite3.connect("blog.db")

    users = [
        # username, email, full_name
        ("bob", "bob@example.com", "Bob Smith"),
        ("john", None, "John Black"),
        ("alice", None, ""),
    ]
    conn.executemany(
        """INSERT INTO users (username, email, full_name) VALUES (?, ?, ?)""",
        users,
    )
    conn.commit()


def show_values() -> None:
    conn = sqlite3.connect("blog.db")
    cur = conn.cursor()

    res = cur.execute("SELECT * FROM users;")
    for row in res:
        print(row[0], row[1], row[2], row[3])


def main() -> None:
    init()
    insert_values()
    show_values()


if __name__ == "__main__":
    main()
