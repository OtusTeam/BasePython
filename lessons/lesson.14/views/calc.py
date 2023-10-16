from fastapi import APIRouter, Depends
from pydantic import BaseModel

router = APIRouter(prefix="/calc", tags=["Calc"])


class CalcParams(BaseModel):
    a: int
    b: int


@router.get("/mul/")
def mul(calc_params: CalcParams = Depends()):
    return {
        "total": calc_params.a * calc_params.b,
        **calc_params.model_dump(),
    }
