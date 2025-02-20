import random

from fastapi import APIRouter
from pydantic import PositiveInt

router = APIRouter()


@router.get("/add", tags=["Numbers"])
def count_add(a: int, b: int):
    return {
        "a": a,
        "b": b,
        "sum": a + b,
    }


@router.get("/random-numbers", tags=["Numbers", "Random"])
def generate_random_numbers(
    count: PositiveInt,
):
    return {
        "numbers": [
            random.randint(1, 10000)
            for _ in range(count)
        ]
    }
