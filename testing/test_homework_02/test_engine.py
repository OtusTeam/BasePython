from dataclasses import is_dataclass

import pytest
from faker import Faker

fake = Faker()

homework = pytest.importorskip("homework_02")
module_engine = homework.engine


def is_dataclass_instance(obj):
    return is_dataclass(obj) and not isinstance(obj, type)


class TestEngine:

    def test_engine(self):
        volume = fake.pyint()
        pistons = fake.pyint()
        engine = module_engine.Engine(volume=volume, pistons=pistons)
        assert is_dataclass_instance(engine)
        assert engine.volume == volume
        assert engine.pistons == pistons
