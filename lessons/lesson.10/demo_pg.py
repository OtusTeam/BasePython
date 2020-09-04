import psycopg2


conn = psycopg2.connect(
    host="localhost",
    port=5432,
    database="postgres",
    user="user",
    password="password",
)

print(conn)
cur = conn.cursor()

print(cur)

res = cur.execute("SELECT id, full_name, username FROM users;")
print(res)

users = cur.fetchall()
print(users)

res = cur.execute("INSERT INTO users (username, full_name) VALUES ('sam', 'Sam White');")
print(conn.commit())


conn.close()
