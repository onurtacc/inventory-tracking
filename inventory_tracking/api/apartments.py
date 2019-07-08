from rest_framework import serializers, viewsets
from ..core.models import Apartment


class Serializer(serializers.ModelSerializer):
    class Meta:
        model = Apartment
        fields = '__all__'


class ViewSet(viewsets.ModelViewSet):
    serializer_class = Serializer
    queryset = Apartment.objects.select_related('building')
