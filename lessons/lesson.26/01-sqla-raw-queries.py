from sqlalchemy import create_engine, text, select

import config

engine = create_engine(
    "sqlite:///data.db",
    echo=config.SQLA_DB_ECHO,
)


def main() -> None:
    with engine.connect() as conn:
        res = conn.execute(text("SELECT 1, 2;"))
        print(res.fetchall())

        res = conn.execute(text("SELECT 3 + 4, 5 + 6;"))
        print(res.fetchone())

        res = conn.execute(text("SELECT 7 * 8;"))
        val = res.scalar()
        print(val)
        print(type(val))

        res = conn.execute(select(3))
        val = res.scalar()
        print(val)


if __name__ == "__main__":
    main()
