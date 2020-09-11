import asyncio

from asyncpgsa import pg
from sqlalchemy import MetaData, Table, Column, Integer, String, Date

metadata = MetaData()


users_table = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=False),
    Column("birth_date", Date, nullable=False),
)


def left_pad(text: str, min_length: int) -> str:
    if len(text) < min_length:
        text = " " * (min_length - len(text)) + text
    return text


async def main():
    await pg.init(
        "postgresql://username:password@localhost/demo"
        # host=HOST,
        # port=PORT,
        # database=DB_NAME,
        # user=USER,
        # # loop=loop,
        # password=PASS,
        # min_size=5,
        # max_size=10
    )

    users_query = users_table.select()
    results = await pg.query(users_query)
    for index, row in enumerate(results):
        if index == 0:
            print(" | ".join([left_pad(name, 13) for name in row.keys()]))
        print(" | ".join([left_pad(str(value), 13) for value in row.values()]))

    james = await pg.fetchrow(users_query.where(users_table.c.name == "James"))
    print()
    print(james)


if __name__ == '__main__':
    asyncio.run(main())
