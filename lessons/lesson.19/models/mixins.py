from datetime import datetime
from sqlalchemy import DateTime, Column


class TimestampMixin:
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)