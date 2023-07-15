from django.urls import reverse
from pytest_django.asserts import assertTemplateUsed


class TestHomeView:
    def test_status_code(self, client):
        url = reverse("home")
        response = client.get(url)

        assert response.status_code == 200

    def test_template_used(self, client):
        url = reverse("home")
        response = client.get(url)

        assertTemplateUsed(response, "restaurant/index.html")
