from pydantic import BaseModel


class CalcInput(BaseModel):
    a: int
    b: int
