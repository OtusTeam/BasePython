from sqlalchemy import BigInteger, Identity
from sqlalchemy.orm import Mapped, mapped_column


class IdIntPkMixin:

    id: Mapped[int] = mapped_column(
        BigInteger,
        Identity(always=True),
        primary_key=True,
    )
