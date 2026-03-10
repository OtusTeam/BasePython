import sqlite3

DB_FILENAME = "blog.db"


sql_create_users_table = """
create table if not exists users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username VARCHAR(32) UNIQUE NOT NULL,
    email VARCHAR(150) UNIQUE,
    full_name VARCHAR(100) NOT NULL DEFAULT ''
);
"""


def demo_select() -> None:
    conn = sqlite3.connect(DB_FILENAME)
    cur = conn.cursor()

    cur.execute("SELECT 1;")
    print("fetch one result:", cur.fetchone())

    cur.execute("SELECT 1, 2, 3;")
    print("fetch one result:", cur.fetchone())
    print("fetch one result:", cur.fetchone())

    cur.execute("SELECT 2 + 3;")
    print("fetch sum result:", cur.fetchone())

    conn.close()


def create_table_users() -> None:
    conn = sqlite3.connect(DB_FILENAME)
    cur = conn.cursor()
    cur.execute(sql_create_users_table)
    conn.close()


def insert_values() -> None:
    users_data = [
        # username, email, full_name
        ("bob", "bob@example.com", "Bob"),
        ("john", "john@example.com", "Johnathan"),
        ("alice", None, ""),
    ]
    conn = sqlite3.connect(DB_FILENAME)
    conn.executemany(
        "INSERT INTO users (username, email, full_name) VALUES (?, ?, ?)",
        users_data,
    )
    conn.commit()
    conn.close()


def show_values() -> None:
    conn = sqlite3.connect(DB_FILENAME)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    res = cur.execute("SELECT id, username, email, full_name FROM users order by id;")
    for row in res:
        # print(row)
        print(row[0], row[1], row[2], row[3])
        print(row["id"], row["username"], row["email"], row["full_name"])

    conn.close()


def main() -> None:
    # demo_select()
    # create_table_users()
    # insert_values()
    show_values()


if __name__ == "__main__":
    main()
