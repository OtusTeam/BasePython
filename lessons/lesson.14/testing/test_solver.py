import random

import pytest

from solver import Solver


@pytest.fixture
def value_a():
    return random.randint(1, 100)


@pytest.fixture
def value_b():
    return random.randint(1, 100)


@pytest.fixture
def solver(value_a, value_b) -> Solver:
    return Solver(value_a, value_b)


class TestSolver:

    def test_add(
        self,
        solver: Solver,
        value_a,
        value_b,
    ) -> None:
        assert solver.add() == value_a + value_b

    def test_mul(
        self,
        solver: Solver,
        value_a,
        value_b,
    ) -> None:
        assert solver.mul() == value_a * value_b


"""
@pytest.fixture(
    params=[
        pytest.param((1, 2), id="1,2"),
        pytest.param((3, 4), id="3,4"),
    ]
)
def solver(request) -> Solver:
    a, b = request.param
    return Solver(a, b)


class TestSolver:

    def test_add(self, solver: Solver) -> None:
        assert solver.add() == solver.a + solver.b

    def test_mul(self, solver: Solver) -> None:
        assert solver.mul() == solver.a * solver.b
"""
