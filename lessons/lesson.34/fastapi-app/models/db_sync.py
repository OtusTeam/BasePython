from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from config import db_url, db_echo

engine = create_engine(
    db_url,
    # echo=True only for debug!!
    echo=db_echo,
)

session_factory = sessionmaker(
    bind=engine,
    expire_on_commit=False,
)
