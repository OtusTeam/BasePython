from sqlalchemy import create_engine, text

# enable for debug
ECHO = True
# ECHO = False
engine = create_engine(
    url="sqlite:///:memory:",
    echo=ECHO,
)


def main() -> None:
    with engine.connect() as conn:
        result = conn.execute(text("SELECT 1 + 2"))
        # print(result.fetchall())
        # print(result.scalars().all())
        print("result:", result.scalar())

        result = conn.execute(text("SELECT 'Hello World!'"))
        # print(result.fetchall())
        print("result:", result.scalar())

        result = conn.execute(text("SELECT 1 + 2, 3 +4"))
        # print(result.fetchall())
        # print("result:", result.all())
        print("result:", result.one())


if __name__ == "__main__":
    main()
