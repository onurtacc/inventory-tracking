from rest_framework import serializers, viewsets
from ..core.models import Room


class RoomSerializer(serializers.ModelSerializer):
    apartment = serializers.StringRelatedField()
    total_price = serializers.IntegerField(source='get_furniture_prices')

    class Meta:
        model = Room
        fields = '__all__'


class RoomViewSet(viewsets.ModelViewSet):
    serializer_class = RoomSerializer
    queryset = Room.objects.select_related('apartment__building')
