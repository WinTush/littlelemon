import pytest
from pytest_factoryboy import register
from rest_framework.test import APIClient

from .test_restaurant.factories import BookingFactory, MenuFactory

register(BookingFactory)
register(MenuFactory)


@pytest.fixture
def api_client():
    return APIClient()
