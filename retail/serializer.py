from rest_framework.serializers import ModelSerializer

from retail.models import NetworkUnit, Product


class NetworkUnitSerializer(ModelSerializer):

    class Meta:
        model = NetworkUnit
        fields = "__all__"


class ProductSerializer(ModelSerializer):

    class Meta:
        model = Product
        fields = "__all__"
