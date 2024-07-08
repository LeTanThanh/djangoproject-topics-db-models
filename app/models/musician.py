from django.db.models import CharField, Model


class Musician(Model):
    first_name = CharField(max_length=50)
    last_name = CharField(max_length=50)
    instrument = CharField(max_length=100)
