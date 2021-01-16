from rest_framework import status
from rest_framework.generics import ListAPIView

from drf_spectacular.utils import extend_schema

from products.models import (
    Product,
)
from products.serializers import (
    ProductSerializer,
)


@extend_schema(
    summary='Call for read list product',
    responses={
        status.HTTP_200_OK: ProductSerializer
    }
)
class ProductsView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
