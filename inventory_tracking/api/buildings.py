from rest_framework import serializers, viewsets
from ..core.models import Building


class BuildingSerializer(serializers.ModelSerializer):
    total_price = serializers.IntegerField(source='get_all_prices')

    class Meta:
        model = Building
        fields = '__all__'


class BuildingViewSet(viewsets.ModelViewSet):
    serializer_class = BuildingSerializer
    queryset = Building.objects.all()
