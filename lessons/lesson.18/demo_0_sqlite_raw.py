import sqlite3

conn = sqlite3.connect('./db.sqlite3')

cur = conn.cursor()

cur.execute("SELECT 1, 'hi', ?;", (';DROP TABLE', ))
print(cur.fetchone())
