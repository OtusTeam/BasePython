from sqlalchemy import (
    create_engine,
    MetaData,
    Table,
    Column,
    Integer,
    String,
)

db_url = "sqlite:///first.db"
db_echo = False

db_echo = True
engine = create_engine(
    url=db_url,
    echo=db_echo,
)

metadata = MetaData()

authors_table = Table(
    "authors",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("username", String(32), nullable=False, unique=True),
    Column("email", String(150), nullable=True, unique=True),
    # Column("foobar", String(150), nullable=True, unique=True),
)


# мы получили этот SQL автоматически при запуске скрипта.
# писать это вруную не надо. запрос сгенерирован на основе описания таблицы.
SQL = """
CREATE TABLE authors (
	id INTEGER NOT NULL, 
	username VARCHAR(32) NOT NULL, 
	email VARCHAR(150), 
	PRIMARY KEY (id), 
	UNIQUE (username), 
	UNIQUE (email)
)
"""

def main():
    print(metadata.tables)
    metadata.create_all(bind=engine)
    print(authors_table.c.username)
    print(repr(authors_table.c.username))


if __name__ == '__main__':
    main()
