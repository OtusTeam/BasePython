from sqlalchemy import create_engine

from config import DB_PATH, DB_ECHO

engine = create_engine(
    f"sqlite:///{DB_PATH}",
    echo=DB_ECHO,
)
