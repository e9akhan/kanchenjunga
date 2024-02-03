"""
    Module name :- models
"""

import random

from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Department(models.Model):
    """
        Department Model.
    """
    name = models.CharField(max_length=50)

    @classmethod
    def create_random_departments(cls):
        department_list = []

        for i in range(15):
            department_list.append(
                cls(
                    name = 'Cohort - ' + str(i)
                )
            )
        
        cls.objects.bulk_create(department_list)

    def __str__(self):
        return self.name


class EquipmentType(models.Model):
    """
        Equipment Type Model.
    """
    name = models.CharField(max_length = 50)

    @property
    def get_total_equipments(self):
        return self.equipment.count()

    @property
    def get_functional_equipments(self):
        return len(Equipment.objects.filter(functional = True, equipment_type=self))
    
    @property
    def get_assigned_equipments(self):
        return len(Equipment.objects.filter(equipment_type=self).exclude(user = None))

    @property
    def get_remaining_equipments(self):
        return self.get_functional_equipments - self.get_assigned_equipments
    
    @classmethod
    def create_random_equipment_types(cls):
        equipment_types = [
            'Laptop',
            'PC',
            'Keyboard',
            'Mouse',
            'Speaker',
            'CPU'
        ]

        equipment_type_list = []

        for equipment_type in equipment_types:
            equipment_type_list.append(
                cls(
                    name = equipment_type
                )
            )

        cls.objects.bulk_create(equipment_type_list)

    def save(self, **kwargs):
        equipment_list = []
        print(self.equipment.all())
        for equipment in self.equipment.all():
            equipment.label = self.name[:3] + equipment.label[3:]
            equipment_list.append(equipment)
        
        Equipment.objects.bulk_update(equipment_list, ['label'])
        return super().save(**kwargs)
    
    def __str__(self):
        return self.name


class Equipment(models.Model):
    """
        Equipment Model.
    """
    label = models.CharField(max_length=15)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None, null=True, blank=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, default=None, null=True, blank=True)
    equipment_type = models.ForeignKey(EquipmentType, on_delete=models.CASCADE, related_name='equipment')
    functional = models.BooleanField(default=True)

    @property
    def set_label(self):
        try:
            id = list(self.equipment_type.equipment.all())[-1]
            count = int(id.label[6:]) + 1
        except IndexError:
            count = 1
        return f'{self.equipment_type.name[:3]} - {count:0>6}'
    
    @classmethod
    def create_random_equipments(cls):
        departments = list(Department.objects.all())
        equipment_types = list(EquipmentType.objects.all())
        functionality = [True, False]

        equipment_list = []

        for _ in range(500):
            instance = cls(
                department = random.choice(departments),
                equipment_type = random.choice(equipment_types),
                functional = random.choice(functionality)
            )
            instance.label = instance.set_label

            equipment_list.append(instance)
        
        cls.objects.bulk_create(equipment_list)
    
    def __str__(self):
        return self.label