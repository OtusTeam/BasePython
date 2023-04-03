import math
import random
from django.test import TestCase


def add_to_random(value):
    return random.randint(1, 4) + value


def mock_randint(start, end, *args, **kwargs):
    return 3


class TestMath(TestCase):

    def test_sqrt(self):
        self.assertEqual(math.sqrt(4), 2)

    def test_add_to_random(self):
        random.randint = mock_randint
        result = add_to_random(10)
        self.assertEqual(result, 13)