import psycopg2

conn = psycopg2.connect(
    host="localhost",
    port="5432",
    user="user",
    password="password",
    database="postgres",
)

print(conn)

cur = conn.cursor()
print(cur)

res = cur.execute("""
    SELECT *
    FROM users
    WHERE username is not NULL;
""")

print(res)

for row in cur.fetchall():
    print(row)


# res = cur.execute("""
#     INSERT INTO users (username, full_name)
#     VALUES ('ann', 'Ann Brown');
# """)

res = cur.execute(
    """
    INSERT INTO users (username, full_name)
    VALUES (%s, %s);
    """,
    ["nick", "Nick Robinson"],
)

print(conn.commit())

conn.close()
