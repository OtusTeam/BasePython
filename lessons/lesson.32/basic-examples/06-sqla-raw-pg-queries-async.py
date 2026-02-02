import asyncio

from sqlalchemy import text, select, func
from sqlalchemy.ext.asyncio import create_async_engine

import config

engine = create_async_engine(
    url=config.SQLA_DB_URL_ASYNC,
    echo=config.SQLA_DB_ECHO,
)


async def main() -> None:
    async with engine.connect() as conn:
        res = await conn.execute(text("SELECT now();"))
        print(res.scalars().all())

        res = await conn.execute(text("SELECT 1, 2, 3;"))
        print(res.fetchone())

        res = await conn.execute(text("SELECT 1 + 2, 3 + 4;"))
        print(res.fetchall())

        res = await conn.execute(text("SELECT 7 * 8;"))
        val = res.scalar()
        print(val, type(val))

        res = await conn.execute(select(3))
        val = res.scalar()
        print(val, type(val))

        res = await conn.execute(select(5))
        val = res.scalars().all()
        print(val, type(val))

        res = await conn.execute(select(7))
        val = res.fetchall()
        print(val, type(val))

        select_info = select(func.now(), func.version(), func.length(text("'hello'")))
        print(select_info)
        res = await conn.execute(select_info)
        print(res.fetchone())


if __name__ == "__main__":
    asyncio.run(main())
