from django.db.models import CharField, Model


class Fruit(Model):
    name = CharField(max_length=100, primary_key=True)
