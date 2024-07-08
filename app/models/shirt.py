from django.db.models import CharField, Model


class Shirt(Model):
    SIZE_CHOICES = {
        'S': 'Small',
        'M': 'Medium',
        'L': 'Large',
    }
    size = CharField(max_length=1, choices=SIZE_CHOICES)
