from factory import Faker
from factory.django import DjangoModelFactory


class MusicianFactory(DjangoModelFactory):
    class Meta:
        model = 'app.Musician'

    first_name = Faker('first_name')
    last_name = Faker('last_name')
    instrument = Faker('word')
