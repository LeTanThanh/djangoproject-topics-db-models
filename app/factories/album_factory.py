from factory import Faker, SubFactory
from factory.django import DjangoModelFactory


class AlbumFactory(DjangoModelFactory):
    class Meta:
        model = 'app.Album'

    artist = SubFactory(factory='app.factories.musician_factory.MusicianFactory')
    name = Faker(provider='name')
    release_date = Faker(provider='date')
    num_stars = Faker(provider='pyint', min_value=0, max_value=5)
