import sqlite3

# DB_FILENAME = "tutorial.db"
DB_FILENAME = "db.sqlite3"


def main():
    sql_create_table = '''
    CREATE TABLE IF NOT EXISTS authors
    (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username VARCHAR UNIQUE NOT NULL,
        email VARCHAR UNIQUE
    );
    '''
    con = sqlite3.connect(DB_FILENAME)
    cursor = con.cursor()
    cursor.execute(sql_create_table)

    username = 'bob'
    email = 'DROP TABLE authors; \' ` bob@example.com'
    cursor.execute(
        "INSERT INTO authors (username, email) VALUES (?, ?);",
        (username, email),
    )

    con.commit()

    cursor.close()
    con.close()


if __name__ == '__main__':
    main()
