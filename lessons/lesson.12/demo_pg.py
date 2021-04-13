import psycopg2

conn = psycopg2.connect(
    host="localhost",
    port="5432",
    database="postgres",
    user="user",
    password="password",
)

print(conn)
cur = conn.cursor()
print(cur)


def show_all_users():
    res = cur.execute("SELECT id, full_name, username FROM users;")
    # print(res)

    users = cur.fetchall()
    print(users)
    for user_row in users:
        print(f"User #{user_row[0]} {user_row[1]} ({user_row[2]})")


show_all_users()

# cur.execute("SELECT * FROM test WHERE id = %s", (3,))
new_username = 'ann'
new_full_name = 'Ann Gray'

res = cur.execute(
    "INSERT INTO users (username, full_name) VALUES (%s, %s);",
    (new_username, new_full_name)
)

print("cur res after insert", res)
print(conn.commit())

show_all_users()
conn.close()
