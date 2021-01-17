from rest_framework import status
from rest_framework.generics import ListAPIView

from drf_spectacular.utils import extend_schema

from categories.models import (
    CategoryModel,
)
from categories.serializers import (
    CategorySerializer,
)


@extend_schema(
    summary='Call to get a list of categories',
    responses={
        status.HTTP_200_OK: CategorySerializer
    }
)
class CategoriesView(ListAPIView):
    queryset = CategoryModel.objects.all()
    serializer_class = CategorySerializer
