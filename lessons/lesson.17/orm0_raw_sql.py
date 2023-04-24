import sqlite3

DB_FILENAME = "db.sqlite3"


def main():
    sql_create_table = """
    CREATE TABLE IF NOT EXISTS authors
    (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username VARCHAR UNIQUE NOT NULL,
        email VARCHAR UNIQUE 
    );
    """

    conn = sqlite3.connect(DB_FILENAME)
    cursor = conn.cursor()
    cursor.execute(sql_create_table)

    # username = "admin"
    # email = "admin@admin.org"
    username = "bob"
    email = "bob@example.com"
    # sql injection
    # email = "'); DROP TABLE authors; SELECT ('"

    cursor.execute(
        """
    INSERT INTO authors (username, email)
    VALUES (?, ?);
    """,
        (username, email),
    )
    # cursor.execute(
    #     """
    # INSERT INTO authors (username, email)
    # """
    #     + f"VALUES ('{username}', '{email}');",
    # )
    conn.commit()
    cursor.close()


if __name__ == "__main__":
    main()
