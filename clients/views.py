from drf_spectacular.utils import extend_schema

from rest_framework import status
from rest_framework.generics import (
    CreateAPIView,
)
from clients.serializers import (
    ClientSerializer,
)


@extend_schema(
    summary='Call for save new client email',
    responses={
        status.HTTP_201_CREATED: ClientSerializer
    }
)
class ClientView(CreateAPIView):
    serializer_class = ClientSerializer
