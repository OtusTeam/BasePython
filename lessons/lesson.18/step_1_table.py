from sqlalchemy import (
    create_engine,
    MetaData,
    Table,
    Column,
    Integer,
    String,
    Boolean
)

DB_URL = 'sqlite:///users.sqlite3'
# DB_URL = 'postgresql+pg8000://username:passwd@localhost:5432/users' #psycopg2
DB_ECHO = True

engine = create_engine(url=DB_URL, echo=DB_ECHO)

metadata = MetaData()

user_table = Table(
    'users',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('username', String(20), unique=True),
    Column('is_staff', Boolean, default=False, nullable=False)
)


def create_database():
    metadata.create_all(bind=engine)


if __name__ == '__main__':
    create_database()