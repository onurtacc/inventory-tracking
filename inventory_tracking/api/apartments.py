from rest_framework import serializers, viewsets
from ..core.models import Apartment


class ApartmentSerializer(serializers.ModelSerializer):
    building = serializers.StringRelatedField()
    total_price = serializers.IntegerField(source='get_room_prices')

    class Meta:
        model = Apartment
        fields = '__all__'


class ApartmentViewSet(viewsets.ModelViewSet):
    serializer_class = ApartmentSerializer
    queryset = Apartment.objects.select_related('building')
