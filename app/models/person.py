from django.db.models import CharField, Model


class Person(Model):
    first_name = CharField(max_length=30, blank=False)
    last_name = CharField(max_length=30, blank=False)
