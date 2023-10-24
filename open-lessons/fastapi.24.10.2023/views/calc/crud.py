from .schemas import CalcInput


def calc_mul(calc: CalcInput):
    return {
        "total": calc.a * calc.b,
        "calc": calc.model_dump(),
    }
