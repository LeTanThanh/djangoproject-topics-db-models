from django.db.models import (
    CASCADE, CharField, DateField, ForeignKey, Model, PositiveIntegerField,
)


class Album(Model):
    artist = ForeignKey(
        'app.Musician',
        on_delete=CASCADE,
        related_name='albums'
    )
    name = CharField(max_length=100)
    release_date = DateField()
    num_stars = PositiveIntegerField()
