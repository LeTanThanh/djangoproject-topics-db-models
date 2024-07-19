from django.db.models import CharField, Model


class Shirt(Model):
    SIZE_CHOICES = {
        'S': 'Small',
        'M': 'Medium',
        'L': 'Large',
    }
    size = CharField(max_length=1, choices=SIZE_CHOICES)

    @classmethod
    def size_choices(cls):
        return list(cls.SIZE_CHOICES.keys())

    @classmethod
    def size_values(cls):
        return list(cls.SIZE_CHOICES.values())
