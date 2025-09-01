from sqlalchemy import text, select
from sqlalchemy import create_engine

engine = create_engine(
    "sqlite:///:memory:",
    echo=True,
)


def main() -> None:
    with engine.connect() as connection:
        res = connection.execute(text("SELECT 1, 2;"))
        print(res.fetchone())

        res = connection.execute(text("SELECT 2 + 3;"))
        # print(res.fetchone())
        print(res.scalar())

        res = connection.execute(select(7))
        print(res.scalar())


if __name__ == "__main__":
    main()
