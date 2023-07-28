
from sqlalchemy import (
    create_engine,
    Table,
    MetaData,
    Column,
    Integer,
    String,
)

DB_URL = "sqlite:///example1.db"
# DB_ECHO = False
DB_ECHO = True

engine = create_engine(url=DB_URL, echo=DB_ECHO)

metadata = MetaData()

authors_table = Table(
    "authors",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("username", String(32), nullable=False, unique=True),
    Column("email", String(100), nullable=True, unique=True),
)


def main():
    sql = """
    CREATE TABLE authors (
        id INTEGER NOT NULL, 
        username VARCHAR(32) NOT NULL, 
        email VARCHAR(100), 
        PRIMARY KEY (id), 
        UNIQUE (username), 
        UNIQUE (email)
    );
    """
    metadata.create_all(bind=engine)


if __name__ == '__main__':
    main()

