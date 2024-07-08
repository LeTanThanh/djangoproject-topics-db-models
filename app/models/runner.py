from django.db.models import CharField, Model, TextChoices


class Runner(Model):
    MEDAL_CHOICES = TextChoices('MedalType', 'GOLD SILVER BRONZE')

    name = CharField(max_length=60)
    medal = CharField(max_length=10, choices=MEDAL_CHOICES)
