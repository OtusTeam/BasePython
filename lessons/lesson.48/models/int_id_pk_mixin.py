from sqlalchemy.orm import Mapped, mapped_column


class IntIdPkMixin:
    id: Mapped[int] = mapped_column(primary_key=True)
