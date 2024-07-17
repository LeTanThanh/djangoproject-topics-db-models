from factory import sequence
from factory.django import DjangoModelFactory
from faker import Faker


class FruitFactory(DjangoModelFactory):
    class Meta:
        model = 'app.Fruit'

    @sequence
    def name(n):
        faker_fruit = Faker().word()
        return f'{n}{faker_fruit}'
