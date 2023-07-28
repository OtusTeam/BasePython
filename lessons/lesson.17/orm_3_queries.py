from datetime import datetime

from sqlalchemy import (
    create_engine,
    Column,
    Integer,
    String,
    Boolean,
    DateTime,
    false,
    func,
)

from sqlalchemy.orm import declarative_base, Session

DB_URL = "postgresql+psycopg2://username:passwd@localhost:5432/blog"
# DB_ECHO = False
DB_ECHO = True

engine = create_engine(url=DB_URL, echo=DB_ECHO)


Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String(32), nullable=False, unique=True)
    email = Column(String(100), nullable=True, unique=True)
    is_staff = Column(
        Boolean,
        nullable=False,
        default=False,
        server_default=false(),
    )
    created_at = Column(
        DateTime,
        nullable=False,
        default=datetime.utcnow,
        server_default=func.now(),
    )

    def __str__(self):
        return f"User(id={self.id}, username={self.username!r}, email={self.email!r}, is_staff={self.is_staff})"

    def __repr__(self):
        return str(self)


def create_user(
    session: Session,
    username: str,
    email: str | None = None,
) -> User:
    user = User(username=username, email=email)

    session.add(user)
    session.commit()

    print(user)
    return user


def get_user_by_id(session: Session, user_id: int) -> User | None:
    user = session.get(User, user_id)
    print("user", user_id, user)
    return user


def get_user_by_username(session: Session, username: str) -> User | None:
    # user = session.query(User).filter_by(username=username).one()
    user = session.query(User).filter_by(username=username).one_or_none()

    print("user", username, user)

    return user


def get_users(session: Session) -> list[User]:
    users = session.query(User).order_by(User.id).all()
    print("users:", users)
    return users


def get_user_by_email(session: Session, email: str) -> User | None:
    user = session.query(User).filter(User.email == email).one_or_none()
    print("user with email", email, user)
    return user


def get_user_by_email_domain(session: Session, domain: str) -> list[User]:
    users = session.query(User).filter(User.email.ilike(f"%{domain}")).order_by(User.id).all()
    print("users with email domain", domain, users)
    return users


def run_queries():
    with Session(engine) as session:
        create_user(session, username="john")
        create_user(session, username="sam", email="sam@example.com")
        create_user(session, username="bob", email="bob@ya.ru")
        create_user(session, username="kate", email="kate@example.com")

        get_user_by_id(session, user_id=1)
        get_user_by_id(session, user_id=2)
        get_user_by_id(session, user_id=1)
        get_user_by_id(session, user_id=4)

        get_users(session)

        get_user_by_username(session, "john")
        get_user_by_username(session, "nick")

        get_user_by_email(session, "bob@ya.ru")
        get_user_by_email(session, "admin@ya.ru")
        get_user_by_email_domain(session, "ya.ru")
        get_user_by_email_domain(session, "yahoo.com")
        get_user_by_email_domain(session, "example.com")


def main():
    sql_1 = """
    CREATE TABLE users (
        id SERIAL NOT NULL, 
        username VARCHAR(32) NOT NULL, 
        email VARCHAR(100), 
        is_staff BOOLEAN DEFAULT false NOT NULL, 
        created_at TIMESTAMP WITHOUT TIME ZONE NOT NULL, 
        PRIMARY KEY (id), 
        UNIQUE (username), 
        UNIQUE (email)
    );
    """
    sql_2 = """
    CREATE TABLE users (
        id SERIAL NOT NULL, 
        username VARCHAR(32) NOT NULL, 
        email VARCHAR(100), 
        is_staff BOOLEAN DEFAULT false NOT NULL, 
        created_at TIMESTAMP WITHOUT TIME ZONE DEFAULT now() NOT NULL, 
        PRIMARY KEY (id), 
        UNIQUE (username), 
        UNIQUE (email)
    );
    """
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    run_queries()


if __name__ == '__main__':
    main()

