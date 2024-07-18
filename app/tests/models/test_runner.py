import pytest
from django.db.utils import IntegrityError
from django.test import TestCase

from app.factories.runner_factory import RunnerFactory
from app.models.runner import Runner


class TestRunner(TestCase):
    """
    Test name
    """
    def test_name_when_none(self):
        with pytest.raises(IntegrityError) as exc_info:
            RunnerFactory.create(name=None)

        integrity_error = exc_info.value

        assert str(integrity_error) == 'NOT NULL constraint failed: app_runner.name'

    """
    Test medal
    """
    def test_medal_when_none(self):
        with pytest.raises(IntegrityError) as exc_info:
            RunnerFactory.create(medal=None)

        integrity_error = exc_info.value

        assert str(integrity_error) == 'NOT NULL constraint failed: app_runner.medal'

    def test_medal_when_gold(self):
        runner = RunnerFactory.create(medal='GOLD')

        assert runner.get_medal_display() == 'Gold'

    def test_medal_when_silver(self):
        runner = RunnerFactory.create(medal='SILVER')

        assert runner.get_medal_display() == 'Silver'

    def test_medal_when_bronze(self):
        runner = RunnerFactory.create(medal='BRONZE')

        assert runner.get_medal_display() == 'Bronze'

    """
    Test @classmethod medal_choices
    """
    def test_medal_choices(self):
        assert Runner.medal_choices() == ['GOLD', 'SILVER', 'BRONZE']

    """
    Test @classmethod medal_values
    """
    def test_medal_values(self):
        assert Runner.medal_values() == ['Gold', 'Silver', 'Bronze']
