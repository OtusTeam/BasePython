from sqlalchemy import create_engine

from config import DB_URL, DB_ECHO

engine = create_engine(
    # f"sqlite:///{DB_PATH}",
    DB_URL,
    echo=DB_ECHO,
)
