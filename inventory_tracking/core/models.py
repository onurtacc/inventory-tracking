from django.db import models
from inventory_tracking.common.timetrackedmodel import TimeTrackedModel


class Building(TimeTrackedModel):
    name = models.CharField(max_length=255)
    no = models.CharField(max_length=255)
    address = models.TextField()

    class Meta:
        verbose_name = "Bina"
        verbose_name_plural = "Binalar"
        ordering = ['created_at']

    def __str__(self):
        return self.name


class Apartment(TimeTrackedModel):
    building = models.ForeignKey(Building, related_name="apartments", on_delete=models.CASCADE)
    apartment_no = models.IntegerField()
    floor = models.IntegerField()
    square_meter = models.IntegerField()

    class Meta:
        unique_together = ("building", "apartment_no")
        verbose_name = "Daire"
        verbose_name_plural = "Daireler"
        ordering = ['apartment_no']

    def __str__(self):
        return self.building.name + " - " + str(self.apartment_no)


class Room(TimeTrackedModel):
    apartment = models.ForeignKey(Apartment, related_name="rooms", on_delete=models.CASCADE)
    name = models.CharField(max_length=255, help_text="for example: kitchen, living room etc.")

    class Meta:
        verbose_name = "Oda"
        verbose_name_plural = "Odalar"
        ordering = ['created_at']

    def __str__(self):
        return self.apartment.__str__() + " - " + self.name


class Furniture(TimeTrackedModel):
    room = models.ForeignKey(Room, related_name="furnishings", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    price = models.IntegerField(verbose_name="Price (₺)")

    class Meta:
        verbose_name = "Eşya"
        verbose_name_plural = "Eşyalar"
        ordering = ['created_at']

    def __str__(self):
        return self.name
