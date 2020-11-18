from unittest import TestCase

import pytest

from solver import Solver, mul, sub, SUB_ERROR_TEXT


class TestSolver(TestCase):

    def test_add(self):
        res = Solver.add(1, 2)
        self.assertEqual(res, 3)


@pytest.mark.parametrize('args, expected_result', [
    (('spam', 3), 'spamspamspam'),
    ((4, 3), 12),
])
def test_mul(args, expected_result):
    res = mul(*args)
    assert res == expected_result


class TestSub:
    def test_sub_raises(self):
        with pytest.raises(TypeError) as exc_info:
            sub('', 1)

        assert str(exc_info.value) == SUB_ERROR_TEXT

    @pytest.mark.parametrize('args, expected_result', [
        pytest.param(
            (3, 4), -1,
            id="sub_int",
        ),
        pytest.param(
            (5.6, .5), 5.1,
            id="sub_float",
        ),
    ])
    def test_sub_ok(self, args, expected_result):
        res = sub(*args)
        assert res == expected_result
