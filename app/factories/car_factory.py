from factory import SubFactory
from factory.django import DjangoModelFactory


class CarFactory(DjangoModelFactory):
    class Meta:
        model = 'app.Car'

    manufacturer = SubFactory('app.factories.manufacturer_factory.ManufacturerFactory')
