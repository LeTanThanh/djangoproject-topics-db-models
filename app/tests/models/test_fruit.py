import pytest
from django.test import TestCase

from app.factories.fruit_factory import FruitFactory


class TestFruit(TestCase):
    """
    Test id not primary_key
    """
    def test_id_when_not_primary_key(self):
        fruit = FruitFactory.create()

        with pytest.raises(AttributeError) as exc_info:
            fruit.id

        attribute_error = exc_info.value

        assert str(attribute_error) == "'Fruit' object has no attribute 'id'"

    """
    Test name
    """
    def test_name_when_primary_key(self):
        name = 'fruit'
        FruitFactory.create(name=name)

        with pytest.raises(Exception) as exc_info:
            FruitFactory.create(name=name)

        integrity_error = exc_info.value

        assert str(integrity_error) == 'UNIQUE constraint failed: app_fruit.name'
