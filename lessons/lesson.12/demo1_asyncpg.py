import asyncio
import asyncpg
from datetime import date


async def main():
    conn = await asyncpg.connect(
        "postgresql://username:password@localhost/demo"
        # user='user',
        # password='password',
        # database='database',
        # host='127.0.0.1'
    )
    await conn.execute(
        "INSERT INTO users(name, birth_date) VALUES($1, $2)",
        # "INSERT INTO users(name, birth_date) VALUES(?, ?)",
        "John",
        date(1977, 7, 21),
    )

    rows = await conn.fetch("SELECT id, name, birth_date FROM users;")
    print(rows)
    today = date.today()
    for r in rows:
        print(r["id"], r["name"], today - r["birth_date"])
        # print(r[0])

    john = await conn.fetchrow("SELECT * FROM users WHERE name = $1", "John")
    print(john)

    # values = await conn.fetch()
    await conn.close()


if __name__ == '__main__':
    asyncio.run(main())
