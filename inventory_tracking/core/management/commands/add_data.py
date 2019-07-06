from django.core.management.base import BaseCommand
from inventory_tracking.core.models import Building, Apartment, Room, Furniture
import random


class Command(BaseCommand):
    help = "Insert 20 Building, 10 Apartment, 3 Room, 5 Furniture into database."

    def handle(self, *args, **options):
        self.stdout.write("Cleaning Database...")
        Building.objects.all().delete()

        self.stdout.write("Generating Buildings...")
        buildings = []

        for num in range(1, 21):
            buildings.append(
                Building(name=f"Apartman #{num}", no=random.randint(1, 40), address=f"Lorem Ipsum Dolor Sit Amet")
            )

        Building.objects.bulk_create(buildings)

        self.stdout.write("Generating Apartments...")
        apartments = []
        apartment_id = 1

        for build in Building.objects.all():
            apartment_no = 1
            for num in range(apartment_id * 10, (apartment_id * 10 + 10)):
                apartments.append(
                    Apartment(
                        building=build,
                        apartment_no=apartment_no,
                        floor=random.randint(1, 10),
                        square_meter=random.randint(60, 160)
                    )
                )
                apartment_no += 1
            apartment_id += 1

        Apartment.objects.bulk_create(apartments)

        self.stdout.write("Generating Rooms...")

        rooms = []
        room_names = ['Mutfak', 'Oturma Odası', 'Salon']
        for apart in Apartment.objects.all():
            for name in room_names:
                rooms.append(
                    Room(
                        apartment=apart,
                        name=name
                    )
                )

        Room.objects.bulk_create(rooms)

        self.stdout.write("Generating Furnishings...")

        furniture = []
        furnishings = ['Televizyon', 'Bilgisayar', 'Kanepe', 'Halı', 'Masa']

        for r in Room.objects.all():
            for furnt in furnishings:
                furniture.append(
                    Furniture(
                        room=r,
                        name=furnt,
                        price=random.randint(200, 4000)
                    )
                )
        Furniture.objects.bulk_create(furniture)

        self.stdout.write(
            self.style.SUCCESS(f'Inserted 20 Building, 10 Apartment, 3 Room and 5 Furniture')
        )
