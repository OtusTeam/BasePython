from sqlalchemy.orm import Session

from models.db import engine


def get_session() -> Session:
    with Session(engine) as session:
        try:
            yield session
        finally:
            # optional!! cleanup
            session.rollback()
