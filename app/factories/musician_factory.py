from factory import Faker
from factory.django import DjangoModelFactory


class MusicianFactory(DjangoModelFactory):
    class Meta:
        model = 'app.Musician'

    first_name = Faker(provider='first_name')
    last_name = Faker(provider='last_name')
    instrument = Faker(provider='word')
