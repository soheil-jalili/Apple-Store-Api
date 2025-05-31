from django.urls import path, re_path

from products import views

app_name = 'products'
urlpatterns = [
    path('search/', views.ProductSearchView.as_view(), name='product_search'),
    path('<str:slug>', views.DetailView.as_view(), name='product_detail'),
]
