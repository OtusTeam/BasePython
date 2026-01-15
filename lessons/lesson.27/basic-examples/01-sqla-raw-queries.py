from sqlalchemy import create_engine, text, select

import config

engine = create_engine(
    url=config.SQLA_DB_URL,
    echo=config.SQLA_DB_ECHO,
)


def main() -> None:
    with engine.connect() as conn:
        res = conn.execute(text("SELECT 1, 2, 3;"))
        print(res.fetchone())

        res = conn.execute(text("SELECT 1 + 2, 3 + 4;"))
        print(res.fetchall())

        res = conn.execute(text("SELECT 7 * 8;"))
        val = res.scalar()
        print(val, type(val))

        res = conn.execute(select(3))
        val = res.scalar()
        print(val, type(val))

        res = conn.execute(select(5))
        val = res.scalars().all()
        print(val, type(val))

        res = conn.execute(select(7))
        val = res.fetchall()
        print(val, type(val))


if __name__ == "__main__":
    main()
