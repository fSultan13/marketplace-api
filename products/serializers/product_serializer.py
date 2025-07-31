from rest_framework import fields, serializers

from products.models import Product, ProductSize, ProductImages, ProductsAttributeM2M


class ImagesFromProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImages
        fields = [
            "image",
            "is_preview",
        ]


class SizesFromProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductSize
        fields = [
            "size",
            "quantity",
        ]


class SubtypeFromProductSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source="subtype.name")

    class Meta:
        model = ProductsAttributeM2M
        fields = [
            "name"
        ]

class AttributesFromProductSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='attribute.name')
    unit = serializers.CharField(source='attribute.unit')

    class Meta:
        model = ProductsAttributeM2M
        fields = [
            "name",
            "value",
            "unit"
        ]

class ProductSerializer(serializers.ModelSerializer):
    images = ImagesFromProductSerializer(many=True)
    sizes = SizesFromProductSerializer(many=True)
    subtypes = SubtypeFromProductSerializer(many=True)
    attributes = AttributesFromProductSerializer(many=True)
    type = serializers.CharField(source='type.name')
    brand = serializers.CharField(source='brand.name')

    class Meta:
        model = Product
        fields = [
            "name",
            "description",
            "price",
            "created_at",
            "brand",
            "type",
            "slug",
            "images",
            "sizes",
            "subtypes",
            "attributes",
        ]

