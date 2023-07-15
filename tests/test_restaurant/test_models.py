import pytest
from django.utils import timezone

pytestmark = pytest.mark.django_db


class TestMenuModel:
    def test_str_method(self, menu_factory):
        menu = menu_factory(title="test_menu")
        assert str(menu) == "test_menu"


class TestBookingModel:
    def test_str_method(self, booking_factory):
        time_now = timezone.now()
        booking = booking_factory(name="John Doe", booking_date=time_now)
        assert str(booking) == f"John Doe: {time_now}"
