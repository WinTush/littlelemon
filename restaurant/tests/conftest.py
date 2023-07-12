from pytest_factoryboy import register

from .factories import BookingFactory, MenuFactory

register(BookingFactory)
register(MenuFactory)
