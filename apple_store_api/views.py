from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apple_store_api.serializers import ProductSerializer
from products.models import ProductCategory, Product
from products.serializers import CategorySerializer


class HomeView(APIView):
    def get(self, request):
        # categories
        categories = ProductCategory.objects.all()
        serializer = CategorySerializer(categories, many=True)

        # best-selling products
        best_selling = Product.objects.all().order_by('-sales_count')[:4]
        best_selling_serializer = ProductSerializer(instance=best_selling, many=True)



        return Response({
            'categories': serializer.data,
            'most_buy': best_selling_serializer.data
        }, status=status.HTTP_200_OK)
