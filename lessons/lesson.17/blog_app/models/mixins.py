from datetime import datetime

from sqlalchemy import (
    Column,
    DateTime,
)


class TimestampMixin:
    created_at = Column(DateTime, default=datetime.utcnow)
