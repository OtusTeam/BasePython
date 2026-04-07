from collections.abc import Generator
from typing import Annotated

from fastapi import Depends
from sqlalchemy.orm import Session

from models import session_factory


def get_session() -> Generator[Session]:
    with session_factory() as session:
        yield session


GetSession = Annotated[
    Session,
    Depends(get_session),
]
