from sqlalchemy import create_engine

from config import DB_URL, DB_ECHO

engine = create_engine(
    DB_URL,
    echo=DB_ECHO,
)
