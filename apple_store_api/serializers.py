from rest_framework import serializers

from products.models import Product, ProductImage, Poster


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['id', 'product_images']


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    images = ProductImageSerializer(many=True, read_only=True)


class PosterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poster
        fields = '__all__'
