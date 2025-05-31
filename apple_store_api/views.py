from django.utils import timezone
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from apple_store_api.serializers import ProductSerializer, PosterSerializer, CartItemSerializer
from products.models import ProductCategory, Product, Poster, CartItem
from products.serializers import CategorySerializer


class HomeView(APIView):
    def get(self, request):
        # categories
        categories = ProductCategory.objects.all()[:7]
        serializer = CategorySerializer(categories, many=True)

        # slider items products
        slider_items = Product.objects.filter(is_slider=True)[:4]
        slider_items_serializer = ProductSerializer(instance=slider_items, many=True)

        # amazing_offers
        now = timezone.now()
        amazing_offers = Product.objects.filter(is_discounted=True, discount_end_time__gt=now)[:4]
        amazing_offers_serializer = ProductSerializer(instance=amazing_offers, many=True)

        # best-selling products
        best_selling = Product.objects.all().order_by('-sales_count')[:4]
        best_selling_serializer = ProductSerializer(instance=best_selling, many=True)

        # apple watches product
        apple_watches_item = Product.objects.filter(category__category_title='اپل واچ')[:4]
        apple_watches_item_serializer = ProductSerializer(instance=apple_watches_item, many=True)

        # poster main
        poster_main_item = Poster.objects.filter(is_footer_poster=False).order_by('-created')[:2]
        poster_main_item_serializer = PosterSerializer(instance=poster_main_item, many=True)

        # poster footer
        poster_footer_item = Poster.objects.filter(is_footer_poster=True).last()
        poster_footer_item_serializer = PosterSerializer(instance=poster_footer_item)

        return Response({
            'categories': serializer.data,
            'slider_items': slider_items_serializer.data,
            'amazing_offers': amazing_offers_serializer.data,
            'best_selling': best_selling_serializer.data,
            'main_poster': poster_main_item_serializer.data,
            'apple_watches': apple_watches_item_serializer.data,
            'poster_footer': poster_footer_item_serializer.data,
        }, status=status.HTTP_200_OK)


class AddToCartView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        product_id = request.data.get('product')
        quantity = int(request.data.get('quantity', 1))

        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)

        cart_item, created = CartItem.objects.get_or_create(user=request.user, product=product)
        if not created:
            cart_item.quantity += quantity
        else:
            cart_item.quantity = quantity
        cart_item.save()

        return Response({'message': 'Added to cart successfully'}, status=status.HTTP_200_OK)


class ClearCartView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request):
        CartItem.objects.filter(user=request.user).delete()
        return Response({'message': 'Cart cleared successfully'}, status=status.HTTP_200_OK)


class RemoveFromCartView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request):
        product_id = request.data.get('product')

        try:
            cart_item = CartItem.objects.get(user=request.user, product_id=product_id)

            if cart_item.quantity > 1:
                cart_item.quantity -= 1
                cart_item.save()
                return Response({'message': 'One item removed from cart'}, status=status.HTTP_200_OK)
            else:
                cart_item.delete()
                return Response({'message': 'Item removed from cart'}, status=status.HTTP_200_OK)

        except CartItem.DoesNotExist:
            return Response({'error': 'Item not found in cart'}, status=status.HTTP_404_NOT_FOUND)


class GetCartItems(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        cart_items = CartItem.objects.filter(user=request.user)
        serializer = CartItemSerializer(cart_items, many=True)
        total_price = sum([
            item.product.product_price * item.quantity for item in cart_items
        ])
        return Response({
            'cart': serializer.data,
            'total_price': total_price,
        }, status=status.HTTP_200_OK)
