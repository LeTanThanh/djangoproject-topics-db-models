from factory.django import DjangoModelFactory
from factory.faker import Faker

from app.models.runner import Runner


class RunnerFactory(DjangoModelFactory):
    class Meta:
        model = 'app.Runner'

    name = Faker(provider='name')
    medal = Faker(provider='random_element', elements=Runner.medal_choices())
