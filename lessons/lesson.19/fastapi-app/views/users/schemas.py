from pydantic import BaseModel, Field, PositiveInt
from typing import Annotated


class User(BaseModel):
    id: PositiveInt
    name: Annotated[str, Field(min_length=3, max_length=15)]
    age: Annotated[int, Field(ge=14, le=100)]
    city: Annotated[str, Field(default="defoult city", min_length=2, max_length=12)]


"""Считаю важным отметить, что испольщование Annotated в BaseModel является скорее
фичей, нежели повсеместной практикой, чаше всего вы встретите подобную форму записи"""

"""class Record(BaseModel):
    id: PositiveInt
    name: str = Field(min_length=3, max_length=15)
    age: str = Field(ge=14, le=100)
    city: str = Field(default='defoult city', min_length=2, max_length=12)"""
