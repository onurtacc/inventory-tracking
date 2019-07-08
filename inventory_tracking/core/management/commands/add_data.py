from django.core.management.base import BaseCommand
from inventory_tracking.core.models import Building, Apartment, Room, Furniture
import random


class Command(BaseCommand):
    help = "Insert 5 Building, 10 Apartment per building, 3 Room per apartment, 5 Furniture per room into database"

    def handle(self, *args, **options):
        self.stdout.write("Cleaning Database...")
        Building.objects.all().delete()

        self.stdout.write("Generating Buildings...")
        buildings = []

        for num in range(1, 6):
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

        furnitures = []
        furnishings = ['Televizyon', 'Bilgisayar', 'Kanepe', 'Halı', 'Masa']

        for r in Room.objects.all():
            for furniture in furnishings:
                furnitures.append(
                    Furniture(
                        room=r,
                        name=furniture,
                        price=random.randint(200, 4000)
                    )
                )
        Furniture.objects.bulk_create(furnitures)

        self.stdout.write(
            self.style.SUCCESS(f'SUCCESS')
        )
