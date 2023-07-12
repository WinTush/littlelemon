from django.db import models


class Menu(models.Model):
    title = models.CharField(max_length=255, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.SmallIntegerField(default=0)

    def __str__(self):
        return self.title


class Booking(models.Model):
    name = models.CharField(max_length=255)
    no_of_guests = models.SmallIntegerField(default=0)
    booking_date = models.DateTimeField()

    def __str__(self):
        return f"{self.name}: {self.booking_date}"
