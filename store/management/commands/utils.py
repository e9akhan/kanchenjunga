"""
    Create fake data.
"""

from django.core.management.base import BaseCommand
from store.models import EquipmentType, Equipment, Allocation


class Command(BaseCommand):
    """
    Command class to create fake data.
    """

    help = "Generate random data for Department, EquipmentType, Equipment."

    def handle(self, *args, **options):
        """
        Overriding handle().
        """
        EquipmentType.create_random_equipment_types()
        Equipment.create_random_equipments()
        Allocation.create_random_allocations()

        self.stdout.write(self.style.SUCCESS("Random data created."))
