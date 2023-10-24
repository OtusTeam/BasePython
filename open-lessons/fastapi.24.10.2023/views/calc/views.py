from fastapi import Depends, APIRouter

from . import crud
from .schemas import CalcInput

router = APIRouter(prefix="/calc", tags=["Calc"])


@router.get("/add/")
def calc_add(a: int, b: int):
    return {
        "total": a + b,
        "a": a,
        "b": b,
    }


@router.get("/mul/")
def calc_mul(calc: CalcInput = Depends()):
    return crud.calc_mul(calc=calc)
