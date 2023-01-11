from main import Solver, dev
import pytest
import random
from unittest import mock


@pytest.fixture
def get_solver():
    return Solver(1, 2)


@pytest.fixture
def get_other_solver():
    return Solver(4, 2)


@pytest.fixture
def solver_mix(request):
    a, b = request.param
    return Solver(a, b)


# pytest
class TestSolver:

    def test_add(self, get_solver):
        assert get_solver.add() == 3

    @pytest.mark.parametrize(
        'solver_mix, result',
        (
            ((1, 2), 3),
            ((2, 3), 5),
            ((4, 5), 9)
        ),
        indirect=['solver_mix']
    )
    def test_add_many(self, solver_mix, result):
        assert solver_mix.add() == result

    @pytest.mark.parametrize(
        'params, result',
        (
                ((1, 2), 3),
                ((2, 3), 5),
                ((4, 5), 9)
        ),
    )
    def test_add_many_simple(self, params, result):
        solver = Solver(*params)
        assert solver.add() == result

    def test_mul(self, get_solver):
        assert get_solver.mul() == 2

    def test_mull_other(self, get_other_solver):
        assert get_other_solver.mul() == 8

    def test_add_random_value(self, get_solver):
        value = get_solver.add_random_value()
        assert value >= 4 and value <= 103

        def rand_int_mock(start, end):
            return 66

        # random.randint = rand_int_mock
        with mock.patch('random.randint', rand_int_mock):
            value = get_solver.add_random_value()
            assert value == 69

        with mock.patch('random.randint', return_value=66):
            value = get_solver.add_random_value()
            assert value == 69

@pytest.mark.parametrize(
    'a, b, result',
    (
            (8, 2, 4),
            (6, 3, 2),
            (4, 2, 2)
    )
)
def test_dev(a, b, result):
    assert dev(a, b) == result


def test_dev_exception():
    with pytest.raises(ZeroDivisionError):
        dev(10, 0)
