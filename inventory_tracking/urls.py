from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from .core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^api/', include('inventory_tracking.api.urls', namespace='api')),
    path('', views.listing, name='list'),
]
