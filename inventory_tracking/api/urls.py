from django.conf.urls import url, include
from rest_framework import routers
from inventory_tracking.api import buildings, apartments, rooms, furnishings

router = routers.DefaultRouter()
router.register(r'buildings', buildings.BuildingViewSet, 'ApiBuilding')
router.register(r'apartments', apartments.ApartmentViewSet, 'ApiApartment')
router.register(r'rooms', rooms.RoomViewSet, 'ApiRoom')
router.register(r'furnishings', furnishings.FurnitureViewSet, 'ApiFurniture')

app_name = 'api'

urlpatterns = [
    url(r'^', include(router.urls))
]
