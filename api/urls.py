from django.urls import path

from . import views

urlpatterns = [
    path("menu", views.MenuItemsView.as_view(), name="menu-list"),
    path("menu/<int:pk>", views.SingleMenuItemView.as_view(), name="menu-detail"),
]
