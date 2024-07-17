import pytest
from django.db.utils import IntegrityError
from django.test import TestCase

from app.factories.car_factory import CarFactory
from app.factories.manufacturer_factory import ManufacturerFactory
from app.models.car import Car


class TestCar(TestCase):
    """
    Test manufacturer
    """
    def test_manufacturer_when_none(self):
        with pytest.raises(IntegrityError) as exc_info:
            CarFactory.create(manufacturer=None)

        integrity_error = exc_info.value

        assert str(integrity_error) == 'NOT NULL constraint failed: app_car.manufacturer_id'

    def test_manufacturer_when_present(self):
        manufacturer = ManufacturerFactory.create()
        car = CarFactory.create(manufacturer=manufacturer)

        assert car.manufacturer == manufacturer

    def test_manufacturer_on_delete(self):
        manufacturer = ManufacturerFactory.create()
        car = CarFactory.create(manufacturer=manufacturer)

        manufacturer.delete()

        with pytest.raises(Car.DoesNotExist):
            car.refresh_from_db()

    def test_manufacturer_related_name(self):
        manufacturer = ManufacturerFactory.create()
        car = CarFactory.create(manufacturer=manufacturer)

        assert car in manufacturer.cars.all()
