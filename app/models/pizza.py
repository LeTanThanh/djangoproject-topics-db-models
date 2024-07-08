from django.db.models import ManyToManyField, Model


class Pizza(Model):
    toppings = ManyToManyField('app.Topping')
