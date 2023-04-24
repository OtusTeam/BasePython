from datetime import datetime

from sqlalchemy import (
    create_engine,
    Table,
    MetaData,
    Column,
    Integer,
    String,
    Text,
    DateTime,
    func,
)

DB_URL = "sqlite:///example1.db"

# DB_ECHO = False
DB_ECHO = True

engine = create_engine(
    url=DB_URL,
    echo=DB_ECHO,
)

metadata = MetaData()

authors_table = Table(
    "authors",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("username", String(20), unique=True, nullable=False),
    Column("email", String(180), unique=True),
    # Column("email", String(180), unique=True, nullable=True),
    Column(
        "bio",
        Text,
        nullable=False,
        default="hello world",
        server_default="",
    ),
    Column(
        "created_at",
        DateTime,
        default=datetime.utcnow,
        server_default=func.now(),
    ),
)


def main():
    sql_drop = """DROP TABLE authors;"""
    metadata.drop_all(bind=engine)
    # print(metadata.tables)
    sql = """
    CREATE TABLE authors (
        id INTEGER NOT NULL, 
        username VARCHAR(20) NOT NULL, 
        email VARCHAR(180), 
        bio TEXT DEFAULT '' NOT NULL, 
        created_at DATETIME DEFAULT (CURRENT_TIMESTAMP), 
        PRIMARY KEY (id), 
        UNIQUE (username), 
        UNIQUE (email)
    );
    """
    metadata.create_all(bind=engine)


if __name__ == "__main__":
    main()
