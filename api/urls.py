from django.urls import include, path
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter(trailing_slash=False)
router.register(r"booking", views.BookingViewSet)

urlpatterns = [
    path("menu", views.MenuItemsView.as_view(), name="menu-list"),
    path("menu/<int:pk>", views.SingleMenuItemView.as_view(), name="menu-detail"),
    path("", include(router.urls)),
]
