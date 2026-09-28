from datetime import datetime

from sqlalchemy import func, DateTime
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
)


class CreatedAt:

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
    )
