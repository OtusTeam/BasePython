from sqlalchemy import create_engine, text

engine = create_engine(
    url="sqlite:///:memory:",
    echo=True,
)


def main() -> None:
    with engine.connect() as conn:
        res = conn.execute(text("SELECT 1, 2, 3"))
        # print(res.fetchall())
        print(res.fetchone())

        res = conn.scalar(text("SELECT 7 * 8"))
        print("result:", res)

        res = conn.execute(text("SELECT 7 * 8"))
        print(res)
        # print(res.all())
        # print(res.scalar())
        print("result:", res.scalar())


if __name__ == "__main__":
    main()
