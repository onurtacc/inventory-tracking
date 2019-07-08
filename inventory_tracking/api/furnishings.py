from rest_framework import serializers, viewsets
from ..core.models import Furniture


class Serializer(serializers.ModelSerializer):
    class Meta:
        model = Furniture
        fields = '__all__'


class ViewSet(viewsets.ModelViewSet):
    serializer_class = Serializer
    queryset = Furniture.objects.select_related('room__apartment__building')
