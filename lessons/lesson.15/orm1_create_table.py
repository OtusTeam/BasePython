from sqlalchemy import (
    create_engine,
    Table,
    MetaData,
    Column,
    Integer,
    String,
    Text,
)


DB_URL = "sqlite:///example1.db"
# optional!!
DB_ECHO = True
# DB_ECHO = False

engine = create_engine(url=DB_URL, echo=DB_ECHO)

metadata = MetaData()
# metadata = MetaData(bind=engine)

# def init(self, table_name: str, metadata: MetaData, *cols: Column):
#     metadata.register(self)

authors_table = Table(
    "authors",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("username", String(16), unique=True, nullable=False),
    Column("email", String(200), unique=True),
    Column("bio", Text),
)



def create_db_and_table():
    sql = """
    CREATE TABLE authors (
        id INTEGER NOT NULL, 
        username VARCHAR(16) NOT NULL, 
        email VARCHAR(200), 
        PRIMARY KEY (id), 
        UNIQUE (username), 
        UNIQUE (email)
    );
    """
    metadata.create_all(bind=engine)


if __name__ == "__main__":
    'DROP TABLE authors;'
    metadata.drop_all(bind=engine)
    create_db_and_table()
    # print(metadata.tables)
