from django.utils import timezone
from rest_framework import serializers

from products.models import Product, ProductImage, Poster, ColorProduct


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['id', 'product_images']


class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = ColorProduct
        fields = ['id', 'code_color']


class ProductSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True, read_only=True)
    discount_time_left = serializers.SerializerMethodField()
    colors = ColorSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = '__all__'

    def get_discount_time_left(self, obj):
        if obj.discount_end_time and obj.is_discounted:
            now = timezone.now()
            if obj.discount_end_time > now:
                delta = obj.discount_end_time - now
                return {
                    'days': delta.days,
                    'hours': delta.seconds // 3600,
                    'minutes': (delta.seconds % 3600) // 60,
                }
        return None


class PosterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poster
        fields = '__all__'
