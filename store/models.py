"""
    Module name :- models
"""

import random
from datetime import date, timedelta

from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class EquipmentType(models.Model):
    """
    Equipment Type Model.
    """

    name = models.CharField(max_length=50)

    @property
    def get_total_equipments(self):
        """
        Get total equipments.
        """
        return self.equipment.count()

    @property
    def get_functional_equipments(self):
        """
        Get functional equipments.
        """
        return len(
            [
                equipment
                for equipment in self.equipment.all()
                if equipment.functional is True
            ]
        )

    @property
    def get_assigned_equipments(self):
        """
        Get assigned equipments.
        """
        return len(
            [
                equipment
                for equipment in self.equipment.all()
                if equipment.assigned is True and equipment.functional is True
            ]
        )

    @property
    def get_remaining_equipments(self):
        """
        Get remaining equipments.
        """
        return self.get_functional_equipments - self.get_assigned_equipments

    @classmethod
    def create_random_equipment_types(cls):
        """
        Create random equipment types.
        """
        equipment_types = ["Laptop", "Monitor", "Keyboard", "Mouse", "Speaker", "CPU"]

        equipment_type_list = []

        for equipment_type in equipment_types:
            equipment_type_list.append(cls(name=equipment_type))

        cls.objects.bulk_create(equipment_type_list)

    def __str__(self):
        """
        String Representation.
        """
        return self.name


class Equipment(models.Model):
    """
    Equipment Model.
    """

    label = models.CharField(max_length=10)
    serial_number = models.CharField(max_length=20)
    model_number = models.CharField(max_length=20)
    brand = models.CharField(max_length=30)
    price = models.FloatField()
    buy_date = models.DateField()
    equipment_type = models.ForeignKey(
        EquipmentType, on_delete=models.CASCADE, related_name="equipment"
    )
    functional = models.BooleanField(default=True)
    assigned = models.BooleanField(default=False)

    @property
    def set_label(self):
        """
        Automatically set label.
        """
        try:
            temp_id = list(self.equipment_type.equipment.all())[-1]
            count = int(temp_id.label[6:]) + 1
        except IndexError:
            count = 1
        return f"{self.equipment_type.name[:3]}-{count:0>6}"

    @classmethod
    def create_random_equipments(cls):
        """
        Create random equipments.
        """
        equipment_types = list(EquipmentType.objects.all())
        functionality = [True, False]
        serail_numbers = [f'{random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}' for _ in range(1000)]
        model_numbers = [f'Model-{number}' for number in serail_numbers]
        buy_dates = [date.today() - timedelta(days=x) for x in range(40)]
        brands = ['Samsung', 'Nokia', 'Microsoft', 'Apple', 'Logitech', 'Dell']

        equipment_list = []

        for _ in range(500):
            instance = cls(
                buy_date = random.choice(buy_dates),
                price=random.randint(1000, 10000),
                serial_number=random.choice(serail_numbers),
                model_number=random.choice(model_numbers),
                equipment_type=random.choice(equipment_types),
                functional=random.choice(functionality),
                brand = random.choice(brands)
            )
            instance.label = instance.set_label

            equipment_list.append(instance)

        cls.objects.bulk_create(equipment_list)

    def __str__(self):
        """
        String Representation.
        """
        return self.label


class Allocation(models.Model):
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.equipment} - {self.user}'
