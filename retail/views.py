from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView,
)

from retail.models import NetworkUnit, Product
from retail.serializer import NetworkUnitSerializer, ProductSerializer
from retail.permissions import IsActive


class NetworkUnitCreateAPIView(CreateAPIView):
    queryset = NetworkUnit.objects.all()
    serializer_class = NetworkUnitSerializer
    permission_classes = [IsActive]


class NetworkUnitListAPIView(ListAPIView):
    queryset = NetworkUnit.objects.all()
    serializer_class = NetworkUnitSerializer
    permission_classes = [IsActive]
    filter_backends = [SearchFilter]
    search_fields = ["country"]


class NetworkUnitRetrieveAPIView(RetrieveAPIView):
    queryset = NetworkUnit.objects.all()
    serializer_class = NetworkUnitSerializer
    permission_classes = [IsActive]


class NetworkUnitUpdateAPIView(UpdateAPIView):
    queryset = NetworkUnit.objects.all()
    serializer_class = NetworkUnitSerializer
    permission_classes = [IsActive]

    def perform_update(self, serializer):
        if "debt" in serializer.validated_data:
            serializer.validated_data.pop("debt")
            raise Exception("You can't update dept")
        super().perform_update(serializer)


class NetworkUnitDestroyAPIView(DestroyAPIView):
    queryset = NetworkUnit.objects.all()
    serializer_class = NetworkUnitSerializer
    permission_classes = [IsActive]


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsActive]
