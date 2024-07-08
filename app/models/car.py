from django.db.models import CASCADE, ForeignKey, Model


class Car(Model):
    manufacturer = ForeignKey(
        'app.Manufacturer',
        on_delete=CASCADE
    )
