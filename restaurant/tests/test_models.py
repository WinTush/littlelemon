import pytest

from restaurant.models import Booking, Menu

pytestmark = pytest.mark.django_db


class TestMenuModel:
    def test_str_method(self, menu_factory):
        menu: Menu = menu_factory()
        assert str(menu) == menu.title


class TestBookingModel:
    def test_str_method(self, booking_factory):
        booking: Booking = booking_factory()
        assert str(booking) == f"{booking.name}: {booking.booking_date}"
