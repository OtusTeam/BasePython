import pytest


class TestAddClass:
    def test_sum_case_4(data):
        data.pop()
        assert sum(data) == 10


    def test_sum_case_5(data):
        data.append(6)
        assert sum(data) == 21