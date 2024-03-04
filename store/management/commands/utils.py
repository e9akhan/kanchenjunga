"""
    Create fake data.
"""

import random

from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from store.models import EquipmentType, Equipment, Allocation
from itertools import permutations


class Command(BaseCommand):
    """
    Command class to create fake data.
    """

    help = "Generate random data for Department, EquipmentType, Equipment."

    def handle(self, *args, **options):
        """
        Overriding handle().
        """
        first_names = ["John", "Micheal", "David", "Maria", "Stephen", "Joe", "Donald", "George", "Moses", "Stuart", "Rahul", "Rohit", "Muhammad"]
        last_names = ["Watson", "Pointing", "Dsouza", "Beckham", "Stark", "Broad", "Sunak", "Rodriguez", "Angelo", "Mathews", "Sharma", "Khan", "Gupta"]
        user_list = []

        for first_name, last_name in zip(permutations(first_names, 1), permutations(last_names, 1)):
            username = first_name[0] + last_name[0] + "@123"
            email = first_name[0] + last_name[0] + "@example.com"

            user = User(
                username=username,
                email=email,
                first_name=first_name[0],
                last_name=last_name[0],
            )

            user.set_password(first_name[0] + "@123")
            user_list.append(user)

        User.objects.bulk_create(user_list)

        EquipmentType.create_random_equipment_types()
        Equipment.create_random_equipments()
        Allocation.create_random_allocations()

        self.stdout.write(self.style.SUCCESS("Random data created."))
