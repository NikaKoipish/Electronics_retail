from rest_framework.routers import DefaultRouter

from retail.apps import RetailConfig
from django.urls import path

from retail.views import (
    NetworkUnitListAPIView,
    NetworkUnitCreateAPIView,
    NetworkUnitRetrieveAPIView,
    NetworkUnitUpdateAPIView,
    NetworkUnitDestroyAPIView,
    ProductViewSet,
)

app_name = RetailConfig.name

router = DefaultRouter()
router.register(r"product", ProductViewSet, basename="product")

urlpatterns = [
    path("", NetworkUnitListAPIView.as_view(), name="network_list"),
    path("create/", NetworkUnitCreateAPIView.as_view(), name="network_create"),
    path("<int:pk>/", NetworkUnitRetrieveAPIView.as_view(), name="network_retrieve"),
    path("<int:pk>/update/", NetworkUnitUpdateAPIView.as_view(), name="network_update"),
    path(
        "<int:pk>/delete/", NetworkUnitDestroyAPIView.as_view(), name="network_delete"
    ),
] + router.urls
