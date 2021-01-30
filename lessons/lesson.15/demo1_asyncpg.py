import asyncio
from datetime import date

import asyncpg


async def run():
    conn = await asyncpg.connect(
        user='user',
        password='password',
        database='postgres',
        host='127.0.0.1',
    )

    john = await conn.fetchrow(
        """
        SELECT * FROM users
        WHERE name = $1;
        """,
        "John",
    )
    print("John:", john)

    await conn.execute(
        """
        INSERT INTO users(name, birth_date)
        VALUES ($1, $2);
        """,
        "Kate",
        date(1991, 8, 13),
    )

    rows = await conn.fetch(
        """
        SELECT * FROM users;
        """
    )

    today = date.today()
    for r in rows:
        print(r["name"], today - r["birth_date"])

    await conn.close()


if __name__ == '__main__':
    asyncio.run(run())
