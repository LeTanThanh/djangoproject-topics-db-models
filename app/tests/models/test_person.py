import pytest
from django.db.utils import IntegrityError
from django.test import TestCase

from app.factories.person_factory import PersonFactory


class TestPerson(TestCase):
    """
    Test first_name
    """
    def test_first_name_when_none(self):
        with pytest.raises(IntegrityError) as exc_info:
            PersonFactory.create(first_name=None)

        integrity_error = exc_info.value

        assert str(integrity_error) == 'NOT NULL constraint failed: app_person.first_name'

    """
    Test last_name
    """
    def test_last_name_when_none(self):
        with pytest.raises(IntegrityError) as exc_info:
            PersonFactory.create(last_name=None)

        integrity_error = exc_info.value

        assert str(integrity_error) == 'NOT NULL constraint failed: app_person.last_name'
