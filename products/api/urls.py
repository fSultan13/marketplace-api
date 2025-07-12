from django.urls import path

from products.api.views import ProductListViewSet

urlpatterns = [
    path('products/', ProductListViewSet.as_view({"get": "list"}), name='product-list'),
    path('products/<slug:slug>/', ProductListViewSet.as_view({"get": "retrieve"}), name='product'),
]
