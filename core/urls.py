from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r"customer", views.CustomerViewSet, basename="customer")
router.register(r"product", views.ProductViewSet, basename="product")
router.register(r"order", views.OrderViewset, basename="order")


urlpatterns = [
    path("", include(router.urls)),
    path("orderitem/", views.OrderItemView.as_view()),
]
