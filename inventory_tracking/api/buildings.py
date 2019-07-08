from rest_framework import serializers, viewsets
from ..core.models import Building


class Serializer(serializers.ModelSerializer):
    class Meta:
        model = Building
        fields = '__all__'


class ViewSet(viewsets.ModelViewSet):
    serializer_class = Serializer
    queryset = Building.objects.all()
