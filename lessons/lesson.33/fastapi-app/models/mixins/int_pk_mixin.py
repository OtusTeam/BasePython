from sqlalchemy.orm import Mapped, mapped_column


class IntPkMixin:
    """
    INT - integer (type of field)
    PK - primary key (the main identifier for records in the table)
    MIXIN - an additional class to be added to a new class
    """
    # id: Mapped[UUID] = Column(UUID(as_uuid=True), primary_key=True)
    id: Mapped[int] = mapped_column(primary_key=True)


# если вы импортировали данные в Postgres вместе с айдишниками
# счётчик PK не будет обновлен автоматически,
# то надо обновить единожды
# PG example set sequence value
"""
# set new value
set_val(
    # sequence name
    "sequence-name",
    # start from
    # get current max id for this table
    SELECT COALICE(MAX(id), 0) FROM tablename
)
"""