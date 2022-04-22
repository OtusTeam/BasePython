from sqlalchemy import (
    create_engine,
    MetaData,
    Table,
    Column,
    Integer,
    String,
    Boolean,
)

# from sqlalchemy.dialects.postgresql import JSONB
# from sqlalchemy.dialects.mysql import JSON

DB_URL = "sqlite:///example-01.db"
DB_ECHO = True
engine = create_engine(url=DB_URL, echo=DB_ECHO)

metadata = MetaData()
users_table = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("username", String(20), unique=True),
    Column("is_staff", Boolean, default=False, nullable=False),
)


def create_table():
    sql = """
    CREATE TABLE users (
        id INTEGER NOT NULL, 
        username VARCHAR(20), 
        is_staff BOOLEAN NOT NULL, 
        PRIMARY KEY (id), 
        UNIQUE (username)
    ) 
    """
    metadata.create_all(bind=engine)


if __name__ == '__main__':
    # print(engine, [engine])
    # print(users_table, [users_table])
    create_table()
