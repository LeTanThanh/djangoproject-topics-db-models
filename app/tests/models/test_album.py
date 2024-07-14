from datetime import date

import pytest
from django.db.utils import IntegrityError
from django.test import TestCase

from app.factories.album_factory import AlbumFactory
from app.factories.musician_factory import MusicianFactory


class TestAlbum(TestCase):
    """
    Test artist
    """
    def test_artist_when_none(self):
        with pytest.raises(IntegrityError) as exc_info:
            AlbumFactory.create(artist=None)

        integrity_error = exc_info.value

        assert str(integrity_error) == 'NOT NULL constraint failed: app_album.artist_id'

    def test_artist_when_present(self):
        musician = MusicianFactory.create()
        album = AlbumFactory.create(artist=musician)

        assert album.artist == musician

    def test_artist_related_name(self):
        musician = MusicianFactory.create()
        album = AlbumFactory.create(artist=musician)

        assert album in musician.albums.all()

    """
    Test name
    """
    def test_name_when_none(self):
        with pytest.raises(IntegrityError) as exc_info:
            AlbumFactory.create(name=None)

        integrity_error = exc_info.value

        assert str(integrity_error) == 'NOT NULL constraint failed: app_album.name'

    def test_name_when_valid(self):
        album = AlbumFactory.create(name='a' * 100)

        assert album

    """
    Test release_date
    """
    def test_release_date_when_none(self):
        with pytest.raises(IntegrityError) as exc_info:
            AlbumFactory.create(release_date=None)

        integrity_error = exc_info.value

        assert str(integrity_error) == 'NOT NULL constraint failed: app_album.release_date'

    def test_release_date_when_valid(self):
        release_date = date(2024, 12, 31)
        album = AlbumFactory.create(release_date=release_date)

        assert album

    """
    Test num_stars
    """
    def test_num_stars_when_none(self):
        with pytest.raises(IntegrityError) as exc_info:
            AlbumFactory.create(num_stars=None)

        integrity_error = exc_info.value

        assert str(integrity_error) == 'NOT NULL constraint failed: app_album.num_stars'

    def test_num_stars_when_negative(self):
        with pytest.raises(IntegrityError) as exc_info:
            AlbumFactory.create(num_stars=-1)

        integrity_error = exc_info.value

        assert str(integrity_error) == 'CHECK constraint failed: num_stars'

    def test_num_stars_when_valid(self):
        album = AlbumFactory.create(num_stars=1)

        assert album
