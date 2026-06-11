from sqlalchemy import create_engine, text

engine = create_engine(
    url="sqlite:///:memory:",
    echo=True,
)


def main():
    with engine.connect() as conn:
        res = conn.execute(text("SELECT 2 + 3, LOWER('HELLO THERE!');"))
        print("res:", res.fetchone())

        res = conn.execute(text("SELECT 5 * 8;"))
        print("res (fetch):", res.fetchone())
        res = conn.execute(text("SELECT 5 * 8;"))
        print("res (scalar):", res.scalar())


if __name__ == "__main__":
    main()
