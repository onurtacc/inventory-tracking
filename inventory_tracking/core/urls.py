from django.conf.urls import url
from . import views

urlpatterns = [
    url('^$', views.main_page, name="main"),

    url(r'buildings/$', views.building_list, name='building_list'),
    url(r'buildings/new', views.BuildingCreate.as_view(), name='building_new'),
    url(r'buildings/edit/(?P<pk>\d+)', views.BuildingUpdate.as_view(),
        name='building_update'),

    url(r'apartments/$', views.apartment_list, name='apartment_list'),
    url(r'apartments/new', views.ApartmentCreate.as_view(), name='apartment_new'),
    url(r'apartments/edit/(?P<pk>\d+)', views.ApartmentUpdate.as_view(),
        name='apartment_update'),

    url(r'rooms/$', views.rooms_list, name='room_list'),
    url(r'rooms/new', views.RoomCreate.as_view(), name='room_new'),
    url(r'rooms/edit/(?P<pk>\d+)', views.RoomUpdate.as_view(),
        name='room_update'),

    url(r'furnishings/$', views.furnishings_list, name='furniture_list'),
    url(r'furnishings/new', views.FurnitureCreate.as_view(template_name='form.html'), name='furniture_new'),
    url(r'furnishings/edit/(?P<pk>\d+)', views.FurnitureUpdate.as_view(template_name='form.html'),
        name='furniture_update'),

    url(r'sum/$', views.aggregate, name='aggregate'),

]
