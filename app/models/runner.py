from django.db.models import CharField, Model, TextChoices


class Runner(Model):
    MEDAL_CHOICES = TextChoices('MedalType', 'GOLD SILVER BRONZE')

    name = CharField(max_length=60)
    medal = CharField(max_length=10, choices=MEDAL_CHOICES)

    @classmethod
    def medal_choices(cls):
        choices = cls.MEDAL_CHOICES.choices
        return [choice for choice, value in choices]

    @classmethod
    def medal_values(cls):
        choices = cls.MEDAL_CHOICES.choices
        return [value for choice, value in choices]
