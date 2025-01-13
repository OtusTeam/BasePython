from sqlalchemy import create_engine

from config import BASE_DIR


db_filename = "users.db"
db_filepath = BASE_DIR / db_filename

engine = create_engine(
    f"sqlite:///{db_filepath}",
    echo=True,  # echo only for debug!!
)
