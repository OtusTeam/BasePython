from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from config.settings import settings

engine = create_engine(
    url=settings.db.url,
    echo=settings.db.sqla.echo,
    pool_size=settings.db.sqla.pool_size,
    max_overflow=settings.db.sqla.max_overflow,
)


session_factory = sessionmaker(bind=engine)
