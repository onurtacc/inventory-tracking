from django.contrib import admin
from .models import Building, Apartment, Room, Furniture


class BuildingAdmin(admin.ModelAdmin):
    search_fields = ('name', 'no')
    list_display = ('name', 'no')


admin.site.register(Building, BuildingAdmin)


class Rooms(admin.StackedInline):
    model = Room
    extra = 0


class ApartmentAdmin(admin.ModelAdmin):
    search_fields = ('building', 'apartment_no', 'floor', 'square_meter')
    list_display = ('apartment_no', 'building', 'floor', 'square_meter')
    list_filter = ["building"]

    inlines = [
        Rooms
    ]


admin.site.register(Apartment, ApartmentAdmin)


class FurnitureAdmin(admin.ModelAdmin):
    search_fields = ('room', 'name')
    list_display = ('name', 'price', 'room')
    list_filter = ["room"]


admin.site.register(Furniture, FurnitureAdmin)
