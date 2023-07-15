import pytest
from django.urls import reverse
from rest_framework import status

pytestmark = pytest.mark.django_db


class TestMenuItemsView:
    def test_status_code(self, api_client):
        url = reverse("menu-list")
        response = api_client().get(url)

        assert response.status_code == status.HTTP_200_OK

    def test_create_menu_item(self, api_client):
        url = reverse("menu-list")
        data = {"title": "Pizza", "price": "10.99"}
        response = api_client().post(url, data)

        assert response.status_code == status.HTTP_201_CREATED
        assert response.data["title"] == data["title"]
        assert response.data["price"] == data["price"]


class TestSingleMenuItemView:
    def test_status_code(self, api_client, menu_factory):
        menu = menu_factory()
        url = reverse("menu-detail", args=[menu.id])
        response = api_client().get(url)

        assert response.status_code == status.HTTP_200_OK

    def test_get_menu_item(self, api_client, menu_factory):
        menu = menu_factory(title="Burger")
        url = reverse("menu-detail", args=[menu.id])
        response = api_client().get(url)

        assert response.data.get("title") == menu.title

    def test_update_menu_item(self, api_client, menu_factory):
        menu = menu_factory(title="Burger", price=9.99)
        url = reverse("menu-detail", args=[menu.id])
        data = {"title": "Cheeseburger", "price": "12.99"}
        response = api_client().patch(url, data)

        assert response.status_code == status.HTTP_200_OK
        assert response.data["title"] == data["title"]
        assert response.data["price"] == data["price"]

    def test_delete_menu_item(self, api_client, menu_factory):
        menu = menu_factory()
        url = reverse("menu-detail", args=[menu.id])
        response = api_client().delete(url)

        assert response.status_code == status.HTTP_204_NO_CONTENT
