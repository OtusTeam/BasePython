from sqlalchemy import create_engine

from config.settings import settings

engine = create_engine(
    url=settings.db.url,
    echo=settings.db.sqla.echo,
)
