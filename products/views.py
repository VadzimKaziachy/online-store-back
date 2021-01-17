from drf_spectacular.utils import (
    extend_schema,
    OpenApiParameter,
)

from rest_framework import status
from rest_framework.generics import (
    ListAPIView,
)

from django_filters.rest_framework import (
    DjangoFilterBackend,
)

from products.models import (
    Product,
)
from products.filters import (
    ProductFilter
)
from products.serializers import (
    ProductSerializer,
)


@extend_schema(
    summary='Call for read list product',
    parameters=[
        OpenApiParameter(name='category', required=False, type=int),
    ],
    responses={
        status.HTTP_200_OK: ProductSerializer
    }
)
class ProductsView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_class = ProductFilter
