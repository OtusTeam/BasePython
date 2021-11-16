from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine(
    "postgresql://user:password@localhost:5432/blog_app",
    echo=False,
)

session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)


def session_dependency():
    session = Session()
    yield session
    session.close()
