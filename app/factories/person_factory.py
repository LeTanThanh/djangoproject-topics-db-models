from factory.django import DjangoModelFactory
from factory.faker import Faker


class PersonFactory(DjangoModelFactory):
    class Meta:
        model = 'app.Person'

    first_name = Faker(provider='first_name')
    last_name = Faker(provider='last_name')
