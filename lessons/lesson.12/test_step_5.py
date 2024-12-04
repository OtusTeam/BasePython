import pytest


def test_case_5(sample_data):
    sample_data.append(6)
    assert  sample_data == [1, 2, 3, 4, 5, 6]


def test_sum_case_6(sample_data):
    sample_data.remove(4)
    assert  sample_data == [1, 2, 3, 5]
