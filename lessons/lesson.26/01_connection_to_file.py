from sqlalchemy import text
from sqlalchemy import create_engine

from config import BASE_DIR

db_filename = "accounts.db"
db_filepath = BASE_DIR / db_filename

engine = create_engine(
    f"sqlite:///{db_filepath}",
    echo=True,  # echo only for debug!!
)


def main():
    with engine.connect() as conn:
        result = conn.execute(text("select 1 + 2"))
        print(result.scalar())


if __name__ == "__main__":
    main()
