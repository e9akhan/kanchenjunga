from django.contrib import admin
from store.models import Department, Equipment, EquipmentType

# Register your models here.
admin.site.register(Department)


@admin.register(EquipmentType)
class EquipmentTypeAdmin(admin.ModelAdmin):
    verbose_name = 'Equipment Type'


@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    list_display = ['label', 'equipment_type', 'user', 'department', 'functional']
