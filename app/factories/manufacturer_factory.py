from factory.django import DjangoModelFactory


class ManufacturerFactory(DjangoModelFactory):
    class Meta:
        model = 'app.Manufacturer'
