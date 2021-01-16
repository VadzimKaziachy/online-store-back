from rest_framework import status
from rest_framework.generics import ListAPIView

from drf_spectacular.utils import extend_schema

from categories.models import (
    Category,
)
from categories.serializers import (
    CategorySerializer,
)


@extend_schema(
    summary='Call for read list category',
    responses={
        status.HTTP_200_OK: CategorySerializer
    }
)
class CategoriesView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
