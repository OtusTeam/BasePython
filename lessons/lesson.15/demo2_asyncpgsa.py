import asyncio
from datetime import date

from asyncpgsa import pg
from sqlalchemy import (
    Table,
    MetaData,
    Column,
    Integer,
    String,
    Date,
)

metadata = MetaData()

users_table = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=False, default="", server_default=""),
    Column("birth_date", Date),
)


async def main():
    await pg.init(
        user="user",
        password="password",
        database="postgres",
        host="127.0.0.1",
        # loop=loop,
        min_size=5,
        max_size=10
    )

    users_query = users_table.select()
    # print(users_query)

    results = await pg.query(users_query)
    for res in results:
        print(res)

    ins = users_table.insert().values(name="Nick", birth_date=date(1994, 7, 30))
    await pg.execute(ins)

    print("---")

    nick = await pg.fetchrow(users_query.where(users_table.c.name == "Nick"))
    print(nick)


if __name__ == '__main__':
    asyncio.run(main())
