from .models import Products
from rest_framework import serializers


class ProductsSerializer(serializers.ModelSerializer):
    different_name_for_discount_price = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Products
        fields = [
            'name',
            'content',
            'price',
            'sale_price',
            'different_name_for_discount_price'
        ]

    def get_different_name_for_discount_price(self, obj):
        return obj.discount_price()
