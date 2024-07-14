from rest_framework import serializers
from .models import Producto

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ['idproducto', 'nombreart', 'marca', 'descripcion', 'precio', 'stock', 'imagen']
