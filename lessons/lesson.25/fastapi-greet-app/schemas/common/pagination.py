from typing import Annotated

import annotated_types
from pydantic import BaseModel, Field

from config import API_VERSION


class LimitOffsetPaginationSchema(BaseModel):
    limit: Annotated[
        int,
        annotated_types.Gt(0),
        annotated_types.Le(100),
    ] = Field(
        10,
    )
    offset: Annotated[int, annotated_types.Ge(0)] = Field(
        0,
    )


class ObjectsPaginationSchema(BaseModel):
    limit: int = Field(example=10)
    offset: int = Field(example=0)
    total_count: int = Field(example=100)


class MetadataSchema(BaseModel):
    pagination: ObjectsPaginationSchema
    api_version: str = API_VERSION
