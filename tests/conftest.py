from pytest_factoryboy import register

from .test_restaurant.factories import BookingFactory, MenuFactory

register(BookingFactory)
register(MenuFactory)
