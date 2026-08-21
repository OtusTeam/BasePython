from collections.abc import Generator

from sqlalchemy import create_engine
from sqlalchemy.exc import IntegrityError
from sqlalchemy.exc import OperationalError
from sqlalchemy.exc import TimeoutError as SQLAlchemyTimeoutError
from sqlalchemy.orm import Session
from sqlalchemy.orm import sessionmaker

from app.config import get_settings
from app.exceptions import DatabaseBusyError
from app.exceptions import DatabaseUnavailableError
from app.exceptions import DataConflictError

settings = get_settings()
db_config = settings.database
sqla_config = db_config.sqlalchemy

engine = create_engine(
    db_config.url,
    echo=sqla_config.echo,
    pool_pre_ping=True,
    pool_use_lifo=True,
    pool_size=sqla_config.pool_size,
    max_overflow=sqla_config.max_overflow,
    pool_timeout=sqla_config.pool_timeout_seconds,
    pool_recycle=sqla_config.pool_recycle_seconds,
    connect_args={
        "connect_timeout": sqla_config.connect_timeout_seconds,
        "application_name": settings.app.name,
    },
)

SessionFactory = sessionmaker(
    bind=engine,
    expire_on_commit=False,
)


def get_session() -> Generator[Session]:
    try:
        with SessionFactory() as session:
            try:
                yield session
            except Exception:
                session.rollback()
                raise
    except SQLAlchemyTimeoutError as exc:
        raise DatabaseBusyError from exc
    except OperationalError as exc:
        raise DatabaseUnavailableError from exc
    except IntegrityError as exc:
        raise DataConflictError from exc
