from django.test import TestCase

from app.factories.manufacturer_factory import ManufacturerFactory


class TestManufacturer(TestCase):
    def test_success(self):
        manufacturer = ManufacturerFactory.create()

        assert manufacturer
