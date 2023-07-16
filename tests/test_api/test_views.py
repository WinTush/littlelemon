import pytest
from django.urls import reverse
from rest_framework import status

pytestmark = pytest.mark.django_db


class TestMenuListView:
    url = reverse("menu-list")

    def test_status_code(self, api_client):
        response = api_client.get(self.url)

        assert response.status_code == status.HTTP_200_OK

    def test_unauthenticated_create_menu_item(self, api_client):
        data = {"title": "Pizza", "price": "10.99"}
        response = api_client.post(self.url, data)

        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_unauthorized_create_menu_item(self, authenticated_client):
        data = {"title": "Pizza", "price": "10.99"}
        response = authenticated_client.post(self.url, data)

        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_admin_create_menu_item(self, admin_client):
        data = {"title": "Pizza", "price": "10.99"}
        response = admin_client.post(self.url, data)

        assert response.status_code == status.HTTP_201_CREATED
        assert response.data["title"] == data["title"]
        assert response.data["price"] == data["price"]


class TestMenuDetailView:
    def test_status_code(self, api_client, menu_factory):
        menu = menu_factory()
        url = reverse("menu-detail", args=[menu.id])
        response = api_client.get(url)

        assert response.status_code == status.HTTP_200_OK

    def test_get_menu_item(self, api_client, menu_factory):
        menu = menu_factory(title="Burger")
        url = reverse("menu-detail", args=[menu.id])
        response = api_client.get(url)

        assert response.data.get("title") == menu.title

    def test_unauthorized_update_menu_item(self, authenticated_client, menu_factory):
        menu = menu_factory(title="Burger", price=9.99)
        url = reverse("menu-detail", args=[menu.id])
        data = {"title": "Cheeseburger", "price": "12.99"}
        response = authenticated_client.patch(url, data)

        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_update_menu_item(self, admin_client, menu_factory):
        menu = menu_factory(title="Burger", price=9.99)
        url = reverse("menu-detail", args=[menu.id])
        data = {"title": "Cheeseburger", "price": "12.99"}
        response = admin_client.patch(url, data)

        assert response.status_code == status.HTTP_200_OK
        assert response.data["title"] == data["title"]
        assert response.data["price"] == data["price"]

    def test_unauthorized_delete_menu_item(self, authenticated_client, menu_factory):
        menu = menu_factory()
        url = reverse("menu-detail", args=[menu.id])
        response = authenticated_client.delete(url)

        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_delete_menu_item(self, admin_client, menu_factory):
        menu = menu_factory()
        url = reverse("menu-detail", args=[menu.id])
        response = admin_client.delete(url)

        assert response.status_code == status.HTTP_204_NO_CONTENT


class TestBookingListView:
    url = reverse("booking-list")

    def test_status_code(self, api_client):
        response = api_client.get(self.url)

        assert response.status_code == status.HTTP_200_OK

    def test_unauthenticated_create_booking(self, api_client):
        data = {
            "name": "John Doe",
            "no_of_guests": 4,
            "booking_date": "2022-01-01T12:00:00Z",
        }
        response = api_client.post(self.url, data)

        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_authenticated_create_booking(self, authenticated_client):
        data = {
            "name": "John Doe",
            "no_of_guests": 4,
            "booking_date": "2022-01-01T12:00:00Z",
        }
        response = authenticated_client.post(self.url, data)

        assert response.status_code == status.HTTP_201_CREATED
        assert response.data["name"] == data["name"]
        assert response.data["no_of_guests"] == data["no_of_guests"]
        assert response.data["booking_date"] == data["booking_date"]


class TestBookingDetailView:
    def test_get_booking(self, api_client, booking_factory):
        booking = booking_factory(name="John Doe")
        url = reverse("booking-detail", args=[booking.id])
        response = api_client.get(url)

        assert response.data.get("name") == booking.name

    def test_update_booking(self, authenticated_client, booking_factory):
        booking = booking_factory(name="John Doe", no_of_guests=4)
        url = reverse("booking-detail", args=[booking.id])
        data = {
            "name": "Jane Doe",
            "no_of_guests": 6,
            "booking_date": "2022-01-02T12:00:00Z",
        }
        response = authenticated_client.put(url, data)

        assert response.status_code == status.HTTP_200_OK
        assert response.data["name"] == data["name"]
        assert response.data["no_of_guests"] == data["no_of_guests"]
        assert response.data["booking_date"] == data["booking_date"]

    def test_delete_booking(self, authenticated_client, booking_factory):
        booking = booking_factory()
        url = reverse("booking-detail", args=[booking.id])
        response = authenticated_client.delete(url)

        assert response.status_code == status.HTTP_204_NO_CONTENT
