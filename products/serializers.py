from rest_framework import serializers

from products.models import ProductCategory, ProductImage



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = '__all__'