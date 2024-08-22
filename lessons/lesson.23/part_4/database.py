from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models import Base

engine = create_engine('sqlite:///vet_clinic.db', echo=True)
session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)

def create_all():
    Base.metadata.create_all(engine)
