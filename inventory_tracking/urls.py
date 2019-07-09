from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^api/', include('inventory_tracking.api.urls', namespace='api')),
    path('', include('inventory_tracking.core.urls')),
]
