from django.core.management.base import BaseCommand
from store.models import EquipmentType, Equipment


class Command(BaseCommand):
    help = "Generate random data for Department, EquipmentType, Equipment."

    def handle(self, *args, **options):
        EquipmentType.create_random_equipment_types()
        Equipment.create_random_equipments()

        self.stdout.write(self.style.SUCCESS("Random data created."))
