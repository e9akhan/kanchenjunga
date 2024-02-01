"""
    Module name :- models
"""

from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Department(models.Model):
    """
        Department Model.
    """
    name = models.CharField(max_length=50)

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
        return len(Equipment.objects.filter(functional = True))
    
    @property
    def get_assigned_equipments(self):
        return len(Equipment.objects.exclude(user = None))

    @property
    def get_remaining_equipments(self):
        return self.get_functional_equipments - self.get_assigned_equipments
    
    def __str__(self):
        return self.name


class Equipment(models.Model):
    """
        Equipment Model.
    """
    label = models.CharField(max_length=10)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None, null=True, blank=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    equipment_type = models.ForeignKey(EquipmentType, on_delete=models.CASCADE)
    functional = models.BooleanField(default=True)

    @property
    def set_label(self):
        count = self.equipment_type.equipment.count()
        return f'{self.equipment_type.equipment.count()} - {count:0>6}'

    def save(self, **kwargs):
        self.label = self.set_label
        return super().save(**kwargs)
    
    def __str__(self):
        return self.label