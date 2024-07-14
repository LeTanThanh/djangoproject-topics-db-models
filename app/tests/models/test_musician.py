import pytest
from django.db.utils import IntegrityError
from django.test import TestCase

from app.factories.musician_factory import MusicianFactory


class TestMusician(TestCase):
    """
    Test first_name
    """
    def test_when_first_name_is_null(self):
        with pytest.raises(IntegrityError) as exc_info:
            MusicianFactory.create(first_name=None)

        integrity_error = exc_info.value

        assert str(integrity_error) == 'NOT NULL constraint failed: app_musician.first_name'

    """
    Test last_name
    """
    def test_when_last_name_is_null(self):
        with pytest.raises(IntegrityError) as exc_info:
            MusicianFactory.create(last_name=None)

        integrity_error = exc_info.value

        assert str(integrity_error) == 'NOT NULL constraint failed: app_musician.last_name'

    """
    Test instrument
    """
    def test_when_instrument_is_null(self):
        with pytest.raises(IntegrityError) as exc_info:
            MusicianFactory.create(instrument=None)

        integrity_error = exc_info.value

        assert str(integrity_error) == 'NOT NULL constraint failed: app_musician.instrument'
