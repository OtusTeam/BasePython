from typing import Annotated

from fastapi import Path
from fastapi import Query

PrimaryKey = Annotated[int, Path(ge=1, le=2_147_483_647)]
Offset = Annotated[int, Query(ge=0, le=9_223_372_036_854_775_807)]
Limit = Annotated[int, Query(ge=1, le=100)]
