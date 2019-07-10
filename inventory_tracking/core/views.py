from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from .models import Building, Apartment, Room, Furniture


def main_page(request):
    return render(request, "partials/layout.html")


def building_list(request):
    return render(request, "building_list.html")


class BuildingCreate(CreateView):
    model = Building
    fields = ['name', 'no', 'address']
    success_url = reverse_lazy('building_list')
    template_name = 'form.html'


class BuildingUpdate(UpdateView):
    model = Building
    fields = ['name', 'no', 'address']
    success_url = reverse_lazy('building_list')
    template_name = 'form.html'


def apartment_list(request):
    return render(request, "apartment_list.html")


class ApartmentCreate(CreateView):
    model = Apartment
    fields = ['building', 'apartment_no', 'floor', 'square_meter']
    success_url = reverse_lazy('apartment_list')
    template_name = 'form.html'


class ApartmentUpdate(UpdateView):
    model = Apartment
    fields = ['building', 'apartment_no', 'floor', 'square_meter']
    success_url = reverse_lazy('apartment_list')
    template_name = 'form.html'


def rooms_list(request):
    return render(request, "room_list.html")


class RoomCreate(CreateView):
    model = Room
    fields = ['apartment', 'name']
    success_url = reverse_lazy('room_list')
    template_name = 'form.html'


class RoomUpdate(UpdateView):
    model = Room
    fields = ['apartment', 'name']
    success_url = reverse_lazy('room_list')
    template_name = 'form.html'


def furnishings_list(request):
    return render(request, "furniture_list.html")


class FurnitureCreate(CreateView):
    model = Furniture
    fields = ['room', 'name', 'price']
    success_url = reverse_lazy('furniture_list')
    template_name = 'form.html'


class FurnitureUpdate(UpdateView):
    model = Furniture
    fields = ['room', 'name', 'price']
    success_url = reverse_lazy('furniture_list')
    template_name = 'form.html'
