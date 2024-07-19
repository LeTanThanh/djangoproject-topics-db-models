from factory import Faker
from factory.django import DjangoModelFactory

from app.models.shirt import Shirt


class ShirtFactory(DjangoModelFactory):
    class Meta:
        model = 'app.Shirt'

    size = Faker('random_element', elements=Shirt.size_choices())
