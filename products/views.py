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
    ProductModel,
)
from products.filters import (
    ProductFilter
)
from products.serializers import (
    ProductSerializer,
)


@extend_schema(
    summary='Call for a list of products',
    parameters=[
        OpenApiParameter(name='category', required=False, type=int),
    ],
    responses={
        status.HTTP_200_OK: ProductSerializer
    }
)
class ProductsView(ListAPIView):
    queryset = ProductModel.objects.all()
    serializer_class = ProductSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_class = ProductFilter
