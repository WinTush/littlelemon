import pytest
from django.contrib.auth.models import User
from pytest_factoryboy import register
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient

from .test_restaurant.factories import BookingFactory, MenuFactory

register(BookingFactory)
register(MenuFactory)


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def admin_client(api_client):
    admin = User.objects.create_superuser("admin")
    token = Token.objects.create(user=admin)
    api_client.credentials(HTTP_AUTHORIZATION=f"Token {token.key}")
    return api_client


@pytest.fixture
def authenticated_client(api_client):
    user = User.objects.create_user("testuser")
    token = Token.objects.create(user=user)
    api_client.credentials(HTTP_AUTHORIZATION=f"Token {token.key}")
    return api_client
