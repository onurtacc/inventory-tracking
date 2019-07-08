from rest_framework import serializers, viewsets
from ..core.models import Furniture


class FurnitureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Furniture
        fields = '__all__'


class FurnitureViewSet(viewsets.ModelViewSet):
    serializer_class = FurnitureSerializer
    queryset = Furniture.objects.select_related('room__apartment__building')
