import sqlite3


def main():
    con = sqlite3.connect("tutorial.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE movie(title, year, score)")
    data = [
        ("Monty Python Live at the Hollywood Bowl", 1982, 7.9),
        ("Monty Python's The Meaning of Life", 1983, 7.5),
        ("Monty Python's Life of Brian", 1979, 8.0),
    ]
    cur.executemany("INSERT INTO movie (title, year, score) VALUES(?, ?, ?)", data)
    con.commit()  # Remember to commit the transaction after executing INSERT.

    res = con.execute("SELECT title, year FROM movie ORDER BY score DESC")
    for row in res:
        print(row)

    con.close()


if __name__ == '__main__':
    main()
