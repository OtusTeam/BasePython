from sqlalchemy import text
from sqlalchemy import create_engine

engine = create_engine(
    "sqlite:///:memory:",
    echo=True,  # echo only for debug!!
)


def main():
    with engine.connect() as conn:
        result = conn.execute(text("select 1 + 2"))
        print(result.scalar())


if __name__ == "__main__":
    main()
