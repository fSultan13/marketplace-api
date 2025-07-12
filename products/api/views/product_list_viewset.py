from rest_framework import mixins, viewsets
from rest_framework.generics import ListAPIView

from products.models import Product
from products.serializers import ProductSerializer


class ProductListViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'slug'
