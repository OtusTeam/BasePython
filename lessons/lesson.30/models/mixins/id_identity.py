from sqlalchemy import (
    Identity,
)
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
)


class IdIdentity:

    id: Mapped[int] = mapped_column(
        Identity(always=True),
        primary_key=True,
    )
