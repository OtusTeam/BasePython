from datetime import datetime
from sqlalchemy import (
    Column, DateTime,
)


class CreatedAtMixin:
    created_at = Column(
        DateTime,
        default=datetime.utcnow,
        nullable=False,
    )
