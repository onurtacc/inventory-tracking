from django.shortcuts import render
from .models import Building, Apartment, Room, Furniture


def listing(request):
    payload = {
        'buildings': Building.objects.all(),
        'apartments': Apartment.objects.select_related('building'),
        'rooms': Room.objects.select_related('apartment__building'),
        'furnishings': Furniture.objects.select_related('room__apartment__building'),
    }
    return render(request, "list.html", payload)
