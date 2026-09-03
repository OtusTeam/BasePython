from sqlalchemy import (
    create_engine,
    select,
    func,
    String,
    insert,
)
from sqlalchemy.orm import (
    DeclarativeBase,
    Mapped,
    mapped_column,
    Session,
)

engine = create_engine(
    "sqlite:///./blog.db",
    echo=True,  # debug flag!
)


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(
        primary_key=True,
    )
    username: Mapped[str] = mapped_column(
        String(32),
        unique=True,
    )

    email: Mapped[str | None] = mapped_column(
        String(200),
        unique=True,
    )
    full_name: Mapped[str] = mapped_column(
        String(100),
        unique=False,
        server_default="",
    )


def create_tables():
    users_table = User.__table__
    print(users_table)
    print(repr(users_table))
    print(Base.metadata.tables)
    # никогда в проде!
    # только через миграции
    Base.metadata.create_all(bind=engine)


# это я сюда скопировал ПРОСТО ДЛЯ ДЕМОНСТРАЦИИ
# в реальный код мы это НЕ КОПИРУЕМ
# это debug лог для нашего исследования.
got_sql = """\
CREATE TABLE users (
	id INTEGER NOT NULL, 
	username VARCHAR(32) NOT NULL, 
	email VARCHAR(200), 
	full_name VARCHAR(100) DEFAULT '' NOT NULL, 
	PRIMARY KEY (id), 
	UNIQUE (username), 
	UNIQUE (email)
)
"""


def insert_values(session: Session):
    bob = User(
        username="bob",
        email="bob@example.com",
    )
    kyle = User(
        username="kyle",
    )
    alice = User(
        username="alice",
        full_name="Alice White",
    )
    session.add(bob)
    session.add(kyle)
    session.add(alice)
    # session.add_all([bob, alice])
    session.commit()


def fetch_values(session: Session):
    stmt = select(User).where(
        # User.email.is_not(None),
        User.email.is_(None),
        (func.length(User.username) > 3),
    )
    print(stmt)
    # users = session.execute(stmt).all()
    # for (user,) in users:
    #     print(user)
    users = session.scalars(stmt).all()
    for user in users:
        print(
            user.id,
            user.username,
            user.email,
            user.full_name,
        )
        if user.username == "kyle":
            user.username = "kyle@ya.ru"

    session.commit()


def main():
    create_tables()
    with Session(engine) as session:
        # insert_values(session)
        fetch_values(session)

    # engine.dispose()


if __name__ == "__main__":
    main()
