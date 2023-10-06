from django.db import models


class BaseMode(models.Model):
    objects = models.Manager()

    class Meta:
        abstract = True


class Booking(BaseMode):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    no_of_guests = models.IntegerField(default=0)
    booking_date = models.DateTimeField()


class Menu(BaseMode):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    inventory = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.title} : {str(self.price)}'
