from django.urls import path, re_path

from products import views

urlpatterns = [
    path('search/', views.ProductSearchView.as_view(), name='product_search'),
]
