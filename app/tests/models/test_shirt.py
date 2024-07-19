import pytest
from django.db.utils import IntegrityError
from django.test import TestCase

from app.factories.shirt_factory import ShirtFactory
from app.models.shirt import Shirt


class TestShirt(TestCase):
    """
    Test size
    """
    def test_size_when_none(self):
        with pytest.raises(IntegrityError) as exc_info:
            ShirtFactory.create(size=None)

        integrity_error = exc_info.value

        assert str(integrity_error) == 'NOT NULL constraint failed: app_shirt.size'

    def test_size_when_small(self):
        shirt = ShirtFactory.create(size='S')

        assert shirt.get_size_display() == 'Small'

    def test_size_when_medium(self):
        shirt = ShirtFactory.create(size='M')

        assert shirt.get_size_display() == 'Medium'

    def test_size_when_large(self):
        shirt = ShirtFactory.create(size='L')

        assert shirt.get_size_display() == 'Large'

    """
    Test @classmethod size_choices
    """
    def test_size_choices(self):
        assert Shirt.size_choices() == ['S', 'M', 'L']

    """
    Test @classmethod size_values
    """
    def test_size_values(self):
        assert Shirt.size_values() == ['Small', 'Medium', 'Large']
