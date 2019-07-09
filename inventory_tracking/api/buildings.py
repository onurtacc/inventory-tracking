from rest_framework import serializers, viewsets
from ..core.models import Building


class BuildingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Building
        fields = '__all__'


class BuildingViewSet(viewsets.ModelViewSet):
    pagination_class = None
    serializer_class = BuildingSerializer
    queryset = Building.objects.all()
