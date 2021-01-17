from rest_framework import serializers

from clients.models import (
    ClientModel
)


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientModel
        fields = (
            'id',
            'email',
            'created'
        )
        read_only_fields = (
            'id',
            'created'
        )
