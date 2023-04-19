import sqlite3


def main():
    database = "my.db"
    connection = sqlite3.connect(database=database)
    sql = "SELECT 1, 2, 3, 2 + 3;"
    cur = connection.cursor()
    cur.execute(sql)
    result = cur.fetchall()
    print(result)


if __name__ == "__main__":
    main()
