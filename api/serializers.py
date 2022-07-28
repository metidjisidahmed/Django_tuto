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
        # in the route create_product_by_name we just passed our req.body and not a Products instance  that's why we have to this checking since discount doesnt have a default not null value
        if not isinstance(obj, Products):
            return None
        return obj.discount_price()
