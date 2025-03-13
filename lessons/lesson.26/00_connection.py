from sqlalchemy import create_engine, text

engine = create_engine(
    "sqlite:///:memory:",
    echo=True,
)


def main():
    with engine.connect() as conn:
        # result = conn.execute(text("SELECT 1 + 2"))
        result = conn.execute(text("SELECT 'Hello World'"))
        print(result.scalar())


if __name__ == "__main__":
    main()
