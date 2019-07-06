from django.shortcuts import render
from .models import Building, Apartment, Room, Furniture


def listing(request):
    payload = {
        'buildings': Building.objects.all()
    }
    return render(request, "list.html", payload)
