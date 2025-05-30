from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apple_store_api.serializers import ProductSerializer
from products.models import Product


class ProductSearchView(APIView):
    def get(self, request):
        search = request.GET.get('search', '')
        products = Product.objects.filter(product_title__icontains=search)
        if products:
            serializer = ProductSerializer(products, many=True)
            return Response({
                'products': serializer.data
            }, status=status.HTTP_200_OK)
        return Response({
            'message': 'محصولی یافت نشد'
        })
