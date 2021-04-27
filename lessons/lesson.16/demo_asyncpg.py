"""
DEMO DOC
"""

import asyncio
from datetime import datetime

import asyncpg

PG_CONN_URI = "postgresql://user:password@localhost/project"


async def create_table():
    # conn = await asyncpg.connect(user='user', password='password',
    #                              database='database', host='127.0.0.1')

    conn = await asyncpg.connect(PG_CONN_URI)

    await conn.execute(
        """
        CREATE TABLE demo_asyncpg (
            id SERIAL PRIMARY KEY,
            "name" VARCHAR,
            created_at timestamp
        );
        """
    )
    await conn.close()
    print("created table")


async def add_item():
    conn = await asyncpg.connect(PG_CONN_URI)

    await conn.execute(
        """
        INSERT INTO demo_asyncpg("name", created_at) 
        VALUES ($1, $2)
        """,
        "John",
        datetime.utcnow(),
    )

    await conn.close()
    print("added item")


async def get_item():
    conn = await asyncpg.connect(PG_CONN_URI)

    john = await conn.fetchrow(
        """
        SELECT * FROM demo_asyncpg
        WHERE "name" = $1
        """,
        "John",
    )
    print("john:", john)
    print(f"record #{john['id']}, name={john['name']!r}, created_at={john['created_at']!r}")
    await conn.close()


async def main():
    await create_table()
    await add_item()
    await get_item()


if __name__ == '__main__':
    asyncio.run(main())
