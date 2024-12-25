import sqlite3

con = sqlite3.connect("tutorial.db")

cur = con.cursor()
cur.execute("CREATE TABLE movie(title, year, score);")
res = cur.execute("SELECT name FROM sqlite_master;")
print(res.fetchone())

res = cur.execute("SELECT current_timestamp from sqlite_master;")
print(res.fetchone()[0])
