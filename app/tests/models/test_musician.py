import pytest
from django.db.utils import IntegrityError
from django.test import TestCase

from app.factories.musician_factory import MusicianFactory


class TestMusician(TestCase):
    """
    Test first_name
    """
    def test_first_name_when_none(self):
        with pytest.raises(IntegrityError) as exc_info:
            MusicianFactory.create(first_name=None)

        integrity_error = exc_info.value

        assert str(integrity_error) == 'NOT NULL constraint failed: app_musician.first_name'

    def test_first_name_when_valid(self):
        musician = MusicianFactory.create(first_name='a' * 50)

        assert musician

    """
    Test last_name
    """
    def test_last_name_when_none(self):
        with pytest.raises(IntegrityError) as exc_info:
            MusicianFactory.create(last_name=None)

        integrity_error = exc_info.value

        assert str(integrity_error) == 'NOT NULL constraint failed: app_musician.last_name'

    def test_last_name_when_valid(self):
        musician = MusicianFactory.create(last_name='a' * 50)

        assert musician

    """
    Test instrument
    """
    def test_instrument_when_none(self):
        with pytest.raises(IntegrityError) as exc_info:
            MusicianFactory.create(instrument=None)

        integrity_error = exc_info.value

        assert str(integrity_error) == 'NOT NULL constraint failed: app_musician.instrument'

    def test_instrument_when_valid(self):
        musician = MusicianFactory.create(instrument='a' * 100)

        assert musician
