from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def home(request: HttpRequest) -> HttpResponse:
    """
    Renders the home page of the restaurant website.

    Parameters:
    - request (HttpRequest): The HTTP request object.

    Returns:
    - response (HttpResponse): The HTTP response object containing the rendered home page.

    Raises:
    - None

    Example usage:
    response = home(request)
    """
    return render(request, "restaurant/index.html")
