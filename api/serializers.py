from rest_framework import serializers
from .models import OrdenProduccion, Palet, Producto


class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = "__all__"


class OrdenProduccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrdenProduccion
        fields = "__all__"

class PaletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Palet
        fields = "__all__"
