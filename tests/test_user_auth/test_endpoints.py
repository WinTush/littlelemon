import pytest
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status


@pytest.mark.django_db
class TestDjoserAuth:
    def test_users_endpoint_exists(self, client):
        url = reverse("user-list")
        data = {
            "username": "testuser",
            "password": "testpassword",
        }

        response = client.post(url, data=data)
        assert response.status_code == status.HTTP_201_CREATED

    def test_token_login_endpoint_exists(self, client):
        url = reverse("login")
        data = {
            "username": "testuser",
            "password": "testpassword",
        }
        User.objects.create_user(**data)

        response = client.post(url, data=data)
        assert response.status_code == status.HTTP_200_OK
