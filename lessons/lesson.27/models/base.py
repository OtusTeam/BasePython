from sqlalchemy import create_engine, event
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import declared_attr
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from config import db_filepath


class Base(DeclarativeBase):
    id: Mapped[int] = mapped_column(primary_key=True)

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return cls.__name__.lower()


engine = create_engine(
    f"sqlite:///{db_filepath}",
    echo=True,  # echo only for debug!!
)


# Define a function to set PRAGMA foreign_keys = ON
def set_foreign_keys_on(dbapi_conn, connection_record):
    cursor = dbapi_conn.cursor()
    cursor.execute("PRAGMA foreign_keys = ON;")
    cursor.close()


# Listen for the 'connect' event
event.listen(engine, "connect", set_foreign_keys_on)
