from django_filters import (
    FilterSet,
)

from products.models import (
    ProductModel,
)


class ProductFilter(FilterSet):
    class Meta:
        model = ProductModel
        fields = (
            'category',
        )
