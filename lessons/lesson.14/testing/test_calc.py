import pytest

from calc import add


class TestAdd:

    @pytest.mark.parametrize(
        "a, b, expected",
        [
            (1, 2, 3),
            (1, 1, 2),
            ("2", "3", "23"),
            pytest.param(3, 4, 7),
        ],
    )
    def test_add(self, a, b, expected):
        assert add(a, b) == expected

    @pytest.mark.parametrize(
        "a, b, expected_match",
        [
            (1, "1", "unsupported operand type"),
            ("1", 1, "can only concatenate str"),
        ],
    )
    def test_raises(self, a, b, expected_match):
        with pytest.raises(TypeError, match=expected_match):
            add(a, b)
