from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter(trailing_slash=False)
router.register(r"booking", views.BookingViewSet)
router.register(r"menu", views.MenuViewSet)

urlpatterns = router.urls
