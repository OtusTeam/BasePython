from collections.abc import Iterator
from typing import Annotated

from fastapi import Depends
from fastapi import Request
from sqlalchemy.orm import Session

from bookshelf.config.settings import Settings


def settings_dep(request: Request) -> Settings:
    return request.app.state.settings


SettingsDep = Annotated[Settings, Depends(settings_dep)]


def session_dep(request: Request) -> Iterator[Session]:
    with request.app.state.sessionmaker() as session:
        yield session


SessionDep = Annotated[Session, Depends(session_dep)]
