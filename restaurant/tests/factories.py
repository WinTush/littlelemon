import factory
from django.utils import timezone

from restaurant.models import Booking, Menu


class MenuFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Menu

    title = factory.Sequence(lambda n: f"Menu {n}")
    price = 2.5


class BookingFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Booking

    name = factory.Faker("name")
    booking_date = factory.LazyFunction(timezone.now)
