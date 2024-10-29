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
-- Set new value for the sequence
SELECT setval(
    -- sequence name
    'sequence-name',
    -- get current max id for this table
    COALESCE((SELECT MAX(id) FROM tablename), 0)
);
"""
