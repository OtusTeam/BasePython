from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from config import settings


engine = create_engine(
    url=settings.db.sync_url,
    echo=settings.db.echo,
    pool_size=settings.db.pool_size,
    max_overflow=settings.db.max_overflow,
)

session_factory = sessionmaker(bind=engine)
