import uuid

from django.db import models
from slugify import slugify

from products.models.brand import Brand
from products.models.product_types import ProductType


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, related_name='products')
    type = models.ForeignKey(ProductType, on_delete=models.PROTECT, related_name='products')

    slug = models.SlugField(unique=True, max_length=255, editable=False, null=True)

    class Meta:
        db_table = "products"
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # Генерируем slug только при создании объекта
        if self.pk is None:
            self.slug = slugify(str(uuid.uuid4().int)[:5] + ' ' + str(self.name))
        super().save(*args, **kwargs)
