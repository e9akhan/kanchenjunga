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
    def get_remaining_equipments(self):
        """
        Get total equipments.
        """
        return len(Equipment.get_non_assigned_items(self))

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

    @property
    def set_label(self):
        """
        Automatically set label.
        """
        try:
            temp_id = list(self.equipment_type.equipment.all())[-1]
            count = int(temp_id.label[4:]) + 1
        except IndexError:
            count = 1
        return f"{self.equipment_type.name[:3]}-{count:0>6}"

    @property
    def get_current_user(self):
        allocations = self.allocation.all()
        if allocations:
            return allocations[-1].user
        return "None"
    
    @classmethod
    def get_all_equipments(cls, equipment_type):
        return cls.object.filter(equipment_type = equipment_type)
    
    @classmethod
    def get_all_functional_equipments(cls, equipment_type):
        return cls.objects.filter(equipment_type = equipment_type, functional = True)

    @classmethod
    def get_non_functional_equipments(cls, equipment_type):
        return cls.objects.filter(equipment_type = equipment_type, functional = False)

    @classmethod
    def get_assigned_items(cls, equipment_type):
        equipments = cls.objects.filter(equipment_type = equipment_type)
        assigned_equipments = []
        
        for equipment in equipments:
            allocations = equipment.allocation.all()
            if not allocations:
                continue

            last_allocation = list(allocations)[-1]
            if not last_allocation.returned:
                assigned_equipments.append(equipment)

        return assigned_equipments
    
    @classmethod
    def get_non_assigned_items(cls, equipment_type):
        equipments = cls.objects.filter(equipment_type = equipment_type)
        non_assigned_equipments = []

        for equipment in equipments:
            allocations = equipment.allocation.all()
            if not allocations:
                non_assigned_equipments.append(equipment)
                continue

            last_allocation = list(allocations)[-1]
            if last_allocation.returned:
                non_assigned_equipments.append(equipment)

        return non_assigned_equipments

    @classmethod
    def create_random_equipments(cls):
        """
        Create random equipments.
        """
        equipment_types = list(EquipmentType.objects.all())
        functionality = [True, False]
        serial_numbers = [f'{random.randint(0, 9)}{random.randint(0, 9)}{random.randint(0, 9)}' for _ in range(1000)]
        model_numbers = [f'Model-{number}' for number in serial_numbers]
        buy_dates = [date.today() - timedelta(days=x) for x in range(40)]
        brands = ['Samsung', 'Nokia', 'Microsoft', 'Apple', 'Logitech', 'Dell']

        equipment_list = []

        for _ in range(500):
            instance = cls(
                buy_date = random.choice(buy_dates),
                price=random.randint(1000, 10000),
                serial_number=random.choice(serial_numbers),
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
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE, related_name='allocation')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    returned = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.equipment} - {self.user}'
