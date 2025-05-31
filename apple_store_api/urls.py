"""
URL configuration for apple_store_api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from apple_store_api import views
from apple_store_api.settings import DEBUG, MEDIA_URL, MEDIA_ROOT
from apple_store_api.views import AddToCartView, ClearCartView, RemoveFromCartView, GetCartItems

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/product/', include('products.urls')),
    path('api/home/', views.HomeView.as_view(), name='home'),
    path('api/account/', include('account.urls')),
    path('api/cart/checkout/', GetCartItems.as_view(), name='get_cart_items'),
    path('api/cart/add/', AddToCartView.as_view(), name='add-to-cart'),
    path('api/cart/remove/', RemoveFromCartView.as_view(), name='remove-from-cart'),
    path('api/cart/remove-all/', ClearCartView.as_view(), name='remove-all-cart'),
]

if DEBUG:
    urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
