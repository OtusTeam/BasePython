from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine("sqlite:///example.db", echo=True)

session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)
