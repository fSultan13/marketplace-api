from django_filters.rest_framework import FilterSet, filters, DjangoFilterBackend
from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import OpenApiParameter, extend_schema
from rest_framework import mixins, viewsets, pagination
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import AllowAny

from products.models import Product, SubType
from products.serializers import ProductSerializer


def filter_subtypes(queryset, name, value):
    names = [v.strip() for v in value.split(",")]
    return queryset.filter(subtypes__subtype__name__in=names).distinct()


class ProductFilter(FilterSet):
    brand = filters.CharFilter(field_name="brand__name")
    type = filters.CharFilter(field_name="type__name")

    subtype = filters.CharFilter(method=filter_subtypes)

    class Meta:
        model = Product
        fields = ['brand', 'type', 'subtype']


class ProductPagination(pagination.PageNumberPagination):
    page_size = 16


@extend_schema(
    parameters=[
        OpenApiParameter("brand", OpenApiTypes.STR, OpenApiParameter.QUERY, description="Название бренда"),
        OpenApiParameter("type", OpenApiTypes.STR, OpenApiParameter.QUERY, description="Название типа продукта"),
        OpenApiParameter(
            "subtype",
            OpenApiTypes.STR,
            OpenApiParameter.QUERY,
            description="Название подтипа. Можно передавать несколько через запятую: subtype=1,2,3",
            many=True,
        ),
        OpenApiParameter(
            "ordering",
            OpenApiTypes.STR,
            OpenApiParameter.QUERY,
            description="Сортировка: price, -price, created_at, -created_at, rating, -rating, views, -views,",
        ),
        OpenApiParameter(
            "page",
            OpenApiTypes.INT,
            OpenApiParameter.QUERY,
            description="Номер страницы",
        ),
    ]
)
class ProductListViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    permission_classes = [AllowAny]

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'slug'

    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_class = ProductFilter
    ordering_fields = ['price', 'created_at' , 'rating', 'views']
    ordering = ['price']

    pagination_class = ProductPagination
