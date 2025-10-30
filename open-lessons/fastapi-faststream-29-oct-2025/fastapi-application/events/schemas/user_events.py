from typing import Literal

from pydantic import BaseModel


class UserRegistered(BaseModel):
    user_id: int
    email: str


class UserStatisticsRequest(BaseModel):
    user_id: int
    kind: Literal["fizz", "buzz"] = "buzz"


class UserStatisticsResponse(BaseModel):
    user_id: int
    kind: Literal["fizz", "buzz"]
    foo: int
    bar: str
    baz: float
