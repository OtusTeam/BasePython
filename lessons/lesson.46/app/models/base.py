from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import DeclarativeBase, declared_attr


class Base(DeclarativeBase):
    id: Mapped[int] = mapped_column(primary_key=True)
