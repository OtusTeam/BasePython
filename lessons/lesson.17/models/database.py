from sqlalchemy import create_engine, Column, Integer
from sqlalchemy.orm import declarative_base, sessionmaker, scoped_session, declared_attr


class Base:

    @declared_attr
    def __tablename__(cls):
        return f"blog_{cls.__name__.lower()}s"

    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return str(self)


engine = create_engine("sqlite:///example-db.sqlite", echo=True)
Base = declarative_base(bind=engine, cls=Base)


session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)


if __name__ == '__main__':
    print("Base:", Base)
    print("Base mro", Base.mro())
    print("Session:", Session)
    session = Session()
    print("session:", session)
