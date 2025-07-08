from sqlalchemy import (
    create_engine,
    String,
)
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

db_url = "sqlite:///second.db"
db_echo = False

db_echo = True
engine = create_engine(
    url=db_url,
    echo=db_echo,
)


class Base(DeclarativeBase):
    pass


#  old style, never use!
# class Author(Base):
#     id = Column(Integer, primary_key=True)
#     username = Column(String(32), nullable=False, unique=True)
#     email = Column(String(150), nullable=True, unique=True)


class Author(Base):
    __tablename__ = "authors"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(
        String(32),
        unique=True,
    )
    email: Mapped[str | None] = mapped_column(
        String(150),
        unique=True,
    )


def main():
    print(Base.metadata.tables)
    # print(Author.__table__, repr(Author.__table__))
    Base.metadata.create_all(bind=engine)
    print(Author.username, repr(Author.username))


# мы не создавали это вручную.
# запрос сгенерирован автоматически на основе модели
GENERATED_SQL = """
CREATE TABLE authors (
	id INTEGER NOT NULL, 
	username VARCHAR(32) NOT NULL, 
	email VARCHAR(150), 
	PRIMARY KEY (id), 
	UNIQUE (username), 
	UNIQUE (email)
)
"""

if __name__ == '__main__':
    main()
