from django.conf.urls import url, include
from rest_framework import routers
from inventory_tracking.api import buildings, apartments, rooms, furnishings

router = routers.DefaultRouter()
router.register(r'buildings', buildings.ViewSet, 'ApiBuilding')
router.register(r'apartments', apartments.ViewSet, 'ApiApartment')
router.register(r'rooms', rooms.ViewSet, 'ApiRoom')
router.register(r'furnishings', furnishings.ViewSet, 'ApiFurniture')

app_name = 'api'

urlpatterns = [
    url(r'^', include(router.urls))
]
