import pytest
from faker import Faker

fake = Faker()

homework = pytest.importorskip("homework_02")
module_base = homework.base
module_plane = homework.plane
exceptions = homework.exceptions


@pytest.fixture
def plane():
    weight = fake.pyint()
    fuel = fake.pyint()
    fuel_consumption = fake.pyint()
    max_cargo = fake.pyint(1000, 50000)
    plane = module_plane.Plane(weight, fuel, fuel_consumption, max_cargo)
    return plane


class TestPlane:

    def test_init(self):
        weight = fake.pyint()
        fuel = fake.pyint()
        fuel_consumption = fake.pyint()
        max_cargo = fake.pyint(1000, 50000)
        plane = module_plane.Plane(weight, fuel, fuel_consumption, max_cargo)
        assert isinstance(plane, module_base.Vehicle)
        assert plane.weight == weight
        assert plane.fuel == fuel
        assert plane.fuel_consumption == fuel_consumption
        assert plane.max_cargo == max_cargo
        assert plane.cargo == 0

    def test_load_cargo_ok(self, plane):
        assert plane.cargo == 0
        assert plane.max_cargo > 0
        cargo = fake.pyint(1, plane.max_cargo)
        expected = plane.cargo + cargo
        plane.load_cargo(cargo)
        assert plane.cargo == expected

    def test_load_cargo_overload(self, plane):
        assert plane.cargo == 0
        assert plane.max_cargo > 0
        cargo = fake.pyint(plane.max_cargo + 1, plane.max_cargo * 2)
        with pytest.raises(exceptions.CargoOverload):
            plane.load_cargo(cargo)
        assert plane.cargo == 0

    def test_remove_all_cargo(self, plane):
        cargo = fake.pyint()
        plane.cargo = cargo
        assert plane.cargo > 0
        res = plane.remove_all_cargo()
        assert res == cargo
        assert plane.cargo == 0

    def test_load_cargo_fits_exact(self, plane):
        assert plane.cargo == 0
        assert plane.max_cargo > 0
        cargo = plane.max_cargo
        plane.load_cargo(cargo)
        assert plane.cargo == cargo
