from rest_framework import serializers, viewsets
from ..core.models import Room


class Serializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'


class ViewSet(viewsets.ModelViewSet):
    serializer_class = Serializer
    queryset = Room.objects.select_related('apartment__building')
